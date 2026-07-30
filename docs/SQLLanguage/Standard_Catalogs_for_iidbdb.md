---
title: "Standard Catalogs for iidbdb"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Standard_Catalogs_for_iidbdb.htm"
canonical_id: "actian-data-platform-standard-catalogs-for-iidbdb"
---

## Standard Catalogs for iidbdb

The master database (iidbdb) contains these additional Standard Catalogs:

iiaudit

iidatabase_info

iidbprivileges

iiextend_info

iilocation_info

iiprofiles

iirolegrants

iiroles

iisecurity_state

iiusers

### iidatabase_info Catalog

This catalog describes attributes for a database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| database_name | char(32) | Name of the database |
| database_owner | char(32) | Owner of the database |
| data_location | char(32) | Default data location for this database |
| work_location | char(32) | Default work location for this database |
| ckp_location | char(32) | Default checkpoint location for this database |
| jnl_location | char(32) | Default journal location for this database |
| dump_location | char(32) | Default dump file location for this database |
| compat_level | char(4) | Database compatibility level |
| compat_level_minor | integer | Unused; defaults to 0 |
| database_service | integer | Database services available (such as: Is the database distributed? Can it be accessed through gateways?)Bitmask of database attributes: |
|  |  | 0x00000000 | Default |
|  |  | 0x00000001 | Distributed database |
|  |  | 0x00000002 | Coordinator database for a distributed database |
|  |  | 0x00000004 | Gateway database |
|  |  | 0x00010000 | Regular IDs are translated to upper case |
|  |  | 0x00020000 | Database created with LP64 |
|  |  | 0x00040000 | Delimited IDs are translated to upper case |
|  |  | 0x00080000 | Delimited IDs are not translated |
|  |  | 0x00100000 | Real user IDs are not translated |
|  |  | 0x00200000 | Unicode types in Normal Form C can be stored in database |
|  |  | 0x40000000 | Database forced consistent by verifydb |
|  |  | 0x80000000 | Unicode types in Normal Form D can be stored in database |
| security_label | char(8) | Empty stringThis column is deprecated. |
| access | integer | Bitmask of database access attributes.**Note:**The bit mask is set only if Actian Data Platform utilities are used to change the access rights to the database. Using a grant [no]access on database dbnameto public statement does not change the access from global to private or vice versa in iidatabase_info.Bitmasks as follows: |
|  |  | 0x00000000 | Database is private |
|  |  | 0x00000001 | Database is globally accessible |
|  |  | 0x00000002 | Unused |
|  |  | 0x00000004 | Database was/is in process of being destroyed |
|  |  | 0x00000008 | Database was/is in process of being created |
|  |  | 0x00000010 | Database is operational, i.e. is accessible to users |
|  |  | 0x00000020 | Database was created in an earlier Actian Data Platform release and has not yet been upgraded |
|  |  | 0x00000040 | Database was created via an earlier Actian Data Platform version and is in the process of being upgraded or the upgrade attempt was made and failed |
|  |  | 0x00000080 | Database created with B1 security |
|  |  | 0x00000100 | Not supported. Do not wait during destroydb if the database is busy |
|  |  | 0x00000200 | Production mode |
|  |  | 0x00000400 | No online checkpoints |
|  |  | 0x00000800 | Database is read only |
| database_id | integer | Unique numeric identifier for this database in the installation |

### iidbprivileges Catalog

The iidbprivileges catalog contains information about the privileges defined in a database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| database_name | char(32) | The name of the database on which the privilege is defined |
| grantee_name | char(32) | The name of the grantee for which the privilege is granted:  User  Group  Role  Public |
| gr_type | char(1) | Authorization type of the grantee:  U – user  G – group  R – role  P – public |
| cr_tab | char(1) | Indicates if the grantee has the create table privilege:  U – undefined  Y – yes  N – no |
| cr_proc | char(1) | Indicates if the grantee has the create procedure privilege:  U – undefined  Y – yes  N – no |
| lk_mode | char(1) | Indicates if the grantee has the set lockmode privilege:  U – undefined  Y – yes  N – no |
| db_access | char(1) | Y if grantee can connect to databases |
| up_syscat | char(1) | Y if grantee can update catalog tables |
| db_admin | char(1) | Indicates if the grantee has the db_admin privilege:  U – undefined  Y – yes  N – no |
| global_usage | char(1) | Reserved for future use |
| qry_io_lim | integer | The limit of I/O per query for the grantee if qry_io is Y |
| qry_io | char(1) | Indicates whether the query_io_limit privilege has been defined for the database and authorization type specified in database_name and grantee_name, respectively:Y – limit exists  N – no limit  U – undefined |
| qry_row_lim | integer | The limit of query rows per query for the grantee if qry_row is Y |
| qry_row | char(1) | Indicates whether the query_row_limit privilege has been defined for the database and authorization type specified in database_name and grantee_name, respectively.Y – limit exists  N – no limit  U – undefined |
| sel_syscats | char(1) | Y if grantee has select_syscat privileges |
| idle_time | char(1) | Y if grantee has an idle time limit |
| idle_time_lim | integer | Idle time limit in seconds |
| conn_time | char(1) | Y if grantee has a connect time limit |
| conn_time_lim | integer | Connect time limit in seconds |
| sess_prio | char(1) | Y if grantee has the session priority privilege and can alter session priorities |
| sess_pri_lim | integer | Highest priority to which a session owned by this grantee can be set |

