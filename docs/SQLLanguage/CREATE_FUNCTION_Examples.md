---
title: "CREATE FUNCTION Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_FUNCTION_Examples.htm"
canonical_id: "actian-data-platform-create-function-examples"
---

## CREATE FUNCTION Examples

1. Create a function named “add” that adds the values that correspond to function parameters a and b, both of integer data type, and returns the result as an integer. The function is written in JavaScript and can be called with its parameters swapped.

```
CREATE OR REPLACE FUNCTION add(a INTEGER, b INTEGER) RETURN (INTEGER) AS LANGUAGE JAVASCRIPT SOURCE='return a+b',COMMUTATIVE=TRUE;
```

2. Create a function that adds the values that correspond to function parameters a, b, and c, all of integer data type, and returns the result as an integer. The function is written in JavaScript.

```
CREATE OR REPLACE FUNCTION add(a INTEGER, b INTEGER, c INTEGER) RETURN (INTEGER) AS LANGUAGE JAVASCRIPT SOURCE='return a+b+c';
```

3. Create a function in SQL that adds the integer value corresponding to parameter n to the timestamp value corresponding to parameter d and returns it as a timestamp.

```
CREATE OR REPLACE FUNCTION dateadd(d TIMESTAMP, n INTEGER) RETURN (TIMESTAMP) ASBEGIN RETURN d+n*interval'1'day; END;
```

4. Create functions in SQL that calculate the hyperbolic sine, cosine, and tangent of the value corresponding to parameter x.

```
CREATE OR REPLACE FUNCTION cosh(x FLOAT8)RETURN(FLOAT8) ASBEGIN RETURN (EXP(x)+EXP(-x))/2;END;
```

```
CREATE OR REPLACE FUNCTION sinh(x FLOAT8)RETURN(FLOAT8) AS BEGIN RETURN (EXP(x)-EXP(-x))/2;END;
```

```
CREATE OR REPLACE FUNCTION tanh(x FLOAT8)RETURN(FLOAT8) AS BEGIN RETURN sinh(x)/cosh(x); END;
```

5. Create a skew function in SQL:

```
CREATE OR REPLACE FUNCTION skew(x FLOAT8) RETURN(FLOAT8)AS
```

```
  DECLARE n,av_x,av_x2,m3,sd FLOAT8 NOT NULL;
```

```
  BEGIN
```

```
  SELECT :n=count(x);
```

```
  SELECT :av_x=sum(x)/n;
```

```
  SELECT :av_x2=av_x*av_x;
```

```
  SELECT :sd=sqrt((sum(x*x)-2*sum(x)*av_x+av_x2*n)/(n-1));
```

```
  SELECT :m3=(sum(x*x*x)-3*av_x*sum(x*x)+3*av_x2*sum(x)-av_x2*av_x*n)/n;
```

```
  RETURN m3/(sd*sd*sd)
```

```
  END;
```

6. Create a kurtosis function in SQL:

```
CREATE OR REPLACE FUNCTION kurtosis(x FLOAT8) RETURN(FLOAT8)AS
```

```
  DECLARE n,av_x,av_x2,m4,m2 FLOAT8 NOT NULL;
```

```
  BEGIN
```

```
  SELECT :n=count(x);
```

```
  SELECT :av_x=sum(x)/n;
```

```
  SELECT :av_x2=av_x*av_x;
```

```
  SELECT :m2=(sum(x*x)-2*sum(x)*av_x+av_x2*n)/n
```

```
  SELECT :m4=(sum(x*x*x*x)-4*av_x*sum(x*x*x)+6*av_x2*sum(x*x)-4*av_x2*av_x*sum(x)+          av_x2*av_x2*n)/n;
```

```
  RETURN m4/(m2*m2)-3
```

```
  END;
```

!!! note "Note"

    Not all errors are detected when the function is compiled.

    JavaScript: If a JavaScript function contains no RETURN statement, you will see an error at runtime. The exact error depends on the specific problem with the function. If the function does not give a result, you will see the error: “ERROR: SCALAR_UDF:No return in Javascript UDF”. If the error is a runtime error in the UDF, then you will see a different error. ]
    Python: If a Python function contains no RETURN statement, the following error occurs when you define the function: “ERROR: UDF 'udfname': Return (required in UDF's AST.)” ]
