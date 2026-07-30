---
title: "Manage Integration Listeners"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "Manage_Integration_Listeners.htm"
canonical_id: "actian-data-platform-manage-integration-listeners"
---

## Manage Integration Listeners

Integration listeners are an API endpoint that will remotely execute Actian Data Platform configurations. You can create a workflow in a third-party application that integrates data from a particular location by triggering the API call that executes the configuration and fetch the data to process.

Configurations that are specified in a listener must already exist in the account. See [Configurations](../DataLoading/BatchDataLoad.md).

To create a listener

1. On the navigation pane on the left, click Listeners.

    The Integrations Listener page is displayed, listing all listeners, if any.

2. Click the Add Listener button.

    The Add Listener dialog appears on the right.

3. Enter an alias name for the listener.
4. Select a configuration that this listener, when activated, will run.

5. Click Add.

    The listener is created, and the Manage Listener dialog is displayed.

6. From the Edit Keys dropdown, select Generate New Keys.

    A dialog opens.

7. Click Generate Keys to confirm the creation of the keys.
8. Click the Copy button to copy the Access Key to the clipboard and paste it in your third-party application.

![](images/CopyToClipboardIcon.png)

9. In the Actian Data Platform, click the Copy button to copy the Secret Key to the clipboard and paste it in your third-party application.
10. Click Save to save the listener.

11. Click outside the dialog to close it.

To edit or delete a listener

1. On the navigation pane on the left, click Listeners.

    The Integrations Listener page is displayed, listing all listeners.

2. Click the name of the listener you want to modify.

    The Manage Listener dialog appears on the right.

3. Do one or more of the following:

    - Select a new configuration from the dropdown.

    - From the Edit Keys dropdown, select Generate New Keys and confirm the creation of new keys.

    - From the Edit Keys dropdown, select Delete Keys and confirm the deletion of the keys.

4. Click the Save button.
5. To delete the listener, from the Edit Keys dropdown, select Delete Listener and confirm the deletion of the listener.
