---
title: "List of Logic Blocks"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "List_of_Logic_Blocks.htm"
canonical_id: "actian-data-platform-list-of-logic-blocks"
---

## List of Logic Blocks

The following table lists the available [Logic Blocks](../Integrations/Logic_Blocks.md).

| Block | Function | Description |
| --- | --- | --- |
| [IF/Else Block](../Integrations/Logic_Blocks.md) | If(expression, if_true, if_false) | Returns a value based on whether an expression evaluates to TRUE or FALSE. |
| [Comparison Operators Block](../Integrations/Logic_Blocks.md) | operand1 == operand2operand1 <> operand2operand1 < operand2operand1 <= operand2operand1 > operand2operand1 >= operand2 | Comparison operators compare the contents in a field to either the contents in another field or a constant. The operands may be numeric or string values. If both operands are numeric, then a numeric comparison is performed. If either of the operands is a string value, then a string comparison is performed. |
| [Logical Operator Block](../Integrations/Logic_Blocks.md) | operand1 And operand2operand1 Or operand2 | The “And” operator determines the logical conjunction of the two operands by treating nonzero values as a value of TRUE and zero values as FALSE.The “Or” operator determines the logical disjunction of the two operands. If either or both operands evaluate to TRUE (nonzero), then the result is TRUE. |
| [Is Null Block](../Integrations/Logic_Blocks.md) | IsNull(parameter) | Returns TRUE if the argument contains a null value, otherwise, returns FALSE. |
| [Is Numeric Block](../Integrations/Logic_Blocks.md) | IsNumeric(parameter) | Returns TRUE if the argument can be converted to numeric data type, otherwise, returns FALSE. |
