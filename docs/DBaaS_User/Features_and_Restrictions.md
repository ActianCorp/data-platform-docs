---
title: "Features and Restrictions"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Features_and_Restrictions.htm"
canonical_id: "actian-data-platform-features-and-restrictions"
---

## Features and Restrictions

Query Editor is a web application that enables you to write and run SQL queries and visualize the results.

Features:

- Connects to the current warehouse
- Contains sample airline database data with sample queries

- Enables you to examine the database schema
- Lets you run sample queries and queries you have written

- Enables you to run multiple queries in one execution
- Creates and saves new queries and lets you clone existing queries

- Tags queries with keywords for future searching
- Formats query text with line breaks and indents

- Enables you to keep queries private or share them with other native warehouse users
- Exports query results to popular file formats

Restrictions:

- Query Editor allows only one instance per session and functions only when the warehouse is running.
- Idle sessions are terminated after 24 hours.

- Query Editor uses the Allow List IP address for connection. You cannot connect to it from anywhere unless the IP is allow listed. For more information, see Update Allow List IP Addresses.
- Query Editor supports multiple SQL statements in the console that can be executed simultaneously, separated by semi-colons. AWS AV-1 & Azure: The result set is displayed only for the last select statement if multiple select statements are provided.

- Select statements whose results display millions of rows may cause the session to disconnect and restart. Limit your results to fewer rows.
