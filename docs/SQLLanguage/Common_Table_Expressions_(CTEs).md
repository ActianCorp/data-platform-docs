---
title: "Common Table Expressions (CTEs)"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Common_Table_Expressions_(CTEs).htm"
canonical_id: "actian-data-platform-common-table-expressions-ctes"
---

## Common Table Expressions (CTEs)

A Common Table Expression (CTE) is a temporary named result set, derived from a simple query and defined within the execution scope of a SELECT or INSERT statement.

After a CTE is defined, it can be referenced like a table or view can in a SELECT or INSERT statement. A CTE can also be used in a ...AS SELECT or CREATE VIEW statement as part of its defining SELECT statement.

A CTE is similar to a derived table in that it is not stored and lasts only for the duration of the query. Unlike a derived table, a CTE behaves more like an in-line view and can be referenced multiple times in the same query.

Using a CTE makes complex queries easier to read and maintain. Because a CTE can be referred to multiple times in a query, syntax can be simpler. You can divide the query into separate building blocks, which you can then use to build more complex CTEs until the final result set is returned.

Among other things, a CTE may be useful when you need to join the results of a GROUP BY with another table.

More information:

[WITH (common_table_expression)](../SQLLanguage/WITH_(common_table_expression).md)

## Common Table Expression Format

A query that uses a common table expression has the following format:

```
[ WITH { with_list_element },... ] SELECT_expr ;
```

where with_list_elementformat is:

```
table_name [ ( { column_name },... ) ] AS ( query_expr ) ;
```

## Components of a CTE

This simple example shows the components of a common table expression.

```
 s (c INT, i INT);
```

```
INSERT INTO s VALUES (10,1),(20,2),(30,3),(100,15),(200,15),(300,15);
```

```
COMMIT;
```

```
/* Define the CTE expression and column list */
```

```
WITH t(z) AS
```

```
/* Define the CTE query */
```

```
(
```

```
        SELECT c FROM s WHERE i > 10
```

```
 )
```

```
/*Define outer query that references the CTE name */
```

```
SELECT t.z FROM t ORDER BY 1;
```

```
Executing . . .
```

```
z
```

```
-------------
```

```
          100
```

```
          200
```

```
          300
```

```
(3 rows)
```

The t is the name of the first (and in this case only) WITH element (also known as a CTE). There can be multiple WITH elements in the same query. Each WITH element can be referred to by its name as though it were a view. The scope of each WITH element extends to the right through the rest of the SQL statement. WITH elements can refer to others that have been declared already in the current statement. For example:

```
WITH
```

```
 t(z) AS (
```

```
        SELECT c FROM s WHERE i > 10
```

```
 ),
```

```
 u(a,i) AS (
```

```
        SELECT z, 15 FROM t
```

```
 )
```

```
SELECT u.a,s.i FROM u,s WHERE s.i=u.i ORDER BY 1;
```

```
Executing . . .
```

```
a             i
```

```
------------- ------------
```

```
          100           15
```

```
          100           15
```

```
          100           15
```

```
          200           15
```

```
          200           15
```

```
          200           15
```

```
          300           15
```

```
          300           15
```

```
          300           15
```

```
(9 rows)
```

## How CTEs Are Used

Each time a WITH element name is referenced, either from the main query or from another WITH element, a new derived table and correlation instance are created.

This is simple when a WITH element contains only a table or view in its FROM list. When one WITH element refers to another, however, derived tables are replicated for the full recursive set of referred to elements and not only for the element itself.

## Examples of Using CTEs: The Person and Relative Tables

The CTE examples in this section assume the following data in two tables:

