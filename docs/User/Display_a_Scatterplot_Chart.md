---
title: "Display a Scatterplot Chart"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Display_a_Scatterplot_Chart.htm"
canonical_id: "actian-data-platform-display-a-scatterplot-chart"
---

## Display a Scatterplot Chart

To display a scatterplot chart

1. Run your query to display the results in the query results pane (see [Run Your Own Queries](../User/Run_Your_Own_Queries.md) or [Run Sample Queries](../User/Run_Sample_Queries.md)).
2. Do the following:

    ![](images/QueryConfigureVisualizationIcon.png)

    The Configure Visualization dialog opens. ]

    Google Cloud and AWS AV-2: If this is the first time creating a chart, click the Create Chart button.

    The Results Chart panel opens. ]

3. From the Type of Visualization dropdown menu, select Scatterplot.

    Fields for the chart type are displayed.

4. Set values for each field in the selected chart type.

    AWS AV-1 and Azure:

| Field | Description |
| --- | --- |
| x Axis | The query result column to determine the x-axis values and range |
| y Axis | The query result column to use to determine the y-axis values and range |
| Size | The query result column to use to determine the width of the line or diameter of the data point |
| Color | The query result column to use to identify a series of data. Each value will map to a series, resulting in a new line with a new color. |
| x Facet | The query result column to use to break a chart into multiple small charts, arranged on the x axis. A small chart will be created for each value. |
| Y Facet | The query result column to use to break a chart into multiple small charts, arranged on the y axis. A small chart will be created for each value. |
| Quick Filter | Toggle to show or hide quick filter functionality |
| Show Trendline | Toggle to show or hide trendline and related trendline UI |

    Google Cloud and AWS AV-2:

| Field | Description |
| --- | --- |
| X-Axis | The query result column to determine the x-axis values and range |
| Y-Axis | The query result column to use to determine the y-axis values and range |

5. Click OK or Create Chart.

    The graph is displayed.

For more information, see [Open a Chart in a New Window](../User/Open_a_Chart_in_a_New_Window.md) and [Save a Chart Image as a PNG File](../User/Save_a_Chart_Image_as_a_PNG_File.md).
