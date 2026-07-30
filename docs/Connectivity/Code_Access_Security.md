---
title: "Code Access Security"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Code_Access_Security.htm"
canonical_id: "actian-data-platform-code-access-security"
---

## Code Access Security

The .NET Data Provider assembly requires the FullTrust permission to load, access the network, read and write certain files, and use other system resources.

The .NET Data Provider is a strongly named assembly, making it eligible for installation into the Global Assembly Cache and resistant to code tampering.

The Ingres.Client assembly contains the attribute AllowPartiallyTrustedCallersAttribute (APTCA) to allow the .NET Data Provider to be called by a partially trusted assembly. APTCA has no effect on Ingres or Actian Data Platform database security. Database security checks are performed as usual.