| Person table |  |  | Relatives table |  |
| --- | --- | --- | --- | --- |
| Name | Gender |  | Name | Parent |
| Me | M |  | Me | Mom |
| Sis | F |  | Me | Dad |
| Dad | M |  | Sis | Mom |
| Mom | F |  | Sis | Dad |
| Bro | M |  | Bro | Mom |
| StSis | F |  | Bro | Dad |
| Uncle1 | M |  | Dad | GrDad |
| Uncle2 | M |  | Dad | GrMa |
| Aunt | F |  | StSis | Dad |
| GrDad | M |  | StSis | StMom |
| GrMa | F |  | Uncle1 | GrDad |
| GrGrDad | M |  | Uncle1 | GrMa |
| GrGrMa | F |  | Uncle2 | GrDad |
| Son | M |  | Uncle2 | GrMa |
| GrSon | M |  | Aunt | GrDad |
| Daugtr | F |  | Aunt | GrMa |
| GrDaugtr | F |  | GrDad | GrGrDad |
| Dog | F |  | GrDad | GrGrMa |
| StMom | F |  | Son | Me |
| Niece | F |  | GrSon | Son |
| Nephew | M |  | Daugtr | Me |
| Cousin | M |  | GrDaugtr | Son |
|  |  |  | Niece | Sis |
|  |  |  | Nephew | Bro |
|  |  |  | Cousin | Uncle1 |

With this data we can perform simple lookups that can be used to answer relationship questions.

Q: Who is the mother of whom?

To answer who is the mother of whom we can write:

```
WITH
```

```
ismother(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='F'
```

```
)
```

```
SELECT * FROM ismother
```

```
ORDER BY 1,2;
```

The ismotherresult set is returned:

ismother

```
name           child
```

```
------         -------
```

```
GrGrMa         GrDad
```

```
GrMa           Aunt
```

```
GrMa           Dad
```

```
GrMa           Uncle1
```

```
GrMa           Uncle2
```

```
Mom            Bro
```

```
Mom            Me
```

```
Mom            Sis
```

```
Sis            Niece
```

```
StMom          StSis
```

### Referring to a Defined WITH Element

Q: Who are parents?

To determine who are parents we could simply apply a UNION where we needed it, but we can also define a further element, isparent:

```
WITH
```

```
ismother(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='F'
```

```
),
```

```
isfather(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='M'
```

```
),
```

```
isparent(name, child) AS (
```

```
        SELECT name,child FROM ismother
```

```
        UNION ALL
```

```
        SELECT name,child FROM isfather
```

```
)
```

```
SELECT * FROM isparent
```

```
ORDER BY 1,2;
```

The isparentresult set is returned:

isparent

```
name          child
```

```
------        ------
```

```
Bro           Nephew
```

```
Dad           Bro
```

```
Dad           Me
```

```
Dad           Sis
```

```
Dad           StSis
```

```
GrDad         Aunt
```

```
GrDad         Dad
```

```
GrDad         Uncle1
```

```
GrDad         Uncle2
```

```
GrGrDad       GrDad
```

```
GrGrMa        GrDad
```

```
GrMa          Aunt
```

```
GrMa          Dad
```

```
GrMa          Uncle1
```

```
GrMa          Uncle2
```

```
Me            Daugtr
```

```
Me            Son
```

```
Mom           Bro
```

```
Mom           Me
```

```
Mom           Sis
```

```
Sis           Niece
```

```
Son           GrDaugtr
```

```
Son           GrSon
```

```
StMom         StSis
```

```
Uncle1        Cousin
```

Because the dependencies are simple, the same result could be achieved with simple substitution into derived tables as shown here:

```
SELECT * FROM
```

```
        ( SELECT name,child FROM
```

```
                ( SELECT parent AS name,r.name AS child
```

```
                  FROM person p JOIN relatives r
```

```
                        ON p.name=r.parent AND gender='F'
```

```
                ) AS ismother
```

```
          UNION ALL
```

```
          SELECT name,child FROM
```

```
                ( SELECT parent AS name,r.name AS child
```

```
                  FROM person p JOIN relatives r
```

```
                        ON p.name=r.parent AND gender='M'
```

```
                ) AS isfather
```

```
        ) AS isparent
```

```
ORDER BY 1,2;
```

### Using Nested WITH Element References

The following example introduces the first level of complexity.

Q: Who are grandparents?

Finding who are grandparents could be achieved by a joining of two isparentreferences but, as before, we will define the gender specific elements and union them.

The complexity arises when you notice that:

ismotherand isfatherare both present in the definition of isparent.

ismotherand isfatherare also both present in the definition of isgrfatherand isgrmother, both of which also refer to isparent.

For this to work, the instances of ismotherand isfathermust be distinct in the join from those expanded in isparent. Now it is seen why this acts like an inline view: Although the elements are defined once, nested references between these cause recursive replication of derived tables to the referenced elements.

