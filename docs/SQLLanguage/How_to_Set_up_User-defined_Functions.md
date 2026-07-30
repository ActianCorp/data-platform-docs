---
title: "How to Set up User-defined Functions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "How_to_Set_up_User-defined_Functions.htm"
canonical_id: "actian-data-platform-how-to-set-up-user-defined-functions"
---

## How to Set up User-defined Functions

The process for configuring the use of UDFs is as follows:

1. Specify the languages (other than SQL) that UDFs are implemented in on the installation configuration parameter ii.hostname.config.udf_languages in config.dat.

    Valid values for udf_languages are:

    **none** – No languages are available; UDFs cannot be created.

    **javascript** – (Default) Only JavaScript UDFs are available.

    **python** – Only Python UDFs are available.

    **javascript,python** – Both JavaScript and Python UDFs are available.

    For example:

```
iisetres ii.hostname.config.udf_languages javascript,python
```

:   **Notes:**

    - If udf_languages is changed after UDFs are created, existing UDFs using the language will report an error on X100 startup and when used in queries.

    - If language support cannot be loaded for a specified language on any node, then the database will not start.

2. Perform the following additional steps if using Python UDFs:

    Linux:

    a. Install Python 3.6 libraries using the Python 3.6 installer appropriate for your operating system and version.

**Note:**Do not change the default version of Python on your operating system. Install 3.6 in a separate area and tell Vector where to find the library.

    b. Create a symbolic link in the /usr/lib directory for every node in your installation, pointing libpython3.6m.so.rh-python36-1.0 to the Python 3.6 library to be used. For example:

```
ln -s /usr/lib64/libpython3.6m.so.1.0 /vector/opt/Actian/VectorVW/ingres/lib/libpython3.6m.so.rh-python36-1.0
```

!!! note "Note"

    The Linux environment variable PYTHONHOME must either be empty or set to a valid path.

    Windows:

    a. Install Python 3.6.8 libraries using the Python 3.6 installer appropriate for your operating system and version.

    b. Set the Vector environment variable UDF_PYTHONHOME to the path where Python is installed. For example:

```
ingsetenv UDF_PYTHONHOME C:\Python36
```

    c. Set the Windows System environment variable PYTHONHOME in System Properties (select Control Panel, System, Advanced system settings, Environment variables, System variables) to the path where Python is installed. For example:

```
PYTHONHOME=C:\Python36
```

Also see [CREATE FUNCTION](../SQLLanguage/CREATE_FUNCTION.md).
