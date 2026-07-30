---
title: "Cluster CPU Load"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Cluster_CPU_Load.htm"
canonical_id: "actian-data-platform-cluster-cpu-load"
---

## Cluster CPU Load

Measures 1-, 5-, and 15-minute CPU load averages as supplied by /proc/loadavg.

```
cpuLoad -w w1,w5,w15 -c c1,c5,c15
```

The load average is a count of jobs in the run queue that are either runnable or waiting for disk I/O. The warning and critical limits are expressed as floating point triples for 1-, 5-, and 15-minute load averages. The limits only make sense with respect to core count on the machine. For example, a limit of 1.0 on an 8-core machine translates into a load average of 8, meaning the run queue length is the same as the core count and the machine is considered fully loaded.

```
CPU Load OK Nodes: 4
```

The detail section displays this information:

| Detail | Description |
| --- | --- |
| Status | Status of the service |
| Status Information | See following example for details |
| Last Check Time | Date and time the CPU load status was checked |
| Next Scheduled Check | Date and time of the next CPU load status check |
| Last State Change | Date and time when the status last changed |
| In Schedule Downtime? | Displays whether the warehouse is currently in scheduled downtime |
| Last Update | Date and time when the service was last updated |

The following detail is an Actian Warehouse instance with 1 leader and 3 workers each, configured with 32 cores. Warning alarm thresholds are 2.0, 1.25 and 1.25 for the 1-, 5-, and 15-minute load averages, respectively. Critical alarm threshold is 4.0 for 1, 5, and 15 load averages. A warning alarm would be triggered if the 1-minute load average exceeds 64 (32 cores * 2.0) or the 5- and 15-minute load averages exceed 40 (32 cores * 1.5).

```
cpu_load > 2.0,1.25,1.25 -> Warning, > 4.0,4.0,4.0 -> Critical Load Average
```

```
Role  Cores  1 min.   5 min.  15 min.   Node
```

```
   L    32    5.89     3.70     2.04    warehouses-av-8q99p2tn04of-vectorh-leader-0.warehouses-av-8q99p2tn04of-vectorh-leader.warehouses.svc.cluster.local
```

```
   W    32    4.47     2.55     1.36    warehouses-av-8q99p2tn04of-vectorh-worker-1.warehouses-av-8q99p2tn04of-vectorh-worker.warehouses.svc.cluster.local
```

```
   W    32    5.52     3.62     1.81    warehouses-av-8q99p2tn04of-vectorh-worker-0.warehouses-av-8q99p2tn04of-vectorh-worker.warehouses.svc.cluster.local
```

```
   W    32    4.53     3.00     1.50    warehouses-av-8q99p2tn04of-vectorh-worker-2.warehouses-av-8q99p2tn04of-vectorh-worker.warehouses.svc.cluster.local
```

Graph metrics:

| leader_load5 | leader node 5 minute load average |
| --- | --- |
| worker_load5_min | min 5 minute load average for a slave node |
| worker_load5_avg | average 5 minute load average for all slave nodes |
| worker_load5_max | max 5 minute load average for a slave node |
