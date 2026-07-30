---
title: "MESSAGE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "MESSAGE_Examples.htm"
canonical_id: "actian-data-platform-message-examples"
---

## MESSAGE Examples

1. Return debugging text to the application:

```
MESSAGE 'Inserting new row';    INSERT INTO tab VALUES (:val);    MESSAGE 'About to commit change';    COMMIT;    MESSAGE 'Deleting newly inserted row';    DELETE FROM tab WHERE tabval = :val;    MESSAGE 'Returning with pending change';    RETURN;
```

2. Return a message number to the application. The application can extract the international message text out of a message file.

```
IF iierrornumber > 0 THEN        MESSAGE 58001;    ELSEIF iirowcount <> 1 THEN        MESSAGE 58002;    ENDIF;
```

3. Send a message to the error log file:

```
MESSAGE 'User attempting to update payroll table'    WITH DESTINATION = (ERROR_LOG);
```
