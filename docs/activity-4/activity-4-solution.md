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

---

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
  - [ ] Given the extracted data, when missing, then 100% of missing should be resolved.
  - [ ] Given the extracted data, when invalid values are handled, then 100% of invalid fields should be resolved.
  - [ ] Given the extracted data, when data cleaning is performed, then it should complete in less than 1 second per 1,000 rows.
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

### User Story 1 - Data Extraction Acceptance Criteria 1

```txt
Given the database contains 10,500 rows with 4 fields,  
when the data is extracted,  
then it should complete in less than 1 minute.
```

Here we need to UNIT test that the following things happen:

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
  - SQL queries pass linting and formatting checks.
  - Python scripts pass linting and formatting checks.
  - Test coverage on the database extraction script is at least 90%.

> ***Why are we not testing the number of rows extracted?***  
> Because the number of rows extracted is not a fixed value.  
> It is dependent on the data in the source database.  
> We can test that the number of rows extracted is within a certain range, but we cannot test that it is an exact number.

---

## Over to You

Take the second acceptance criteria and create a set of test cases for it.

---

### User Story 1 - Data Extraction Acceptance Criteria 2

```txt
Given the CSV file contains 5,200 rows with 5 columns,  
when the data is extracted,  
then it should complete in less than 30 seconds.
```

Here we need to UNIT test that the following things happen:

- ***Performance Test***:
  - [ ] - Verify that the data extraction completes in less than 30 seconds (regardless of the number of rows).
- ***Functional Tests***:
  - [ ] - Verify that the data extraction retrieves exactly 5 columns per row.
- ***Data Integrity Tests***:
  - [ ] - Verify data consistency between the extracted data and the source CSV file.
  - [ ] - Verify data accuracy for a sample of rows.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles a file read error gracefully
  - [ ] - Verify that the code handles a file format error gracefully
  - [ ] - Verify that the code handles a file read timeout error gracefully
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the CSV extraction script is at least 90%.

---

### User Story 1 - Data Cleaning Acceptance Criteria 1

```txt
Given the extracted data,  
when duplicates are removed,  
then 100% of duplicates should be removed.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***:
  - [ ] - Verify that the data cleaning removes all duplicates.
  - [ ] - Verify that the data cleaning does not remove any non-duplicates.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles a data cleaning error gracefully
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data cleaning script is at least 90%.

---

### User Story 1 - Data Cleaning Acceptance Criteria 2

```txt
Given the extracted data,  
When missing values are handled,  
then 100% of missing should be resolved.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***:
  - [ ] - Verify that all missing values in the extracted data are handled according to the specified rules.
  - [ ] - Verify that missing values in specific columns are handled correctly.
  - [ ] - Verify that multiple missing values in the same row or column are handled correctly.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles errors in handling missing values gracefully.
- ***Data Integrity Tests***:
  - [ ] - Verify that the data remains consistent after handling missing values.
  - [ ] - Verify that the data remains accurate after handling missing values.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data cleaning script is at least 90%.

---

### User Story 1 - Data Cleaning Acceptance Criteria 3

```txt
Given the extracted data,
When invalid values are handled,
then 100% of invalid fields should be resolved.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***:
  - [ ] - Verify that all invalid values in the extracted data are handled according to the specified rules.
  - [ ] - Verify that invalid values in specific columns are handled correctly.
  - [ ] - Verify that multiple invalid values in the same row or column are handled correctly.
- ***Reliability Tests***:
  - [ ] - Verify that the data remains consistent after handling invalid values.
  - [ ] - Verify that the data remains accurate after handling invalid values.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data cleaning script is at least 90%.

---

### User Story 1 - Data Cleaning Acceptance Criteria 4

```txt
Given the extracted data,
When data cleaning is performed,
then it should complete in less than 1 second per 1,000 rows.
```

Here we need to INTEGRATION tests that the following things happen:

- ***Functional Tests***:
  - [ ] - Verify that a combination of missing and invalid values in the same row or column are handled correctly.
- ***Performance Test***:
  - [ ] - Verify that the data cleaning completes in less than 1 second per 1,000 rows.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles errors in data cleaning gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data cleaning script is at least 90%.

---

### User Story 1 - Data Transformation Acceptance Criteria 1

```txt
Given the cleaned data,
When the customer demographics dataset (CSV) and transaction dataset (database) are merged,
then the merge should be performed correctly using the customer_id field as the key.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify successful merge using `customer_id` as the key.
  - [ ] - Verify correct number of rows after merge.
  - [ ] - Verify presence of all expected columns in the merged dataset.
  - [ ] - Verify merge with different join types using `customer_id` as the key.
