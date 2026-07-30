---
title: "SQL CLI Macros"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_CLI_Macros.htm"
canonical_id: "actian-data-platform-sql-cli-macros"
---

## SQL CLI Macros

The SQL CLI macro facility lets you:

- Tailor the SQL language to your needs.
- Remove strings of text from the query buffer and replace them with other text.

- Change environment variables using built-in macros.
- Build simple branching into SQL scripts.

By default, macros are disabled. To enable macros issue the \macro command.

## Macro Concepts

All SQL CLI macros are defined as two parts:

- The templatepart
- The replacementpart

A macro can be created using the {define} macro statement. The basic form of the {define} command is:

```
{define; $$t; $$r}
```

Where “t” and “r” are the templateand replacementparts of the macro.

The SQL CLI contains a macro processor that substitutes the replacementpart of the macro for the templatepart. For example:

```
{define; ins $t $v; insert into $t VALUES ( $v )}\eval
```

```
ins t001 27\list
```

This macro causes the word “ins” followed by the next two values to be expanded into:

```
INSERT INTO t001 VALUES ( 27 )
```

The template part establishes a symbol that, when encountered in the SQL CLI macro workspace, signals SQL CLI to invoke the symbol's definition. When a macro is encountered, the template part is removed and replaced with the replacement part.

For example, the template “get” causes the corresponding definition of “get” to be invoked. If the replacement part of the “get” macro is "SELECT", all instances of the word “get” in the query text are replaced with the word “SELECT”:

```
\macro
```

```
{define;get;SELECT}\eval
```

```
get * from iitables\g
```

The SQL CLI expands the “get” macro as follows:

```
SELECT * FROM iitables\g
```

The following example shows all instances of the word “get” in the query text being replaced with the word “foo”:

```
\macro
```

```
{define;get;foo}\eval
```

```
SELECT get.* FROM iitables get\g
```

The SQL CLI expands the “get” macro as follows:

```
SELECT foo.* FROM iitables foo\g
```

Macros can accept parameters. Parameters are specified as a single letter or digit preceded by a dollar sign, e.g. $2 or $k.

For example, the template “get $1” allows the “get” macro to accept a single parameter.

If the “get” macro is defined as:

```
{define;get $1;SELECT table_name FROM iitables t1 WHERE t1.table_reltid=$1}
```

```
get 24
```

selects table_name from iitables where table_reltid is 24 (this will return two rows).

If the “get” macro were defined as:

```
{define;get $a $1;SELECT first $a * FROM iitables t1 WHERE t1.table_reltid=$1}
```

```
get 1 24
```

selects the first row from iitables where table_reltid is 24.

## System Macros

Built-in System Macros are as follows. Parameter are specifiers with one ($) or two dollar signs ($$), as discussed in [Parameter Prescan](../SQLLanguage/SQL_CLI_Macros.md).

**{begintrap}**

:   Executed before the query is submitted.

**{continuetrap}**

:   Executed after the query executes.

**{define; $$t; $$r}**

:   Defines a macro.

:   Special processing (see [Special {define} Processing](../SQLLanguage/SQL_CLI_Macros.md)) occurs on the template (t) part.

**{dump}**

:   Dumps all macros in {rawdefine} form.

**{dump; $$n}**

:   Returns the value of the macros that match n.It uses the same algorithm as {remove}.

**{editor}**

:   Defines the online editor to use in the \edit command.

:   To change the default vi editor to the ed editor, enter:

```
{define;{editor};/bin/ed}
```

:   which invokes the ed editor in response to the \e command.

**{endtrap}**

:   Executed after the query is submitted, but before the query executes.

**{errornumber}**

:   By default returns the generic error number. If II_EMBED_SET is set to dbmserror, the DBMS error is returned instead.

**{ifeq; $$a; $$b; $t; $f}**

:   Compares the numbers aand b. If the numbers match, the returned value is t; otherwise, the returned value is f.

**{ifgt; $$a; $$b; $t; $f}**

:   Compares the numbers a and b. If a is greater than b the returned value is t; otherwise the returned value is f.

**{ifsame; $$a; $$b; $t; $f}**

:   Compares the strings a and b. If the strings match, the returned value is t; otherwise the returned value is f.

**{rawdefine; $$t; $$r}**

:   Is another form of {define}, where the special processing does not take place. Rawdefine is rarely used. Seen when listing macros with the \list command, because Actian Data Platform converts all {define} statements into their corresponding {rawdefine} form.

