---
title: "Run Sample Queries"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "RunSampleQueries.htm"
canonical_id: "actian-data-platform-runsamplequeries"
---

# Run Sample Queries

The following table contains queries you can run against the “sample” data set, which is included with every warehouse you provision. It contains airline data from the U.S. Department of Transportation Bureau of Transportation Statistics (the most current data available from [https://transtats.bts.gov](https://transtats.bts.gov)).

Copy the commands from the “SQL” column and paste them into your query document. To use the Query Editor, see [Run Your Own Queries](../User/Run_Your_Own_Queries.md).

!!! note "Note"

    If you are accessing the warehouse using the SQL Command Line Interface (CLI, installed with the [Avalanche Client Runtime Package](../User/Access_Warehouse_or_Database_Connection_Informat.md)) through a terminal monitor, be sure to end each command with \g. If you are using a JDBC connection and a third-party tool such as DBeaver, the \g line terminator is not needed.

| Description | SQL |
| --- | --- |
| Which day has the most flights from 2014–2019 ordered by number of flights descending | `SELECT description AS day_of_week, Count(*) AS num_flights FROM sample.ontime a, sample.l_weekdays b WHERE a.year BETWEEN 2014 AND 2019 AND a.dayofweek = b.code GROUP BY 1 ORDER BY 2 DESC` |
| Which day of the week has the most delayed flights from 2014–2019, ordered by number of flights descending | `SELECT description AS day_of_week, Count(*) AS no_flightsFROM sample.ontime a, sample.l_weekdays bWHERE depdelay > 10 AND "year" BETWEEN 2014 AND 2019 AND a.dayofweek = b.codeGROUP BY 1ORDER BY no_flights DESC` |
| Total number of flights where year > 2014 | `SELECT year, Count(*) AS numberofflightsFROM sample.ontimeWHERE year > 2014GROUP BY year` |
| Percentage of delays for each carrier for 2018. | `SELECT t3.description AS airline, total, delayed, Varchar(delayed*100/total) + '%' AS percentage FROM (SELECT reporting_airline, Count(*) AS delayed FROM sample.ontime WHERE depdelay > 10 AND year = 2018 GROUP BY reporting_airline) t JOIN (SELECT reporting_airline, Count(*) AS total FROM sample.ontime WHERE year = 2018 GROUP BY reporting_airline) t2 ON ( t.reporting_airline = t2.reporting_airline ) JOIN sample.l_unique_carriers t3 ON Char(t3.code) = t.reporting_airline ORDER BY percentage DESC` |
| Count all the rows in the ontime table | `SELECT Count(*) AS count FROM sample.ontime` |
| Which cities are served the most by other cities | `SELECT TOP 10 destcityname AS Destination, Count(DISTINCT origincityname) AS OriginCityCount FROM sample.ontime WHERE year = 2018 GROUP BY 1 ORDER BY 2 DESC` |
| Top 10 Markets with most destinations | `SELECT m.description AS Market,Listagg(DISTINCT c.origincityname, '; ') within GROUP (ORDER BY c.origincityname) AS originarea,count(*) AS num_of_destinationsFROM (SELECT origincitymarketid,destcitymarketidFROM sample.ontimeWHERE year = 2018GROUP BY 1,2) ctJOIN(SELECT origincitymarketid,origincitynameFROM sample.ontimeGROUP BY 1,2) cON c.origincitymarketid = ct.origincitymarketidJOIN sample.l_city_market_id m on m.code= ct.origincitymarketidGROUP BY 1ORDER BY 3 DESCFETCH first 10 rows only` |
| Reasons for aircraft delays for 2018 | `SELECT 'Carrier Delay' AS Type, Count(*) AS TotalFROM sample.ontimeWHERE ( carrierdelay != 0 AND carrierdelay IS NOT NULL ) AND year = 2018UNIONSELECT 'Weather Delay' AS Type, Count(*) AS TotalFROM sample.ontimeWHERE ( weatherdelay != 0 AND weatherdelay IS NOT NULL ) AND year = 2018UNIONSELECT 'Nas Delay' AS Type, Count(*) AS TotalFROM sample.ontimeWHERE ( nasdelay != 0 AND nasdelay IS NOT NULL ) AND year = 2018UNIONSELECT 'Security Delay' AS Type, Count(*) AS TotalFROM sample.ontime WHERE ( securitydelay != 0 AND securitydelay IS NOT NULL ) AND year = 2018UNION SELECT 'Late Aircraft' AS Type, Count(*) AS TotalFROM sample.ontime WHERE ( lateaircraftdelay != 0 AND lateaircraftdelay IS NOT NULL ) AND year = 2018 ORDER BY 2 DESC` |

To load your own data into a warehouse, go to theData Loading Guide. See [Data Loading Overview](../DataLoading/DataLoadingOverview.md).
