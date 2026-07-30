---
title: "SQL CLI Commands"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_CLI_Commands.htm"
canonical_id: "actian-data-platform-sql-cli-commands"
---

## SQL CLI Commands

Terminal monitor commands can manipulate the contents of the query buffer or your environment. Unlike the SQL statements that are buffered until the \go command is issued, SQL CLI commands are executed as soon as the Return key is pressed.

All SQL CLI commands must be preceded with a backslash (\). If a backslash is entered literally, it must be enclosed in quotes. For example, the following statement inserts a backslash into the test table:

```
INSERT INTO test VALUES('\')\g
```

Some SQL CLI commands accept a file name as an argument. These commands must appear alone on a single line. The SQL CLI interprets all characters appearing on the line after such commands as a file name. Those SQL CLI commands that do not accept arguments can be stacked on a single line. For example:

```
\date\go\date
```

returns the date and time before and after execution of the SQL statements in the query buffer.

SQL CLI commands include:

**\ansistamp**

:   Displays timestamps in ANSI format.

**\append or \a**

:   Appends to the query buffer. Typing \append after completion of a query overrides the auto-clear feature and guarantees that the query buffer is not reset until executed again.

**\[no]bell**

:   Includes (\bell) or does not include (\nobell) a bell (that is, Ctrl+G) with \continue or \go.

:   Default: \nobell

**\branch [label] | ?{ expression} operator value label**

:   Permits arbitrary branching in an \include file.

:   If followed by **label**it is an unconditional branch; if followed by **?{****expression****}****operator value label** it is a conditional branch.

**expression**

:   Made up of a macro. Spaces within an expression terminates the expression.

**operators**

:   Can be one of: +, -, *, /, >, >=, <, <=, and =. The left unary operator “!” can be used to indicate logical negation.

**value**

:   Dependent on the expression.

**label**

:   A conditional branch.

**\colformat column_name [column_format]**

:   Establishes a column name/format pair to be used in result sets.

:   column_name is the name of a column.

:   column_format is a Report-Writer style format string that defines the format for column output. If omitted, any defined format string for the specified column name is removed.

:   Examples:

```
* \colformat d1 d'03/02/1901'
```

```
* \colformat f2 +f10.7
```

```
* \colformat s3 -c3
```

```
* SELECT date('now') d1, 1.5 f2, 'testing' s3\g
```

```
Executing . . .
```

```

```

```
┌──────────┬──────────┬───┐
```

```
│d1        │f2        │s3 │
```

```
├──────────┼──────────┼───┤
```

```
│07/09/2011│ 1.5000000│tes│
```

```
└──────────┴──────────┴───┘
```

**\[no]continue or [no]co**

:   Continues (\continue) or does not continue (\nocontinue) statement processing on error. The error message is displayed.

:   Default: \co. The default can be changed by setting II_TM_ON_ERROR.

**\date**

:   Prints the current date and time.

**\eval or \v**

:   Puts the result back into the macro workspace.

:   You can use the \eval and \list commands to test a macro invocation before executing it explicitly with \g.

**\go or \g**

:   Processes the current query. The contents of the buffer are transmitted to Actian Data Platform and run.

**\list or \l**

:   Prints macros on the terminal. You can use the \eval and \list commands to test a macro invocation before executing it explicitly with \g.

**\[no]macro**

:   Enables (\macro) or disables (\nomacro) macro definition.

:   The default is \nomacro.

**\mark label**

:   Sets a label for \branch. Branching in SQL CLI is only permitted in a \include file.

:   Must be followed with a label that a \branch will go to. Can be before or after the \branch operator.

**\[no]padding**

:   Resets padding (\padding) to the default, which is that columns are space-padded to column width defined by data type; column titles may be truncated.

:   \nopadding trims space padding from column output; column titles are shown in full.

**\print or \p**

:   Prints the current query. The contents of the buffer are printed on the user terminal. Silent mode has no affect on this command.

**\quit or \q**

:   Exits the SQL CLI.

**\reset or \r**

:   Empties the workspace before you enter the next query (resets the query buffer).

**\[no]runtime or \[no]rt or \rt [block|statement]**

:   Switches into “run time” mode, which prints the time taken (to six decimal places) to execute the SQL. Elapsed time can be shown for transaction (block) or statement (the default).

```
* \rt
```

```
* SELECT count(*) FROM foo\g
```

```
Executing . . .
```

```
┌──────────────────────┐
```

```
│col1                  │
```

```
├──────────────────────┤
```

```
│             514198976│
```

```
└──────────────────────┘
```

```
(1 row in 0.065921 secs)
```

**\showcf**

:   Displays all column name/format pairs defined with \colformat.

```
* \showcf
```

```
d1 : d'03/02/1901'
```

```
f2 : +f10.7
```

```
s3 : -c3
```

!!! note "Note"

    If a format is specified that is invalid for the data type selected, a warning message is displayed and the results are returned as if no format was specified. This can misalign the output because the column title width will reflect the specified column format. For example:

```
* SELECT 100000 s3 UNION SELECT 20000\g
```

:   returns E_FM600B_FMT_DATATYPE_INVALID beside the affected rows.

**\[no]silent or \nosil**

:   Turns on (\silent) or turns off (\nosilent) silent mode.

**\[no]suppress**

:   Suppresses (\suppress) or does not suppress (\nosuppress) the printing of the resulting data that is returned from the query.

**\time**

:   Prints the current date and time.

**\timestamp or \ts**

:   Prints the current date and time to two decimal places:

```
24-May-2012 09:29:18.17
```

**\[no]titles**

:   Turns on (\titles) or turns off (\notitles) column titles.

**\[no]trim**

:   Trims (\trim) space padding from column output; column titles are shown in full.

:   \notrim resets padding to the default, which is that columns are space-padded to column width defined by data type; column titles may be truncated.

**\vdelimiter or \vdelim char**

:   Sets the column separator to the specified character.

:   \vdelimiter uses the first ten non-blank bytes and ignores any extra characters; this allows for multi-byte character sets, such as UTF8.

:   charcan be one of the following:

SPACE

:   Changes the vertical separator to a space character.

TAB

:   Changes the vertical separator to a tab character.

NONE

:   Changes the vertical separator to an empty string.

:   \vdelim with no character specified resets the separator to the default character, which is one of the following:

    - Line-drawing character if output is to a terminal

    - | if output is to a file or other command

    - Space if in silent mode

    - Character as specified with -v flag on the command line

:   By default, silent mode shows column titles and separates columns with a space. If a vertical separator is specified, either with -v or \vdelimiter, the new separator is used, but in silent mode no leading and trailing separator is shown.

!!! note "Note"

    Both \vdelimiter and -v replace the | with the specified character. They do not create a delimited file. For example **\vdelimiter SPACE** or -**v" "**creates a file where the columns are separated by a space, but spaces will pad the column data and spaces may be in the data itself.

**\[no]vertical or \[no]vert**

:   Enables or disables vertical output, in which each column is displayed one output row after another with a “table row” heading.

```
* SELECT first 3 table_name, table_owner FROM iitables\g
```

```
Executing . . .
```

```

```

```
**** Row : 1 ****
```

```
table_name : iiprotect
```

```
table_owner : $ingres
```

```

```

```
**** Row : 2 ****
```

```
table_name : iiddb_nodecosts
```

```
table_owner : $ingres
```

```

```

```
**** Row : 3 ****
```

```
table_name : iirole
```

```
table_owner : $ingres
```

```

```

```
(3 rows)
```
