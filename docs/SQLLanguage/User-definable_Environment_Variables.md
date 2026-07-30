---
title: "User-definable Environment Variables"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "User-definable_Environment_Variables.htm"
canonical_id: "actian-data-platform-user-definable-environment-variables"
---

## User-definable Environment Variables

Some Actian X environment variables can be set or reset by individual users in their local environment using operating system commands. Those set in a user’s local environment supersede the Actian X environment variables set system-wide.

Linux:****A good place to set user-defined environment variables is the user’s profile file.

## Example: Set an Environment Variable in the Local Environment

An environment variable typically set in the user’s local environment is TERM_INGRES. It specifies the termcap definition to be used by the forms system. It can be redefined locally by entering commands at the operating system prompt as in the following example:

Windows:

```
SET TERM_INGRES=IBMPCD
```

Linux:

```
TERM_INGRES=vt100f export TERM_INGRES
```

## Display Current Value for Variables

A user can display the values set in their environment with the following command entered at the operating system prompt:

Windows:

```
SET
```

Linux:

```
env
```
