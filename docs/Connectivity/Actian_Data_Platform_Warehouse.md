---
title: "Actian Data Platform Warehouse"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Actian_Data_Platform_Warehouse.htm"
canonical_id: "actian-data-platform-actian-data-platform-warehouse"
---

## Actian Data Platform Warehouse

An Actian Data Platform warehouse (also referred to as an instance) consists of a unique geographical location, ownership, and warehouse ID, together with any data files created.

The Actian Data Platform server and databases reside in the cloud. There are no local databases. Locally installed components include ODBC, JDBC, and .NET drivers, and a SQL command line tool (see [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md)).

## Server Installation

Server installation happens through Actian Data Platform in the cloud when you create a warehouse. For more information, see [Create a Warehouse](../User/Create_a_Warehouse.md).

## Client Installation

A client installation consists of the API components that support client applications (JDBC Driver, ODBC Driver, and .NET Data Provider) and their associated tools. A client installation does not run a warehouse or store any data. A Name server process (iigcn) is needed only if you are defining and using vnodes. This is typically not the case for Actian Data Platform users, who instead use dynamic vnodes where all information is provided in the connection string (see [What is a Vnode (Virtual Node)?](../Connectivity/What_is_a_Vnode_(Virtual_Node)_3f.md)).
