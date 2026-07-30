---
title: "COMMENT ON"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "COMMENT_ON.htm"
canonical_id: "actian-data-platform-comment-on"
---

## COMMENT ON

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL

The COMMENT ON statement creates a comment on a table, view, or column.

To display the comments, use the HELP COMMENT statement (not valid in Query Editor).

To delete the comments, issue the COMMENT ON statement and specify an empty string (' '). Comments on tables and views are deleted when the table or view is dropped.

To query comments on a certain table, use the iidbms_comment system catalog.

This statement has the following format:

```
[EXEC SQL] COMMENT ON             TABLE [schema.]name |             VIEW [schema.]name |            COLUMN [schema.]table_name.column_name              IS 'remark_text'
```

**name**

:   Specifies the name of the object for which the comment is defined.

:   For COMMENT ON VIEW the name must be the name of a view.

:   For COMMENT ON TABLE the name can be the name of a table or view.

**remark_text**

:   Defines the text of the comment. The text string must be surrounded by single quotes.

:   **Limits:** The maximum length for a comment is 1600 characters.

## COMMENT ON Examples

Store comments about a table:

1. Create a comment on the authors table.

```
COMMENT ON TABLE authors IS   'It was the best of times, it was the worst   of times. It was...'
```

2. Delete comments on the authors table.

```
COMMENT ON TABLE authors IS '';
```

3. Comment on column, name, in the authors table.

```
COMMENT ON COLUMN authors.name IS 'Call me Ishmael';
```