```
WITH
```

```
ismother(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='F'
```

```
),
```

```
isfather(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='M'
```

```
),
```

```
isparent(name, child) AS (
```

```
        SELECT name,child FROM ismother
```

```
        UNION ALL
```

```
        SELECT name,child FROM isfather
```

```
),
```

```
isgrfather(name, grchild) AS (
```

```
        SELECT f.name,p.child
```

```
        FROM isfather f JOIN isparent p ON f.child=p.name
```

```
),
```

```
isgrmother(name, grchild) AS (
```

```
        SELECT f.name,p.child
```

```
        FROM ismother f JOIN isparent p ON f.child=p.name
```

```
)
```

```
SELECT name,'isgrfather',grchild FROM isgrfather
```

```
UNION ALL
```

```
SELECT name,'isgrmother',grchild FROM isgrmother
```

```
ORDER BY 2,1,3;
```

grandparents

```
name         col2           grchild
```

```
---------    -----------    -----------
```

```
Dad          isgrfather     Daugtr
```

```
Dad          isgrfather     Niece
```

```
Dad          isgrfather     Nephew
```

```
Dad          isgrfather     Son
```

```
GrDad        isgrfather     Bro
```

```
GrDad        isgrfather     Cousin
```

```
GrDad        isgrfather     Me
```

```
GrDad        isgrfather     Sis
```

```
GrDad        isgrfather     StSis
```

```
GrGrDad      isgrfather     Aunt
```

```
GrGrDad      isgrfather     Dad
```

```
GrGrDad      isgrfather     Uncle1
```

```
GrGrDad      isgrfather     Uncle2
```

```
Me           isgrfather     GrDaugtr
```

```
Me           isgrfather     GrSon
```

```
GrGrMa       isgrmother     Aunt
```

```
GrGrMa       isgrmother     Dad
```

```
GrGrMa       isgrmother     Uncle1
```

```
GrGrMa       isgrmother     Uncle2
```

```
GrMa         isgrmother     Bro
```

```
GrMa         isgrmother     Cousin
```

```
GrMa         isgrmother     Me
```

```
GrMa         isgrmother     Sis
```

```
GrMa         isgrmother     StSis
```

```
Mom          isgrmother     Daugtr
```

```
Mom          isgrmother     Niece
```

```
Mom          isgrmother     Nephew
```

```
Mom          isgrmother     Son
```

Q: Who are brother and sister?

To further illustrate nested CTEs, we ask the question, “Who are brother and sister?”

We can define a sharefather(and a sharemother) by checking each pairing of persons with whether there exists a third person such that the relationship isfather (or ismother) holds for both. Taking a union of these gives the answer:

```
WITH
```

```
ismother(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='F'
```

```
),
```

```
isfather(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='M'
```

```
),
```

```
isparent(name, child) AS (
```

```
        SELECT f.name, f.child FROM isfather f
```

```
        UNION ALL
```

```
        SELECT m.name, m.child FROM ismother m
```

```
),
```

```
sharefather(name, sibling, father) AS (
```

```
        SELECT a.child,b.child,a.name
```

```
        FROM isfather a JOIN isfather b
```

```
                ON a.name=b.name AND a.child<b.child
```

```
),
```

```
sharemother(name, sibling, mother) AS (
```

```
        SELECT a.child,b.child,a.name
```

```
        FROM ismother a JOIN ismother b
```

```
                ON a.name=b.name AND a.child<b.child
```

```
)
```

```
SELECT name, sibling FROM sharefather UNION
```

```
SELECT name, sibling FROM sharemother ORDER BY 1,2;
```

issibling

```
name         sibling
```

```
--------     -------
```

```
Aunt         Dad
```

```
Aunt         Uncle1
```

```
Aunt         Uncle2
```

```
Bro          Me
```

```
Bro          Sis
```

```
Bro          StSis
```

```
Dad          Uncle1
```

```
Dad          Uncle2
```

```
Daugtr       Son
```

```
GrDaugtr     GrSon
```

```
Me           Sis
```

```
Me           StSis
```

```
Sis          StSis
```

