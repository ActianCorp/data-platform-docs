---
title: "IngresDataReader Object--Retrieve Data from the Database"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "IngresDataReader_Object--Retrieve_Data_from_the.htm"
canonical_id: "actian-data-platform-ingresdatareader-object-retrieve-data-from-the"
---

## IngresDataReader Object--Retrieve Data from the Database

The .NET Data Provider provides the IngresDataReader object to retrieve a read-only, forward-only stream of data from an Ingres result-set created by a SELECT query or row-producing database procedure. Using the IngresDataReader increases application performance and reduces system overhead because only one row of data at a time is in memory.

## Build the IngresDataReader

After creating an instance of the IngresCommand object, call Command.ExecuteReader to build the IngresDataReader to retrieve rows from a data source, as shown in the following example:

Visual Basic:

```
Dim rdr As IngresDataReader = cmd.ExecuteReader()
```

C#:

```
IngresDataReader rdr = cmd.ExecuteReader();
```

## IngresDataReader Methods

Use the Read method of the IngresDataReader object to obtain a row from the results of the query. To access each column of the returned row, pass the name or ordinal reference of the column to the IngresDataReader.

For best performance, the IngresDataReader provides a series of methods that allow you to access column values in their native data types (GetDateTime, GetDouble, GetGuid, GetInt32, and so on). For a list of typed accessor methods, see the [IngresDataReader Class](../Connectivity/NET_Data_Provider_Classes.md). Use the typed accessor when you know the underlying data type. When using a type accessor, use the correct accessor to avoid an InvalidCastException being thrown when no type conversions are performed.

## Example: Using the IngresDataReader

The following is an implementation of IngresDataReader.

```
static void DataReaderDemo(string connstring)
```

```
{
```

```
    IngresConnection conn = new IngresConnection(connstring);    string strNumber;
```

```
    string strName;
```

```
    string strSSN;    conn.Open();    IngresCommand cmd = new IngresCommand(
```

```
        "select number, name, ssn  from personnel", conn);    IngresDataReader reader = cmd.ExecuteReader();    Console.Write(reader.GetName(0) + "\t");
```

```
    Console.Write(reader.GetName(1) + "\t");
```

```
    Console.Write(reader.GetName(2));
```

```
    Console.WriteLine();    while (reader.Read())
```

```
    {
```

```
        strNumber= reader.IsDBNull(0)?
```

```
            "<none>":reader.GetInt32(0).ToString();
```

```
        strName  = reader.IsDBNull(1)?
```

```
            "<none>":reader.GetString(1);
```

```
        strSSN   = reader.IsDBNull(2)?
```

```
            "<none>":reader.GetString(2);        Console.WriteLine(
```

```
        strNumber + "\t" + strName + "\t" + strSSN);
```

```
    }    reader.Close();
```

```
    conn.Close();
```

```
}
```

## ExecuteScalar Method--Obtain a Single Value from a Database

To return database information that is a single value rather than in the form of a table or data stream—for example, to return the result of an aggregate function such as Count(*), Sum(Price), or Avg(Quantity)—use the IngresCommand object's ExecuteScalar method. The ExecuteScalar method returns as a scalar value the value of the first column of the first row of the result set.

The following code example uses the Count aggregate function to return the number of records in a table:

Visual Basic:

```
Dim cmd As IngresCommand = New IngresCommand("SELECT Count(*) FROM Personnel", conn)Dim count As Int32 = CInt(cmd.ExecuteScalar())
```

C#:

```
IngresCommand cmd = new IngresCommand("SELECT Count(*) FROM Personnel", conn);Int32 count = (Int32)cmd.ExecuteScalar();
```

## GetSchemaTable Method--Obtain Schema Information from a Database

The .NET Data Provider enables you to obtain schema information from Ingres data sources. Such schema information includes database schemas or catalogs available from the data source, database tables and views, and constraints that exist for database tables.

The .NET Data Provider exposes schema information using the GetSchemaTable method of the IngresDataReader object. This method returns a DataTable that describes the resultset column metadata. For more information on this metadata, see [GetSchemaTable Columns Returned](../Connectivity/NET_Data_Provider_Classes.md).

If the ExecuteReader(CommandBehavior.KeyInfo) method was called in the IngresCommand object when building the IngresDataReader, additional information about primary key columns, unique columns, and base names are retrieved from the database catalog and included in the returned DataTable.
