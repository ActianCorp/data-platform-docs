---
title: "What You Should Know When Creating Multiple Sessions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "What_You_Should_Know_When_Creating_Multiple_Sess.htm"
canonical_id: "actian-data-platform-what-you-should-know-when-creating-multiple-sess"
---

## What You Should Know When Creating Multiple Sessions

The Actian Data Platform treats each session in a multiple-session application as an individual application. When creating multiple-session applications, keep the following points in mind:

- Be sure that the server parameter connect_limit is large enough to accommodate the number of sessions required by the application.
- An application can encounter deadlock against itself. For example, one session may attempt to update a table that was locked by another session.

- An application can also lock itself out in an undetectable manner. For example, if a table is updated in a transaction in one session and selected from in another transaction in a second session, the second session waits indefinitely.
