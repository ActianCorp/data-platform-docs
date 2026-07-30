---
title: "SQL CLI Character Input and Output"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_CLI_Character_Input_and_Output.htm"
canonical_id: "actian-data-platform-sql-cli-character-input-and-output"
---

## SQL CLI Character Input and Output

When non-printable ASCII characters are entered through the SQL CLI, the SQL CLI replaces these characters with blanks.

For example, if you enter the statement:

```
INSERT INTO test VALUES('^La')
```

the SQL CLI converts the ^L to a blank before sending it to Actian Data Platform, and then displays the message:

```
Non-printing character nnn converted to blank
```

where nnn is replaced with the actual character.

To insert non-printing data into a char or varchar field, specify the data as a hexadecimal value. For example:

```
INSERT INTO test VALUES(x'07');
```

This feature can be used to insert a newline character into a column:

```
INSERT INTO test VALUES('Hello world'+x'0a');
```

This statement inserts ’Hello world\n’ into the test table.

On output, if the data type is char or varchar, any binary data are shown as octal numbers (\000, \035, and so on.). To avoid ambiguity, any backslashes present in data of the char or varchar type are displayed as double backslashes. For example, if you insert the following into the test table:

```
INSERT INTO test VALUES('\aa')
```

when you retrieve that value, you see:

```
\\aa
```
