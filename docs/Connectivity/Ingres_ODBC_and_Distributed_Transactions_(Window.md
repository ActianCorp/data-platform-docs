---
title: "Ingres ODBC and Distributed Transactions (Windows)"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Ingres_ODBC_and_Distributed_Transactions_(Window.htm"
canonical_id: "actian-data-platform-ingres-odbc-and-distributed-transactions-window"
---

## Ingres ODBC and Distributed Transactions (Windows)

The Ingres ODBC 3.5 Driver fully supports enlistment of the ODBC connection in a distributed transaction on Windows. The ODBC driver works with the Microsoft Distributed Transaction Coordinator (MSDTC), Ingres DBMS Server, and the Ingres XA Distributed Transaction Processing (DTP) subsystem to allow the Ingres connection to participate in the distributed transaction on Windows with other Ingres or non-Ingres participants.

To enlist in a transaction represented by a ITransaction interface, the ODBC Driver supports the SQLSetConnectionAttr(hDBC, SQL_ATTR_ENLIST_IN_DTC, pITransaction) statement. Applications such as ODBC .NET Data Provider, Microsoft Transaction Server (MTS), or ordinary applications acquire a ITransaction pointer to a MSDTC transaction, and call the ODBC Driver with the request to enlist the ODBC connection in the transaction. When the commit or rollback is required for the MSDTC transaction, the ODBC driver works as a Resource Manager (RM) with MSDTC to execute the commit or rollback for the XA transaction on the Ingres DBMS Server.

## How You Enable the Use of Distributed Transactions through the ODBC Driver

To use distributed transactions through the ODBC Driver and to maintain security within Windows, the Ingres DBA must register the ODBC driver to Windows, and the Windows MSDTC account must be enabled and registered to Ingres.

To enable the use of distributed transactions

1. Enable XA Transactions:

    Select Start, Control Panel, System and Security, Administrative Tools, Component Services, Computers, My Computer, Distributed Transaction Coordinator, (right-click) Local DTC, Properties, Security tab, Enable XA Transactions.

2. Add to the Windows registry the DLL name of the ODBC Driver (caiiod35.dll). (Windows XP SP2 and later requires that the DLL name of a MSDTC XA Resource Manager be defined in the Windows registry to enhance the security of the system.)

!!! note "Note"

    This step is not necessary if distributed transactions (SQL_ATTR_ENLIST_IN_DTC feature of the driver) will not be used.

    To register the ODBC Driver, add the following entry to HKLM\Microsoft\MSDTC\XADLL:

```
caiiod35.dll  REG_SZ   C:\Program Files\Actian\IngresII\ingres\bin\caiiod35.dll
```

3. Ensure that the Network Service account on Windows is authorized to access Ingres. (During recovery operations, the MSDTC proxy calls the ODBC driver under the NetworkService account on Windows.)

    Register the Network Service account with the Ingres Name Service. Using Visual DBA or accessdb utilities, add “networkservice” as an Ingres user. Only the name for the user account is required; no privileges are required.

## Vnode Definitions When Using Distributed Transactions through ODBC

For remote Ingres servers, vnodes must be of type Global, not Private, for “Login/password data” and “Connection data” records in the vnode definition. Global definitions are required because portions of MSDTC run under the Windows System account and need the global login and connection data to connect to Ingres for transaction recovery.

If needed, the vnode definition login records must contain the username/password information, not the application connection string, because the username/password information is needed by the MS Transaction Manager and Ingres to connect to the server when XA recovery is needed. Only the vnode information, not the application connection string, is available at that time.

## Troubleshooting Distributed Transactions through ODBC

[Microsoft][ODBC Driver Manager] Failed to enlist on calling object’s transaction

Possible actions include:

    - Check that the MSDTC service is running.

    - Select Start, Settings, Control Panel, Administrative Tools, Services, MSDTC.

    - Check the Windows Event Viewer's application and system logs for any MS DTC messages.

    - Check for messages in the client machine's Ingres log on $II_SYSTEM\ingres\files\errlog.log.

    - Check for messages in the server machine's Ingres log.

    - If using MTS, check the MTS Transaction Timeout value:

1. Start the MS Transaction Server Explorer.
1. Select Computers.

1. Right-click the computer (often My Computer) where the transaction was initiated.
1. Click the Options property tab.

It is unlikely that the component’s transaction aborted due to transaction time-out (default is 60 seconds) before the database enlistment is completed. However, if your transaction takes an unusually long time to enlist, you might consider increasing the Transaction Timeout value.

DTC transaction recovery is not working as expected

If DTC transaction recovery is not working as expected, check the Windows event viewer log/application screen for MS DTC messages. Also check the Ingres error log file %II_SYSTEM%\ingres\files\errlog.log on both the client and server machines.

To turn on the display of error messages and tracing of Ingres XA transaction processing

Issue this command:

```
ingsetenv II_XA_TRACE_FILE "C:\mydir\xatrace.log"
```

Ingres XA tracing should normally be turned off (ingunset II_XA_TRACE_FILE) because the trace output can accumulate to a significant volume over time.
