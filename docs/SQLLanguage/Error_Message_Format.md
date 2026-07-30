---
title: "Error Message Format"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Error_Message_Format.htm"
canonical_id: "actian-data-platform-error-message-format"
---

## Error Message Format

Every error message consists of an error code and the accompanying error message text.

All error codes begin with E_, followed by one or two letters plus a 4-digit hexadecimal number, and, optionally, descriptive text or the decimal equivalent of the hex error code. For example:

```
E_GE9D6C_CONSTR_VIO
```

indicates a constraint violation.

If the error is a local error, the two letters following E_ indicate which facility issued the error. If the error is a generic error number, the two letters are GE. The hexadecimal error code is unique for each error.

Local error codes are stored in $II_SYSTEM/ingres/files/english/messages/message.text

Generic error codes are stored in $II_system/ingres/files/generr.h