```
Uncle1       Uncle2
```

Q: Who are full siblings?

Noting that the previous result includes a few step relations suggests a query to determine only full siblings by joining sharefatherand sharemother:

```
WITH
```

```
ismother(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='F'
```

```
),
```

```
isfather(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='M'
```

```
),
```

```
isparent(name, child) AS (
```

```
        SELECT f.name, f.child FROM isfather f
```

```
        UNION ALL
```

```
        SELECT m.name, m.child FROM ismother m
```

```
),
```

```
sharefather(name, sibling, father) AS (
```

```
        SELECT a.child,b.child,a.name
```

```
        FROM isfather a JOIN isfather b
```

```
                ON a.name=b.name AND a.child<>b.child
```

```
),
```

```
sharemother(name, sibling, mother) AS (
```

```
        SELECT a.child,b.child,a.name
```

```
        FROM ismother a JOIN ismother b
```

```
                ON a.name=b.name AND a.child<>b.child
```

```
),
```

```
issibling(name,sibling,mother,father) AS (
```

```
        SELECT sf.name,sf.sibling,sm.mother,sf.father
```

```
        FROM sharefather sf JOIN sharemother sm
```

```
        ON sf.name=sm.name AND sf.sibling=sm.sibling
```

```
)
```

```
SELECT * FROM issibling
```

```
ORDER BY 1, 2;
```

full siblings

```
name           sibling           mother         father
```

```
------------   ---------------   ------------   ----------
```

```
Aunt           Dad               GrMa           GrDad
```

```
Aunt           Uncle1            GrMa           GrDad
```

```
Aunt           Uncle2            GrMa           GrDad
```

```
Bro            Me                Mom            Dad
```

```
Bro            Sis               Mom            Dad
```

```
Dad            Aunt              GrMa           GrDad
```

```
Dad            Uncle1            GrMa           GrDad
```

```
Dad            Uncle2            GrMa           GrDad
```

```
Me             Bro               Mom            Dad
```

```
Me             Sis               Mom            Dad
```

```
Sis            Bro               Mom            Dad
```

```
Sis            Me                Mom            Dad
```

```
Uncle1         Aunt              GrMa           GrDad
```

```
Uncle1         Dad               GrMa           GrDad
```

```
Uncle1         Uncle2            GrMa           GrDad
```

```
Uncle2         Aunt              GrMa           GrDad
```

```
Uncle2         Dad               GrMa           GrDad
```

```
Uncle2         Uncle1            GrMa           GrDad
```

Q: Who are aunts and uncles?

If we add elements issonand isdaughterthen we can also derive hasnephewand hasniecebased on the other tables.

```
WITH
```

```
ismother(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='F'
```

```
),
```

```
isfather(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='M'
```

```
),
```

```
isparent(name, child) AS (
```

```
        SELECT f.name, f.child FROM isfather f
```

```
        UNION ALL
```

```
        SELECT m.name, m.child FROM ismother m
```

```
),
```

```
sharefather(name,sibling,father) AS (
```

```
        SELECT p2.name,p3.name,a.name
```

```
        FROM person p2,person p3,isfather a JOIN isfather b ON a.name=b.name
```

```
        WHERE p2.name<>p3.name AND a.child=p2.name AND b.child=p3.name
```

```
),
```

```
sharemother(name,sibling,mother) AS (
```

```
        SELECT p2.name,p3.name,a.name
```

```
        FROM person p2, person p3,ismother a JOIN ismother b ON a.name=b.name
```

```
        WHERE p2.name<>p3.name AND a.child=p2.name AND b.child=p3.name
```

```
),
```

```
issibling AS (
```

```
        SELECT sf.name,sf.sibling,sf.father,sm.mother
```

```
        FROM sharefather sf JOIN sharemother sm
```

```
        ON sf.name=sm.name AND sf.sibling=sm.sibling
```

```
),
```

```
isson(name, mother, father) AS (
```

```
        SELECT p1.name,ms.name,fs.name
```

```
        FROM person p1 LEFT OUTER JOIN isfather fs
```

```
                ON p1.name=fs.child
```

```
                        LEFT OUTER JOIN ismother ms
```

```
                ON p1.name=ms.child
```

