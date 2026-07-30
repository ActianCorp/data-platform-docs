---
title: "MongoDB"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "MongoDB.htm"
canonical_id: "actian-data-platform-mongodb"
---

## MongoDB

The MongoDB connector is used to read JavaScript Object Notation (JSON) documents in a MongoDB database.

- [Prerequisites](../Integrations/MongoDB.md)
- [Connection Details](../Integrations/MongoDB.md)

- [Source Details](../Integrations/MongoDB.md)
- [Additional Information](../Integrations/MongoDB.md)

Prerequisites

You must have the MongoDB account and credentials.

To connect via an agent using MongoDB connector:

- Download the Actian Integration Agent. See [Download an Agent](../Integrations/Download_an_Agent.md).
- Install the Actian Integration Agent on your machine. See [Install an Agent](../Integrations/Install_an_Agent.md).

- Register the Actian Integration Agent with Actian Data Platform. See [Register an Agent](../Integrations/Register_an_Agent.md).

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Host/URI | Specifies the host name or MongoDB URI of the MongoDB server. This is a mandatory property. |
| Agent | Select the Actian Integration Agent that is installed on your system and is registered to the logged in user (The agent must be registered to the logged in user, otherwise it will not work).This property is only applicable when connecting via an agent. |
| Port | (Optional) Specifies the port number of the MongoDB server. If omitted, the default port number is 27017. |
| User | (Optional) Specifies the username or identifier that authenticates to the MongoDB server. Omit this keyword if the user security is disabled on the server for the connectivity. |
| Password | (Optional) Specifies the password of the user that authenticates to the MongoDB server. Omit this keyword if the user security is disabled on the server for the connectivity. |
| Database | (Optional) Specifies the name of the database on the MongoDB server. |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Collection | Specifies the name of MongoDB collection in the database to operate on. This is a mandatory property. |
| Query | (Optional) Specifies the text of the JSON query that selects the documents to operate on. For example, {"name":{"$eq":"fred"}} |
| Quantity | (Optional) Specifies the total number of records to read from the database. |
| Limit | (Optional) Specifies the maximum number of documents to return from the parsed data. |
| Select Source Tables | (Optional) Select which arrays of objects in the JSON data you wish to map to tables in the target. |

Additional Information

Limitations: Any document you want to add into a MongoDB collection must be a JSON document.