**{read $$s}**

:   Types s and reads a line from the terminal. The typed line acts as the replacement text for the macro.

**{readcount}**

:   Contains the number of characters read in the most recent {read} or {readdefine}.

:   A Ctrl+Z (VMS) or Ctrl+D (UNIX) (end of file) becomes -1; a single newline becomes zero; and so forth, so that the number accurately reflects printing characters.

**{readdefine; $$n; $$s}**

:   Types s and reads a line, but it further creates a macro called n, which is set to the line entered at the terminal. This lets you set aside a line for further processing.

:   The replacement text for {readdefine} is the count of the number of characters in the line. {readcount} is set to this number.

**{remove}**

:   Removes all macros.

**{remove; $$n}**

:   Removes all macros beginning with name $n.

:   For example, typing:

```
{define; get part $n; ... }{define; get emp $x; ... }
```

:   defines two macros that start with the word “get”.

:   To remove both “get” macros, type:

```
{remove; get}
```

:   To remove the first macro only, type:

```
{remove; get part}
```

**{substr; $$b; $$e; $$s}**

:   Returns the part of string s between character positions b and e, numbered from one. If b or e is out of range, it is moved in range as much as possible.

**{shell}**

:   Defines the pathname of a shell to use in the \shell command.

**{tuplecount}**

:   Is set after every query, but before {continuetrap} is executed, to the number of rows returned by a select or the number of rows changed in an update.

:   It is not set for some SQL statements (CREATE VIEW, for example). If multiple queries are run at once, it is set to the number of rows that satisfied the last query run.

**{type $$s}**

:   Types s onto the terminal.

## Macro Evaluation

When you write a {define} statement, it is not processed immediately; macro processing occurs when the query buffer is evaluated.

The SQL CLI commands \go, \list, and \eval evaluate the workspace. You can use the \eval and \list commands to test a macro invocation before executing it explicitly with the \go command.

For example, to test the “get” macro, type:

```
{define;get;SELECT}\eval
```

```
get * FROM iitables\list
```

The SQL CLI types:

```
SELECT * from iitable
```

The statement is not executed.

To execute the “get” statement, type:

```
{define;get;SELECT}\eval
```

```
get * FROM iitables\go
```

```
\reset
```

The \reset command assures that the workspace is cleared before the next query is entered.

## Macro Parameters

A macro can have parameters. A parameter can be:

- A single word
- A string delimited with quotes (' ')

- Another macro

A parameter is terminated by a semicolon, space, tab, newline, or the end of the template (right brace }) that follows the parameter.

In the template descriptor for {define}:

```
{define;$t;$r}
```

- The first parameter t ends at the first semicolon.
- The second parameter r ends at the first right brace.

For example:

```
{define;x;SELECT * FROM iitables}
```

System macros (see [System Macros](../SQLLanguage/SQL_CLI_Macros.md)) are always surrounded by braces and can be nested, as in the macro definition:

```
{define;x;{read data:}}
```

The first right brace closes the {read} macro; the second right brace closes the {define} macro.

## Parameter Prescan

Sometimes it is useful to “macro process” a parameter before using it in the replacementpart.

For prescan to occur, the parameter must be specified in the template with two dollar signs ($$) instead of one, and the actual parameter must begin with an @ sign.

## Using Tab or Newline

If you want to insert a real tab or newline, use \t for tab or \n for newline.

For example, the “sel” macro reads a string and uses the “get” macro to substitute the word SELECT for get.

The resulting string is used with the “sel” parameter “n”, which is the name of a table, as follows:

```
{define;get;SELECT}\eval
```

```
{define;sel $n\n; \
```

```
get table_name FROM iitables WHERE \
```

```
table_name LIKE '$n'}\eval
```

To get all tables_name in iitables with a name that includes “index”:

```
sel ‘%index%'\g
```

## Use of Quotes

Sometimes text strings must be passed through the macro processor without being processed. In such cases single quotes must surround the literal text (for example, to pass the word sel through without converting it to select type 'sel').

If you want to enter more than one word for substitution into a macro parameter, you must quote the parameter.

For example, if you define a macro:

```
{define; sel $1 $2; SELECT $1 FROM part WHERE $2}\eval
```

Invoke it with the query:

