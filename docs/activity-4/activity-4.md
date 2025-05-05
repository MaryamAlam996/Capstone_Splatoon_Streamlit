# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)

## Activity 4: Plan the Test Strategy

---

## Test Cases

To determine the test cases needed for the ETL pipeline, we need to consider the following:

1. The User Story
2. The Acceptance Criteria
3. The Definition of Done
4. The Data Sources (mock or otherwise)
5. The Expected Outcomes

### User Story 1

```txt
As a Data Analyst,  
I want access to a single, clean, and accurate dataset combining customer demographics and transaction data,  
So that I can analyse customer behaviour without worrying about data inconsistencies and can rely on it for analysis without manual checks.
```

### Acceptance Criteria the Require Test Cases

- **Data Extraction**
  - [ ] Given the database contains 10,500 rows with 4 fields, when the data is extracted, then it should complete in less than 1 minute.
  - [ ] Given the CSV file contains 5,200 rows with 5 columns, when the data is extracted, then it should complete in less than 30 seconds.
- **Data Cleaning**
  - [ ] Given the extracted data, when duplicates are removed, then 100% of duplicates should be removed.
  - [ ] Given the extracted data, when missing values are handled, then 100% of missing should be resolved.
  - [ ] Given the extracted data, when invalid values are handled, then 100% of invalid fields should be resolved.
  - [ ] Given the extracted data, when data cleaning is performed, then it should complete in less than 1 second per 1,000 rows.
- **Data Transformation**
  - [ ] Given the cleaned data, when the customer demographics dataset (CSV) and transaction dataset (database) are merged, then the merge should be performed correctly using the `customer_id` field as the key.
  - [ ] Given the cleaned data, when calculating the total amount spent by each customer, then the `total_spent` field should be accurate and
- **Data Transformation**
  - [ ] Given the cleaned data, when the customer demographics dataset (CSV) and transaction dataset (database) are merged, then the merge should be performed correctly using the `customer_id` field as the key.
  - [ ] Given the cleaned data, when calculating the total amount spent by each customer, then the `total_spent` field should be accurate and reflect the sum of all amount values for each `customer_id`.
  - [ ] Given the cleaned data, when filtering for active customers, then only customers with `is_active` set to `True` should be included.
- **Data Quality**
  - [ ] Given the transformed dataset, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the transformed dataset, when data validation is performed, then it should complete in less than 1 second per 1,000 rows.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

### Strategy

1. Take the acceptance criteria and identify the types of test needed
2. Create a test cases for each type of test needed
3. Refer to the acceptance criteria and definition of done to ensure the tests prove "done-ness"

---

#### Data Extraction Acceptance Criteria 1

```txt
Given the database contains 10,500 rows with 4 fields,  
when the data is extracted,  
then it should complete in less than 1 minute.
```

Here we need to test that the following things happen:

- ***Performance Test***:
  - [ ] - Verify that the data extraction completes in less than 1 minute (regardless of the number of rows).
- ***Functional Tests***:
  - [ ] - Verify that the data extraction retrieves exactly 4 fields per row.
- ***Data Integrity Tests***:
  - [ ] - Verify data consistency between the extracted data and the source database.
  - [ ] - Verify data accuracy for a sample of rows.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles a database connection error gracefully
  - [ ] - Verify that the code handles a database query error gracefully
  - [ ] - Verify that the code handles a database timeout error gracefully
- ***Code Quality Tests***:
  - [ ] - SQL queries pass linting and formatting checks.
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the database extraction script is at least 90%.

> ***Why are we not testing the number of rows extracted?***  
> Because the number of rows extracted is not a fixed value.  
> It is dependent on the data in the source database.  
> We can test that the number of rows extracted is within a certain range, but we cannot test that it is an exact number.

---
---

## Over to You

Take the second acceptance criteria and create a set of test cases for it.

---

### Data Extraction Acceptance Criteria 2

```txt
Given the CSV file contains 5,200 rows with 5 columns,  
when the data is extracted,  
then it should complete in less than 30 seconds.
```

Here we need to test that the following things happen:

- ***Test Type 1***:
  - Test Case 1
...

Add as needed!

---