- ***Reliability Tests***:
  - [ ] - Verify handling of missing `customer_id` values.
  - [ ] - Verify handling of duplicate `customer_id` values.
- ***Data Integrity Tests***:
  - [ ] - Verify data integrity after merge.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 1 - Data Transformation Acceptance Criteria 2

```txt
Given the cleaned data,
When calculating the total amount spent by each customer,
then the total_spent field should be accurate and reflect the sum of all amount values for each customer_id.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the total_spent field accurately reflects the sum of all amount values for each customer_id.
  - [ ] - Verify that the calculation of total_spent correctly handles missing amount values.
  - [ ] - Verify that the calculation of total_spent correctly includes zero amount values in the sum.
  - [ ] - Verify that the calculation of total_spent correctly includes negative amount values in the sum.
  - [ ] - Verify that the total_spent field accurately reflects the sum of amount values for customers with multiple transactions.
- ***Reliability Tests***:
  - [ ] - Verify that the calculation of total_spent performs correctly and efficiently with a large number of transactions.
  - [ ] - Verify that the calculation of total_spent handles data type mismatches gracefully.
- ***Data Integrity Tests***:
  - [ ] - Verify that the data remains consistent and accurate after calculating the total_spent field.
  - [ ] - Verify that the total_spent field is accurate for a sample of customers by manually calculating the sum of amount values and comparing it to the computed total_spent.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 1 - Data Transformation Acceptance Criteria 3

```txt
Given the cleaned data,
When filtering for active customers,
then only customers with is_active set to True should be included.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that only customers with is_active set to True are included in the filtered dataset.
  - [ ] - Verify that customers with is_active set to False are excluded from the filtered dataset.
  - [ ] - Verify that customers with missing is_active values are excluded from the filtered dataset.
  - [ ] - Verify that customers with invalid is_active values are excluded from the filtered dataset.
  - [ ] - Verify that the filtered dataset contains all expected columns.
- ***Reliability Tests***:
  - [ ] - Verify that the filtering for active customers returns suitable data if no customers have is_active set to True.
- ***Data Integrity Tests***:
  - [ ] - Verify that the data remains consistent and accurate after filtering for active customers.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 1 - Data Quality Acceptance Criteria 1

```txt
Given the transformed dataset,
When data validation is performed,
then 99% of records should be accurate.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags inaccurate records.
    - [ ] - Verify that there are no missing customer_id values in the merged data.
  - [ ] - Verify that data validation correctly calculates the accuracy percentage of the records.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 1 - Data Quality Acceptance Criteria 2

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of expected columns and rows should be present.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags missing columns and rows.
  - [ ] - Verify that data validation correctly calculates the percentage of expected columns and rows present.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 1 - Data Quality Acceptance Criteria 3

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of records should have consistent formats and values.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags inconsistent formats and values.
  - [ ] - Verify that data validation correctly calculates the percentage of records with consistent formats and values.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 1 - Data Quality Acceptance Criteria 4

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of records should maintain integrity constraints.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags records that violate integrity constraints.
  - [ ] - Verify that data validation correctly calculates the percentage of records that maintain integrity constraints.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 1 - Data Quality Acceptance Criteria 5

```txt
Given the transformed dataset,
When data validation is performed,
then it should complete in less than 1 second per 1,000 rows.
```

Here we need to INTEGRATION test that the following things happen:

- ***Performance Test***:
  - [ ] - Verify that data validation completes in less than 1 second per 1,000 rows.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 1 - Documentation Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Code should be documented with clear and concise comments.

---

### User Story 1 - Documentation Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - User-facing documentation should be updated to reflect new or changed functionality.

---

### User Story 1 - Testing Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Unit tests should cover all new functionality.

---

### User Story 1 - Testing Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - Integration tests should cover interactions between components.

---

### User Story 1 - Testing Acceptance Criteria 3

Here we need to manually check that, during a code review, that:

- [ ] - All tests should pass successfully.

---

### User Story 1 - Testing Acceptance Criteria 4

Here we need to manually check that, during a code review, that:

- [ ] - Test coverage should meet the project's required threshold of 90%.

---

### User Story 2 - Customer Insights

```txt
As a Data Analyst,  
I want to know how much each customer has spent and their average transaction value,  
So that I can identify high-value customers for further analysis
```

***Acceptance Criteria***

- **Data Transformation**
  - [ ] - Given the cleaned data, when calculating the total amount spent by each customer, then the `total_spent` field should be accurate and reflect the sum of all amount values for each `customer_id`.
  - [ ] - Given the cleaned data, when calculating the average transaction value for each customer, then the `avg_transaction_value` field should be accurate and reflect the average of all amount values for each `customer_id`.
  - [ ] - Given the cleaned data, when filtering for high-value customers, then only customers with a `total_spent` greater than **$500** should be included.
- **Data Quality**
  - [ ] - Given the transformed dataset, when data validation is performed, then 99% of records should be accurate.
  - [ ] - Given the transformed dataset, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] Given the transformed dataset, when data validation is performed, then the error rate should be less than 1%.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

---

### User Story 2 - Data Transformation Acceptance Criteria 1

```txt
Given the cleaned data,
When calculating the total amount spent by each customer,
then the total_spent field should be accurate and reflect the sum of all amount values for each customer_id.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the total_spent field accurately reflects the sum of all amount values for each customer_id.
  - [ ] - Verify that the calculation of total_spent correctly handles missing amount values.
  - [ ] - Verify that the calculation of total_spent correctly includes zero amount values in the sum.
  - [ ] - Verify that the calculation of total_spent correctly includes negative amount values in the sum.
  - [ ] - Verify that the total_spent field accurately reflects the sum of amount values for customers with multiple transactions.
