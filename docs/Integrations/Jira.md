---
title: "Jira"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Jira.htm"
canonical_id: "actian-data-platform-jira"
---

## Jira

The JIRA connector allows you to coordinate with JIRA the development of a product, bug tracking, issue tracking, and project management.

- [Prerequisites](../Integrations/Jira.md)
- [Connection Details](../Integrations/Jira.md)

- [Additional Information](../Integrations/Jira.md)

Prerequisites

You must have a JIRA account to generate the access token. You can use two types of authentication: basic authentication or a personal access token.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Base URL | The Base URL for accessing the JIRA APIs. For example:`/rest/api` |
| API version | Latest API version. |
| Access Token | The API token to access JIRA. You can use basic authentication to build a username:password string and encode the string to Base64 or you can generate a personal access token in your JIRA account. The authorization header is either Authorization: Basic or Authorization: Bearer <PAT/Personal Access Token>. |

Additional Information

Please refer to the JIRA API documentation for more information on authentication. The JIRA API documentation can be found at [https://developer.atlassian.com/server/jira/platform/basic-authentication](https://developer.atlassian.com/server/jira/platform/basic-authentication).
