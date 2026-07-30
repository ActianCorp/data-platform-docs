---
title: "Pivot Tables"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Pivot_Tables.htm"
canonical_id: "actian-data-platform-pivot-tables"
---

## Pivot Tables

A pivot table summarizes data selected from a table and groups it in a meaningful way. Selected column values become headings in the pivot table.

Consider the following table:

```
DROP TABLE IF EXISTS p;
```

```
CREATE TABLE p(name CHAR(5), val TINYINT, itm TINYINT);
```

```
INSERT INTO p VALUES('a',6,1),('a',9,1),('a',1,3),('a',2,3),
```

```
  ('a',9,1),('a',7,5),('b',6,1),('b',2,4),('b',0,9);
```

```
SELECT * FROM p;
```

```

```

```
+------+------+------+
```

```
|name  |val   |itm   |
```

```
+------+------+------+
```

```
|a     |     6|     1|
```

```
|a     |     9|     1|
```

```
|a     |     1|     3|
```

```
|a     |     2|     3|
```

```
|a     |     9|     1|
```

```
|a     |     7|     5|
```

```
|b     |     6|     1|
```

```
|b     |     2|     4|
```

```
|b     |     0|     9|
```

```
+------+------+------+
```

A pivot table lets you display columns of data grouped down the left side by name, with values in the itm column as headings, and each column showing the aggregation of val.

Here is an example pivot table based on the above data:

```
SELECT name,pv.*
```

```
  FROM p PIVOT (MAX(val)FOR itm IN (0,1,2,3,4,5,6,7,8,9)) AS pv
```

```
  GROUP BY name
```

```
  ORDER BY name;
```

```

```

```
+------+------+------+------+------+------+------+------+------+------+------+
```

```
|name  |0     |1     |2     |3     |4     |5     |6     |7     |8     |9     |
```

```
+------+------+------+------+------+------+------+------+------+------+------+
```

```
|a     |      |     9|      |     2|      |     7|      |      |      |      |
```

```
|b     |      |     6|      |      |     2|      |      |      |      |     0|
```

```
+------+------+------+------+------+------+------+------+------+------+------+
```

## PIVOT Format

The PIVOT is a SQL table reference and can be given a correlation variable.

PIVOT detects what column or columns to be grouped by so the GROUP BY can be used but is redundant.

PIVOT has the following format:

```
PIVOT (aggr-expr FOR selector IN (in-value-list, ...) {NOT IN AS var}) {AS pvt}
```

where:

**aggr-expr**

:   Specifies the aggregation used to present the row value under the corresponding data heading.

**FOR selector**

:   Specifies the column whose data will be pivoted to become the headings.

**IN in-value-list**

:   Lists the values from the selector column that will be the headings in the pivot table. By default, the data items will be matched exactly but if the data is not discrete, a range can be specified by using the keyword TO instead of a comma.

:   The in-value-list has the following format:

```
[ value1 [AS alias], value2 [AS alias],...
```

```
| value1 TO value2 [AS alias],...
```

```
| value1 TO value2 TO value3...
```

```
]
```

:   Ranges can overlap. The AS keyword can be used to adjust the column label to allow it to be clearly distinct from others.

:   The AS keyword in the in-value-list must follow either a simple value or a simple range. It cannot be used with the shorthand, multiple TO keyword syntax.

**NOT IN AS var**

:   (Optional) Catches the data from the selector column that fails to match any of the in-value-list elements. For discrete data this will be the simple collection of values not listed in the in-value-list. For a non-discrete in-value-list selection, this will include data that falls before or after the total range plus any holes implied by the ranges if they are non-contiguous.

:   If the in-value selector column contains any NULL values, then these rows will contribute to the NOT IN set, if specified.

**AS pvt**

:   Assigns an alias to the column headings.

More than one pivot can be specified at a time and the pvt can be used to identify which columns come from which pivot, as shown in [Range Pivoting](../SQLLanguage/Pivot_Tables.md).

## Pivot Table Examples

Consider the following table:

```
CREATE TABLE pe(
```

```
  country VARCHAR(10)NULL,
```

```
  yr SMALLINT NOT NULL,
```

```
  sales MONEY NULL);
```

