---
title: "RETURN ROW"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "RETURN_ROW.htm"
canonical_id: "actian-data-platform-return-row"
---

## RETURN ROW

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc

The RETURN ROW statement composes a row using the values computed by the result expressions and returns it to the caller of the procedure in which it is contained. It can only be used within a database procedure. A RETURN ROW statement can be executed more than once in a single procedure invocation (for example, from within a FOR or WHILE loop) and offers a mechanism for passing multiple row images back to the caller.

Procedures containing RETURN ROW statements must also contain a RESULT ROW clause and the number of expressions in each RETURN ROW statement must be equal to the number of entries in the RESULT ROW clause. The data type of the result expressions must also be compatible with the corresponding entries in the RESULT clause.

The RETURN ROW statement can only be used in a procedure called directly from a host language program. It cannot be used in a procedure that is called from another database procedure.

#### Syntax

The RETURN ROW statement has the following format:

```
RETURN ROW (result_expression {,result_ expression});
```

#### Permissions

You must have CREATE_PROCEDURE privilege.

#### Related Statements

[CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md)

[FOR - ENDFOR](../SQLLanguage/FOR_-_ENDFOR.md)[](../SQLLanguage/FOR_-_ENDFOR.md)