```
sel 'p.name, p.qoh * p.stk AS weight' 'p.cn=10'\l
```

The query is evaluated as:

```
SELECT p.name, p.qoh * p.stk AS weight FROM part WHERE p.cn=10
```

## Use of Backslashes

To continue a macro definition on another line, enter a backslash and then a carriage return. For example:

```
{define; get $n; SELECT table_name FROM iitables \
```

```
WHERE table_name = '$n'}
```

To disallow the special meaning of characters, precede them with the backslash character (\). To enter a real backslash, use two backslashes (\\).

For example, an accent mark can be included in a quoted parameter by preceding it with a backslash:

```
here is a '\'quoted'\' string
```

Evaluates to:

```
here is a 'quoted' string
```

## Special {define} Processing

When you define a macro using {define}, special processing takes place. In {define}, all sequences of spaces, tabs, and newlines in the template, as well as all “non-spaces” between words are turned into:

| Character | Description |
| --- | --- |
| \\| | Matches any number of spaces, tabs, or newlines.Matches zero, but only between words, as can occur with punctuation. For example, \\| matches the spot between the last character of a word and a comma following it. |
| \^ | Matches exactly one space, tab, or newline |
| \& | Matches exactly zero spaces, tabs, or newlines, but only between words.If the template ends with a parameter, the \& character is added at the end. |

Typically you do not see them, but they can appear in the output of a {dump} command.

## SQL CLI Macro Examples

1. SQL CLI will “sleep” for 3 seconds:

```
\shell sleep 3
```

2. SQL CLI will execute commands inside xyz.sh

```
\shell /home/user01/xyz.sh
```

    or

```
\shell ./xyz.sh
```

    For example if xyz.sh contains:

```
echo
```

```
echo hello john
```

```
echo
```

```
sql -S foo <<EOF
```

```
SELECT ASCII(COUNT(*)) FROM iitables\g
```

```
EOF
```

```
echo
```

```
exit
```

    This will return:

```
*\sh ./xyz.sh
```

```
hello john
```

```
147
```

```
continue
```

3. A simple branch:

```
\branch ?{ifsame;@{read Enter data:};a;1;0}=1 valueok
```

    The {read Enter data:} writes “Enter data:” on the terminal and accepts input from the terminal.

    The {read Enter data:} macro is preceded by an @ because the parameter must be pre-scanned.

    What is typed in response to {read Enter data:} becomes the first parameter in the {ifsame;@{read Enter data:};a;1;0} macro.

    The {ifsame;@{read Enter data:};a;1;0} macro compares the first parameter to the second parameter which is the character “a”.

    If “a” is entered on the terminal, {ifsame; ...} evaluates to 1, the third parameter.

    If anything other than “a” is entered, {ifsame; ...} evaluates to 0, the forth parameter.

    If {ifsame; ...} is equal to 1, the code branches to the label ''valueok''.

4. A branching loop:

```
\macro
```

```
\mark noindex
```

```
SELECT CHAR(table_name,32) FROM iitables WHERE table_reltid = RANDOM(180,189) \g
```

```
/* If the row count is greater than 1, then the table has an index  branch to "end"*/
```

```
/* Otherwise try again by branching to "retry"*/
```

```
\branch ?{ifgt;@{tuplecount};1;0;1}=1 retry
```

```
\branch end
```

```
\mark retry
```

```
{type table has no index}\v
```

```
\branch noindex
```

```
\mark end
```

```
\q
```

5. An example of prescan:

```
{define;typeit $$s;{type $s}}\eval
```

```
{define;line;this is text}\eval
```

```
typeit line\eval
```

    Gives:

```
line
```

    However, the entry:

```
typeit @line\eval
```

    Gives:

```
this is text
```

    Another example:

```
\macro
```

```
{define;x;@{tuplecount}}\eval
```

```
SELECT * FROM iitables WHERE table_name LIKE '%index%'\g
```

    This will set x to 10:

```
{type @x}\eval
```

```
{define;y;@{tuplecount}}\eval
```

```
SELECT count(*) FROM iitables WHERE table_name LIKE '%index%'\g
```

    This will set y to 1:

```
{type @y}\eval
```

    If the “x” and “y” are not macro processed, as in the following:

```
{ifeq;x;y;{type @x equal to y};{type @x not equal y }}\eval
```

    the preceding evaluates to: 1 equal to 10, which is an incorrect evaluation.

    If the “x” and “y” are macro processed as in the following:

