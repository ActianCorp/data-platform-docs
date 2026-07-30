---
title: "Availability of Your KMS When Starting and Stopping Warehouses"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Availability_of_Your_KMS_When_Starting_and_Stopp.htm"
canonical_id: "actian-data-platform-availability-of-your-kms-when-starting-and-stopp"
---

## Availability of Your KMS When Starting and Stopping Warehouses

When starting and stopping warehouses, master key ID decryption must be available. This means that your master key ID must be enabled.

Your KMS master key ID must not be disabled or deleted from your KMS provider. If it is, warehouses using that disabled master key ID will fail on startup.