- ***Reliability Tests***:
  - [ ] - Verify that the calculation of total_spent performs correctly and efficiently with a large number of transactions.
  - [ ] - Verify that the calculation of total_spent handles data type mismatches gracefully.
- ***Data Integrity Tests***:
  - [ ] - Verify that the data remains consistent and accurate after calculating the total_spent field.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Data Transformation Acceptance Criteria 2

```txt
Given the cleaned data,
When calculating the average transaction value for each customer,
then the avg_transaction_value field should be accurate and reflect the average of all amount values for each customer_id.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the avg_transaction_value field accurately reflects the average of all amount values for each customer_id.
  - [ ] - Verify that the calculation of avg_transaction_value correctly handles missing amount values.
  - [ ] - Verify that the calculation of avg_transaction_value correctly includes zero amount values in the average.
  - [ ] - Verify that the calculation of avg_transaction_value correctly includes negative amount values in the average.
  - [ ] - Verify that the avg_transaction_value field accurately reflects the average of amount values for customers with multiple transactions.
- ***Reliability Tests***:
  - [ ] - Verify that the calculation of avg_transaction_value performs correctly and efficiently with a large number of transactions.
  - [ ] - Verify that the calculation of avg_transaction_value handles data type mismatches gracefully.
- ***Data Integrity Tests***:
  - [ ] - Verify that the data remains consistent and accurate after calculating the avg_transaction_value field.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Data Transformation Acceptance Criteria 3

```txt
Given the cleaned data,
When filtering for high-value customers,
then only customers with a total_spent greater than $500 should be included.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that only customers with a total_spent greater than $500 are included in the filtered dataset.
  - [ ] - Verify that customers with a total_spent less than or equal to $500 are excluded from the filtered dataset.
  - [ ] - Verify that customers with missing total_spent values are excluded from the filtered dataset.
  - [ ] - Verify that customers with invalid total_spent values are excluded from the filtered dataset.
  - [ ] - Verify that the filtered dataset contains all expected columns.
- ***Reliability Tests***:
  - [ ] - Verify that the filtering for high-value customers returns suitable data if no customers have a total_spent greater than $500.
- ***Data Integrity Tests***:
  - [ ] - Verify that the data remains consistent and accurate after filtering for high-value customers.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Data Quality Acceptance Criteria 1

