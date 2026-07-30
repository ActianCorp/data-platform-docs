---
title: "Syntax Rules for Startup Files and Environment Variables"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Syntax_Rules_for_Startup_Files_and_Environment_V.htm"
canonical_id: "actian-data-platform-syntax-rules-for-startup-files-and-environment-v"
---

## Syntax Rules for Startup Files and Environment Variables

Keep the following general syntax rules in mind while setting up startup files and environment variables:

- Set statements in startup files cannot contain more than one SET statement per line. Each statement must be on a line by itself.
- Set statements that are read from a file but executed only by the SQL CLI must be terminated with “\g”.

- Set statements defined directly inside Actian Data Platform environment variables (not written in a file) never contain the string “\g”.
- Set statements defined directly inside Actian Data Platform environment variables (not written in a file) can contain multiple set statements separated by a semicolon up to a total length of 64 characters.

- The SQL CLI [Dayfile](../SQLLanguage/Syntax_Rules_for_Startup_Files_and_Environment_V.md) cannot contain set statements. It contains informational startup messages only.
- Actian Data Platform environment variables set with the following commands are global for the Actian Data Platform installation and affect the target of the environment variable for all users in a warehouse:

```
ingsetenv
```

- Actian Data Platform environment variables set from the local user environment apply only to the user setting them. Other users are not affected. This is the case, for example, when Actian Data Platform environment variables are set interactively, or:

    Windows:****Through the System icon in the Control Panel.

    Linux:****From a user’s .login, .profile, or .cshrc file.

## Dayfile

This name affects all users of the SQL and QUEL single-line terminal monitors.

Dayfile contains text messages only (not SET statements), which appear as an informational header whenever the terminal monitors are started up. The message header can be suppressed with the -d command line flag.
