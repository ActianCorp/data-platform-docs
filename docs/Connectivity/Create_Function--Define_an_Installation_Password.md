---
title: "Create Function--Define an Installation Password for the Local Instance"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Create_Function--Define_an_Installation_Password.htm"
canonical_id: "actian-data-platform-create-function-define-an-installation-password"
---

## Create Function--Define an Installation Password for the Local Instance

In netutil non-interactive mode, you can use the create function to create an Installation Password for the local instance.

This function has the following format:

```
create global login local_vnode * password
```

**local_vnode**

:   Identifies the name that has been configured as LOCAL_VNODE on this instance. This name can be found on the Configure Name Server screen of the CBF utility.

**password**

:   Defines the Installation Password you have chosen for this instance.

Example: Define an Installation Password

This command defines an Installation Password for the local instance, which has a local_vnode name of “payroll:”

```
create gl login payroll * payroll_password
```