```txt
Given the transformed dataset,
When data validation is performed,
then 99% of records should be accurate.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags inaccurate records.
    - [ ] - Verify that there are no missing customer_id values in the merged data (checks for orphaned records).
- ***Reliability Tests***:
  - [ ] - Verify that the code handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Data Quality Acceptance Criteria 2

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of expected columns and rows should be present.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags missing columns and rows.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Data Quality Acceptance Criteria 3

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of records should have consistent formats and values.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags inconsistent formats and values.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Data Quality Acceptance Criteria 4

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of records should maintain integrity constraints.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that data validation correctly identifies and flags records that violate integrity constraints.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Data Quality Acceptance Criteria 5

```txt
Given the transformed dataset,
When data validation is performed,
then the error rate should be less than 1%.
```

Here we need to UNIT test that the following things happen:

- ***Data Integrity Tests***
  - [ ] - Verify that the error rate is less than 1%.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 2 - Documentation Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Code should be documented with clear and concise comments.

---

### User Story 2 - Documentation Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - User-facing documentation should be updated to reflect new or changed functionality.

---

### User Story 2 - Testing Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Unit tests should cover all new functionality.

---

### User Story 2 - Testing Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - Integration tests should cover interactions between components.

---

### User Story 2 - Testing Acceptance Criteria 3

Here we need to manually check that, during a code review, that:

- [ ] - All tests should pass successfully.

---

### User Story 2 - Testing Acceptance Criteria 4

Here we need to manually check that, during a code review, that:

- [ ] - Test coverage should meet the project's required threshold of 90%.

---

### User Story 3 - Customer Insights

```txt
As a Business Stakeholder,  
I want to identify high-value customers who have spent more than $500,  
So that we can target them for loyalty rewards
```

***Acceptance Criteria***

- **Data Transformation**
  - [ ] Given the cleaned data, when calculating the total amount spent by each customer, then the ``total_spent`` field should be accurate and reflect the sum of all `amount` values for each `customer_id`.
  - [ ] Given the cleaned data, when filtering for high-value customers, then only customers with a ``total_spent`` greater than **$500** should be included.
- **Data Quality**
  - [ ] Given the transformed dataset, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the transformed dataset, when data validation is performed, then 100% of records should maintain integrity constraints.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

---

### User Story 3 - Data Transformation Acceptance Criteria 1

```txt
Given the cleaned data,
When calculating the total amount spent by each customer,
then the total_spent field should be accurate and reflect the sum of all amount values for each customer_id.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the total_spent field accurately reflects the sum of all amount values for each customer_id.
  - [ ] - Verify that the calculation of total_spent correctly includes zero amount values in the sum.
  - [ ] - Verify that the calculation of total_spent correctly includes negative amount values in the sum.
  - [ ] - Verify that the total_spent field accurately reflects the sum of amount values for customers with multiple transactions.
- ***Reliability Tests***
  - [ ] - Verify that the calculation of total_spent handles data type mismatches gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after calculating the total_spent field.
  - [ ] - Verify that the total_spent field is accurate for a sample of customers by manually calculating the sum of amount values and comparing it to the computed total_spent.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 3 - Data Transformation Acceptance Criteria 2

```txt
Given the cleaned data,
When filtering for high-value customers,
then only customers with a total_spent greater than $500 should be included.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that only customers with a total_spent greater than $500 are included in the filtered dataset.
  - [ ] - Verify that customers with a total_spent of $500 or less are excluded from the filtered dataset.
  - [ ] - Verify that the total_spent field is correctly calculated for each customer before filtering.
  - [ ] - Verify that customers with a total_spent exactly equal to $500 are excluded from the filtered dataset.
  - [ ] - Verify that customers with missing or null total_spent values are excluded from the filtered dataset.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after filtering for high-value customers.
  - [ ] - Verify that the filtered dataset accurately reflects the customers with a total_spent greater than $500.
    - [ ] - Verify that there are no missing customer_id values in the merged data (checks for orphaned records).
- ***Reliability Tests***:
  - [ ] - Verify that the code handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 3 - Data Quality Acceptance Criteria 1

```txt
Given the transformed dataset,
When data validation is performed,
then 99% of records should be accurate.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags inaccurate records.
  - [ ] - Verify that data validation correctly calculates the accuracy percentage of the records.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
  - [ ] - Verify that the accuracy percentage calculation is correct for a sample of records.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 3 - Data Quality Acceptance Criteria 2

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of expected columns and rows should be present.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags missing columns and rows.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 3 - Data Quality Acceptance Criteria 3

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of records should have consistent formats and values.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags inconsistent formats and values.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 3 - Data Quality Acceptance Criteria 4

