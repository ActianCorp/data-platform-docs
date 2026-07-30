---
title: "JSON Sequences"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Sequences.htm"
canonical_id: "actian-data-platform-json-sequences"
---

## JSON Sequences

A sequence is a set of values retrieved from an JSON object using a JSON path containing a wildcard.

A sequence can be returned using the JSON_QUERY function when wrapped inside an array wrapper.

A sequence can also be passed as an operand to a comparison function or an item method.

When passed as an operand into a comparison function, each value in the sequence is tested using the comparison operator. If an invalid comparison is detected (for example, a data type conflict) then an error is returned. If a comparison returns TRUE, and the mode is lax, then TRUE is immediately returned. If the mode is strict, all values of the sequence are checked to confirm that no comparison errors occur.

When a sequence is passed to an item method, the item method is run against all values of the sequence.