```
 INSERT INTO pe VALUES
```

```
 ('Australia',2005,1309047.1978),('Germany',2006,521230.8475),
```

```
 ('US', 2007,2838512.3550),('France', 2008, 922179.0400),
```

```
 ('Australia',2007,3033784.2131),('France', 2005,180571.6920),
```

```
 ('UK', 2006,591586.8540),('Canada', 2006, 621602.3823),
```

```
 ('UK', 2005,291590.5194),('US', 2005, 1100549.4498),
```

```
 ('Canada',2007, 535784.4624),('France', 2007, 1026324.9692),
```

```
 ('Germany',2007,1058405.7305),('Australia', 2006,2154284.8835),
```

```
 ('UK',2008, 1210286.2700),('US', 2008, 3324031.1600),
```

```
 ('Germany', 2008, 1076890.7700),('UK', 2007, 1298248.5675),
```

```
 ('Australia',2008,2563884.2900),('Canada', 2005, 146829.8074),
```

```
 ('Germany', 2005, 237784.9902),('Canada', 2008, 673628.2100),
```

```
 ('US',2006, 2126696.5460),('France', 2006, 514942.0131);
```

```

```

```
+----------+------+--------------------+
```

```
|country   |yr    |sales               |
```

```
+----------+------+--------------------+
```

```
|Australia |  2005|         $1309047.20|
```

```
|Australia |  2006|         $2154284.88|
```

```
|Australia |  2007|         $3033784.21|
```

```
|Australia |  2008|         $2563884.29|
```

```
|Canada    |  2005|          $146829.81|
```

```
|Canada    |  2006|          $621602.38|
```

```
|Canada    |  2007|          $535784.46|
```

```
|Canada    |  2008|          $673628.21|
```

```
|France    |  2005|          $180571.69|
```

```
|France    |  2006|          $514942.01|
```

```
|France    |  2007|         $1026324.97|
```

```
|France    |  2008|          $922179.04|
```

```
|Germany   |  2005|          $237784.99|
```

```
|Germany   |  2006|          $521230.85|
```

```
|Germany   |  2007|         $1058405.73|
```

```
|Germany   |  2008|         $1076890.77|
```

```
|UK        |  2005|          $291590.52|
```

```
|UK        |  2006|          $591586.85|
```

```
|UK        |  2007|         $1298248.57|
```

```
|UK        |  2008|         $1210286.27|
```

```
|US        |  2005|         $1100549.45|
```

```
|US        |  2006|         $2126696.55|
```

```
|US        |  2007|         $2838512.36|
```

```
|US        |  2008|         $3324031.16|
```

```
+----------+------+--------------------+
```

### Sales Summary

The following creates a pivot table in which sales for each country is summarized for each year. By default, the column heading will be the data element chosen but as with ordinary result columns these can be renamed with an AS alias to give a more appropriate name if necessary.

```
SELECT country, p."2005",p."2006",p."2007",p."2008"
```

```
  FROM pe
```

```
  PIVOT(SUM(sales) FOR yr IN (2005, 2006, 2007, 2008)) AS p
```

```
  ORDER BY country;
```

```

```

```
+----------+--------------+--------------+--------------+--------------+
```

```
|country   |2005          |2006          |2007          |2008          |
```

```
+----------+--------------+--------------+--------------+--------------+
```

```
|Australia |   $1309047.20|   $2154284.88|   $3033784.21|   $2563884.29|
```

```
|Canada    |    $146829.81|    $621602.38|    $535784.46|    $673628.21|
```

```
|France    |    $180571.69|    $514942.01|   $1026324.97|    $922179.04|
```

```
|Germany   |    $237784.99|    $521230.85|   $1058405.73|   $1076890.77|
```

```
|UK        |    $291590.52|    $591586.85|   $1298248.57|   $1210286.27|
```

```
|US        |   $1100549.45|   $2126696.55|   $2838512.36|   $3324031.16|
```

```
+----------+--------------+--------------+--------------+--------------+
```

### Range Pivoting

The following example uses ranges to collect data values from the yr column and uses two pivots to generate both a sum and an average. Note that the result columns are both renamed and reordered.

