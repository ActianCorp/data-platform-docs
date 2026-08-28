---
title: "Actian Data Platform REST APIs"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: ""
canonical_id: "actian-data-platform-rest-apis"
---

# Actian Data Platform REST APIs

This page is the starting point for programmatic access to the Actian Data Platform.
It explains which API to use for which task, how to authenticate, and gives a worked
example that logs in and then starts, scales, and stops a warehouse.

!!! warning "Keep Your Credentials Secret"

    The examples use placeholders such as `<ACCESS_TOKEN>` and `<warehouse-id>`.
    An access token is a credential. Treat it like a password. Never commit it to
    source control, paste it into a shared document, or include it in a support
    request. Rotate a token immediately if it is exposed.

## Choosing API

The platform exposes two independent REST APIs. They authenticate differently and
are scoped differently, so the first step is choosing the right one.

| | Control API | Warehouse Data API |
| --- | --- | --- |
| Use it to | Create, start, stop, scale, and configure warehouses; read tenant, usage, and entitlement information | Read and write data in one warehouse: manage schema, run CRUD operations, run SQL |
| Scope | Global. One endpoint covers every resource in your tenant | Per warehouse. Each warehouse has its own endpoint |
| Base URL | `https://<admiral-host>/api/v1` | `https://<warehouse-id>.<warehouse-domain>/baas/v1` |
| Authentication | Bearer token from the platform login endpoint | BAT token from the warehouse login endpoint |
| Availability | Always available | Must be enabled per warehouse, and the warehouse must be running |
| Documented in | This page | [Warehouse Data API (BaaS)](Warehouse_Data_API.md) |

Both APIs are separate from the SQL and loading interfaces. To load data in bulk,
use one of the documented loading methods instead of either REST API. For more
information, see the Data Loading Guide.

## Interactive Reference

Use the interactive specifications for the full endpoint list, including operations
that this page does not cover.

| API | Specification |
| --- | --- |
| Control API | `https://<admiral-host>/api-docs/` |
| Warehouse Data API | `https://<warehouse-id>.<warehouse-domain>/baas-doc/` |

The `<admiral-host>` and `<warehouse-domain>` values depend on the cloud and region
that your tenant runs in. The warehouse domain is shown on the warehouse
**Connections** page, for example, `avd.actiandatacloud.com` for Google Cloud.

## Authenticating

Platform user accounts authenticate against the identity management login endpoint
and receive an access token. Send that token as a bearer token on every subsequent
Control API request.

```bash
curl -X 'POST' \
  'https://api.im.actiandatacloud.com/v2/api/login' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "<platform-user>",
  "password": "<password>"
}'
```

!!! note "The Content-Type Header Is Required"

    The login request fails if the `Content-Type: application/json` header is not
    set. This is the most common cause of a login that works in a browser-based
    tool but fails from a script.

For a step-by-step walkthrough that uses an API client such as Postman, including
where to find each value, see
[API access with Platform User Accounts](API_access_with_Platform_User_Accounts.md).

Send the returned token on every Control API request:

```
Authorization: Bearer <ACCESS_TOKEN>
```

## Example: Starting, Scaling, Stopping Warehouse

The following sequence is the common administrative path: find your warehouse, start
it, resize it, and then shut it down. Every path is relative to
`https://<admiral-host>/api/v1`.

Two values recur throughout the examples.

| Placeholder | Meaning |
| --- | --- |
| `<resource-type>` | `warehouse` |
| `<warehouse-id>` | The resource identifier, for example, `av-xxxxxxxxxxxx` |

### 1. Listing Warehouses

```bash
curl -X 'GET' \
  'https://<admiral-host>/api/v1/resource/warehouse' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

The response wraps the list in `resources` and reports a `count`:

```json
{
  "resources": [
    {
      "resourceId": "av-xxxxxxxxxxxx",
      "resourceName": "sales-warehouse",
      "status": "Stopped",
      "avalancheUnits": 2,
      "platform": "Google",
      "regionId": "<region>"
    }
  ],
  "count": 1
}
```

The `status` value is one of `Creating`, `Create Failed`, `Running`, `Scaling`,
`Stopping`, `Stopped`, `Stop Failed`, `Starting`, `Start Failed`, `Deleting`, or
`Deleted`.

Optional query parameters narrow the result: `status`, `pageNumber`, `pageSize`, and
`viewType` (either `detail` or `basic`).

### 2. Starting Warehouse

```bash
curl -X 'PUT' \
  'https://<admiral-host>/api/v1/resource/warehouse/<warehouse-id>/start' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

