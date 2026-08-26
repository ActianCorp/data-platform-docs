---
title: "MCP Server for Platform Management"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: ""
canonical_id: "actian-data-platform-mcp-server-platform-management"
---

# MCP Server for Platform Management

This MCP server lets you manage and observe your platform resources (warehouses,
tenant entitlements, usage, events, and telemetry) from an AI client using natural
language. It implements the
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/), an open standard
for connecting AI clients to external tools and data.

After the server is connected to an MCP-aware client, such as Claude Desktop,
Claude Code, or the MCP Inspector, you can ask questions such as
*"list my warehouses"* or *"show usage for warehouse `wh-123` last week"*, and the
client calls the matching tool on the server.

!!! note "This Is Not the Warehouse SQL Endpoint"

    Actian offers two different MCP servers, and both are reached at a path
    named `/mcp`. This page covers the **platform management** server, whose tools
    administer warehouses and report on tenant usage. It does not run SQL and
    cannot read your table data.

    To explore schemas and run SQL queries against a warehouse, use the MCP Server
    for Analytics Engine instead. That server is enabled per warehouse and is
    documented separately in the
    [Actian MCP Server documentation](https://docs.actian.com/mcp-server/). See
    the *Actian Data Platform* page in the *Analytics Engine* section.

## Server Capabilities

The server speaks MCP over HTTP streamable transport at the path `/mcp`, and
exposes 12 tools across six domains.

| Domain | Tools | Purpose |
| --- | --- | --- |
| Warehouse | `list_warehouses`, `get_warehouse`, `start_warehouse`, `stop_warehouse`, `scale_warehouse`, `update_warehouse_allow_list` | Manage warehouses (lifecycle, scale, network allow list) |
| Tenant | `get_tenant_details`, `get_tenant_entitlements` | Inspect tenant quota, feature flags, and entitlements |
| Usage | `get_usage_details` | Retrieve metered consumption data for a warehouse |
| Domain events | `get_warehouse_domain_events` | Retrieve CloudEvents emitted by a warehouse or other subject |
| Telemetry | `get_telemetry_metrics` | Retrieve telemetry metrics (for example, CPU) for a resource |
| Utility | `server_status` | Confirm the server is reachable and authentication is working |

The server does not publish MCP resources or prompts. Its surface is tools only.
If your client has a resources or prompts panel, it is empty for this server. That
is expected; use the tool catalog instead.

### Service Endpoints

| Path | Method | Purpose |
| --- | --- | --- |
| `/mcp` | POST | MCP protocol endpoint. All tool calls go here |
| `/health` | GET | Liveness probe; returns `{"status": "ok"}` |
| `/mcp/apiinfo` | GET | Deployment information: `service`, `version`, `gitCommit`, `deploymentName` |
| `/.well-known/oauth-protected-resource/mcp` | GET | OAuth Protected Resource Metadata (resource URL, issuer, supported scopes, client ID) |

## Connecting MCP Client

The server is a full OAuth 2.0 protected resource. A client that supports remote
MCP servers drives the authorization flow itself, opening a browser, signing you
in, and attaching the result to every request, so you do not manage any
credentials by hand.

!!! note "Supported Clients"

    Actian currently supports connecting with the MCP Inspector, Claude (Desktop
    and Code), and VS Code. If you need a different client supported,
    [contact support](Contact_Support.md).

Every client needs the same two things to add the server.

| What | Value |
| --- | --- |
| Server URL | `https://<mcp-host>/mcp` |
| Client ID | Read from the Protected Resource Metadata at `https://<mcp-host>/.well-known/oauth-protected-resource/mcp` |

No client secret is needed. Leave that field blank if your client asks for one.

Claude also needs a **local callback port**, the port on your machine that it
temporarily listens on to receive the OAuth redirect during login. This is fixed
at `3118`; it is registered as part of the client ID's redirect URI and is not a
value you choose yourself.

=== "Claude Code"

    Claude Code takes the client ID and callback port as explicit arguments:

    ```bash
    claude mcp add aap-mcp \
      --transport http \
      https://<mcp-host>/mcp \
      --client-id <CLIENT_ID> \
      --callback-port 3118
    ```

=== "VS Code"

    Add a server entry to `mcp.json` with just the URL:

    ```json
    {
      "servers": {
        "aap-mcp": {
          "type": "http",
          "url": "https://<mcp-host>/mcp"
        }
      }
    }
    ```

    When you first connect, VS Code opens an OAuth dialog asking for a client ID
    and client secret. Enter the client ID as described above and leave the
    secret field blank.

### Verifying Connection

Once your client is connected, ask it to call the `server_status` tool (see
[Utility Tools](#utility-tools)), for example, *"is the MCP server working?"* It
confirms the server is reachable and that your authentication is active.

## Scopes

Each tool requires one of these scopes, granted based on your account's
permissions:

| Scope | Used by |
| --- | --- |
| `read:warehouses` | `list_warehouses`, `get_warehouse`, `get_usage_details` |
| `write:warehouses` | `start_warehouse`, `stop_warehouse`, `scale_warehouse`, `update_warehouse_allow_list` |
| `read:tenant` | `get_tenant_details`, `get_tenant_entitlements` |
| `retrieve:events` | `get_warehouse_domain_events` |
| `retrieve:telemetry` | `get_telemetry_metrics` |

If your account does not have a scope a tool needs, that tool call fails with an
authorization error. See [Troubleshooting](#troubleshooting).

## Tool Conventions

These conventions apply to every tool:

- Tools resolve your identity automatically once your client is connected. You
  never pass tokens, user names, or tenant IDs as tool parameters.
- Tools marked **read-only** do not change state.
- Dates are ISO 8601 strings. In a date range, `from_date` must be strictly
  earlier than `to_date`.
- Invalid input is returned as a structured error that names the offending field.

## Warehouse Tools

### list_warehouses

Lists the warehouses visible to you. Read-only. Scope: `read:warehouses`. No
parameters.

Example prompt:

> "List all my warehouses."

Response shape:

```json
{
  "resources": [
    { "id": "wh-abc-123" }
  ],
  "count": 1
}
```

Only `id` is guaranteed on each resource. Additional fields returned by the
platform, such as name, status, or region, are passed through unchanged.

### get_warehouse

Gets the full details of a single warehouse. Read-only. Scope: `read:warehouses`.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `warehouse_id` | string (non-empty) | Yes | Warehouse identifier |

Example prompt:

> "Show me details for warehouse `wh-abc-123`."

Example tool call:

```json
{ "warehouse_id": "wh-abc-123" }
```

As with `list_warehouses`, only `id` is guaranteed; other fields are passed through.

### start_warehouse

Starts a stopped warehouse. Scope: `write:warehouses`.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `warehouse_id` | string (non-empty) | Yes | Warehouse identifier |

Example prompt:

> "Start warehouse `wh-abc-123`."

Example response:

```json
{
  "operation_status": "in_progress",
  "warehouse_id": "wh-abc-123",
  "warehouse_status": "starting"
}
```

`operation_status` is one of `in_progress`, `succeeded`, `rejected`, or `failed`.
Starting is asynchronous. Poll `get_warehouse` to confirm the warehouse has
reached the state you want.

### stop_warehouse

Stops a running warehouse. Scope: `write:warehouses`.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `warehouse_id` | string (non-empty) | Yes | Warehouse identifier |

Example prompt:

> "Stop warehouse `wh-abc-123`."

### scale_warehouse

Scales a warehouse to a target number of Actian Units (AUs). Scope:
`write:warehouses`.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `warehouse_id` | string (non-empty) | Yes | Warehouse identifier |
| `avalanche_units` | integer (greater than 0) | Yes | Target AU count |

Example prompt:

> "Scale warehouse `wh-abc-123` to 8 units."

Example tool call:

```json
{ "warehouse_id": "wh-abc-123", "avalanche_units": 8 }
```

### update_warehouse_allow_list

Updates a warehouse's IP allow list by adding entries, removing entries, or
relabeling existing entries. Scope: `write:warehouses`.

At least one of `additions`, `removals`, or `changeLabel` must be non-empty.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `warehouse_id` | string (non-empty) | Yes | Warehouse identifier |
| `allow_list_changes.additions` | `LabeledCIDR[]` | No | Entries to add |
| `allow_list_changes.removals` | `LabeledCIDR[]` | No | Entries to remove |
| `allow_list_changes.changeLabel` | `LabeledCIDR[]` | No | Existing entries whose label should change |

A `LabeledCIDR` has this shape:

```json
{ "allowListIp": "10.1.0.0/24", "label": "Corporate Network" }
```

`allowListIp` is required and must be a valid IP address or CIDR block. `label` is
optional for `additions` and `removals`, and is expected for `changeLabel`, whose
purpose is to set a new label.

Example prompt:

> "Add `10.1.0.0/24`, labeled Corporate Network, to the allow list of warehouse
> `wh-abc-123`."

Example tool call:

```json
{
  "warehouse_id": "wh-abc-123",
  "allow_list_changes": {
    "additions": [
      { "allowListIp": "10.1.0.0/24", "label": "Corporate Network" }
    ]
  }
}
```

## Tenant Tools

### get_tenant_details

Gets details for your tenant, including AU quota and consumption and the enabled
feature flags. Read-only. Scope: `read:tenant`. No parameters.

Example prompt:

> "What is my tenant's AU quota, and which feature flags are enabled?"

### get_tenant_entitlements

Gets your tenant's entitlements, grouped by resource type (`compute` and `storage`),
sorted by entitlement end date, along with the current entitlement phase.
Read-only. Scope: `read:tenant`. No parameters.

The entitlement phase is one of `trial`, `free-trial-exhausted`,
`free-trial-expired`, `enterprise`, or `no-entitlements`.

Example prompt:

> "Show me my tenant's current entitlements and trial status."

## Usage Tools

### get_usage_details

Retrieves metered consumption for one warehouse over a date range, broken down by
granularity. Results are keyed by category, for example, `DWH`, `DWH_API`, and
`DWH_backup`, with consumption records per period. Read-only. Scope:
`read:warehouses`.

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `warehouse_id` | string (non-empty) | Yes | — | Warehouse identifier |
| `from_date` | ISO date (`YYYY-MM-DD`) | Yes | — | Start of the range (inclusive) |
| `to_date` | ISO date (`YYYY-MM-DD`) | Yes | — | End of the range (must be later than `from_date`) |
| `granularity` | enum | No | `daily` | One of `hourly`, `daily`, `weekly`, `monthly`, `quarterly`, `yearly` |

Example prompt:

> "Show me daily usage for warehouse `wh-abc-123` between 2026-05-01 and
> 2026-05-31."

Example tool call:

```json
{
  "warehouse_id": "wh-abc-123",
  "from_date": "2026-05-01",
  "to_date": "2026-05-31",
  "granularity": "daily"
}
```

Response shape:

```json
{
  "duration": "P1D",
  "data": {
    "DWH": [
      {
        "id": "wh-abc-123",
        "consumption": {
          "2026-05-01T00:00:00Z": [
            { "ppid": "compute", "unit": "AUSeconds", "quantity": 3600 }
          ]
        }
      }
    ]
  }
}
```

## Domain Events Tools

### get_warehouse_domain_events

Retrieves Actian-formatted CloudEvents for a subject, normally a warehouse,
within a date range. Read-only. Scope: `retrieve:events`.

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `subject` | string (non-empty) | Yes | — | CloudEvent subject, normally the warehouse or resource ID |
| `from_date` | ISO date | Yes | — | Start of the range (inclusive) |
| `to_date` | ISO date | Yes | — | End of the range (must be later than `from_date`) |
| `max_count` | integer (1–1000) | No | `1000` | Maximum number of events to return |
| `sources` | string array | No | — | Filter by CloudEvent source. Each entry must match `tag:actian.com,2024:event/source/{sourceId}/{customPart}` |
| `event_types` | string array | No | — | Filter by CloudEvent type. Each entry must start with `com.actian.` |

Example prompt:

> "Show me all warehouse events for `wh-abc-123` last week."

Example tool call:

```json
{
  "subject": "wh-abc-123",
  "from_date": "2026-05-25",
  "to_date": "2026-06-01",
  "max_count": 100
}
```

Returned event shape (CloudEvents 1.0):

```json
{
  "id": "<uuid>",
  "source": "tag:actian.com,2024:event/source/<sourceId>/<custom>",
  "specversion": "1.0",
  "type": "com.actian.<...>",
  "datacontenttype": "application/json",
  "dataschema": "<url>",
  "subject": "wh-abc-123",
  "time": "2026-05-26T12:34:56Z",
  "actianeventversion": "0.1.1",
  "data": {
    "tenant": "...",
    "operator": "...",
    "operation": "...",
    "description": "...",
    "traceid": "<uuid>"
  }
}
```

## Telemetry Tools

### get_telemetry_metrics

Retrieves telemetry metrics for a resource (a warehouse, database, or job) over a
time window. Read-only. Scope: `retrieve:telemetry`.

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `resource_id` | string (non-empty) | Yes | — | Resource identifier |
| `resource_type` | string array (at least one entry) | Yes | — | Any of `database`, `job`, `warehouse` |
| `from_date` | ISO date | Yes | — | Start of the range (sent as `timeStart`) |
| `to_date` | ISO date | Yes | — | End of the range (sent as `timeEnd`, must be later than `from_date`) |
| `metric` | string | No | — | Restrict results to a single metric name |
| `from_offset` | integer (0 or greater) | No | `0` | Pagination offset |
| `size` | integer (1–99) | No | `10` | Page size. `from_offset` plus `size` must not exceed 10000 |

Example prompt:

> "Get telemetry metrics for warehouse `wh-abc-123` over the last 24 hours."

Example tool call:

```json
{
  "resource_id": "wh-abc-123",
  "resource_type": ["warehouse"],
  "from_date": "2026-05-31",
  "to_date": "2026-06-01",
  "size": 50
}
```

Returned metric shape:

```json
{
  "timestamp": "2026-05-31T12:00:00Z",
  "labels": { "warehouse": "wh-abc-123" },
  "metric": { "type": "cpu_utilization", "value": 0.42 }
}
```

## Utility Tools

### server_status

Confirms that the server is running and reachable, and that your authentication is
propagating correctly. Read-only. No parameters. No specific scope is required;
any authenticated connection can call it.

Example response:

```json
{
  "status": "ok",
  "message": "MCP Warehouse Server is running.",
  "authenticated": true,
  "scopes": ["read:warehouses"]
}
```

## Troubleshooting

Tool failures are returned as structured errors with this shape:

```json
{
  "error_code": "authorization_error",
  "message": "Required scope 'read:warehouses' is missing"
}
```

The `error_code` value is one of `authentication_error`, `authorization_error`,
`validation_error`, `service_error`, or `internal_error`.

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `error_code` is `authorization_error` | Your account does not have the scope the tool requires | Reconnect or re-authenticate your client. If it persists, ask your administrator to grant the required access. See [Scopes](#scopes). |
| `error_code` is `authentication_error` | Your client's connection is not authenticated, or your session has expired | Reconnect or re-authenticate your client. |
| The error message names a parameter, for example, a blank ID, `from_date` not earlier than `to_date`, or a malformed CIDR block | Invalid tool parameters | Check the parameter table for the tool you called; the message identifies the offending field. |
| `error_code` is `validation_error` | The platform response did not match the expected schema | Usually transient. Retry. If it persists, [contact support](Contact_Support.md). |

### Checking Server Reachability

```bash
curl -sS 'https://<mcp-host>/health'
```

Returns:

```json
{"status":"ok"}
```

### Checking Deployed Version

Useful when confirming whether a fix has been deployed:

```bash
curl -sS 'https://<mcp-host>/mcp/apiinfo'
```

Returns:

```json
{
  "service": "aap-mcp-server",
  "version": "<APP_VERSION>",
  "gitCommit": "<APP_GIT_COMMIT>",
  "deploymentName": "<APP_DEPLOYMENT_NAME>"
}
```
