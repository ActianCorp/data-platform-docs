---
title: "Sparkforce Platform"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Sparkforce_Platform.htm"
canonical_id: "actian-data-platform-sparkforce-platform"
---

# Sparkforce Platform

## Introduction

Sparkforce is a specialized feature of the Actian Analytics AI Platform designed for users who need to bridge the gap between large-scale data lake access, machine learning, and high-speed analytics. By integrating open-source standards, including Apache Spark, MLflow, and VS Code with the Actian Analytics Engine, Sparkforce provides a unified, cloud-native environment for developing data-intensive applications and managing entire machine learning lifecycles.

The platform’s architecture rests on four foundational pillars:

    - Simplicity: A high-level data frame API and a lightweight, 1.5 MB client library remove the operational hurdles typically associated with distributed processing. This streamlined solution makes Sparkforce an ideal choice for embedding data logic into mobile applications and microservices.

    - Efficiency: By using Spark Connect, the platform enables lazy execution, which allows client applications to dispatch transformation logic without requiring intermediate data transfers.

    - Flexibility: Sparkforce includes preconfigured drivers for AWS, Azure, and Google Cloud Storage (GCS), alongside support for modern table formats such as Iceberg and Delta. These tools allow you to combine various data lake sources with the Actian Analytics Engine in a single federated query.

    - Extensibility: The platform features a modular set of services, including Spark Connect, MLflow, and Code Server. You can enable these independently for each warehouse to match your specific workload requirements.
