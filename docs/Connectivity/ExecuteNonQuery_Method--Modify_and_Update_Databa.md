---
title: "ExecuteNonQuery Method--Modify and Update Database"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "ExecuteNonQuery_Method--Modify_and_Update_Databa.htm"
canonical_id: "actian-data-platform-executenonquery-method-modify-and-update-databa"
---

## ExecuteNonQuery Method--Modify and Update Database

Using the .NET Data Provider, you can use the IngresCommand’s ExecuteNonQuery method to process SQL statements that modify data but do not return rows, such as INSERT, UPDATE, DELETE, and other non-resultset commands such as CREATE TABLE.

Although rows are not returned by the ExecuteNonQuery method, input and output parameters and return values can be passed and returned using the Parameters property of the IngresCommand object.

The following code example executes an UPDATE statement to update a record in a database using ExecuteNonQuery:

```
static void DemoUpdate(string connstring)
```

```
{    IngresConnection conn = new IngresConnection(connstring);    conn.Open();    IngresCommand cmd = new IngresCommand(        "update demo_personnel set name = 'Howard Lane' "+        "  where number = 200", conn);    int numberOfRecordsAffected = cmd.ExecuteNonQuery();    Console.WriteLine(numberOfRecordsAffected.ToString() +        " records updated.");    conn.Close();}
```

## IngresDataAdapter Object--Manage Data

An IngresDataAdapter object has four properties for retrieving and updating data source records:

- SelectCommand returns selected data from the data source.

    The SelectCommand property must be set before calling the Fill method of the IngresDataAdapter.

- InsertCommand inserts data into the data source.
- UpdateCommand updates data in the data source.

- DeleteCommand deletes data from the data source.

    The InsertCommand, UpdateCommand, and DeleteCommand properties must be set before the Update method of the IngresDataAdapter is called, depending on what changes were made to the data in the DataSet. For example, if rows have been added, the InsertCommand must be set before calling Update.

    When Update is processing an inserted, updated, or deleted row, the IngresDataAdapter uses the respective Command property to process the action. Current information about the modified row is passed to the Command object through the Parameters collection.

    For example, when updating a row, the UPDATE statement uses a unique identifier to identify the row in the table being updated. The unique identifier is commonly the value of a primary key field, or unique non-null index. The UPDATE statement uses parameters that contain the unique identifier, the columns, and the values to be updated, as shown in the following SQL statement:

```
static void DemoAdapter(string connstring)
```

```
{
```

```
    IngresConnection  conn = new IngresConnection (connstring);
```

```
    IngresDataAdapter  adapter = new IngresDataAdapter ();    adapter.SelectCommand = new IngresCommand (
```

```
        "select * from personnel", conn);    adapter.UpdateCommand = new IngresCommand (
```

```
        "update personnel  set name = ?, number = ? where ssn = ?",
```

```
        conn);
```

```
    adapter.UpdateCommand.Parameters.Add(
```

```
        "@name", IngresType.Char,"name");
```

```
    adapter.UpdateCommand.Parameters.Add(
```

```
        "@number", IngresType.Int, "number");
```

```
    adapter.UpdateCommand.Parameters.Add(
```

```
        "@oldssn", IngresType.Char, "ssn").SourceVersion =
```

```
        DataRowVersion.Original;    DataSet ds = new DataSet();
```

```
    adapter.Fill(ds, "Personnel");    ds.Tables["Personnel"].Rows[195]["number"] = 4199;
```

```
    adapter.Update(ds, "Personnel");
```

```
}
```

### IngresDataAdapter Events

The IngresDataAdapter exposes the following events, which you can use to respond to changes made to data source data:

**RowUpdating**

:   An UPDATE, INSERT, or DELETE operation on a row (by a call to one of the Update methods) is about to start.

**RowUpdated**

:   An UPDATE, INSERT, or DELETE operation on a row (by a call to one of the Update methods) is complete.

**FillError**

:   An error has occurred during a Fill operation. Inherited from DBDataAdapter.
