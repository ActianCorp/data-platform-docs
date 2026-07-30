---
title: "Network Disconnects Due to Perceived Inactivity"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Network_Disconnects_Due_to_Perceived_Inactivity.htm"
canonical_id: "actian-data-platform-network-disconnects-due-to-perceived-inactivity"
---

## Network Disconnects Due to Perceived Inactivity

When running a SQL statement that takes a long time to finish (when doing a data load through copy/external table or running a query that is taking a long time to return results), you receive an “idle connection” message or notice that your connection seems to have hung.

You must keep your TCP connection alive by increasing the TCP keepalive length.

Actian clients such as the Actian SQL CLI or applications that use the ODBC/JDBC driver establish a connection to the Actian Data Platform using standard TCP/IP. When you run some SQL commands that could take a long time, especially commands related to data loading such as CREATE TABLE <Actian Data Platform table>AS SELECT * FROM <external table>, your client may time out for various reasons. A common reason could be that your NAT proxy or firewall may be configured to drop TCP connections that are perceived as idle.

TCP provides a mechanism to address this called “TCP keepalive.” It involves sending benign keepalive probes at predefined intervals to signal that the connection is alive and waiting for a response from the server. This is usually enabled by default on most system, but the interval is typically about two hours, which is usually very high for most NAT proxies/firewalls.

For , we recommend that you lower this value to 60 seconds. This is done differently for various operating systems as follows.

Windows

Set or update the following Windows registry key:

```
\HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\TCPIP\Parameters\KeepAliveTime
```

This is a REG_DWORD that expects time in milliseconds.

Set it to 60000 (Decimal) or ea60 (Hexadecimal).

You must reboot your machine for the change to take effect.

Linux

In /etc/sysctl.conf as root, set the following:

```
net.ipv4.tcp_keepalive_intvl = 10
```

```
net.ipv4.tcp_keepalive_probes = 3
```

```
net.ipv4.tcp_keepalive_time = 60
```

No reboot is necessary. Run the following command to enact the changes:

```
sysctl -p
```

macOS

!!! note "Note"

    Changing the keepalive setting does not work on macOS Catalina (10.15) for a version that is less than 10.15.4.

As root, run the following to change values immediately:

```
sysctl -w net.inet.tcp.keepidle=60000 net.inet.tcp.keepcnt=3 net.inet.tcp.keepintvl=10000
```

To make the values persistent across reboots, edit /etc/sysctl.conf and add:

```
net.inet.tcp.keepidle=60000
```

```
net.inet.tcp.keepcnt=3
```

```
net.inet.tcp.keepintvl=10000
```

No reboot is necessary.
