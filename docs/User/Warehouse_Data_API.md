---
title: "Warehouse Data API (BaaS)"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: ""
canonical_id: "actian-data-platform-warehouse-data-api"
---

# Warehouse Data API (BaaS)

The Warehouse Data API (also called the BaaS API) is a REST interface for working
with data in a running Actian warehouse — authenticating, managing schema, and
performing create, read, update, and delete operations, as well as running native
SQL queries.

!!! warning "Keep your tokens secret"

    The examples below use placeholders such as `<warehouse-id>`, `<warehouse-domain>`,
    and `<BAT_TOKEN>`. A BAT token is a credential — treat it like a password. Never
    commit it to source control, paste it into shared documents, or include it in a
    support request. Rotate a token immediately if it is exposed.

In the examples, replace the placeholders with your own values:

| Placeholder | Description |
| --- | --- |
| `<warehouse-id>` | Your warehouse identifier, for example `av-xxxxxxxxxxxx`. |
| `<warehouse-domain>` | The warehouse domain shown in your warehouse connection details (for example, `avd.actiandatacloud.com` for Google Cloud). |
| `<BAT_TOKEN>` | The BAT access token returned when you log in (see [Authentication](#authentication)). |

## Enable the Warehouse Data API

The warehouse must be **running** before you can enable the Data API.

### Using the console

1. Open the [Warehouse Details](../User/Warehouse_Details.md) page for your warehouse.
2. Turn on the **Data API (BaaS)** toggle.

The BaaS service start-up and DNS registration can take a moment — allow some time
before the endpoints become reachable.

### Using REST (for automation)

Send a `PUT` request to the `admiral` `data-api/configure` endpoint. The `admiral`
host is environment-specific; the example below uses a development host and is shown
for illustration.

```bash
curl -X 'PUT' \
  'https://<admiral-host>/api/v1/resource/warehouse/<warehouse-id>/data-api/configure' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "enabled": true
}'
```

## API version, status, and specification

Use these endpoints for basic information about a warehouse's Data API:

| Purpose | Endpoint |
| --- | --- |
| Version | `https://<warehouse-id>.<warehouse-domain>/baas/v1/version` |
| State | `https://<warehouse-id>.<warehouse-domain>/baas/v1/status` |
| Specification | `https://<warehouse-id>.<warehouse-domain>/baas/v1/spec` |

You can import the specification into Postman or render it as a Swagger document.

## Explore the API in Swagger

You can explore all available Data API endpoints using the Swagger interface:

```
https://<warehouse-id>.<warehouse-domain>/baas-doc/
```

## Authentication

### Native login

Authenticate with a native database user name and password. The response returns a
BAT token used to authorize subsequent requests.

```bash
curl -X 'PUT' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db/User/login' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "<username>",
    "password": "<password>",
    "global": false
}'
```

### ActianID login (token exchange)

This login endpoint accepts an ActianID bearer token, registers the user, and returns
a BAT token in the response headers.

```
https://<warehouse-id>.<warehouse-domain>/baas/v1/db/User/login
```

### Using the BAT token

Once you have a BAT token, include it in the `Authorization` header of every request:

```
Authorization: BAT <BAT_TOKEN>
```

### Verify the logged-in user

```bash
curl -X 'GET' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db/User/me' \
  -H 'accept: application/json' \
  -H 'Authorization: BAT <BAT_TOKEN>'
```

Example response:

```json
{
  "id": "/db/User/12",
  "version": 1,
  "acl": {
    "read": { "/db/User/12": "allow" },
    "write": { "/db/User/12": "allow" }
  },
  "createdAt": "2025-08-23T16:30:39.84Z",
  "updatedAt": "2025-08-23T16:30:39.84Z",
  "username": "<user>@example.com.idp",
  "inactive": null
}
```

## Working with data

All data operations require the `Authorization: BAT <BAT_TOKEN>` header.

### Create a table

```bash
curl -X 'POST' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/schema' \
  -H 'accept: application/json' \
  -H 'Authorization: BAT <BAT_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"class":"/db/Teacher","fields":{"name":{"type":"/db/String","name":"name","order":0}},"superClass":"/db/Object","acl":{"schemaAdd":{},"schemaReplace":{},"schemaSubclass":{},"load":{},"insert":{},"update":{},"delete":{},"query":{}}}'
```

### Add a record

```bash
curl -X 'POST' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db/{tableName}' \
  -H 'accept: application/json' \
  -H 'Authorization: BAT <BAT_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"id":"/db/Teacher/11","acl":{"read":{},"write":{}},"createdAt":null,"updatedAt":null,"name":"cc"}'
```

Example response:

```json
{"id":"/db/Teacher/11","version":1,"acl":null,"createdAt":"2025-08-23T18:14:17.251Z","updatedAt":"2025-08-23T18:14:17.251Z","name":"cc"}
```

### Get records

```bash
curl -X 'GET' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db/{tableName}' \
  -H 'accept: application/json' \
  -H 'Authorization: BAT <BAT_TOKEN>'
```

Example response:

```json
[{"id":"/db/Teacher/11","version":1,"acl":null,"createdAt":"2025-08-23T18:14:17.251Z","updatedAt":"2025-08-23T18:14:17.251Z","name":"cc"}]
```

### Update a record

```bash
curl -X 'PUT' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db/{tableName}/{id}' \
  -H 'accept: application/json' \
  -H 'Authorization: BAT <BAT_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "/db/Demo123/123321",
  "Name": "abc"
}'
```

Example response:

```json
{"id":"/db/Demo123/123321","version":3,"acl":null,"createdAt":"2025-09-02T06:10:44.733Z","updatedAt":"2025-09-02T06:24:59.72Z","Name":"abc"}
```

### Delete a record

```bash
curl -X 'DELETE' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db/{tableName}/{id}' \
  -H 'accept: */*' \
  -H 'Authorization: BAT <BAT_TOKEN>'
```

### List all tables

```bash
curl -X 'GET' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db' \
  -H 'accept: application/json' \
  -H 'Authorization: BAT <BAT_TOKEN>'
```

Example response:

```json
["/db/Demo123","/db/Object","/db/String","/db/User","/db/Teacher", "..."]
```

### Run a native SQL query

Pass the query in the `q` parameter (URL-encoded) and set `native=true`.

```bash
curl -X 'GET' \
  'https://<warehouse-id>.<warehouse-domain>/baas/v1/db/query?q=select%20%2A%20from%20Demo&native=true' \
  -H 'accept: application/json' \
  -H 'Authorization: BAT <BAT_TOKEN>'
```

Example response:

```json
[
  {"header":{"columnDefinitions":[{"tableName":"Demo","columnName":"id","columnType":"long","columnWidth":0},{"tableName":"Demo","columnName":"Age","columnType":"Integer","columnWidth":0},{"tableName":"Demo","columnName":"Name","columnType":"String","columnWidth":0}]},"row":null,"message":null},
  {"header":null,"row":{"Demo:id":"700334bc-e702-415e-a08f-42c5976c894f","Demo:Age":10,"Demo:Name":"Actian1"},"message":null}
]
```
