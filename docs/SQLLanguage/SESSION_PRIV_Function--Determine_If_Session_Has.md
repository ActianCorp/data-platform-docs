---
title: "SESSION_PRIV Function--Determine If Session Has a Privilege"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SESSION_PRIV_Function--Determine_If_Session_Has.htm"
canonical_id: "actian-data-platform-session-priv-function-determine-if-session-has"
---

## SESSION_PRIV Function--Determine If Session Has a Privilege

The SESSION_PRIV function determines whether the current session has a subject privilege, or can request it.

This function has the following format:

```
SESSION_PRIV('subject_priv')
```

where subject_priv is any single subject privilege name, such as operator, specified as a text string in upper or lower case. Valid subject privileges are listed under [CREATE PROFILE](../SQLLanguage/CREATE_PROFILE.md).

The following values are returned:

**Y**

:   Indicates session has privilege.

**N**

:   Indicates session does not have the privilege.

**R**

:   Indicates the session can request the privilege and make it active.

Example: The following checks whether the current session has auditor privilege:

```
SELECT SESSION_PRIV('AUDITOR');
```
