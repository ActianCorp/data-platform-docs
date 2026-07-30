---
title: "Target Output Modes"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Target_Output_Modes.htm"
canonical_id: "actian-data-platform-target-output-modes"
---

## Target Output Modes

The supported target output modes are:

- Append – When using Append mode, records from the source dataset will be added, or appended, to the existing records in the target table. The source schema (structure of the data) must be the same as the target schema.

!!! note "Note"

    If you are working with flat files as your targets, then only Replace and Append output modes are applicable.

- Replace – Creates a new warehouse table, or overwrites both the data and the structure of an existing table. Replace mode is the only output mode that allows you to change the target schema. You can use the Replace output mode option with a new table:

    - –if the table does not exist, then it is created using the specified layout on the Mapping tab.

    - –if the table already exists, then the Replace mode deletes the table, and then recreates it using the specified layout on the Source to Target Mapping page.

    - –if you are creating a new target table.

    - –if you want the target table to have a new user defined schema.

!!! note "Note"

    When you drop a table, you also drop any indexes or constraints that the table may have.

- Truncate And Append – Preserves the target schema and the relationships between tables (if you have defined them) and discards any existing records. It truncates the table but preserves the indexes or constraints the table may have. You can use the Truncate and Append output mode option if the table does not exist, then the table will be created automatically.

    Usually, when mapping to a database, you will choose an existing table that the database contains. After you choose a table, the Target Output Mode defaults to Append and the structure of the table is defined on the Source to Target Mapping page. You can change the output mode to Truncate and Append and map your target fields on the Source to Target Mapping page.
