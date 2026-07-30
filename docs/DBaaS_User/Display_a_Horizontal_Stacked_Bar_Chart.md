---
title: "Display a Horizontal Stacked Bar Chart"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Display_a_Horizontal_Stacked_Bar_Chart.htm"
canonical_id: "actian-data-platform-display-a-horizontal-stacked-bar-chart"
---

## Display a Horizontal Stacked Bar Chart

To display a horizontal stacked bar chart

1. Run your query to display the results in the query results pane (see [Run Your Own Queries](../DBaaS_User/Run_Your_Own_Queries_2.md) or [Run Sample Queries](../DBaaS_User/Run_Sample_Queries.md)).
2. Do the following:

![](images/QueryConfigureVisualizationIcon.png)

    The Configure Visualization dialog opens. ]

    Google Cloud and AWS AV-2: If this is the first time creating a chart, click the Create Chart button.

    The Results Chart panel opens. ]

3. From the Type of Visualization dropdown menu, select Stacked Bar - Horizontal.

    Fields for the chart type are displayed.

4. Set values for each field in the selected chart type.

    AWS AV-1 and Azure:

| Field | Description |
| --- | --- |
| Bar Label | The query result column to use to label a bar in a bar chart |
| Bar Value | The query result column to use as a value for a bar in a bar chart. |
| Color | The query result column to use to identify a series of data. Each value will map to a series, resulting in a new line with a new color. |
| Bar Label Facet | The query result column to use to break the chart into multiple small charts. A small chart will be created for each value in the column, along the axis that holds the bar label. |

    Google Cloud and AWS AV-2:

| Field | Description |
| --- | --- |
| Bar Label | The query result column to use to label a bar in a bar chart |
| Bar Value | The query result column to use as a value for a bar in a bar chart. |

5. Click OK or Create Chart.

    The graph is displayed.

For more information, see [Open a Chart in a New Window](../DBaaS_User/Open_a_Chart_in_a_New_Window.md) and [Save a Chart Image as a PNG File](../DBaaS_User/Save_a_Chart_Image_as_a_PNG_File.md).
