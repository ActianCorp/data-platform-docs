---
title: "Using Net"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Using_Net.htm"
canonical_id: "actian-data-platform-using-net"
---

# Using Net

## Connection to Remote Databases

In general, Ingres Net provides users with transparent access to remote databases. Only when the connection is first established must you specify the node on which the database resides and, in some circumstances, the type of server. After you are connected, you can work in the database as if it were local; no further reference to its location is necessary.

!!! note "Note"

    If a default remote node is defined on the local instance, you do not have to specify a vnode name when you make a connection to that node. For information about using this feature, see [Default Remote Nodes](../Connectivity/Default_Remote_Nodes.md).

## Database Access Syntax--Connect to a Remote Database

The syntax for accessing a remote database through an operating system-level command is:

```
command [auth_user] vnode::dbname
```

where:

**command**

:   Is any command used to invoke an Actian Data Platform tool such as sql.

**auth_user**

:   Specifies the user name and password used for connection authentication, whether through OS authentication, DBMS authentication, or another mechanism. This syntax is useful when using DBMS authentication because it allows password entry or prompting with simplified syntax.

:   The auth_user can be one of the following:

+user

:   Prompts for the password of the user.

+user=username

:   Connects as the specified user and prompts for a password.

+user=username,password

:   Connects as the specified user and password. The password is exposed on the command line.

**vnode::**

:   Is the remote node where the database resides. The two colons are required.

:   The remote node can be specified as either:

@host+

:   A connection string that includes the connection data, user authorization, and attributes that are associated with a remote node. For the format of @host+, see [Dynamic Vnode Specification--Connect to Remote Database](../Connectivity/Using_Net.md).

vnode_name

:   The virtual node name that points to the connection data and authorization data necessary to access a particular remote instance.

**dbname**

:   The name of the database.

Examples:

Start the [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md) (terminal monitor) and connect using vnode “production” to the mydb database:

```
sql production::mydb
```

Connect as the logged in OS user. Prompt for the password:

```
sql +user production::mydb
```

Connect as user fred, and prompt for the password. Fred need not be an OS user:

```
sql +user=fred production::mydb
```

Connect as user fred and enter the password on the command line. Fred need not be an OS user when DBMS authentication is enabled:

```
sql +user=fred,secret production::mydb
```

### Dynamic Vnode Specification--Connect to Remote Database

When connecting to a remote database (using the vnode::dbname syntax), you can specify a dynamic vnode instead of a vnode name. The dynamic vnode specification includes the connection data, user authorization, and attributes that are associated with a remote node.

!!! note "Note"

    A dynamic vnode can be used wherever a vnode is allowed, unless otherwise stated. Actian Data Platform clients typically use dynamic vnodes.

A dynamic vnode specification has the following format:

```
@host,[protocol,]port[,port][;attribute=value{;attribute=value}][[user,password]]
```

Linux: In bash shell, enclose the semicolon in single or double quotes (so it will not be treated as a command terminator). Alternatively, place the entire dynamic vnode specification in single or double quotes. ]

**@host**

:   Identifies the network name or address of the node on which the remote database is located. The @ character is required because it identifies this specification as a dynamic vnode rather than a vnode name.

**protocol**

:   (Optional) Identifies the network protocol to be used by the local node to connect to the remote node.

:   The valid value is: tcp_ip (default protocol).

!!! note "Note"

    On Windows, tcp_ip is the only protocol. On Linux, protocols are tcp_ip and tcp_ipv4.

**port**

:   Identifies the listen address of the instance on the remote node.

    The default Actian Data Platform warehouses use the following ports:

    - JDBC: 27839

    - ODBC: 27832

**attribute=value**

:   (Optional) One or more additional connection, encryption, and authentication attributes for the connection, as described in [Vnode Attributes Configuration](../Connectivity/Advanced_Vnode_Parameters.md).

**[user,password]**

:   (Optional) Identifies the user name and password on the remote system.

!!! note "Note"

    The user name and password must be enclosed in brackets.

:   Rather than specifying [user, password] in the dynamic vnode specification, you can use the **+user**username****syntax before the dynamic vnode specification. The +user flag prompts for the password, which protects the password from exposure. For example:

```
sql +user=johnny @machine01,tcp_ip,27839::inventory
```

:   If the +user flag is used, you cannot also specify the [user, password] option as part of the dynamic vnode.

Examples of dynamic vnode specifications:

Run the [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md) and connect to node hosta using protocol tcp_ip to a remote port number. The login and password are Johnny and secretpwd. The remote database name is salesfact:

```
sql @hosta,27839;[Johnny,secretpwd]::salesfact
```

```
Linux: sql '@hosta,27839;[Johnny,secretpwd]::salesfact' ]
```

Establish a direct connection by using the connection_type attribute:

```
sql @hosta,27839;encryption_mode=on[Johnny,secretpwd]::salesfact
```

Start the SQL CLI, connect to node myhost01 as user johnny using TCP-IP protocol (the default), and prompt for the password:

```
sql +user=johnny @myhost01,27839::salesfact
```

```
Linux: sql '+user=johnny @myhost01,27839::salesfact' ]
```

## Using the SQL Connect Statement with Net

If you are using the **connect** statement in an application, connect to a database on a remote instance using the following syntax:

```
exec sql connect 'vnode::dbname'
```

!!! note "Note"

    The vnode can be either a dynamic vnode specification (@host+) or a vnode name.

You must use the single quotes around the designation of the vnode and database names. For example, assume that you have an application residing on “napoleon” that wants to open a session with the database “advertisers” on “eugenie.” The following statement performs this task (assuming also that “lady” is a valid vnode name for “eugenie”):

```
exec sql connect 'lady::advertisers';
```
