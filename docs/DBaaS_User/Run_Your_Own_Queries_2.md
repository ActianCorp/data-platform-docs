---
title: "Run Your Own Queries"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Run_Your_Own_Queries_2.htm"
canonical_id: "actian-data-platform-run-your-own-queries-2"
---

## Run Your Own Queries

You can display and run your created queries that are displayed in the query pane.

Query Editor supports simultaneously executing multiple SQL statements that are separated by semi-colons.

- AWS AV-1 and Azure: The result set is only displayed for the last select statement if multiple SELECT statements are provided.
- Google Cloud and AV-2: The result set displays data for all SELECT statements.

To run a single-statement query

1. Create or display your query in the query pane.

    See [Create and Save a New Query](../DBaaS_User/Create_and_Save_a_New_Query.md) or [Open a Saved Query](../DBaaS_User/Open_a_Saved_Query.md).

2. If there are multiple statements on the current query tab, select the one entire statement that you want to run.
3. Click the Run button.

    Results are displayed in the query results pane.

To export the results to a file, see [Export Query Results to a File](../DBaaS_User/Export_Query_Results_to_a_File.md).

AWS AV-1 and Azure: To run a multiple-statement query

1. Create or display your query in the query pane.

    See [Create and Save a New Query](../DBaaS_User/Create_and_Save_a_New_Query.md) or [Open a Saved Query](../DBaaS_User/Open_a_Saved_Query.md).

2. Click the Run button.

    Results for the first statement are displayed in the query results pane.

To export the results to a file, see [Export Query Results to a File](../DBaaS_User/Export_Query_Results_to_a_File.md).

Google Cloud and AWS AV-2: To run a multiple-statement query

1. Create or display your query in the query pane.

    See [Create and Save a New Query](../DBaaS_User/Create_and_Save_a_New_Query.md) or [Open a Saved Query](../DBaaS_User/Open_a_Saved_Query.md).

2. Click the Run button or select Run All Queries from the dropdown.

    Results are displayed in the query results pane.

    Each statement is displayed in a row.

    - Click the View Results link to display that statements results in the query results pane.

    - Click the Back to All Results link to display the table of statement results.

To export the results to a file, see [Export Query Results to a File](../DBaaS_User/Export_Query_Results_to_a_File.md).
