---
title: "Actian Ingres Database as a Service Workflow"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Actian_Ingres_Database_as_a_Service_Workflow.htm"
canonical_id: "actian-data-platform-actian-ingres-database-as-a-service-workflow"
---

## Actian Ingres Database as a Service Workflow

Three phases: loading your database, monitoring your database, and using the DBaaS sidecar.

## Create a New Database Instance

Before you start loading or querying your data, you must create a database. To create a database instance, you must specify its size in terms of Actian units (AUs). For more information, see [Actian Units](../DBaaS_User/Concepts_to_Understand.md).

## Database Instance Details

Monitor the status of your database instance, region where it runs, the Allow List of database access, among other details.

## Use of the Restricted Bash Shell (rbash)

Once you connect via ssh, you are logged into rbash which limits what you can do and what commands you can run. There are the commands you can use. Some of them are ingres commands, some of them are OS commands. Many of the commands have been added because they are needed for other tools not because they are necessarily intended to be used by themselves.
