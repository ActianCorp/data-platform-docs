---
title: "Overview"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Overview.htm"
canonical_id: "actian-data-platform-overview"
---

## Overview

Actian Database as a Service is part of the Actian Data Platform, a platform that provides solutions for all data management needs, data integration, high speed analytics warehouses, and transactional databases. Actian Database as a Service helps to retain control and customize your databases while leveraging cloud infrastructure.

## Advantages of Actian Database as a Service on the Actian Data Platform

The Actian Data Platform includes the direct involvement of Actian’s Ingres Database subject matter experts and support team.

Infrastructure Management: Actian takes care of the underlying infrastructure such as servers, storage, and networking. This includes tasks related to provisioning, scaling, and hardware maintenance.

Database Software Management: Actian handles tasks such as software patches, upgrades, backups, and certain security features.

Operational Management: You share the responsibility for daily operational tasks with Actian. These can include query optimization, table and index management, and application-specific tuning.

Customization: The co-managed model gives you flexibility to work with Actian to customize database configurations, integrate with third-party tools, and implement security.

Support: Actian’s Ingres subject matter experts actively engage with you to maintain optimal database performance, availability, reliability, and health.

You also benefit from cloud economics, by only paying for what you use and having the ability for the service to shut down or sleep after a pre-defined period of inactivity. You can schedule starting, stopping, and scaling the environment to optimize uptime and cost. You have the ability to quickly create new databases, and this environment is ideal to use in a sandbox for development and testing.

## Performance and Concurrency

Actian Vector is the underlying database engine that powers the Actian Data Platform, enabling it to operate on hundreds of tuples of data. Massively Parallel Processing (MPP) architecture provides the coordinated processing of a single task by multiple processors communicating with each other using a messaging interface. This means that you can scale out to hundreds of nodes and petabytes of data. But the Actian Data Platform uses advanced columnar storage, which implements compression by data type, leading to 4–6x improved compression and a reduced data footprint.

To keep your data costs down, compute and storage are separate, so you pay only for what you use. For more information, see [Database Cost and Actian Units](../DBaaS_User/Concepts_to_Understand.md).

Actian Data Platform performs analytical queries as the data warehouse is being updated without any performance degradation. The service is built for high volume of concurrent users, allowing up to 64 concurrent users.

## Videos

## Actian Data Platform Security Overview

Actian Data Platform is a fully managed cloud data service that ensures the highest levels of security. Actian Data Platform provides:

- Private network isolation
- Data encryption

- Robust access control capabilities
- 24x7 maintenance and monitoring

As part of the Cloud Security Alliance, Actian continuously adopts best practices to ensure secure cloud computing.

For more information about these security features, see the [Introduction to Actian Data Platform Security](../Security/Introduction_to_Actian_Data_Platform_Security.md).

## Supported Public Cloud Platforms

The following public cloud platforms are currently supported:

- Amazon Web Services
- Microsoft Azure

- Google Cloud
