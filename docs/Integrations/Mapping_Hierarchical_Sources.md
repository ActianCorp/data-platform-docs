---
title: "Mapping Hierarchical Sources"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Mapping_Hierarchical_Sources.htm"
canonical_id: "actian-data-platform-mapping-hierarchical-sources"
---

## Mapping Hierarchical Sources

Some source connectors return JSON data that contains a hierarchy of objects. The connectors that return JSON includes:

- REST Services
- Amazon S3, Google Cloud Storage, Microsoft Azure Blob or SFTP when the object file type is JSON or Avro. If the file type is Avro, the source connector converts Avro data to JSON.

- OData
- MongoDB

The arrays of objects within the JSON are mapped to tables in the target. For example, if the source connector returns JSON with this structure:

```
{
```

```
   "resources": [
```

```
      {
```

```
         "name": "Fred",
```

```
         "phones": [
```

```
            {
```

```
               "type": "mobile",
```

```
               "number": "888-555-5555"
```

```
            }
```

```
         ]
```

```
      }
```

```
   ]
```

```
}
```

There are two arrays of objects in this JSON code:

1. The “resources” array.
2. The “phones” array, within each “resource” object.

These arrays of objects are mapped to tables in the target.

### Defining the Source

When defining a source, if the source returns JSON data, you will see a property labeled “Select Source Tables”:

![](images/Select%20Source%20Tables.png)

The top-level array is always selected, and selecting the child arrays is optional.

If you click 'View Raw Data', the raw JSON data appears beside the structure. This makes it easier to determine which elements in the hierarchy you wish to map to the target. For example, if you do not want to include phone numbers, do not select the Phones array:

![](images/JSON%20Source%20(Resources).png)

### Defining the Targets

When defining the targets for hierarchical mapping, only the root table is explicitly specified. The child tables are named relative to the root table. In the earlier example, if the main target table is named as “Resources”, then child tables will be named “Resources__<child>”. In the earlier example, if the phones array is selected, then target tables named “Resources” and “Resources__Phones” are created.

A generated "id" field is automatically added to the target tables when mapping from hierarchical sources. If a field named “id” already exists, the generated field name will either be "id1" or named with a suffix to ensures that the field is unique.

You do not have to map to the id field. Unique values are automatically generated when you run the integration.
