---
title: "Nulls"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Nulls.htm"
canonical_id: "actian-data-platform-nulls"
---

## Nulls

A null represents an undefined or unknown value and is specified by the keywordnull. A null is not the same as a zero, a blank, or an empty string.

A null can be assigned to any nullable column when no other value is specifically assigned. More information about defining nullable columns is provided in [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md).

The IFNULL function and the [IS NULL Predicate](../SQLLanguage/Predicates_in_SQL.md) allow nulls in queries to be handled.

## Nulls and Comparisons

Because a null is not a value, it cannot be compared to any other value (including another null value). For example, the following WHERE clause evaluates to false if one or both of the columns is null:

```
WHERE columna = columnb
```

Similarly, the WHERE clause:

WHERE columna < 10 OR columna >= 10

is true for all numeric values of columna, but false if columna is null.

Although generally null values are ignored in comparisons, there are comparisons that can be used that do allow null values to be matched against. It is possible to test for the presence of a null value using IS NULL so a WHERE clause could be constructed that allowed null values to match such as:

WHERE columna=columnb OR (columna IS NULL AND columnb IS NULL)

An operator that embodies this behavior is IS NOT DISTINCT FROM. It behaves like = (equals) and will compare null values as will its <> (not equal) equivalent IS DISTINCT FROM. The following WHERE clause evaluates to false unless both columna and columnb are equal or both columna and columnb are NULL:

```
WHERE columna IS NOT DISTINCT FROM columnb
```

## Nulls and Aggregate Functions

If an aggregate function against a column that contains nulls is executed, the function ignores the nulls. This prevents unknown or inapplicable values from affecting the result of the aggregate. For example, if the aggregate function, AVG(), is applied to a column that holds the ages of your employees, be sure that any ages that have not been entered in the table are not treated as zeros by the function. This distorts the true average age. If a null is assigned to any missing ages, the aggregate returns a correct result: the average of all known employee ages.

Aggregate functions, except COUNT(), return null for an aggregate that has an argument that evaluates to an empty set. (COUNT() returns 0 for an empty set.) In the following example, the select returns null, because there are no rows in the table named test.

```
 testnull (col1 INTEGER NOT NULL);SELECT MAX(col1) AS x FROM testnull;
```

In the above example, use the IFNULL function to return a zero (0) instead of a null:

```
SELECT IFNULL(MAX(coll),0) AS x FROM testnull;
```

!!! note "Note"

    When specifying a column that contains nulls as a grouping column (that is, in the GROUP BY clause) for an aggregate function, nulls in the column are treated as equal for the purposes of grouping as if IS NOT DISTINCT FROM were used. In all other situations, nulls do not compare as equal to other nulls.