```
        WHERE p1.gender='M'
```

```
),
```

```
isdaughter(name, mother, father) AS (
```

```
        SELECT p1.name,md.name,fd.name
```

```
        FROM person p1 LEFT OUTER JOIN isfather fd
```

```
                ON p1.name=fd.child
```

```
                        LEFT OUTER JOIN ismother md
```

```
                ON p1.name=md.child
```

```
        WHERE p1.gender='F'
```

```
),
```

```
hasnephew(name, nephew, sibling) AS (
```

```
        SELECT i.name,s.name,i.sibling
```

```
        FROM issibling i INNER JOIN isson s
```

```
                ON i.sibling=s.mother OR i.sibling=s.father
```

```
),
```

```
hasniece(name, niece, sibling) AS (
```

```
        SELECT i1.name,d.name,i1.sibling
```

```
        FROM issibling i1 INNER JOIN isdaughter d
```

```
                ON i1.sibling=d.mother OR i1.sibling=d.father
```

```
)
```

```
SELECT 'F', name, niece AS rel, sibling FROM hasniece UNION
```

```
SELECT 'M', name, nephew AS rel, sibling FROM hasnephew
```

```
ORDER BY 1,2,3;
```

aunts + uncles

```
col1         name           rel           sibling
```

```
----------   ------------   -----------   -------
```

```
F            Aunt           Cousin        Uncle1
```

```
F            Aunt           Sis           Dad
```

```
F            Aunt           StSis         Dad
```

```
F            Bro            Daugtr        Me
```

```
F            Bro            Niece         Sis
```

```
F            Dad            Cousin        Uncle1
```

```
F            Me             Niece         Sis
```

```
F            Sis            Daugtr        Me
```

```
F            Uncle1         Sis           Dad
```

```
F            Uncle1         StSis         Dad
```

```
F            Uncle2         Cousin        Uncle1
```

```
F            Uncle2         Sis           Dad
```

```
F            Uncle2         StSis         Dad
```

```
M            Aunt           Bro           Dad
```

```
M            Aunt           Me            Dad
```

```
M            Bro            Son           Me
```

```
M            Me             Nephew        Bro
```

```
M            Sis            Nephew        Bro
```

```
M            Sis            Son           Me
```

```
M            Uncle1         Bro           Dad
```

```
M            Uncle1         Me            Dad
```

```
M            Uncle2         Bro           Dad
```

```
M            Uncle2         Me            Dad
```

### WITH Elements in CREATE VIEW

The WITH syntax of a CTE is not only applicable to queries but can also appear in contexts like AS SELECT or CREATE VIEW. For example:

```
CREATE VIEW issibling AS
```

```
WITH
```

```
ismother(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='F'
```

```
),
```

```
isfather(name, child) AS (
```

```
        SELECT parent,r.name
```

```
        FROM person p JOIN relatives r ON p.name=r.parent AND gender='M'
```

```
),
```

```
isparent(name, child) AS (
```

```
        SELECT f.name, f.child FROM isfather f
```

```
        UNION ALL
```

```
        SELECT m.name, m.child FROM ismother m
```

```
),
```

```
sharefather(name,sibling,father) AS (
```

```
        SELECT p2.name,p3.name,a.name
```

```
        FROM person p2,person p3,isfather a JOIN isfather b ON a.name=b.name
```

```
        WHERE p2.name<>p3.name AND a.child=p2.name AND b.child=p3.name
```

```
),
```

```
sharemother(name,sibling,mother) AS (
```

```
        SELECT p2.name,p3.name,a.name
```

```
        FROM person p2, person p3,ismother a JOIN ismother b ON a.name=b.name
```

```
        WHERE p2.name<>p3.name AND a.child=p2.name AND b.child=p3.name
```

```
),
```

```
issibling AS (
```

```
        SELECT sf.name,sf.sibling,sf.father,sm.mother
```

```
        FROM sharefather sf JOIN sharemother sm
```

```
        ON sf.name=sm.name AND sf.sibling=sm.sibling
```

```
)
```

```
SELECT * FROM issibling;
```

!!! note "Note"

    In this example the defined view name happens to be the same as one of the WITH elements in the query. There is no conflict because the WITH element names remain local to the query.
