---
title: "Data Access and Authentication"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Data_Access_and_Authentication.htm"
canonical_id: "actian-data-platform-data-access-and-authentication"
---

## Data Access and Authentication

Direct access to the data warehouse requires an IP allow list as well as database authentication. The data warehouse is not open to the Internet but only available to users connecting from the specified allow list IP addresses.

Access through the Actian Data Platform web console requires authentication against an enterprise IdP using [OpenID Connect](https://openid.net/connect/), based on Oath2.0. Multifactor authentication is available through your Salesforce identity.

Accounts at the IdP have an enforced password policy. Once identity is established, the user is passed back to the Actian warehouses web console for entitlement and access. User access to the web console is entirely separate from the database user level. From the Actian Data Platform console, a user can manage warehouses, list, create, delete, or start and stop warehouses.

When you create a warehouse in the web console, your user ID is set up as the administrator account. This ensures that no default password exists at any time as part of configuration. The data warehouse requires database-level authentication for DBAs and users with access.

You can access the data warehouse through standard protocols such as ODBC, JDBC, and .NET. Encryption is enforced on these protocols. DBAs have the ability to enable Discretionary and Role-Based Access Control (RBAC) framework to limit access to data. Access can be configured at the database level per user account or user group. Permissions can be granularly configured to allow only view-only access or read, write access, update, select, or any combination as necessary.
