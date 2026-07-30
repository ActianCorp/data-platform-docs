---
title: "Errors When Using SSO with JDBC"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Errors_When_Using_SSO_with_JDBC.htm"
canonical_id: "actian-data-platform-errors-when-using-sso-with-jdbc"
---

## Errors When Using SSO with JDBC

Java JDBC app works with SSO as well as SSO-DF. However, when testing SSO with python, the application can hang, requiring it to be killed. The resulting call stack indicates that what causes this issue is the jaydebeapi library or the org.jpype package used.