```txt
Given the transformed dataset,
When data validation is performed,
then 100% of records should maintain integrity constraints.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags records that violate integrity constraints.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 3 - Documentation Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Code should be documented with clear and concise comments.

---

### User Story 3 - Documentation Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - User-facing documentation should be updated to reflect new or changed functionality.

---

### User Story 3 - Testing Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Unit tests should cover all new functionality.

---

### User Story 3 - Testing Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - Integration tests should cover interactions between components.

---

### User Story 3 - Testing Acceptance Criteria 3

Here we need to manually check that, during a code review, that:

- [ ] - All tests should pass successfully.

---

### User Story 3 - Testing Acceptance Criteria 4

Here we need to manually check that, during a code review, that:

- [ ] - Test coverage should meet the project's required threshold of 90%.

---

### User Story 4 - Demographic Trends

```txt
As a Business Stakeholder,  
I want to analyse demographic trends, such as customer age and country, among high-value customers,  
So that I can tailor our marketing campaigns to reach them effectively
```

***Acceptance Criteria***

- **Data Transformation**
  - [ ] Given the cleaned data, when identifying high-value customers, then only customers with a `total_spent` greater than **$500** should be included.
  - [ ] Given the high-value customers, when analysing demographic trends, then the analysis should include `age` and `country` fields.
- **Data Analysis**
  - [ ] Given the high-value customers, when calculating demographic trends, then the average `age` and distribution by `country` should be accurately calculated.
  - [ ] Given the high-value customers, when generating demographic reports, then the reports should include visualizations (e.g., charts, graphs) of age and `country` distributions.
- **Data Quality**
  - [ ] Given the demographic analysis, when data validation is performed, then 99% of records should be accurate.
  - [ ] Given the demographic analysis, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] Given the demographic analysis, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] Given the demographic analysis, when data validation is performed, then 100% of records should maintain integrity constraints.
- **Documentation**
  - [ ] Code should be documented with clear and concise comments.
  - [ ] User-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] Unit tests should cover all new functionality.
  - [ ] Integration tests should cover interactions between components.
  - [ ] All tests should pass successfully.
  - [ ] Test coverage should meet the project's required threshold of 90%.

---

### User Story 4 - Data Transformation Acceptance Criteria 1

```txt
Given the cleaned data,
When identifying high-value customers,
then only customers with a total_spent greater than $500 should be included.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that only customers with a total_spent greater than $500 are included in the filtered dataset.
  - [ ] - Verify that customers with a total_spent of $500 or less are excluded from the filtered dataset.
  - [ ] - Verify that the total_spent field is correctly calculated for each customer before filtering.
  - [ ] - Verify that customers with a total_spent exactly equal to $500 are excluded from the filtered dataset.
  - [ ] - Verify that customers with missing or null total_spent values are excluded from the filtered dataset.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after filtering for high-value customers.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 4 - Data Transformation Acceptance Criteria 2

```txt
Given the high-value customers,
When analysing demographic trends,
then the analysis should include age and country fields.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the analysis includes the age and country fields.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after analysing demographic trends.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data transformation script is at least 90%.

---

### User Story 4 - Data Analysis Acceptance Criteria 1

```txt
Given the high-value customers,
When calculating demographic trends,
then the average age and distribution by country should be accurately calculated.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the average age is accurately calculated.
  - [ ] - Verify that the distribution by country is accurately calculated.
- ***Reliability Tests***:
  - [ ] - Verify that the code handles errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after calculating demographic trends.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data analysis script is at least 90%.

---

### User Story 4 - Data Analysis Acceptance Criteria 2

```txt
Given the high-value customers,
When generating demographic reports,
then the reports should include visualizations (e.g., charts, graphs) of age and country distributions.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the function to generate the age distribution report is called.
  - [ ] - Verify that the function to generate the country distribution report is called.
  - [ ] - Verify that the age distribution report includes a histogram of the age data.
  - [ ] - Verify that the country distribution report includes a bar chart of the country data.
- ***Reliability Tests***
  - [ ] - Verify that the report generation functions handle empty datasets gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data analysis script is at least 90%.

---

### User Story 4 - Data Quality Acceptance Criteria 1

```txt
Given the demographic analysis,
When data validation is performed,
then 99% of records should be accurate.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags inaccurate records.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 4 - Data Quality Acceptance Criteria 2

```txt
Given the demographic analysis,
When data validation is performed,
then 100% of expected columns and rows should be present.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags missing columns and rows.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 4 - Data Quality Acceptance Criteria 3

```txt
Given the demographic analysis,
When data validation is performed,
then 100% of records should have consistent formats and values.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags inconsistent formats and values.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 4 - Data Quality Acceptance Criteria 4

```txt
Given the demographic analysis,
When data validation is performed,
then 100% of records should maintain integrity constraints.
```

Here we need to UNIT test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that data validation correctly identifies and flags records that violate integrity constraints.
- ***Reliability Tests***
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after performing data validation.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 4 - Documentation Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Code should be documented with clear and concise comments.

---

### User Story 4 - Documentation Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - User-facing documentation should be updated to reflect new or changed functionality.

---

### User Story 4 - Testing Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Unit tests should cover all new functionality.

---

### User Story 4 - Testing Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - Integration tests should cover interactions between components.

---

### User Story 4 - Testing Acceptance Criteria 3

Here we need to manually check that, during a code review, that:

- [ ] - All tests should pass successfully.

---

### User Story 4 - Testing Acceptance Criteria 4

Here we need to manually check that, during a code review, that:

- [ ] - Test coverage should meet the project's required threshold of 90%.

