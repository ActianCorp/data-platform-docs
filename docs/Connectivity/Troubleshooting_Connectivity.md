---
title: "Troubleshooting Connectivity"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Troubleshooting_Connectivity.htm"
canonical_id: "actian-data-platform-troubleshooting-connectivity"
---

# Troubleshooting Connectivity

## How Connection Between the Application and Warehouse Is Established

For queries to be processed, applications must establish a connection to the warehouse through Ingres Net. When an application issues a query, the query is sent to the warehouse for execution. The server executes the query and returns data to the application.

For a client to connect to a server through Ingres Net, many internal connections must be made.

Local Connection

When the application, the warehouse, and the database reside on the same instance, establishing a connection is a short process:

1. The application program connects to the local Name Server (iigcn) and requests the listen address (port number) of the local warehouse process.
2. The Name Server returns this information to the application, which thereafter communicates directly with the warehouse through that address.

Remote Connection

When the application and warehouse are on separate instances, the process has more steps:

1. The application inspects the connection string to determine if additional information is needed. For example, the connection and login information associated with a vnode name or the listen address (port number) of the local Communications Server (iigcd). Additional information for the connection is obtained from the local Name Server (iigcn).

    a. The application finds the local Name Server (iigcn) listen address and talks to the local Name Server to request remote access.

    b. The local Name Server passes the listen address of the remote Communications server (iigcc) back to the application. The remote listen address is obtained from either the connection string (if a dynamic vnode specification was used) or the vnode name. If the connection string or vnode name contains a connection attribute requesting the local Communication Server (iigcc) be used for the connection, then the local Name Server also passes the listen address of the local Communications Server to the application.

2. Unless use of the local Communications Server (iigcd) has been requested, the application connects to the remote Communications Server and requests a connection to a warehouse on that remote instance. If the Name Server, in step 1b, returned the local Communications Server’s listen address, then the following additional steps are performed:

    a. The application connects to the local Communications Server, passing it the remote Communications Server’s listen address as part of the remote access request.

    b. The local Communications Server connects to the remote Communications Server and requests a connection to a warehouse on that remote instance.

3. The Communications Server on the remote instance finds the listen address of the Name Server on the remote instance. The Communications Server requests connection information from the Name Server, passing the name of the database for which a connection is requested.
4. The remote Name Server returns the listen address of a warehouse that is capable of servicing a request for connection to the target database.

5. The remote Communications Server connects to the warehouse on the remote instance.

When these steps are completed, a “virtual connection” has been established between the application and the warehouse.
