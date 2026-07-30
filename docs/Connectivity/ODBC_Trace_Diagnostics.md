---
title: "ODBC Trace Diagnostics"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "ODBC_Trace_Diagnostics.htm"
canonical_id: "actian-data-platform-odbc-trace-diagnostics"
---

## ODBC Trace Diagnostics

If you have built your ODBC directly from code such as ADO or C, you can debug your application directly using the appropriate debugger.

ODBC trace logs are a common method for debugging ODBC applications and can be used with any application that uses the Ingres ODBC. ODBC trace logs are the most meaningful if you understand ODBC programming or Ingres internals.

## Standard ODBC Tracing

Standard ODBC tracing is written in a format that summarizes the ODBC functions called and provides information about the arguments passed to the ODBC functions. Here is an excerpt of a standard ODBC trace:

```
python iter     ae4-21c ENTER SQLAllocHandle
```

```
                SQLSMALLINT                  1 <SQL_HANDLE_ENV>
```

```
                SQLHANDLE           00000000
```

```
                SQLHANDLE *         0021FCA4
```

```

```

```
python iter     ae4-21c EXIT  SQLAllocHandle  with return code 0 (SQL_SUCCESS)
```

```
                SQLSMALLINT                  1 <SQL_HANDLE_ENV>
```

```
                SQLHANDLE           00000000
```

```
                SQLHANDLE *         0x0021FCA4 ( 0x00961788)
```

Ingres Support can often generate test cases that reproduce the problem entirely from the information in the ODBC trace log.

## Windows Environments

ODBC trace logs can be created for any Ingres application that uses ODBC. In addition to straight ODBC, applications include, but are not limited to:

- ADO
- OLE DB Provider for ODBC

- .NET Data Provider for ODBC
- Ingres Python DBI Driver

- Ingres PHP ODBC Driver
- Windows Access

- Windows Excel
- OpenOffice Base

- Microsoft ASP pages

!!! note "Note"

    ASP pages, or any ODBC-based application executed from IIS (Internet Information Service) do not support ODBC tracing. See the Microsoft Knowledge Base document 836072 for more information.

The Windows ODBC Administrator is used to enable tracing. The ODBC Administrator may be visible from the Control Panel, or can be executed from the command prompt as \WINDOWS\SYSTEM32\odbcad32.exe (32-bit environments) or \WINDOWS\SysWOW64\odbcad32.exe (64-bit environments).

To enable tracing, click the Tracing tab in the ODBC Administrator’s startup page, and then click the Start tracing now button. The Tracing page includes an entry box that specifies the path and file name of the ODBC trace log file. You can edit this box to redirect ODBC tracing output to another file.

## Linux Environments

This section discusses several methods for supporting ODBC tracing in Linux environments.

### Ingres ODBC CLI

For Ingres ODBC CLI applications, a standard ODBC trace is possible. Ingres does not currently release the code for ODBC trace libraries. However, you can obtain a binary of the ODBC trace library from Ingres Support.

To enable tracing for ODBC CLI applications:

1. Install the ODBC trace library
2. Select Drivers ⇒ Tracing from the Ingres ODBC Administrator, iiodbcadmin.

3. To enable tracing for Linux, select the Set Tracing menu option to turn tracing on, and then select Save.

### UnixODBC Driver Managers

UnixODBC environments support tracing. The Ingres ODBC Administrator can be used to trace in unixODBC environments, as previously documented for ODBC CLI applications. In fact, ODBC DSN definitions can be created in the Ingres ODBC Administrator and can be used in unixODBC applications.

To enable unixODBC tracing by manually editing the odbcinst.ini file, add this code section:

```
[ODBC]
```

```
Trace = yes
```

```
TraceFile = /tmp/odbctrace.log
```

## ODBC Tracing on All Platforms--Internal ODBC Tracing

Internal ODBC tracing is available on all platforms, regardless of the ODBC application used. Internal ODBC tracing follows the conventions of GCA and API tracing and relies on specification of Ingres environment variables to generate the trace.

The environment variable II_ODBC_LOG specifies the file name of the ODBC trace. We recommend specifying the full path of the trace log file; otherwise it may be difficult to find the log after the application is executed.

To prevent the server from writing to the wrong log, the file name can contain one or both of the following parameter values:

**%p** – Replaced at startup with the Process Identifier (PID) of the server process.

**%d** – Replaced at startup with the current date in YYYYMMDD format.

For example:

```
II_ODBC_LOG = $II_SYSTEM/ingres/files/odbctrace_%d_%p.log
```

