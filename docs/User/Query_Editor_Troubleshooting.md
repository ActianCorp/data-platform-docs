---
title: "Query Editor Troubleshooting"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Query_Editor_Troubleshooting.htm"
canonical_id: "actian-data-platform-query-editor-troubleshooting"
---

## Query Editor Troubleshooting

You get an idle session timeout.

Idle Query Editor sessions are terminated after 24 hours.

You get a message about an expired certificate and the browser refuses to connect to Query Editor.

This situation can occur with warehouses that have not been started in over a month.

Simply stop and start the warehouse, and this will update the certificate. See [Stop a Warehouse](../User/Stop_a_Warehouse.md) and [Restart a Warehouse](../User/Restart_a_Warehouse.md).

You get this error: “User authorization check failed. Either the user is not known to this installation, or an incorrect password was supplied.”

You are not authorized to connect to the database.

Contact your system administrator or DBA to add you as a user.

You get a browser-specific “cannot reach this page” error message.

Your IP address is not Allow Listed.

Add your IP address to the Allow Listed IPs and reopen the Query Editor. For instructions, see [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md) and [Launch Query Editor](../User/Launch_Query_Editor.md).

You get a “Session Expired” error message.

The warehouse was stopped or the connection timed out when your window was open.

You must start a new session by navigating to the [Warehouse Details](../User/Warehouse_Details.md) page and launching a new Query Editor session. For instructions, see [Launch Query Editor](../User/Launch_Query_Editor.md).
