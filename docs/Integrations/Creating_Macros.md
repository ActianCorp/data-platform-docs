---
title: "Creating Macros"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Creating_Macros.htm"
canonical_id: "actian-data-platform-creating-macros"
---

## Creating Macros

Macros enable you to run a single integration for different types of users without having to modify the integration itself. Macros are defined when the integration is in the configuration state. Macros can save you time and reduce errors at runtime.

Macros are placeholders you create for values that are typically used during design and runtime, such as target paths, and credentials to access databases. By creating and defining these placeholders, and assigning them a descriptive name, you can easily redefine them as needed.

For example, let’s say you need to run an integration for testing before you run it in a production environment. You know that the test environment and the production environment use different target paths. In this case, you create two configurations from your integration.

When you create the first configuration you define a macro named TARGET_PATH, and set it to the testing environment target path.

When your testing is complete you create another configuration, and change the TARGET_PATH to the production environment path.

You can specify values for macros at the account level or for specific templates and configurations. Macros follow this hierarchy in running integrations, in descending order:

- Account (public, administrators only)
- Template

- User (private)
- Configuration

- Job

Administrators can create and manage macros on the public Macros page:

- [Create Public Macros (Administrators Only)](../Integrations/Create_Public_Macros_(Administrators_Only).md).
- [Manage Public Macros (Administrators Only)](../Integrations/Manage_Public_Macros_(Administrators_Only).md)

Non-administrative users can do the following on the private Macros page:

- [View Macros](../Integrations/View_Macros.md)
- [Edit Macros](../Integrations/Edit_Macros.md)

- [Add Your First Macro](../Integrations/Add_Your_First_Macro.md)
- [Add More Macros](../Integrations/Add_More_Macros.md)

- [Import Macros](../Integrations/Import_Macros.md)
