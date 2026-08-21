---
title: "SQL Communications Area (SQLCA)"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_Communications_Area_(SQLCA).htm"
canonical_id: "actian-data-platform-sql-communications-area-sqlca"
---

## SQL Communications Area (SQLCA)

The SQL Communications Area (SQLCA) consists of a number of variables that contain error and status information accessible by the program. This information reflects only the status of executed embedded SQL database statements. Forms statements do not affect these variables. Because each embedded SQL statement has the potential to change values in the SQLCA, the application must perform any checking and consequent processing required to deal with a status condition immediately after the statement in question. If it does not, the next executed SQL statement changes the status information in the variables.

Each host language implements the SQLCA structure differently.

### Variables that Compose SQLCA

The following list describes the variables that compose the SQLCA (not all variables are currently used):

| SQLCA Variable | Description |
| --- | --- |
| sqlcaid | An 8-byte character string variable initialized to SQLCA. This value does not change. |
| sqlcabc | A 4-byte integer variable initialized to the length in bytes of the SQLCA, 136. This value also does not change. |
| sqlcode | A 4-byte integer variable indicating the SQL return code. Its value falls into one of three categories: |
|  | • = 0 – The statement executed successfully (though there have been warning messages: check sqlwarn0).<br>• < 0 – An error occurred. The value of sqlcode is the negative value of the error number returned to errorno. A negative value sets the sqlerror condition of the WHENEVER statement.<br>• > 0 – The statement executed successfully but an exception condition occurred. The following values are returned:    100 - Indicates that no rows were processed by a DELETE, FETCH, INSERT, SELECT, UPDATE, MODIFY, COPY, CREATE INDEX, or CREATE TABLE AS SELECT statement. This value (100) sets the not found condition of the WHENEVER statement.    700 - Indicates that a message statement in a database procedure has just executed, setting the sqlmessage condition of the WHENEVER statement.    710 - Indicates that a database event was raised. |
| sqlerrm | A varying length character string variable with an initial 2-byte count and a 70-byte long buffer. This variable is used for error messages. When an error occurs for a database statement, the leading 70 characters of the error message are assigned to this variable. If the message contained within the variable is less than 70 characters, the variable contains the complete error message. Otherwise, the variable contains a truncated error message. To retrieve the full error message, use the INQUIRE_SQL statement with the errortext object. If no errors occur, sqlerrm contains blanks. For some languages this variable is divided into two other variables:<br>• sqlerrml – A 2-byte integer count indicating how many characters are in the buffer.<br>• sqlerrmc – A 70-byte fixed length character string buffer. |
| sqlerrp | 8-byte character string variable, currently unused. |
| sqlerrd | An array of six 4-byte integers. Currently only sqlerrd(1) and sqlerrd(3) are in use. Sqlerrd(1) is used to store error numbers returned by the server. For more information about the values returned in sqlerrd(1), see [Types of Error Codes](../SQLLanguage/Types_of_Error_Codes.md).Sqlerrd(3) indicates the number of rows processed by a DELETE, FETCH, INSERT, SELECT, UPDATE, COPY, MODIFY, CREATE INDEX, or CREATE AS...SELECT statement. All other database statements reset this variable to zero. Some host languages start array subscripts at 0. In these languages (C, BASIC), use the subscript, 2, to select the third array element. |
| sqlwarn0-  sqlwarn7 | A set of eight 1-byte character variables that denote warnings when set to W. The default values are blanks.<br>• sqlwarn0 – If set to W, at least one other sqlwarn contains a W. When W is set, the sqlwarning condition of the WHENEVER statement is set.<br>• sqlwarn1 – Set to W on truncation of a character string assignment from the database into a hostvariable. If an indicator variable is associated with the host variable, the indicator variable is set to the original length of the character string.<br>• sqlwarn2 – Set to W on elimination of nulls from aggregates.<br>• sqlwarn3 – Set to W when mismatching number of result columns and result host variables in a FETCH or SELECT statement.<br>• sqlwarn4 – Set to W when preparing (PREPARE) an UPDATE or DELETE statement without a WHERE clause.<br>• sqlwarn5 – Currently unused.<br>• sqlwarn6 – Set to W when the error returned in sqlcode caused the abnormal termination of an open transaction.<br>• sqlwarn7 – Currently unused. |
| sqlext | An 8-byte character string variable not currently in use. |
