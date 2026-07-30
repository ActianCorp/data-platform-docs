---
title: "Create a Database Instance"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Create_a_Database_Instance.htm"
canonical_id: "actian-data-platform-create-a-database-instance"
---

# Create a Database Instance

For information about the difference between an Actian Data Platform database instance and warehouse, see Comparing Warehouses and Databases.

For information about Actian units and database cost, see [Concepts to Understand](../DBaaS_User/Concepts_to_Understand.md).

For Google Cloud, it takes about 5 minutes or longer to create a database, depending on its size.

!!! warning "Important"

    **IMPORTANT!**By default, Actian warehouses are created using an Actian-managed encryption key for data at rest encryption. If you want to use your chosen external customer-managed KMS for data encryption instead, you must set up key management before creating any warehouses.

    Any warehouses created using the Actian-managed encryption key or your external KMS master key ID will continue to use that method—once an encryption method is assigned at warehouse creation, it cannot be changed subsequently.

    For more information, see [Set Up Key Management Service for Data Encryption](../DBaaS_User/Set_Up_Key_Management_Service_for_Data_Encryptio.md).