---

### User Story 5 - Data Storage and Access

```txt
As a Data Scientist,  
I want the cleaned and enriched data to be stored in a SQL table,  
So that I can query it directly for advanced analysis
```

***Acceptance Criteria***

- **Data Loading**
  - [ ] - Given the cleaned and enriched data, when the data is loaded into the target SQL table, then it should complete in less than 5 seconds per 10,000 rows.
  - [ ] - Given the cleaned and enriched data, when the data is loaded into the target SQL table, then the row counts should match expectations.
- **Data Quality**
  - [ ] - Given the loaded data, when data validation is performed, then 99% of records should be accurate.
  - [ ] - Given the loaded data, when data validation is performed, then 100% of expected columns and rows should be present.
  - [ ] - Given the loaded data, when data validation is performed, then 100% of records should have consistent formats and values.
  - [ ] - Given the loaded data, when data validation is performed, then 100% of records should maintain integrity constraints.
  - [ ] - Given the loaded data, when data validation is performed, then the error rate should be less than 1%.
- **Performance**
  - [ ] - Given the entire ETL process, when it is executed, then it should complete within 30 minutes for a full dataset.
  - [ ] - Given the entire ETL process, when it is executed, then no significant performance regressions should be introduced.
- **Documentation**
  - [ ] - Given the ETL process, when it is completed, then the code should be documented with clear and concise comments.
  - [ ] - Given the ETL process, when it is completed, then user-facing documentation should be updated to reflect new or changed functionality.
- **Testing**
  - [ ] - Given the ETL process, when it is completed, then unit tests should cover all new functionality.
  - [ ] - Given the ETL process, when it is completed, then integration tests should cover interactions between components.
  - [ ] - Given the ETL process, when it is completed, then all tests should pass successfully.
  - [ ] - Given the ETL process, when it is completed, then test coverage should meet the project's required threshold of 90%.

---

### User Story 5 - Data Loading Acceptance Criteria 1

```txt
Given the cleaned and enriched data,
When the data is loaded into the target SQL table,
then it should complete in less than 5 seconds per 10,000 rows.
```

Here we need to INTEGRATION test that the following things happen:

- ***Performance Test***:
  - V [ ] - Verify that the data loading process completes in less than 5 seconds per 10,000 rows.
  - [ ] - Verify that the data loading process handles large datasets gracefully.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data loading errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data loading script is at least 90%.

---

### User Story 5 - Data Loading Acceptance Criteria 2

```txt
Given the cleaned and enriched data,
When the data is loaded into the target SQL table,
then the row counts should match expectations.
```

Here we need to INTEGRATION test that the following things happen:

- ***Data Integrity Tests***:
  - [ ] - Verify that the row counts in the target SQL table match the expected row counts.
  - [ ] - Verify that the data loading process handles missing or duplicate records gracefully.
  - [ ] - Verify that the data loading process handles data type mismatches gracefully.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data loading errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data loading script is at least 90%.

---

### User Story 5 - Data Quality Acceptance Criteria 1

```txt
Given the loaded data,
When data validation is performed,
then 99% of records should be accurate.
```

Here we need to INTEGRATION test that the following things happen:

- ***Data Integrity Tests***:
  - [ ] - Verify that data validation correctly identifies and flags inaccurate records.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 5 - Data Quality Acceptance Criteria 2

```txt
Given the loaded data,
When data validation is performed,
then 100% of expected columns and rows should be present.
```

Here we need to INTEGRATION test that the following things happen:

- ***Data Integrity Tests***:
  - [ ] - Verify that data validation correctly identifies and flags missing columns and rows.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 5 - Data Quality Acceptance Criteria 3

```txt
Given the loaded data,
When data validation is performed,
then 100% of records should have consistent formats and values.
```

Here we need to INTEGRATION test that the following things happen:

- ***Data Integrity Tests***:
  - [ ] - Verify that data validation correctly identifies and flags inconsistent formats and values.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 5 - Data Quality Acceptance Criteria 4

```txt
Given the loaded data,
When data validation is performed,
then 100% of records should maintain integrity constraints.
```

Here we need to INTEGRATION test that the following things happen:

- ***Data Integrity Tests***:
  - [ ] - Verify that data validation correctly identifies and flags records that violate integrity constraints.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles data validation errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the data quality script is at least 90%.

---

### User Story 5 - Performance Acceptance Criteria 1

```txt
Given the entire ETL process,
When it is executed,
then it should complete within 30 minutes for a full dataset.
```

Here we need to INTEGRATION test that the following things happen:

