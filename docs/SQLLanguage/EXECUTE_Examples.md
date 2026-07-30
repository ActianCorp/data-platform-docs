---
title: "EXECUTE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "EXECUTE_Examples.htm"
canonical_id: "actian-data-platform-execute-examples"
---

## EXECUTE Examples

1. Although the COMMIT statement can be prepared, once the statement is executed, the prepared statement becomes invalid.

    For example, the following code causes an error on the second EXECUTE statement.

```
statement_buffer = 'commit';    exec sql prepare s1 from :statement_buffer;    process and update data;    exec sql execute s1;    /* Once committed, 's1'	is lost */    process and update more data;    exec sql execute s1;    /* 's1' is NOT a valid statement name */
```

2. When leaving an application, each user deletes all their rows from a working table. User rows are identified by their different access codes. One user can have more than one access code.

```
read group id from terminal;statement_buffer =    'delete from ' + group_id +     ' where access_code = ?';exec sql prepare s2 from :statement_buffer;read access_code from terminal;loop while (access_code <> 0)exec sql execute s2 using :access_code;    read access_code from terminal;end loop;exec sql commit;
```
