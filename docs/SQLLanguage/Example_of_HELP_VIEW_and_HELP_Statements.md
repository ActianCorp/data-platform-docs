---
title: "Example of HELP VIEW and HELP Statements"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Example_of_HELP_VIEW_and_HELP_Statements.htm"
canonical_id: "actian-data-platform-example-of-help-view-and-help-statements"
---

## Example of HELP VIEW and HELP Statements

!!! note "Note"

    HELP commands are valid in interactive SQL but not in the Query Editor.

The following HELP VIEW statement displays information about the iisynonyms view:

```
help view iisynonyms
```

Example output:

```
View:             iisynonyms
```

```
Owner:            $ingres
```

```
Check option:     off
```

```

```

```
View Definition:
```

```
create view  iisynonyms(
```

```
             synonym_name,
```

```
             synonym_owner,
```

```
             table_name,
```

```
             table_owner)
```

```
as
```

```
select synonym_name,
```

```
       synonym_owner,
```

```
       relid,
```

```
       relowner
```

```
from   "$ingres".iirelation,
```

```
       "$ingres".iisynonym
```

```
where  reltid   = syntabbase
```

```
and     reltidx = syntabidx
```

The following HELP statement displays the format of the iisynonyms catalog:

```
help iisynonyms
```

Example output:

```
Name:                 iisynonyms
```

```
Owner:                $ingres
```

```
Created:              17-mar-2019 11:53:42
```

```
Type:                 system catalog
```

```
Version:              II10.0
```

```

```

```
Column Information:
```

```
                                                            Key
```

```
Column Name                Type       Length Nulls Defaults Seq
```

```
synonym_name               char        256    no     no
```

```
synonym_owner              char         32    no     no
```

```
table_name                 char        256    no     yes
```

```
table_owner                char         32    no     yes
```
