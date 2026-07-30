---
title: "How Authentication Works"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "How_Authentication_Works.htm"
canonical_id: "actian-data-platform-how-authentication-works"
---

## How Authentication Works

The creator of the warehouse has exclusive access to Query Editor and must explicitly authorize other users (by creating the user in SQL). For more information, see [Add Native Users](../User/Add_Native_Users.md).

Query Editor attempts to connect to the warehouse using the current console user. If the user is not registered with the warehouse, the user will encounter errors. If the user is authorized, the connection will be seamless to the user.

The Query Editor will open a persistent connection to the db database for the editor window and load the schema for the database upon launch.

The connection will persist for eight hours or until the warehouse shuts down, whichever comes first. Upon session expiration, you must restart Query Editor.

The icon indicator to the right of the connection configuration dropdown provides the status of the connection selected:

AWS AV-1 and Azure: ![](images/SQL_Editor_connection_indicator.png) indicates successful connection. If the connection fails on startup or expires, the status indicator will display a line through it to indicate a disconnected state.

Google Cloud and AWS AV-2: ![](images/GreenCheckmark.png) indicates successful connection. If the connection fails on startup or expires, the status indicator displays ![](images/RedCheckmark.png) to indicate a disconnected state.
