---
title: "Start the SQL CLI"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Start_the_SQL_CLI.htm"
canonical_id: "actian-data-platform-start-the-sql-cli"
---

## Start the SQL CLI

The sql command invokes the Actian SQL CLI. It accepts a variety of flags that define how Actian Data Platform and the SQL CLI operate during your session. For more information, see [sql Command Options and Flags](../SQLLanguage/sql_Command_Options_and_Flags.md).

To start the Actian SQL CLI

1. In the Actian Data Platform on the Warehouses page, click the name of the warehouse you want to connect to.
2. Click the Connections tab.

3. From the Connect to Actian Data Platform Warehouse dropdown, select Actian SQL CLI.

    Two connection strings are displayed:

    - `sql +user=dbuser @av-5iizfn03avmx.actiandatacloud.com,tcp_ip,27832::db`

    This variant prompts you for a password and starts up the SQL CLI session after validating the credentials.

    - `sql @av-5iizfn03avmx.actiandatacloud.com,tcp_ip,27832[dbuser,``<password>``]::db`

    The second variant is used for running queries from a file by redirecting stdin. If you have queries defined in a file and want to run them using the SQL CLI, you can provide the file as stdin to this second variant.

**Note:**Do not insert a space between dbuser and <password>, or connection will fail.
