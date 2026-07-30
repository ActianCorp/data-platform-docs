---
title: "Load Data"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Load_Data.htm"
canonical_id: "actian-data-platform-load-data"
---

## Load Data

You can load data into your database with the copydb or unloaddbcommands using rbash. For more information, see [Use of the Restricted Bash Shell (rbash)](../DBaaS_User/Use_of_the_Restricted_Bash_Shell_(rbash).md).

Be aware of the following before doing the reload:

- Make sure your client system has the required setting for date_alias, II_DATE_FORMAT, II_TIMEZONE_NAME
- An Actian database only allows the default locations (e.g. ii_database). If you use other locations the include the ions the include the -no_loc flag on copydb / unloaddb

- If you have not enabled other page sizes by including your own config.dat during the database instance creation, make sure only page sizes 2048 and 8192 are being used.

After the initial load you can run optimizedb via the vnode from your local system, or use CREATE STATISTICSsql statement.
