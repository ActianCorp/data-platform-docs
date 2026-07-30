---
title: "Mapping Blob URI Syntax to ABFS Syntax"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "AzureURItoABFSSyntax.htm"
canonical_id: "actian-data-platform-azureuritoabfssyntax"
---

# Mapping Blob URI Syntax to ABFS Syntax

The ABFS (Azure Blob File System) driver is used by the Actian Data Platform to access Azure blobs. It uses a different naming scheme from the blob URIs but is compatible with them. Here, we will explain how to rewrite a standard blob URI to an ABFS URL so that you can specify it correctly as a data source.

!!! note "Note"

    The Actian Data Platform only supports blobs that are created in a General-purpose v2 Storage account (which is the default storage account). General-purpose v1 Storage accounts are not supported.

For an Azure blob, the URI includes the name of the storage account, the name of the container, and the name of the blob:

```
https://myaccount.blob.core.windows.net/mycontainer/myblob
```

The URI example shown above maps to the ABFS syntax like this:

```
abfs://mycontainer@myaccount.dfs.core.windows.net/myblob
```

Three things have changed:

1. The https scheme is replaced with abfs.
2. The service endpoint has changed from blob.core.windows.net to dfs.core.windows.net.

3. The container name “mycontainer” has moved before the storage account and has been suffixed with an “@” symbol.

Use this ABFS syntax when creating external tables in Azure and referencing Azure Blob files. For more information, see [Data Loading Overview](../DataLoading/DataLoadingOverview.md) in the Data Loading Guide.