```
{ifeq;@x;@y;{type @x equal to y};{type @x not equal y }}\eval
```

    the preceding evaluates to: 1 not equal to 10, which is a correct evaluation.

6. Prints “<number of rows> tuples touched” by a query after the query has executed:

```
\macro
```

```
{define;{begintrap};{remove;{tuplecount}}}\eval
```

```
{define;{continuetrap}; \
```

```
{ifeq;@{tuplecount};{tuplecount};; \
```

```
{type @{tuplecount} tuples touched}}}\eval
```

```
SELECT COUNT(*) FROM iitables\p\g
```

```
Gives:
```

```
* \macro
```

```
* {define;{begintrap};{remove;{tuplecount}}}\eval
```

```
continue
```

```
* {define;{continuetrap}; \
```

```
* {ifeq;@{tuplecount};{tuplecount};; \
```

```
* {type @{tuplecount} tuples touched}}}\eval
```

```
continue
```

```
* SELECT COUNT(*) FROM iitables\g
```

```
Executing . . .
```

```

```

```
+-------------+
```

```
|col1         |
```

```
+-------------+
```

```
|          147|
```

```
+-------------+
```

```
1 tuples touched
```

7. Finds the SQL statement error number:

```
* \macro
```

```
* SELECT * FROM foo\go
```

```
Executing . . .
```

```
E_US0845 Table 'foo' does not exist or is not owned by you.
```

```
    (Mon May 28 14:04:00 2012)
```

```
continue
```

```
* {type @{errornumber}}\eval
```

```
30100
```

    The value returned is the Generic Error Code.

8. Uses {errornumber} to detect deadlock and to retry.

    Tables test and test2 are being updated in a different order by two different sessions. This is a classic case that can cause a deadlock.

    Step 1: Create two tables:

```
 test  (col1 INTEGER NOT NULL)\go
```

```
INSERT INTO test VALUES (1)\go
```

```
 test2 (col1 INTEGER NOT NULL)\go
```

    Step 2: Create file deadlock_test1.sql containing the following:

```
* SQL script deadlock_test1.sql to show use of {errornumber} macro */
```

```
\macro
```

```
/* need a place to jump back to */
```

```
\mark an insert
```

```
INSERT INTO test SELECT * FROM test\p\g
```

```
/* To guarantee a deadlock */
```

```
\shell sleep 5
```

```
SELECT count(*) FROM test2\p\g
```

```
/* if generic error = 49900 then go to retry label */
```

```
/* The equivalent dbmserror is 4700 /
```

```
\branch ?{ifeq;@{errornumber};49900;1;0}=1 retry
```

```
/* if no deadlock go to the label end */
```

```
\branch end
```

```
/* Offer chance to retry */
```

```
\mark retry
```

```
\branch ?{ifsame;@{read Deadlock would you like to Retry (y/n)};y;1;0}=1 aninsert
```

```
\mark end
```

```
COMMIT\p\g
```

    Step 3: Create file deadlock_test2.sql containing the following:

```
/* SQL script deadlock_test2.sql to show use of {errornumber} macro */
```

```
\macro
```

```
/* need a place to jump back to */
```

```
\mark anupdate
```

```
UPDATE test2 SET col1=10\p\g
```

```
/* To guarantee a deadlock */
```

```
\shell sleep 5
```

```
SELECT count(*) FROM test\p\g
```

```
/* if generic error = 49900 then go to retry label
```

```
/* The equivalent dbmserror is 4700 /
```

```
\branch ?{ifeq;@{errornumber};49900;1;0}=1 retry
```

```
/* if no deadlock go to the label end */
```

```
\branch end
```

```
/* Offer user choice to retry */
```

```
\mark retry
```

```
\branch ?{ifsame;@{read Deadlock would you like to Retry (y/n)};y;1;0}=1 anupdate
```

```
\mark end
```

```
commit\p\g
```

    Step 4: In session one run:

```
sql mydb
```

```
* \i deadlock_test1.sql
```

**Note:**Do not execute the include file yet.

    Step 5: In session two run:

```
sql mydb
```

```
* \i deadlock_test2.sql
```

**Note:**Do not execute the include file yet.

    Step 6: Execute the \include file by pressing Enter on each session.

    One of the sessions will hit the deadlock and you will be offered the chance to retry the query. Answer “y” to retry.