### iiextend_info Catalog

The iiextend_info catalog provides information about which locations databases have been extended to:

| Column Name | Data Type | Description |
| --- | --- | --- |
| location_name | char(32) | Location name for this extent |
| database_name | char(32) | Name of database extended to location_name |
| status | integer | Status of this extentBitmasks are as follows: |
|  |  | 0x00000001 | Database has been successfully extended to this location |
|  |  | 0x00000002 | Location is used as a data location |
|  |  | 0x00000004 | Location is used as a work location |
|  |  | 0x00000008 | Location is used as a auxiliary work location |
| raw_start | integer | Default is 0 |
| raw_blocks | integer | Default is 0 |

### iilocation_info Catalog

The iilocation_info catalog contains information about the database locations.

| Column Name | Data Type | Description |
| --- | --- | --- |
| location_name | char(32) | The name of the location |
| data_usage | char(1) | Y if data location  N if not |
| jrnl_usage | char(1) | Y if journal location  N if not |
| ckpt_usage | char(1) | Y if checkpoint location  N if not |
| work_usage | char(1) | Y if work location  N if not |
| dump_usage | char(1) | Y if dump location  N if not |
| awork_usage | char(1) | Y if auxiliary work location  N if not |
| location_area | char(128) | The location of the area, either:II_CHECKPOINT  II_DATABASE  II_WORK  II_JOURNAL  II_DUMPordirectory name |
| security_label | char(8) | Empty stringThis column is deprecated. |
| raw_pct | integer | Percentage of the raw device allocated to this location |
| status | integer | What the location is used for:Bitmasks as follows: |
|  |  | 0x00000001 | General purpose |
|  |  | 0x00000002 | Dump |
|  |  | 0x00000008 | Database |
|  |  | 0x00000010 | Work |
|  |  | 0x00000020 | Auxiliary work |
|  |  | 0x00000040 | Journal |
|  |  | 0x00000200 | Checkpoint |

### iiprofiles Catalog

Iiprofiles is the standard catalog interface to user profile information.

| Column Name | Data Type | Description |
| --- | --- | --- |
| profile_name | char(32) | Name of profile |
| createdb | char(1) | Y if profile gives by default the right to create databasesR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| trace | char(1) | Y if profile gives by default the right to enabling usage of tracing and debugging featuresR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| audit_all | char(1) | Y if security audit of all user activity is enabled by this profile  N if profile does not give this right |
| security | char(1) | Y if profile gives by default the right to use security related functions such as the creation or deletion of usersR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| operator | char(1) | Y if profile gives by default the right to perform database maintenance operationsR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| maintain_locations | char(1) | Y if profile gives by default the right to create and change the characteristics of database and file locationsR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| maintain_users | char(1) | Y if profile gives by default the right to create, alter or drop users, profiles, groups, and roles, and to grant or revoke database and installation resource controlsR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| maintain_audit | char(1) | Y if profile gives by default the right to enable, disable, or alter security audit, and to change security audit privilegesR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| auditor | char(1) | Y if profile gives by default the right to register, remove and query audit logsR if this subject privilege is enabled by this profile, but is not part of the default privileges for this profileN if profile does not give this right |
| audit_query_text | char(1) | Y if security audit of query text is enabled for this profileN if profile does not give this right |
| expire_date | date | Date when profile expires  Blank if expiration date was not specified |
| lim_sec_label | char(8) | Empty string |
| default_group | char(32) | If specified, group to use if no explicit group was specified when accessing the database and user using this profile does not have an explicit default group, or nogroup specified |
| internal_status | integer | Numeric representation of privileges associated with this profileBitmasks as follows: |
|  |  | 0x00000001 | createdb |
|  |  | 0x00000004 | trace |
|  |  | 0x00000200 | operator |
|  |  | 0x00000400 | audit_all |
|  |  | 0x00000800 | maintain_locations |
|  |  | 0x00002000 | auditor |
|  |  | 0x00004000 | maintain_audit |
|  |  | 0x00008000 | security |
|  |  | 0x00010000 | maintain_users |
|  |  | 0x01000000 | audit_security_text |

### iirolegrants Catalog

The standard catalog interface to information about role grants.

