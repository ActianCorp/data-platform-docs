---
title: "Application Configuration File--Troubleshoot Applications"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Application_Configuration_File--Troubleshoot_App.htm"
canonical_id: "actian-data-platform-application-configuration-file-troubleshoot-app"
---

## Application Configuration File--Troubleshoot Applications

The .NET Data Provider offers a basic trace facility to assist the application developer in identifying a sequence of data provider method calls that may be called incorrectly by an application program. The developer can create a .NET application configuration file that contains keys for Ingres.trace.

For example, you can create a file called myApplication.exe.config in the same directory as the myApplication.exe executable. The myApplication.exe.config text file contains the following:

```
<?xml version="1.0" encoding = "utf-8" ?><configuration>    <appSettings>        <add key="Ingres.trace.log" value="C:\temp\Ingres.trace.log" />        <add key="Ingres.trace.timestamp" value="true" />        <add key="Ingres.trace.drv" value="2" />    </appSettings></configuration>
```

The value= key controls the level of tracing that is produced. Possible key values are:

0 – no tracing (default)
1 – Basic function name detail

2 – Internal connection and messaging detail
3 – Internal state detail

4 – Internal status, length, and count detail
