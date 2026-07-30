---
title: "CREATE VIEW"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_VIEW.htm"
canonical_id: "actian-data-platform-create-view"
---

## CREATE VIEW

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE VIEW statement defines a virtual table.

This statement has the following format:

```
CREATE VIEW view_name [(column_name{, column_name})] AS [WITH common_table_expression] select_stmt
```

**view_name**

:   Defines the name of the view. It must be a valid object name.

**select_stmt**

:   Is a SELECT statement, as described in the SELECT statement description in this chapter.

## CREATE VIEW Example

Create history tables and a current table with a view over all of them. Insert values. Select data from the current table and from the master view. Update some data and perform the select again.

```
DROP IF EXISTS current, history_2010, history_2011, history_2012;
```

```
CREATE TABLE current (
```

```
   id INTEGER NOT NULL,
```

```
   name VARCHAR(20) NOT NULL,
```

```
   effective_start DATE NOT NULL,
```

```
   effective_end DATE);
```

```
CREATE TABLE history_2010 AS SELECT * FROM current;
```

```
CREATE TABLE history_2011 AS SELECT * FROM current;
```

```
CREATE TABLE history_2012 AS SELECT * FROM current;
```

```
CREATE VIEW master AS SELECT id, name, effective_start, effective_end FROM current
```

```
UNION ALL
```

```
SELECT id, name, effective_start, effective_end FROM history_2010 WHERE effective_end IS NOT NULL
```

```
UNION ALL
```

```
SELECT id, name, effective_start, effective_end FROM history_2011 WHERE effective_end IS NOT NULL
```

```
UNION ALL
```

```
SELECT id, name, effective_start, effective_end FROM history_2012 WHERE effective_end IS NOT NULL;
```

```
\p\g
```

```
INSERT INTO current (id, name, effective_start) VALUES (1,'tins','2012-01-23'),(2,'bags','2012-01-30'),(3,'boxes','2012-01-30');
```

```
INSERT INTO history_2010 (id, name, effective_start, effective_end) VALUES
```

```
(1,'tins','2010-01-23','2011-09-30'),(2,'bags','2010-01-30','2010-11-01'),(3,'boxes','2010-12-25','2011-03-20');
```

```
INSERT INTO history_2011 (id, name, effective_start, effective_end) VALUES
```

```
(1,'tins','2011-09-30','2012-01-23'),(2,'bags','2010-11-01','2012-01-30'),(3,'boxes','2011-03-20','2012-01-30');
```

```
\p\g
```

```
SELECT id, MAX(name), MAX(effective_start), MAX(CASE WHEN IFNULL(effective_end,'0001-01-01') = '0001-01-01' THEN 'CURRENT' ELSE CHAR(effective_end) END) FROM current GROUP BY id ORDER BY 2;
```

```
\p\g
```

```
SELECT id, MAX(name), MAX(effective_start), MAX(effective_end) FROM master GROUP BY id ORDER BY 2;
```

```
\p\g
```

```
SELECT id, MAX(name), MAX(effective_start), MAX(effective_end) FROM history_2011 GROUP BY id ORDER BY 2;
```

```
\p\g
```

```
UPDATE current SET effective_end = CURRENT_DATE WHERE id = 2;
```

```
INSERT INTO history_2012 SELECT * FROM current WHERE effective_end IS NOT NULL;
```

```
\p\g
```

```
SELECT id, MAX(name), MAX(effective_start), MAX(CASE WHEN IFNULL(effective_end,'0001-01-01') = '0001-01-01' THEN 'CURRENT' ELSE  CHAR(effective_end) END) FROM current GROUP BY id ORDER BY 2;
```

```
\p\g
```

```
SELECT id, MAX(name), MAX(effective_start), MAX(effective_end) FROM master GROUP BY id ORDER BY 2;
```

```
\p\g
```

```
SELECT id, MAX(name),  MAX(effective_start), MAX(effective_end) FROM history_2011 GROUP BY id ORDER BY 2;
```

```
\p\g
```
