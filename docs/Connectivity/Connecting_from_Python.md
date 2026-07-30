---
title: "Connecting from Python"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Connecting_from_Python.htm"
canonical_id: "actian-data-platform-connecting-from-python"
---

## Connecting from Python

You can connect to the Actian Data Platform through ODBC using Python and pyodbc.

You can get pyodbc at [https://pypi.org/project/pyodbc/](https://pypi.org/project/pyodbc/). Creating a DSN is explained at [https://www.actian.com/company/blog/integrating-python-vector-actianx/](https://www.actian.com/company/blog/integrating-python-vector-actianx/).

The following is a portion of the odbc.ini file with a vnode example:

```
[avalanche]
```

```
Driver=/opt/Actian/Vector_Client/ingres/lib/libiiodbcdriver.1.so
```

```
Vendor=Actian Corporation
```

```
DriverType=Ingres
```

```
Server=avalanche_vnode
```

```
Database=db
```

```
ListenAddress=VW
```

```
ServerType=Ingres
```

where avalanche_vnode is the Actian Data Platform vnode.

The following is a sample connection script:

```
# -*- coding: utf-8 -*-
```

```

```

```
import pyodbc as pdb
```

```

```

```
#using vnode as described above
```

```
#conn = pdb.connect("dsn=avalanche;uid=dbuser;pwd=password")
```

```

```

```
#or direct connection without vnode
```

```
conn= pdb.connect("driver=Ingres;servertype=ingres;server=@localhost,tcp_ip,VW;uid=dbuser;pwd=password;database=db")
```

```

```

More information:

- [Configure a Data Source (Windows)](../Connectivity/Configure_a_Data_Source_(Windows).md)
- [Configure a Data Source (Linux)](../Connectivity/Configure_a_Data_Source_(Linux).md)