- ***Performance Test***:
  - [ ] - Verify that the entire ETL process completes within 30 minutes for a full dataset.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles errors gracefully.
  - [ ] - Verify that the ETL process handles large datasets gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL process is at least 90%.

---

### User Story 5 - Performance Acceptance Criteria 2

```txt
Given the entire ETL process,
When it is executed,
then no significant performance regressions should be introduced.
```

Here we need to INTEGRATION test that the following things happen:

- ***Performance Test***:
  - [ ] - Verify that no significant performance regressions are introduced after changes to the ETL process.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL process is at least 90%.

---

### User Story 5 - Documentation Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Code should be documented with clear and concise comments.

---

### User Story 5 - Documentation Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - User-facing documentation should be updated to reflect new or changed functionality.

---

### User Story 5 - Testing Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Unit tests should cover all new functionality.

---

### User Story 5 - Testing Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - Integration tests should cover interactions between components.

---

### User Story 5 - Testing Acceptance Criteria 3

Here we need to manually check that, during a code review, that:

- [ ] - All tests should pass successfully.

---

### User Story 5 - Testing Acceptance Criteria 4

Here we need to manually check that, during a code review, that:

- [ ] - Test coverage should meet the project's required threshold of 90%.

---

### User Story 6 - Pipeline Deployment and Orchestration

```txt
As a Data Scientist,
I want to be able to refresh the data set, perhaps with new data,
So that I can keep my analysis up to date
```

***Acceptance Criteria***

- ***Data Extraction***
  - [ ] Given new data is available in the source systems, when the ETL pipeline is executed, then the new data should be extracted and included in the final output dataset.
- ***Data Cleaning***
  - [ ] Given the extracted data, when the ETL pipeline is executed, then the output dataset should have duplicates removed.
  - [ ] Given the extracted data, when the ETL pipeline is executed, then missing or invalid values should be handled according to the defined cleaning rules.
- ***Data Transformation***
  - [ ] Given the cleaned data, when the ETL pipeline is executed, then the customer demographics and transaction datasets should be merged correctly, with relationships preserved (e.g., customer_id as the key).
  - [ ] Given the cleaned data, when the ETL pipeline is executed, then calculated fields (e.g., total_spent, avg_transaction_value) should match expected outcomes for sample test cases.
  - [ ] Given the cleaned data, when the ETL pipeline is executed, then filters (e.g., for active customers) should be applied accurately based on the defined rules.
- ***Data Loading***
  - [ ] Given the transformed data, when the ETL pipeline is executed, then the data should be loaded into the target SQL database successfully, with row counts matching expectations.
- ***Data Quality***
  - Given the final dataset, when the ETL pipeline is executed, then the dataset should meet quality requirements:
    - [ ] 100% of expected columns and rows are present.
    - [ ] Records maintain consistent formats and values.
    - [ ] Records uphold integrity constraints.
    - [ ] Error rates remain below the defined threshold (e.g., 1%).
- ***Performance***
  - [ ] Given the ETL pipeline, when executed end-to-end, then it should process the full dataset within acceptable time limits for the environment (e.g., under 30 minutes).
- ***Deployment***
  - [ ] Given the ETL pipeline, when it is deployed, then it should run on a scheduled basis to refresh the dataset with new data.
  - [ ] Given the ETL pipeline, when it is deployed, then it should support manual execution on-demand.
  - [ ] Given the ETL pipeline, when it is deployed, then monitoring and alerting should notify stakeholders of successful and failed runs.
- ***Documentation***
  - [ ] Given the ETL process, when development is completed, then the code should include clear, concise comments.
  - [ ] Given the ETL process, when development is completed, then user-facing documentation should reflect the current functionality.
- ***Testing***
  - [ ] Given the ETL process, when development is completed, then automated tests should validate functionality at the unit, integration, and system levels.
  - [ ] Given the ETL process, when development is completed, then all tests should pass successfully.

---

### User Story 6 - Data Extraction Acceptance Criteria 1

```txt
Given new data is available in the source systems,
When the ETL pipeline is executed,
then the new data should be extracted and included in the final output dataset.
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the ETL pipeline extracts new data from the source systems.
  - [ ] - Verify that the new data is included in the final output dataset.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after extracting new data.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Data Cleaning Acceptance Criteria 1

```txt
Given the extracted data,
When the ETL pipeline is executed,
then the output dataset should have duplicates removed.
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the ETL pipeline removes duplicates from the output dataset.
  - [ ] - Verify that the ETL pipeline handles duplicate records gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after removing duplicates.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Data Cleaning Acceptance Criteria 2

