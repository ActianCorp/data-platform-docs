---
title: "Description"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Description.htm"
canonical_id: "actian-data-platform-description"
---

## Description

The CREATE PROCEDURE statement creates a database procedure that is managed as a named database object by the Actian Data Platform. A database procedure can be executed directly using the EXECUTE PROCEDURE statement or can be invoked by a rule.

A procedure that is directly executed can contain any of the following statements:

- [COMMIT](../SQLLanguage/COMMIT.md)
- [DELETE](../SQLLanguage/DELETE.md)

- [ENDLOOP](../SQLLanguage/ENDLOOP.md)
- [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md)

- [FOR - ENDFOR](../SQLLanguage/FOR_-_ENDFOR.md)
- [IF - THEN - ELSE](../SQLLanguage/IF_-_THEN_-_ELSE.md)

- [INSERT](../SQLLanguage/INSERT.md)
- [MESSAGE](../SQLLanguage/MESSAGE.md)

- [RAISE DBEVENT](../SQLLanguage/RAISE_DBEVENT.md)
- [RAISE ERROR](../SQLLanguage/RAISE_ERROR.md)

- [REGISTER DBEVENT](../SQLLanguage/REGISTER_DBEVENT.md)
- [REMOVE DBEVENT](../SQLLanguage/REMOVE_DBEVENT.md)

- [RETURN](../SQLLanguage/RETURN.md)
- [RETURN ROW](../SQLLanguage/RETURN_ROW.md)

- [ROLLBACK](../SQLLanguage/ROLLBACK.md)
- [SELECT (Interactive)](../SQLLanguage/SELECT_(Interactive).md) and [SELECT (Embedded)](../SQLLanguage/SELECT_(Embedded).md)

- [UPDATE](../SQLLanguage/UPDATE.md)
- [WHILE - ENDWHILE](../SQLLanguage/WHILE_-_ENDWHILE.md)

- Assignment statements

Procedures invoked by [DELETE](../SQLLanguage/DELETE.md) or [UPDATE](../SQLLanguage/UPDATE.md) rules must not reference the old blob column values.

A procedure cannot contain any data definition statements, such as [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md), nor can a procedure create or drop another procedure. Database procedures can execute other database procedures.

The REPEATED clause cannot be used in a statement in the procedure body. However, database procedures confer the same performance benefits as the REPEATED clause.

In a procedure, SELECT statements must assign their results to local variables. Also, SELECT statements can return only a single row of data unless they are contained in a FOR statement. If more rows are returned, no error is issued, but only the first row retrieved is in the result variables.

Both procedure parameters and local variables can be used in place of any constant value in statements in the procedure body. The Actian Data Platform treats procedure parameters as local variables inside the procedure body, although they have an initial value assigned when the procedure is invoked. Preceding colons (:) are only necessary if the referenced name can be interpreted to see more than one object.

Assignment statements assign values (see [Assignment Operations](../SQLLanguage/SQL_Operations.md)) to local variables and procedure parameters in the body of the procedure. Local variables are variables that are declared using the [DECLARE](../SQLLanguage/DECLARE.md) statement in the database procedure. The scope of these variables is the database procedure in which they are declared. Variable assignment statements use the = or := operator to assign values to local variables. The value assigned can be a constant or the result of the evaluation of an expression. The data types of the value and the local variable must be compatible.

Procedure parameters explicitly declared with the INOUT or OUT modes pass their values back to the calling procedure.

All statements, except a statement preceding an END, ENDFOR, or ENDIF, must be terminated with a semicolon.

If working interactively, the BEGIN and END keywords can be replaced with braces { }, but the terminating semicolon must follow the closing brace if another statement is entered after the CREATE PROCEDURE statement and before committing the transactions.
