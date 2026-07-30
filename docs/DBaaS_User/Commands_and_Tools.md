---
title: "Commands and Tools"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Commands_and_Tools.htm"
canonical_id: "actian-data-platform-commands-and-tools"
---

## Commands and Tools

Please refer to the Actian X documentation and the Command Reference Guide for full details of the tools available. See https://docs.actian.com/actianx/11.2/index.html#page/CommandRef/CommandRef_Title.htm

## File access

You should be able to access the filesystem read-only for most of the Actian X instance. You can only write to files and directories under the “home” for the restricted shell which is $II_SYSTEM/ingres/files. However there are no utilities provided which directly create files and command output re-direction is prevented by rbash.

## File system layout

When you log in you are logged in to a so-called “sidecar” container which has its own filesystem but shares access to the files are directories of the Actian X instance. Only the following directories are part of the persistent storage:

/actianx/database

/actianx/backup

/actianx/log

/actianx/work

/opt/Actian/IngresVW/ingres/files

Everything else will be reset if the containers (the “Database” in the console) are restarted.

Discspace

II_TEMPORARY is set to use /tmp for temporary files. This is not part of persistent storage. The space available is shared with the rest of the non-persistent storage.

If you set II_DBMS_LOG it can create large log files. Please be aware of this when decided where to set it to, persistent or non-persistent storage. In many cases use of II_DBMS_LOG should be done with the assistance of Actian Support as many of the messages in the logs are for internal diagnostic use.

Please bear in mind the persistent storage and related locations. You can technically create locations in non-persistent storage directories but if you do so and create databases that use them, you may lose data.

## Databases

A single database is created when the instance is created, called “db”. You can create further databases using createdb. However such databases will not be known to the console. Full support for multiple databases is being added.

## Making Changes

Changes can be made to the configuration using the usual ingres tools – CBF, accessdb, sql etc. Note that ingstart and ingstop are not provided, to restart the Actian X instance use the command “restart”.

## Users

You can create database users using accessdb or the SQL “create user” command (see the SQL User Guide), however you cannot create operating system users. Ensure that you create DBMS passwords for any users you create.

## Monitoring/Troubleshooting

You can monitor the instance using ipm or tools such as iimonitor, logstat and lockstat. You can also access the log files such as the error log $II_SYSTEM/ingres/files/errlog.log
