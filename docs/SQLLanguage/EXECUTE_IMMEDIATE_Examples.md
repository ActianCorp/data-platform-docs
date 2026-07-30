---
title: "EXECUTE IMMEDIATE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "EXECUTE_IMMEDIATE_Examples.htm"
canonical_id: "actian-data-platform-execute-immediate-examples"
---

## EXECUTE IMMEDIATE Examples

1. The following example saves a table until the first day of the next year. Next_year and current_year are integer variables.

```
/* There is no need for a FROM clause in this ** SELECT */exec sql select date_part('year', date('now'))    into :current_year;next_year = current_year + 1;statement_buffer = 'save ' + table_name +     ' until Jan 1 ' + next_year;exec sql execute immediate :statement_buffer;
```

2. The following example reads an SQL statement from the terminal into a host string variable, statement_buffer. If the statement read is “quit,” the program ends. If an error occurs upon execution, the program informs the user.

```
exec sql include sqlca;read statement_buffer from terminal;loop while (statement_buffer <> 'QUIT')exec sql execute immediate :statement_buffer;    if (sqlcode = 0) then    exec sql commit;    else if (sqlcode = 100) then    print 'No qualifying rows for statement:';    print statement_buffer;    else     print 'Error        :', sqlcode;    print 'Statement    :', statement_buffer;    end if;    read statement_buffer from terminal;end loop;
```
