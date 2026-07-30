---
title: "sql Command Options and Flags"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "sql_Command_Options_and_Flags.htm"
canonical_id: "actian-data-platform-sql-command-options-and-flags"
---

## sql Command Options and Flags

The sql command invokes the SQL CLI terminal monitor.

This command has the following format:

```
sql [SQL option flags] [line-mode flags] dbname [+user=[authuser]] [<altin] [>altout]
```

The sql command accepts a variety of flags that define how Actian Data Platform and the SQL CLI operate during your session:

**SQL option flags**

:   Specifies flags that can be used with the SQL CLI and other commands where noted. The SQL option flags determine the format of output or the behavior of the database. You can specify a maximum of twelve SQL option flags:

-cN

:   Sets the minimum field width for printing character columns to N. The default is 6.

-fkxM.N

:   Sets floating-point output column width to M characters (total), including N decimal places, and (if warranted) e+-xx and the decimal indicator character itself.

:   k can be 4 or 8 to apply to f4’s or f8’s respectively.

:   x can be E, F, G, or N (uppercase or lowercase) to specify an output format. E indicates exponential format. F indicates floating-point format. G indicates the floating-point format and guarantees decimal alignment. N indicates floating-point format, decimal alignment, and right-justification.

:   If you specify N or G and the number is too large for the format indicated by the flag, it is displayed in exponential format. To prevent this format overflow, M should be greater than or equal to N + 7.

:   The default display format for both f4 and f8 is n10.3, unless your computer supports the IEEE standard for floating-point numbers, in which case the display format for f4 and f8 is n11.3.

-Ggroupid

:   Specifies a group identifier.

-ikN

:   Sets integer output column width to N. k can be 1, 2, or 4 for i1’s, i2’s, or i4’s, respectively. The default for N is 6 for i1 and i2 fields, and 13 for i4 fields.

-l

:   Locks the database for your exclusive use. When you specify this flag, no one else can open the database while you are in it. If you attempt to take an exclusive lock on a database that is in use, the system informs you that the database is temporarily unavailable.

-Rroleid

:   Specifies a role identifier for the session.

-string_truncation = ignore | warn | fail

:   Sets error handling mode for string truncation errors. Such an error occurs if an attempt is made to insert a string into a table column that is too short to contain the value.

:   ignore – Truncates and inserts the string without issuing an error message.

:   warn – Truncates and inserts the string and issues a warning message.

:   fail – (Default) Terminates the statement and issues an error message. The FAIL option is supported only for singleton INSERTs and COPY. It is supported only in cases where the literal string value can be validated, so it is not supported for CREATE TABLE AS SELECT, INSERT...SELECT, nor for updates where the string value originates from an expression from another table.

-tN

:   Sets the minimum field width for printing text columns to N. The default is 6.

-uusername

:   Specifies the effective user for the session.

:   Double quotes used for delimited names must be escaped. For example: **sql mydb –u\"milo-032345\"**

+U|-U

:   Enables (+U) or disables (-U) user updating of the system catalogs, and takes an exclusive lock on the database. To update system catalogs, you must have the update system tables privilege obtained through accessdb.

+w|-w

:   Indicates to wait (+w) or not wait (-w) for the database. The default is ‑w. If you specify +w, you must wait if certain processes are running (sql –l, sql –U, verifydb, or sysmod) on the given database, before the operation proceeds.

+Y|-Y

:   Enables (+Y) or disables (-Y) user updating of the system catalogs, but does not take an exclusive lock on the database.

**line-mode flags**

:   Specify flags that affect SQL CLI behavior and that can be used with the SQL CLI only:

+a|-a

:   Sets (+a) or clears (-a) the autoclear option in the SQL CLI. When disabled, the query buffer is never automatically cleared; it is as if the \append command was inserted after every \go. This flag requires the query buffer to be cleared using \reset after every query. The default is +a. For more information, see [SQL CLI Query Buffering](../SQLLanguage/SQL_CLI_Query_Buffering.md).