```txt
Given the extracted data,
When the ETL pipeline is executed,
then missing or invalid values should be handled according to the defined cleaning rules.
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the ETL pipeline handles missing or invalid values according to the defined cleaning rules.
  - [ ] - Verify that the ETL pipeline handles missing or invalid values gracefully.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after handling missing or invalid values.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Data Transformation Acceptance Criteria 1

```txt
Given the cleaned data,
When the ETL pipeline is executed,
then the customer demographics and transaction datasets should be merged correctly, with relationships preserved (e.g., customer_id as the key).
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the ETL pipeline merges the customer demographics and transaction datasets correctly.
  - [ ] - Verify that the relationships between the datasets are preserved (e.g., customer_id as the key).
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after merging the datasets.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Data Transformation Acceptance Criteria 2

```txt
Given the cleaned data,
When the ETL pipeline is executed,
then calculated fields (e.g., total_spent, avg_transaction_value) should match expected outcomes for sample test cases.
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the calculated fields (e.g., total_spent, avg_transaction_value) match expected outcomes for sample test cases.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after calculating fields.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Data Transformation Acceptance Criteria 3

```txt
Given the cleaned data,
When the ETL pipeline is executed,
then filters (e.g., for active customers) should be applied accurately based on the defined rules.
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the ETL pipeline applies filters (e.g., for active customers) accurately based on the defined rules.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after applying filters.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Data Loading Acceptance Criteria 1

```txt
Given the transformed data,
When the ETL pipeline is executed,
then the data should be loaded into the target SQL database successfully, with row counts matching expectations.
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the ETL pipeline loads the data into the target SQL database successfully.
  - [ ] - Verify that the row counts in the target SQL database match expectations.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after loading into the target SQL database.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Data Quality Acceptance Criteria 1

```txt
Given the final dataset,
When the ETL pipeline is executed,
then the dataset should meet quality requirements:
- 100% of expected columns and rows are present.
- Records maintain consistent formats and values.
- Records uphold integrity constraints.
- Error rates remain below the defined threshold (e.g., 1%).
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the final dataset meets quality requirements.
- ***Data Integrity Tests***
  - [ ] - Verify that the data remains consistent and accurate after the ETL pipeline is executed.
- ***Reliability Tests***:
  - [ ] - Verify that the ETL pipeline handles errors gracefully.
- ***Code Quality Tests***
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Performance Acceptance Criteria 1

```txt
Given the ETL pipeline,
When executed end-to-end,
then it should process the full dataset within acceptable time limits for the environment (e.g., under 30 minutes).
```

Here we need to End-to-End test that the following things happen:

- ***Performance Test***:
  - [ ] - Verify that the ETL pipeline processes the full dataset within acceptable time limits.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles errors gracefully.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Deployment Acceptance Criteria 1

```txt
Given the ETL pipeline,
When it is deployed,
then it should run on a scheduled basis to refresh the dataset with new data.
```

Here we need to End-to-End test that the following things happen:

- ***Functional Tests***
  - [ ] - Verify that the ETL pipeline runs on a scheduled basis to refresh the dataset with new data.
- ***Reliability Tests***:
  - [ ] - Verify that the system handles errors gracefully
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Deployment Acceptance Criteria 2

```txt
Given the ETL pipeline,
When it is deployed,
then it should support manual execution on-demand.
```

Here we need to manually test that this can happen.

---

### User Story 6 - Deployment Acceptance Criteria 3

```txt
Given the ETL pipeline,
When it is deployed,
then monitoring and alerting should notify stakeholders of successful and failed runs.
```

Here we need to End-to-End test that monitoring and alerting is set up correctly:

- ***Functional Tests***
  - [ ] - Verify that monitoring and alerting notify stakeholders of successful runs.
  - [ ] - Verify that monitoring and alerting notify stakeholders of failed runs.
- ***Code Quality Tests***:
  - [ ] - Python scripts pass linting and formatting checks.
  - [ ] - Test coverage on the ETL pipeline is at least 90%.

---

### User Story 6 - Documentation Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Code should be documented with clear and concise comments.

---

### User Story 6 - Documentation Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - User-facing documentation should be updated to reflect new or changed functionality.

---

### User Story 6 - Testing Acceptance Criteria 1

Here we need to manually check that, during a code review, that:

- [ ] - Unit tests should cover all new functionality.

---

### User Story 6 - Testing Acceptance Criteria 2

Here we need to manually check that, during a code review, that:

- [ ] - Integration tests should cover interactions between components.

---

### User Story 6 - Testing Acceptance Criteria 3

Here we need to manually check that, during a code review, that:

- [ ] - All tests should pass successfully.

---

---
