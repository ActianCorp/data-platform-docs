---
title: "Maintaining Connectivity"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Maintaining_Connectivity.htm"
canonical_id: "actian-data-platform-maintaining-connectivity"
---

# Maintaining Connectivity

The Communications Server starts automatically when you start your Actian warehouse.

A default number of 64 inbound and 64 outbound sessions are configured during the installation process. After the Communications Server has been running, you can change these default limits.

Resetting the maximum number of inbound and outbound sessions does not affect a currently running Communications Server. If you alter these figures after you start a Communications Server, you must stop and restart the server for the new limits to take effect.

The Ingres Net configuration parameters that determine the maximum number of allowed inbound and outbound sessions for a Communications Server are inbound_limit and outbound_limit.

The maximum values that you can assign to inbound_limit and outbound_limit are operating system dependent.

Linux:****When setting inbound and outbound session limits, the maximum number of sessions that can be concurrently supported cannot exceed 14 less than the number of file descriptors allocated to each process. Each session uses two file descriptors, so there cannot be more sessions than half the total number of file descriptors. The following formula expresses the maximum number of connections that can be supported at any given time:

inbound_limit + outbound_limit <= (per_process_open_file_limit - 14) / 2

The number of file descriptors allocated to a process is a Linux kernel parameter (NOFILES on most platforms). ]

Windows:****Actian uses the inbound_limit and outbound_limit values when it allocates resources. Consequently, if the sum of the new values is greater than the sum of the current values, you must shut down the instance (instead of only the Communications Server) and restart it so that the system can allocate the appropriate level of resources. If the sum of the new values is equal to or less than the sum of the current values, you can simply stop the Communications Server and restart it after you have reset the values. ]

## How You Set Inbound and Outbound Session Limits

The inbound_limit and outbound_limit parameters determine the maximum number of allowed inbound and outbound sessions for a Communications Server.
