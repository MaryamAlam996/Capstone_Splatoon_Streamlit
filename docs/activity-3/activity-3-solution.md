# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)

## ETL Pipeline Project Walkthrough

## Activity 3: ETL Pipeline High-Level Plan and Subprocesses

### Activity 3.1 - High-Level Flowchart

Identify the missing steps in the high-level flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing steps.

```mermaid
flowchart TD
    A@{ shape: stadium, label: "Start: Data Sources"} --> B@{ shape: tri, label: "Extract Data"}
    B --> C1@{ shape: cyl, label: "Source 1: SQL Database"}
    B --> C2@{shape: doc, label: "Source 2: CSV/JSON Files"}
    C1 --> D[Data Cleaning*]
    C2 --> D[Data Cleaning*]
    D --> E[Data Transformation**]
    E --> F[Load Transformed Data***]
    F --> G([Deploy Pipeline****])
    

```

---

### Activity 3.2 - Data Cleaning Subprocesses

Identify the missing subprocesses in the data cleaning flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing subprocesses.

```mermaid
flowchart LR
    A[Data Cleaning*] --> B1@{shape: subproc, label: "Remove Duplicates"}
    B1 --> B2@{shape: subproc, label: "Handle Missing Values"}
    B2 --> B3@{shape: subproc, label: "Standardize Formats"}
    B3 --> B4@{shape: subproc, label: "Filter Invalid Data"}
    B4 --> B5@{ shape: lean-r, label: "Cleaned Data" }
```

---

## Activity 3.3 - Data Transformation Subprocesses

Identify the missing subprocesses in the data transformation flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing subprocesses.

```mermaid
flowchart LR
    A[Data Transformation**] --> B1@{shape: subproc, label: "Merge Data"}
    B1 --> B2@{shape: subproc, label: "Calculate Spending Metrics"}
    B2 --> B3@{shape: subproc, label: "Identify High-Value Customers"}
    B3 --> B4@{shape: subproc, label: "Analyze Demographic Trends"}
    B4 --> B5@{ shape: lean-r, label: "Transformed Data" }
```

---

## Activity 3.4 - Loading Subprocesses

Identify the missing subprocesses in the loading flowchart.  Preview the document to see flowchart, edit the `label` key to add the missing subprocesses.

```mermaid
flowchart LR
    A[Load Transformed Data***] --> B1@{shape: subproc, label: "Prepare Target Table"}
    B1 --> B2@{shape: subproc, label: "Insert Data into Staging Table"}
    B2 --> B3@{shape: subproc, label: "Validate Staged Data"}
    B3 --> B4@{shape: subproc, label: "Upsert into Enriched Table"}
    B4 --> B5@{shape: subproc, label: "Clean Up Staging Table"}
    B5 --> B6@{shape: subproc, label: "Validate Loaded Data"}
    B6 --> B7@{shape: lean-r, label: "Final Dataset in SQL Table"}
```

---
