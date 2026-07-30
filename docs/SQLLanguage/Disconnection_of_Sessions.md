---
title: "Disconnection of Sessions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Disconnection_of_Sessions.htm"
canonical_id: "actian-data-platform-disconnection-of-sessions"
---

## Disconnection of Sessions

To disconnect from the current session, the application issues the DISCONNECT statement. To disconnect a session other than the current session, specify the numeric session identifier or connection name. To disconnect all connected sessions, issue the DISCONNECT ALL statement. For more information, see [DISCONNECT](../SQLLanguage/DISCONNECT.md).

After an application disconnects from the current session in a multi-session application, the application must establish the current session by issuing the SET CONNECTION, SET_SQL(SESSION), or CONNECT statement. If no current session is in effect when an application issues a query, an error is returned.
