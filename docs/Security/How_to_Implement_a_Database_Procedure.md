---
title: "How to Implement a Database Procedure"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "How_to_Implement_a_Database_Procedure.htm"
canonical_id: "actian-data-platform-how-to-implement-a-database-procedure"
---

## How to Implement a Database Procedure

To implement a database procedure, follow these basic steps:

1. Create the procedure using the [CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md) statement. You can do this interactively or in Embedded SQL.
2. Grant EXECUTE permission on the database procedure to specified users, groups, or roles, as described in [Object Permissions (Grants)](../Security/Object_Permissions_(Grants).md).

3. Invoke the database procedure by issuing an [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md) statement or triggering a security alarm. Any user who has been granted EXECUTE permission can perform this step.

## Database Procedure Example

The following database procedure accepts as input an employee ID number. The employee matching that ID is moved from the employee table and added to the emptrans table.

```
CREATE PROCEDURE move_emp
```

```
   (id INTEGER NOT NULL) AS
```

```
BEGIN
```

```
   INSERT INTO emptrans
```

```
      SELECT * FROM employee
```

```
         WHERE id = :id;
```

```
   DELETE FROM employee
```

```
      WHERE id = :id;
```

```
END;
```
