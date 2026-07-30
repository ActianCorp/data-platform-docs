---
title: "Ways to Obtain Status Information"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Ways_to_Obtain_Status_Information.htm"
canonical_id: "actian-data-platform-ways-to-obtain-status-information"
---

## Ways to Obtain Status Information

The following functions enable an embedded SQL application program to obtain status information:

**SESSION_PRIV**

:   Returns session privilege information.

**DBMSINFO**

:   Returns information about the current session.

**INQUIRE_SQL**

:   Returns information about the last database statement that was executed.

**SQLCA (SQL Communications Area)**

:   Returns status and error information about the last SQL statement that was executed.

**SQLCODE and SQLSTATE**

:   Stand-alone variables in which the DBMS returns status information about the last SQL statement that was executed.
