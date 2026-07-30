---
title: "Display a Line Chart"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Display_a_Line_Chart.htm"
canonical_id: "actian-data-platform-display-a-line-chart"
---

## Display a Line Chart

To display a line chart

1. Run your query to display the results in the query results pane (see [Run Your Own Queries](../User/Run_Your_Own_Queries.md) or [Run Sample Queries](../User/Run_Sample_Queries.md)).
2. Do the following:

    ![](images/QueryConfigureVisualizationIcon.png)

    The Configure Visualization dialog opens. ]

    Google Cloud and AWS AV-2: If this is the first time creating a chart, click the Create Chart button.

    The Results Chart panel opens. ]

3. From the Type of Visualization dropdown menu, select Line.

    Fields for the chart type are displayed.

4. Set values for each field in the selected chart type.

    AWS AV-1 and Azure:

| Field | Description |
| --- | --- |
| x | The query result column to determine the x-axis values and range |
| y | The query result column to determine the y-axis values and range |
| color/line for each | The query result column to use to identify a series of data. Each value will map to a series, resulting in a new line with a new color. |
| size | The query result column to use to determine the width of the line or diameter of the data point |
| x Facet | The query result column to use to break a chart into multiple small charts, arranged on the x axis. A small chart will be created for each value. |
| y Facet | The query result column to use to break a chart into multiple small charts, arranged on the y axis. A small chart will be created for each value. |
| Quick Filter | Toggle to show or hide quick filter functionality |
| Show Trendline | Toggle to show or hide trendline and related trendline UI |
| y Axis Min | Min value to show on y axis |
| y Axis Max | Max value to show on y axis |

    Google Cloud and AWS AV-2:

| Field | Description |
| --- | --- |
| X-Axis | The query result column to determine the x-axis values and range |
| Y-Axis | The query result column to determine the y-axis values and range |
| y Axis Min | Min value to show on y axis |
| y Axis Max | Max value to show on y axis |

5. Click OK.

    The graph is displayed in the visualization pane.

For more information, see [Open a Chart in a New Window](../User/Open_a_Chart_in_a_New_Window.md) and [Save a Chart Image as a PNG File](../User/Save_a_Chart_Image_as_a_PNG_File.md).