```
SELECT country, p."2005" AS "2005-2006",a."2005" AS "2005-2006 avg",p."2008",
```

```
  a."2008" AS "2008 avg",p.rest,a.rest AS "avg rest"
```

```
  FROM pe
```

```
  PIVOT(SUM(sales) FOR yr IN (2005 TO 2007, 2008)NOT IN AS rest) AS p
```

```
  PIVOT(MONEY(AVG(sales)) FOR yr IN (2005 TO 2007, 2008)NOT IN AS rest) AS a
```

```
  ORDER BY 1;
```

```

```

```
+----------+-----------+-------------+-----------+-----------+-----------+-----------+
```

```
|country   |2005-2006  |2005-2006 avg|2008       |2008 avg   |rest       |avg rest   |
```

```
+----------+-----------+-------------+-----------+-----------+-----------+-----------+
```

```
|Australia |$3463332.08|  $1731666.04|$2563884.29|$2563884.29|$3033784.21|$3033784.21|
```

```
|Canada    | $768432.19|   $384216.10| $673628.21| $673628.21| $535784.46│ $535784.46|
```

```
|France    | $695513.70|   $347756.85| $922179.04| $922179.04|$1026324.97│$1026324.97|
```

```
|Germany   | $759015.84|   $379507.92|$1076890.77|$1076890.77|$1058405.73│$1058405.73|
```

```
|UK        | $883177.37|   $441588.69|$1210286.27|$1210286.27|$1298248.57│$1298248.57|
```

```
|US        |$3227246.00|  $1613623.00|$3324031.16|$3324031.16|$2838512.36│$2838512.36|
```

```
+----------+-----------+-------------+-----------+-----------+-----------+-----------+
```

## Pivot Table Usage Notes

In the previous example, we used the NOT IN clause to define a left-over bucket to aggregate the values falling outside of the specified buckets.

It is possible to list a data bucket but then not output that result; these will still be “IN” the data collection and hence be excluded from any NOT IN aggregation.

The example also uses the TO keyword to indicate that a range of values are to be clustered together. Notice that the TO value (the upper bound) is not included in the bucket. This simplifies the specification of non-overlapping values, so values 2002 TO 2007 will be greater than or equal to 2002 but strictly less than 2007. This example uses integer values, so the convention may seem odd but will make more sense when using data buckets that are less discrete, such as with floating point boundaries or other sortable data types.

For convenience, multiple range buckets can be specified at one time using the shorthand of 2003 TO 2006 TO 2009 TO 2012 instead of 2003 TO 2006, 2006 TO 2009, 2009 TO 2012.

For simplicity, the examples above use numeric columns for the pivot but any sortable data type can be used, such as string, date, timestamp, and time interval columns.

!!! note "Note"

    Case-sensitive data requires that the configuration parameter ii.hostname.createdb.delim_id_case be set to “mixed”; otherwise the column heading and consequent data selection will not match the data values. When using case-sensitive data, the column values in the IN list must be specified in double quotes (“ ”).

The results can also be referred to in selection expressions if needed, but in that case the select expressions will need to be placed in the HAVING clause as they will be referring to the result set. The following example shows these in use (no heading aliases):

```
SELECT COUNTRY, P.*,A.*
```

```
  FROM pe
```

```
  PIVOT(SUM(SALES) FOR YR IN (2005 TO 2007 TO 2008)NOT IN AS REST) AS P
```

```
  PIVOT(MONEY(AVG(SALES)) FOR YR IN (2005 TO 2007 TO 2008)NOT IN AS REST) AS A
```

```
  HAVING A."2005">1000000
```

```
  ORDER BY 1;
```

```

```

```
+----------+--------------+--------------+--------------+------------+------------+------------+
```

```
|country   |2005          |2007          |rest          |2005        |2007        |rest        |
```

```
+----------+--------------+--------------+--------------+------------+------------+------------+
```

```
|Australia |   $3463332.08|   $3033784.21|   $2563884.29| $1731666.04| $3033784.21| $2563884.29|
```

```
|US        |   $3227246.00|   $2838512.36|   $3324031.16| $1613623.00| $2838512.36| $3324031.16|
```

```
+----------+--------------+--------------+--------------+------------+------------+------------+
```
