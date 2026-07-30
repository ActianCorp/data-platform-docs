---
title: "Example: Two Open Sessions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Example_3a_Two_Open_Sessions.htm"
canonical_id: "actian-data-platform-example-3a-two-open-sessions"
---

## Example: Two Open Sessions

The following example shows the use of two open sessions in an application that gathers project information for updating the projects database using the personnel database to verify employee identification numbers. This example illustrates session switching and the use of connection names.

```
exec sql begin declare section;
```

```
     empid integer;
```

```
     found integer;
```

```
...
```

```
exec sql end declare section;
```

```

```

```
/* Set up two database connections */
```

```

```

```
exec sql connect projects as 'projects';
```

```
exec sql connect personnel as 'personnel';
```

```

```

```
/* Set 'projects' database to be current session */
```

```

```

```
exec sql set connection 'projects';
```

```
display project form
```

```
position cursor to emp id field
```

```

```

```
/* Validate user-entered employee id against
```

```
** master list of employees in personnel
```

```
** database. */
```

```
     found = 0;
```

```
     load empid host variable from field on form
```

```
/* Switch to 'personnel' database session */
```

```
     exec sql set connection 'personnel';
```

```
     exec sql repeated select 1 into :found
```

```
          from employee
```

```
          where empid = :empid;
```

```
/* Switch back to 'project' database session */
```

```
     exec sql set connection 'projects';
```

```
     if (found !=1) then
```

```
          print 'Invalid employee identification'
```

```
     else
```

```
          position cursor to next field
```

```
     endif;
```

```
end if
```

```

```

```
/* program code to validate other fields in 'projectform' */
```

```
if user selects 'Save' menu item
```

```
     get project information and update 'projectinfo' table
```

```
...
```

```
exec sql disconnect 'personnel';
```

```
exec sql disconnect 'projects';
```
