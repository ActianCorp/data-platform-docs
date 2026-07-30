---
title: "Status Information in Multiple Sessions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Status_Information_in_Multiple_Sessions.htm"
canonical_id: "actian-data-platform-status-information-in-multiple-sessions"
---

## Status Information in Multiple Sessions

The SQL Communications Area (SQLCA) is a data area in which the Actian Data Platform passes query status information to your application program. Although an application can sustain multiple sessions, there is only one SQLCA per application. However, the values returned by the INQUIRE_SQL(ERRORCODE) and INQUIRE_SQL(ERRORTEXT) statements are specific to a session.

If sessions are switched in a select loop (for example, by calling a routine that switches sessions) and database statements are executed in the alternate session, the values in the SQLCA are reset. When returning to the original session, the values in the SQLCA reflect the results of the statements issued in the alternate session and not the results of the select loop.

When sessions are switched, the values in the SQLCA fields are not updated until after the first SQL statement in the new session has completed. In contrast, the error information returned by INQUIRE_SQL(ERRORTEXT and ERRORNO) always applies to the current session. The results of the session switch are returned in SQLSTATE.

When an application switches sessions within a select loop or other block statement, the SQLCA field values are updated to reflect the status of the statements executed inside the nested session. After the application switches back to the session with the loop, the SQLCA field values reflect the status of the last statement in the nested session. SQLCODE and SQLWARN are not updated until the statement immediately following the loop completes. (The information obtained by INQUIRE_SQL is not valid either until the statement following a loop completes.) For this reason, the application must reset the SQLCODE and SQLWARN fields before continuing the loop.