+d|-d

:   Displays (+d) or does not display (-d) the dayfile (a text file that displays the date and time and other information). The default is +d.

-history_recall | ‑nohistory_recall

:   Linux only: Invokes the SQL CLI with or without history recall functionality. History recall lets you retrieve the history of commands typed in the session, and perform other functions.

left- and right- arrow

:   Browses the line entered.

Backspace

:   Erases a character to the left of the cursor.

Up- and Down- arrow

:   Retrieves the history of the commands typed in this session.

Ctrl+U

:   Erases the line.

Ctrl+K

:   Erases the line from the cursor to the end. ]

-Ppassword

:   Specifies the user password.

-Rrole-name/role-password

:   Identifies the role name and optional role password. Separate the name and password with a slash (/).

+s|-s

:   Displays (+s) or does not display (-s) status messages. -s suppresses all status messages including login and logout messages, the dayfile, and prompts. Error messages are not suppressed. The default is +s.

-S

:   Runs the SQL CLI in silent mode, which shows query output only, and suppresses headers, footers, separators, lines, and row counts. This allows simple reports to be created as SQL scripts and then run without having to edit the output.

-vX

:   Sets the column separator to the character specified by X. The default is vertical bar (|).

**dbname**

:   Specifies the name of the database and, if required, the vnode.

vnode::

:   Identifies the remote node on which the database is located. It must be followed by two colons (::) and the dbname parameter, with no intervening space (vnode::dbname).

:   For more information, see [Creating Server Connection Definitions (Vnodes)](../Connectivity/Creating_Server_Connection_Definitions_(Vnodes).md).

:   The remote node can be specified as either of the following:

vnode_name

:   Is the virtual node name that points to the connection data and authorization data necessary to access a particular remote instance.

@host+

:   Is a “dynamic vnode” connection string that includes the connection data, user authorization, and attributes that are associated with a remote node. The @ character is required because it identifies this specification as a dynamic vnode rather than a vnode name.

**Note:**A dynamic vnode is the form that is typically used with Actian Data Platform. Examples, when used with the Actian SQL CLI:

```
    sql +user=dbuser @av-5iizfg03avmx.actiandatacloud.com,tcp_ip,27832::db    sql @av-5iizfg03avmx.actiandatacloud.com,tcp_ip,27832[dbuser,<password>]::db
```

**+user=[authuser]**

:   Specifies or prompts for the user name (authuser) and password used for connecting to a remote database.

:   This syntax is useful because it allows password entry or prompting with simplified syntax.

:   One of the following can be used:

+user

:   Prompts for the password of the user.

+user=username

:   Connects as the specified user name and prompts for password.

@[username,password]

:   Connects as the specified user name and password. Password is exposed on the command line. Do not enter a space after the comma before password.

**<altin**

:   Specifies a file from which the SQL CLI reads commands. The file must contain all SQL CLI commands needed to run the session.

**>altout**

:   Directs output from the SQL CLI to the specified file. If you specify this parameter, you will not see any output.

### sql Examples

Open the SQL CLI for working in the db database as user dbuser:

```
sql +user=dbuser @av-5iizfn03avmx.actiandatacloud.com,tcp_ip,27832::db
```

Open db and do not print the dayfile:

```
sql @av-5iizfn03avmx.actiandatacloud.com,tcp_ip,27832[dbuser,<password>]::db -d
```

Open db, suppressing the dayfile message and the SQL CLI prompts and messages, and read into the workspace the contents of the batchfile:

```
sql @av-5iizfn03avmx.actiandatacloud.com,tcp_ip,27832[dbuser,<password>]::db -s < batchfile
```

Open db, display float4 columns in G format with two decimal places and integer1 columns with three spaces:

```
sql +user=dbuser @av-5iizfn03avmx.actiandatacloud.com,tcp_ip,27832::db    -f4g12.2 -I13
```