No request body is required. A successful call returns `202 Accepted`:

```json
{
  "resourceId": "av-xxxxxxxxxxxx",
  "message": "<acceptance message>"
}
```

!!! note "Lifecycle Operations Are Asynchronous"

    A `202 Accepted` response means that the request was accepted, not that the
    warehouse is running. Poll `GET /resource/warehouse/<warehouse-id>` until
    `status` reaches `Running` before you connect or issue the next operation. A
    warehouse in a transitional state such as `Starting` or `Scaling` rejects
    further lifecycle requests.

### 3. Scaling Warehouse

Scaling takes a target size in Actian Units (AUs):

```bash
curl -X 'PUT' \
  'https://<admiral-host>/api/v1/resource/warehouse/<warehouse-id>/scale' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "avalancheUnits": 8
}'
```

The `avalancheUnits` value must be one of `2`, `4`, `8`, `16`, `32`, `64`, or `128`.
Any other value is rejected. The response mirrors the start response, returning
`resourceId` and a `message` with `202 Accepted`.

### 4. Stopping Warehouse

```bash
curl -X 'PUT' \
  'https://<admiral-host>/api/v1/resource/warehouse/<warehouse-id>/stop' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

To stop a warehouse automatically after a period of inactivity instead, use the
`idle-stop` endpoint. For more information, see
[Automatic Stopping of Idle Warehouses](Automatic_Stopping_of_Idle_Warehouses_or_Databas.md).

## Updating IP Allow List

Warehouse access is restricted by IP address, so automation that connects from a new
network requires an updated allow list. Send additions, removals, and label changes
in a single request:

```bash
curl -X 'PUT' \
  'https://<admiral-host>/api/v1/resource/warehouse/<warehouse-id>/allowlist-ip' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "additions": [
    { "allowListIp": "10.1.0.0/24", "label": "Corporate Network" }
  ]
}'
```

The body accepts three optional arrays (`additions`, `removals`, and `changeLabel`),
each holding at most 20 entries. Each entry requires `allowListIp`, which is an IPv4
address or CIDR block. The `label` value is an optional description of up to 40
characters, such as an organization, person, or location. Entries report a `status`
of either `applied` or `pending`.

For the console equivalent and the wider access control model, see
[Data Access and Authentication](../Security/Data_Access_and_Authentication.md).

## Other Operations

The preceding endpoints are the most commonly used ones. The interactive reference
also covers the following operations.

| Task | Endpoint |
| --- | --- |
| Create a warehouse | `POST /resource/warehouse` |
| Get one warehouse | `GET /resource/warehouse/<warehouse-id>` |
| Delete a warehouse | `DELETE /resource/warehouse/<warehouse-id>` |
| Restart a warehouse | `PUT /resource/warehouse/<warehouse-id>/restart` |
| Clone a warehouse | `POST /resource/warehouse/clone` |
| Tenant details and entitlements | `GET /tenant`, `GET /tenant/entitlements` |
| Current usage | `GET /usage/current`, `GET /usage/details/timeseries` |
| Backups | `GET /resource/warehouse/<warehouse-id>/backups` |
| Enable the Warehouse Data API | `PUT /resource/warehouse/<warehouse-id>/data-api/configure` |

## Working with Warehouse Data

After a warehouse is running, use the Warehouse Data API to manage schema, read and
write records, and run SQL over HTTP. This API authenticates separately, with a BAT
token that the warehouse itself issues.

For information about enabling the API, authenticating, and the full set of CRUD and
query examples, see [Warehouse Data API (BaaS)](Warehouse_Data_API.md).

## Managing from AI Client

If you prefer to run these operations in natural language rather than call endpoints
directly, the same warehouse, tenant, usage, and telemetry operations are available
as tools over the Model Context Protocol. For more information, see
[MCP Server for Platform Management](MCP_Server.md).
