---
title: "SFTP"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "SFTP.htm"
canonical_id: "actian-data-platform-sftp"
---

## SFTP

With the Secure File Transfer Protocol (SFTP) connector, you can send and fetch files securely to and from an SFTP server.

- [Prerequisites](../Integrations/SFTP.md)
- [Connection Details](../Integrations/SFTP.md)

- [Source Details](../Integrations/SFTP.md)
- [Additional Information](../Integrations/SFTP.md)

Prerequisites

You must have the SFTP account and credentials.

To connect via an agent using SFTP connector:

- Download the Actian Integration Agent. See [Download an Agent](../Integrations/Download_an_Agent.md).
- Install the Actian Integration Agent on your machine. See [Install an Agent](../Integrations/Install_an_Agent.md).

- Register the Actian Integration Agent with Actian Data Platform. See [Register an Agent](../Integrations/Register_an_Agent.md).

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Host | Specifies the host name or IP address of the SFTP server. This is a mandatory property. |
| Agent | Select the Actian Integration Agent that is installed on your system and is registered to the logged in user (The agent must be registered to the logged in user, otherwise it will not work).This property is only applicable when connecting via an agent. |
| Port | (Optional) Specifies the port on which the SFTP server is listening for incoming connections. The default value is 22. |
| Preferred Authentication | (Optional) Specifies the authentication method to try first when establishing a connection. The supported values are Password (default) and Public Key. This property is applicable when Advanced Properties toggle is enabled. |
| User | Specifies the username for connection. This is a mandatory property. |
| Password | (Optional) Specifies the password value to use when performing password-based authentication. |
| Connection Timeout | (Optional) Specifies the amount of time, in seconds, to wait for the server to respond when establishing a connection, before considering the connection attempt unsuccessful. The default value is 30. The value 0 indicates no timeout. This property is applicable when Advanced Properties toggle is enabled. |
| Retry Connection Count | (Optional) Specifies the number of times to retry establishing a connection to the server before giving up and reporting the error. The default value is 0, which indicates no retries. This setting is not applicable when performing a Test connection operation in the design UI, and the value 0 is automatically enforced in that case. This property is applicable when Advanced Properties toggle is enabled. |
| Retry Connection Interval | (Optional) Specifies the amount of time, in seconds, to wait between successive connection retries. The default value is 60. This setting is applicable only when the Retry Connection Count is set to a value greater than 0. This property is applicable when Advanced Properties toggle is enabled. |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Path | Specifies the path of the directory or file to access on the SFTP server. Forward slash (/) character is used as a file separator. This is a mandatory property.**Note:**If the specified path value starts with a forward slash, it is treated as an absolute path; otherwise, it is treated as a path relative to the current default directory for the connection. |
| Data Format | Specifies the data format. This is a mandatory property. Select one of the following as per the data format type:<br>• CSV:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Quote: Specifies the quote character. Default value is ".–Delimiter: Specifies the field delimiter character. Default value is ,.–Escape: Specifies the escape character.–Separator: Specifies the row separator characters. Default value is \r\n.–Character Set: Specifies the character set of the data. Default value is UTF-8.–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.<br>• Excel:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Worksheet Index: Specifies the index of the worksheet. The index of the first worksheet is 1(default).–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.<br>• Avro:The following properties must be configured:–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the AVRO data you wish to map to tables in the target.<br>• Parquet<br>• JSON:The following properties must be configured:–Find Array: If enabled, specifies that the output will iterate on the first array found in the JSON document.–Array Path: Specifies the path of the JSON array within the document. Omit if the document is an array. For example,"/resources".–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the JSON data you wish to map to tables in the target. |
| Limit | (Optional) Specifies the maximum number of records to return. |
| Batch Size | (Optional) Specifies the number of records to return per batch. |

Additional Information

None
