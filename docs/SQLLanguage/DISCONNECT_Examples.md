---
title: "DISCONNECT Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DISCONNECT_Examples.htm"
canonical_id: "actian-data-platform-disconnect-examples"
---

## DISCONNECT Examples

1. Disconnect from the current database.

```
EXEC SQL DISCONNECT;
```

2. Disconnect a session in a multi-session application by specifying the connection name.

```
EXEC SQL DISCONNECT accounting;
```

3. Disconnect a session by specifying its session identifier.

```
EXEC SQL DISCONNECT SESSION 99;
```

4. On an error, roll back pending updates, disconnect the database session.

```
EXEC SQL WHENEVER SQLERROR GOTO err;	...	err:	EXEC SQL ROLLBACK;	EXEC SQL DISCONNECT;
```
