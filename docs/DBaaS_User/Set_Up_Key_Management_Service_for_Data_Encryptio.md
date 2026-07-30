---
title: "Set Up Key Management Service for Data Encryption"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Set_Up_Key_Management_Service_for_Data_Encryptio.htm"
canonical_id: "actian-data-platform-set-up-key-management-service-for-data-encryptio"
---

# Set Up Key Management Service for Data Encryption

All new warehouses can be created with data at rest encryption enabled. There are two options for Key Management Services (KMS) behind the data encryption:

- Actian-managed encryption
- Your customer-managed KMS

These services use a master key encryptionkey to encrypt and decrypt a data encryption key for locking and unlocking the Actian warehouse.

Actian supports the following external KMSs:

- AWS Key Management Service (AKMS), see [Set Up the AWS Key Management Service (AKMS)](../DBaaS_User/Set_Up_the_AWS_Key_Management_Service_(AKMS).md)

Actian does not support external keys from Google Cloud Key Management or Microsoft Azure Key Vault.

!!! note "Note"

    To use your external KMS for data encryption, you must set up the external key before creating any warehouses.

!!! warning "Important"

    **IMPORTANT!**Any warehouses created using the Actian-managed encryption key or your customer-managed external KMS master key always use that method for data key decryption. Once an encryption method is assigned at warehouse creation, it cannot be changed subsequently.
