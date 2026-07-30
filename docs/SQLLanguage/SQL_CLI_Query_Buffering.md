---
title: "SQL CLI Query Buffering"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_CLI_Query_Buffering.htm"
canonical_id: "actian-data-platform-sql-cli-query-buffering"
---

## SQL CLI Query Buffering

Each query that is typed into the SQL CLI is placed in a query buffer rather than executed immediately. Queries are executed when the \go (or \g) execution command is typed. The results, by default, appear on your terminal.

For example, assume you have a table called, employee, that lists all employees in your company. If you want to see a list of those employees who live in a particular city (cityA), enter the following statement:

```
select name from employee where city='cityA'\g
```

The query is placed in the query buffer and executed when you enter \g. The returned rows display on your terminal. (If you type \g twice, your query is executed twice.)

Several other operations can also be performed on the query buffer, including:

- Editing the contents
- Printing the contents

- Writing the contents to another file

After a \go command, the query buffer is cleared if another query is typed in, unless a command that affects the query buffer is typed first. Commands that retain the query buffer contents are:

```
\append     or     \a\edit       or     \e\print      or     \p\bell\nobell
```

For example, typing:

```
help parts\goselect * from parts
```

results in the query buffer containing:

```
select * from parts
```

Whereas, typing:

```
help parts\go\printselect * from parts
```

results in the query buffer containing:

```
help partsselect * from parts
```

This feature can be overridden by executing the \append command before executing the \go command, or by specifying the -a flag when issuing the sql command to begin your session.