| Column Name | Data Type | Description |
| --- | --- | --- |
| role_name | char(32) | Name of granted role |
| gr_type | char(1) | Type of grant:U – user  G – group  R – role  P – public  Blank |
| grantee_name | char(32) | Name of grantee |
| admin_option | char(1) | Y if grantee can GRANT this role to others  N if not |

### iiroles Catalog

The standard catalog interface to information about role identifiers.

| Column Name | Data Type | Description |
| --- | --- | --- |
| role_name | char(32) | Name of this role |
| createdb | char(1) | Y if role provides right to create databases, N otherwise |
| trace | char(1) | Y if role enables usage of tracing and debugging features, N otherwise |
| audit_all | char(1) | Y if security audit of all user activity is enabled by this role, N otherwise |
| security | char(1) | Y if role allows usage of security-related functions such as the creation or deletion of users, N |
| maintain_locations | char(1) | Y if role allows the user to create and change the characteristics of database and file locations, N |
| operator | char(1) | Y if role allows the user to perform database maintenance operations, N |
| maintain_users | char(1) | Y if role enables the right to create, alter or drop users, profiles, groups, and roles, and to grant or revoke database and installation resource controls, N |
| maintain_audit | char(1) | Y if role allows user to enable, disable, or alter security audit, and to change security audit privileges, N |
| auditor | char(1) | Y if role enables the registering, removing, and querying of audit logs, N |
| audit_query_text | char(1) | Y if security audit of query text is enabled by this profile, N |
| security | char(8) | Empty string |
| lim_sec_label | char(8) | Empty string |
| internal_status | integer | Numeric representation of privileges associated with this status.Number is a bitmask as follows: |
|  |  | 0x00000001 | createdb |
|  |  | 0x00000004 | trace |
|  |  | 0x00000200 | operator |
|  |  | 0x00000400 | audit_all |
|  |  | 0x00000800 | maintain_locations |
|  |  | 0x00002000 | auditor |
|  |  | 0x00004000 | maintain_audit |
|  |  | 0x00008000 | security |
|  |  | 0x00010000 | maintain_users |
|  |  | 0x01000000 | audit_security_text |
| internal_flags | integer | Reserved for future use |

### iiusers Catalog

The iiusers catalog contains information about the privileges held by users.

| Column Name | Data Type | Description |
| --- | --- | --- |
| user_name | char(32) | The name of the user |
| createdb | char(1) | Y if the user has the default right to create databasesR if the user has the right but not by defaultN if the user does not have the right |
| trace | char(1) | Y if the user has the default right to use tracing and debugging featuresR if the user has the right but not by defaultN if the user does not have the right |
| audit_all | char(1) | Y if the user has the right to security audit all user activityN if the user does not have the right |
| security | char(1) | Y if the user has the default right to use security-related functions such as creating and deleting usersR if the user has the right but not by defaultN if the user does not have the right |
| maintain_locations | char(1) | Y if the user has the default right to create and change the characteristics of database and file locationsR if the user has the right but not by defaultN if the user does not have the right |
| operator | char(1) | Y if the user has the default right to perform database maintenance operationsR if the user has the right but not by defaultN if the user does not have the right |
| maintain_users | char(1) | Y if the user has the default right to create, alter or drop users, profiles, groups, and roles, and to grant or revoke database and installation resource controlsR if the user has the right but not by defaultN if the user does not have the right |
| maintain_audit | char(1) | Y if the user has the default right to enable, disable, or alter security audit, and to change security audit privilegesR if the user has the right but not by defaultN if the user does not have the right |
| auditor | char(1) | Y if the user has the default right to register, remove, and query audit logsR if the user has the right but not by defaultN if the user does not have the right |
| audit_query_text | char(1) | Y if the user can see query text, enabled if security_audit=(query_text) was specified when creating or altering the userN if the user does not have the right |
| dbms_authentication | char(1) | Y if the user must connect using DBMS authenticationN if the user is not required to connect using DBMS authentication |
| change_password | char(1) | Y if the user has the right to change his passwordN if the user does not have the right |
| expire_date | date | Optional expiration date after which the user cannot log on |
| profile_name | char(32) | The profile associated with this user or blank |
| lim_sec_label | char(8) | Empty string |
| default-group | char(32) | The user's default group or blank |
| internal_status | integer | Numeric representation of privileges associated with this status.Number is a bitmask as follows: |
|  |  | 0x00000001 | createdb |
|  |  | 0x00000004 | trace |
|  |  | 0x00000200 | operator |
|  |  | 0x00000400 | audit_all |
|  |  | 0x00000800 | maintain_locations |
|  |  | 0x00002000 | auditor |
|  |  | 0x00004000 | maintain_audit |
|  |  | 0x00008000 | security |
|  |  | 0x00010000 | maintain_users |
|  |  | 0x01000000 | audit_security_text |
| internal_def_priv | integer | Numeric representation of default privileges, bitmask as above |
| internal_flags | integer | Numeric representation of Actian Data Platform system privileges held by the user |