The environment variable II_ODBC_TRACE specifies the tracing level, which ranges from 0 to 5. (The higher the value, the more detailed the output.)

The ingsetenv utility can be used to specify ODBC tracing. In IIS environments, this utility is the only option.

!!! note "Note"

    Use ingsetenv carefully, since all ODBC applications will “see” these variables whenever they are executed.

Example: ODBC Tracing Using ingsetenv

```
ingsetenv II_ODBC_LOG C:\temp\odbc.log
```

```
ingsetenv II_ODBC_TRACE 5
```

If possible, it is preferable to use platform-specific commands to set the trace variables, especially if your environment executes many ODBC applications simultaneously.

On Windows, ODBC tracing is specified as follows:

```
> set II_ODBC_TRACE=5
```

```
> set II_ODBC_LOG="C:\My Path\odbctrace.log"
```

On Linux, ODBC tracing is specified as follows for Bourne, Korn and Bash shells:

```
# II_ODBC_TRACE=5
```

```
# export II_ODBC_TRACE
```

```
# II_ODBC_LOG=/tmp/odbctrace.log
```

```
# export II_ODBC_LOG
```

You may wish to add GCA or API tracing. The environment variables II_GCA_TRACE and II_API_TRACE can be used in addition to II_ODBC_LOG.

Here is a sample excerpt from an ODBC trace log that specifies both ODBC and GCA tracing:

```
!ODBC Trace: SQLGetInfo (ca7cd0, 77, 21f0a4, 100, 21f144)
```

```
!ODBC Trace: ResetDbc
```

```
!ODBC Trace: SQLDriverConnect ()
```

```
!ODBC Trace: ResetDbc
```

```
!ODBC Trace: ConDriverName
```

```
!ODBC Trace: ConDriverInfo
```

```
!ODBC Trace: SQLConnect (ca7cd0, 0, 0, 0, 0, 0, 0)
```

```
!   0 GCA_REQUEST timeout=120000 async
```

```
!   0     GCA SA_INIT status 00000000 (0)
```

```
!   0     GCA SA_JUMP status 00000000 (1)
```

```
!   0     GCA RQ_INIT status 00000000 (222)
```

```
!   0   GCA_REQUEST target='var/INGRES' prot=66
```

```
!   0     GCA RQ_ALLOC status 00000000 (223)
```

```
!   0     GCA SA_BUFFERS status 00000000 (224)
```

```
!   0     GCA RQ_IS_NOXLATE status 00000000 (225)
```

```
!   0     GCA RQ_IS_RSLVD status 00000000 (226)
```

```
!   0     GCA RQ_ADDR_NSID status 00000000 (227)
```

```
!   0     GCA RQ_IS_NMSVR status 00000000 (228)
```

```
!   0     GCA RQ_USE_NMSVR status 00000000 (229)
```

!!! note "Note"

    Do not define II_API_LOG or II_GCA_LOG if you want to include ODBC trace information. II_ODBC_LOG must be defined.

### Internal versus Standard ODBC Trace Logs

Internal ODBC trace logs are most useful for ODBC problems that are not related to the ODBC, such as:

- Problems connecting to the database
- Errors reported from the warehouse, such as SQL syntax errors, table permission errors, or failure to return data from a query

- Errors related to commit or rollback

On Windows, internal ODBC trace logs is the only option for ODBC applications executed from IIS.

Standard ODBC trace logs are best for general use. Sometimes the best results are obtained by generating both types of trace logs.

## Disable Tracing

Do not forget to disable ODBC tracing after you have generated your test case! ODBC tracing, like all tracing, can have a significant impact on performance. It is even possible that the disk may become full if tracing is enabled for a significant period of time.

### How You Disable Standard Tracing

To disable standard tracing on Windows

1. Click the Tracing tab in the ODBC Administrator.
2. Click the Stop tracing now button.

To disable standard tracing for ODBC CLI applications

1. Execute the iiodbcadmin utility and select the Drivers ⇒ Tracing menu options.
2. Select the Set Tracing menu option to turn tracing off, and then select Save.

To disable standard tracing in unixODBC environments by editing the odbcinst.ini file

1. Open the odbcinst.ini file.
2. Unset tracing with the following edits:

```
[ODBC]
```

```
Trace = no
```

```
TraceFile =
```

### How You Disable Internal Tracing

The ingunset utility turns off variables set via ingsetenv.

In Linux environments, internal tracing is disabled using either unset or unsetenv, depending on the execution shell.

On Windows, ODBC trace variables are unset as follows:

```
> SET II_ODBC_LOG=
```

```
> SET II_ODBC_TRACE=
```
