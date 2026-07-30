---
title: "Core Services"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Core_Services.htm"
canonical_id: "actian-data-platform-core-services"
---

## Core Services

The platform provides following custom-built services designed to support data science, machine learning, and large-scale data processing:

    - Spark: This service uses a decoupled architecture where a thin client creates logical plans that are shipped to the cluster for processing. It is built on gRPC and runs over HTTP/2, removing the requirement for Java or Spark binaries on the client side.

    - MLflow: Serving as the standard tool for managing the machine learning model lifecycle, MLflow handles model tracking, management, and serving. It is configured with a PostgreSQL backend for hyperparameters and a cloud bucket for storing model artifacts.

    - Code Server: Based on the open-source version of Visual Studio Code, this service provides a fully customizable IDE in the browser. It comes preinstalled with essential tools, including Git, PySpark, NumPy, and Pandas, and includes extensions for Python and Jupyter Notebooks.
