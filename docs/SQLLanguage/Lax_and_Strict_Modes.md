---
title: "Lax and Strict Modes"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Lax_and_Strict_Modes.htm"
canonical_id: "actian-data-platform-lax-and-strict-modes"
---

## Lax and Strict Modes

There are two modes for running JSON queries: lax and strict.

The mode determines what values or errors are returned during error or out of range conditions. For example, for out of range conditions, lax mode returns an empty sequence while strict mode returns an error. Strict mode should be used when an object is expected or required to have a specific structure.

The specific effects of lax and strict vary depending on the query and the data being accessed.
