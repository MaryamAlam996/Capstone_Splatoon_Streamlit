# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)

## Activity 1: Identify the User Stories

### Instructions

1. Work with your team to convert the project requirements below into user stories.
   - The 5 goals above translate into 4 ***epics***
     - These should be broken down into 1 or more user stories, using the format:

    ```plaintext
    As a [role], I want [goal/desire] so that [benefit].
    ```

| Epic                                                 | User Requirements                                                                         |
|------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Epic 1: Data Availability, Quality and Trust         | Analysts need a single, clean dataset combining transaction and demographic data.         |
|                                                      | Data scientists need the cleaned dataset stored in a SQL table for analysis.              |
| Epic 2: Customer Insights                            | Analysts want to analyze spending per customer and identify high-value customers.         |
|                                                      | Business stakeholders would like to identify customers who have spent more than **$500**. |
| Epic 3: Demographic Trends                           | Business stakeholders want insights into age and country trends of key customers.         |
| Epic 4: Data Access and Storage                      | Scientists need assurance that the data is clean, consistent, and accurate.               |
|                                                      | Scientists need the cleaned dataset stored in a SQL table for analysis.                   |
|                                                      | Scientists need to be able to reset and update the data for repeat or future analysis     |

Given these epics and their requirements, create user stories for each epic.  There is a hint as to how many stories are needed and the stakeholders involved in it.

### User Stories Solutions

#### Epic 1: Data Availability, Quality, Trust and Access

```txt
USER STORY 1

As a Data Analyst,  
I want access to a single, clean, and accurate dataset combining customer demographics and transaction data,  
So that I can analyze customer behaviour without worrying about data inconsistencies and can rely on it for analysis without manual checks.
```

**NOTE**: There are 2 User Requirements in Epic 1 but only a single User Stories is provided.  This is because the User Requirements are closely related and can be combined into a single User Story.

#### Epic 2: Customer Insights

```txt
USER STORY 2

As a Data Analyst,  
I want to know how much each customer has spent and their average transaction value,  
So that I can identify high-value customers for further analysis

USER STORY 3

As a Business Stakeholder,  
I want to identify high-value customers who have spent more than $500,  
So that we can target them for loyalty rewards
```

#### Epic 3: Demographic Trends

```txt
USER STORY 4

As a Business Stakeholder,  
I want to analyse demographic trends, such as customer age and country, among high-value customers,  
So that I can tailor our marketing campaigns to reach them effectively
```

#### Epic 4: Data Storage and Access

```txt
USER STORY 5

As a Data Scientist,  
I want the cleaned and enriched data to be stored in a SQL table,  
So that I can query it directly for advanced analysis

USER STORY 6

As a Data Scientist,
I want to be able to refresh the data set, perhaps with new data,
So that I can keep my analysis up to date
```

**Note**: Although there are 3 requirements here, they are combined into 2 user stories.  This is because the requirements are closely related and can be combined.
