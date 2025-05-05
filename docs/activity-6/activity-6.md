# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=`true`)

## Activity 6: Project Set Up

1. Setting up the project structure.
2. Setting up production, test and development environments.
3. Installing the required dependencies.
4. Creating the necessary files and folders.

---

### Step 1: Setup the Project Structure

```plaintext
etl-project-demo/
├── config/
│   ├── db_config.py
│   └── env_config.py
├── data/
│   ├── output/
│   ├── processed/
│   └── raw/
│       ├── unclean_customers.csv
│       ├── unclean_transactions.csv
│       └── unclean_transactions.sql
├── docs/
│   └── flowcharts/
│       └── etl_flowchart.md
├── etl/
│   ├── extract/
│   │   └── extract.py (to be populated)
│   ├── load/
│   │   └── load.py (to be populated)
│   ├── sql/
│   │   └── placeholder.sql (to be replaced)
│   ├── transform/
│       └── transform.py (to be populated)
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   └── run_etl.py
├── tests/
│   ├── component_tests/
│   │   └── .gitkeep (to be replaced)
│   ├── integration_tests/
│   │   └── .gitkeep (to be replaced)
│   └── unit_tests
│   │   └── test_db_config.py
│   └── run_tests.py
├── utils/
│   └── logging_utils.py
├── .coveragerc
├── .env.dev
├── .env.test
├── .flake8
├── .gitignore
├── .sqlfluff
├── README.md
├── requirements-setup.txt
├── requirements.txt
└── setup.py
```

Explanation of Folders and Files

- ***config/***: Contains configuration files and scripts:
  - **db_config.py**: A Python script for database configuration and connection setup.
  - **env_config.py**: A Python script for environment configuration and variables loading.
- ***data/***: Contains data files.
  - ***output/***: Stores final output data files that are ready for analysis.
  - ***processed/***: Stores intermediate data files that have been processed.
  - ***raw/***: Stores raw data files (e.g., CSV files) that are extracted from the source (but also the dummy data in this project!)
    - **unclean_customers.csv**: The raw, unclean customer data
    - **unclean_transactions.csv**: The raw, unclean transaction data (to help with the query)
    - **unclean_transactions.sql**: An SQL query that inserts the raw transactions data into a transactions table
- ***docs/***: Contains documentation files.
  - ***flowcharts/***: Stores flowcharts and diagrams related to the ETL process.
    - **etl_flowchart.md**: A markdown file containing the ETL flowchart created using Mermaid.
- ***etl/***: Contains the main ETL scripts.
  - ***extract/***: Contains scripts for data extraction.
    - **extract.py**: Empty file to contain functions for data extraction from various sources.
  - ***load/***: Contains scripts for data loading
    - **load.py**: Empty file to contain functions for loading data into the target database.
  - ***sql/***: Will contain SQL scripts for extracting data from and loading data to databases.
    - **placeholder.sql**: Empty file that will be replaced as the project evolves.
  - ***transform/***: Contains scripts for data transformation.
    - **transform.py**: Empty file to contain functions for data transformation and cleaning.
- ***notebooks/***: Folder for any Jupyter notebooks for exploratory data analysis and prototyping
  - **exploratory_analysis.ipynb**: Empty Jupyter Notebook
- ***scripts/***: Contains scripts for running the ETL pipeline.
  - **run_etl.py**: A script to run the entire ETL pipeline - calls `extract` -> `transform` -> `load` from the appropriate Python script.
- ***tests/***: Contains test scripts for unit testing and performance testing.
  - ***component_tests/***: Folder for storing component tests in (currently has .gitkeep to preserve folder in Git).
  - ***integration_tests/***: Folder for storing integration tests in (currently has .gitkeep to preserve folder in Git).
  - ***unit_tests/***: Folder for storing unit tests in.
    - **test_db_config.py**: Contains `pytest` tests to test the `db_config` functions
  - **run_tests.py**: Contains a script for executing different test runs.
- ***utils/***: Contains utility functions to help keep code clean.
  - **logging_utils.py**: A script to enable the application to log errors to both a file and to the terminal.
- **.coveragerc**: Configuration file to set test coverage parameters, including files/folders and pass %.
- **.env.\***: Environment files for `dev` and `test` that set Source and Target database credentials.
- **.flake8**: Configuration file for Flake8 linting rules for Python.
- **.gitignore**: Configuration file for Git to know which files not to track.
- **.sqlfluff**: Configuration file for SQLFluff linting rules for SQL.
- **README.md**: A markdown file that provides an overview of the project, setup instructions, and usage guidelines.
- **requirements-setup.txt**: Contains a list of required Python packages to be able to use **setup.py** to install the project.
- **requirements.txt**: Contains a list of required Python packages to be able to use **setup.py** to install the project.
- **setup.py**: A setup script for installing the project as a package.

---

### Step 2: Set Up the Environments

#### 2.1. Create `.env.xxx` Files

Create two environment files: `.env.dev` and `.env.test`.

```bash
# Development Environment Variables

# Source Database Configuration
SOURCE_DB_NAME=etl_demo_dev_source
SOURCE_DB_USER=postgres
SOURCE_DB_PASSWORD=
SOURCE_DB_HOST=localhost
SOURCE_DB_PORT=5432

# Target Database Configuration
TARGET_DB_NAME=etl_demo_dev_source
TARGET_DB_USER=postgres
TARGET_DB_PASSWORD=
TARGET_DB_HOST=localhost
TARGET_DB_PORT=5432
```

```bash
# Source Database Configuration
SOURCE_DB_NAME=etl_demo_test_source
SOURCE_DB_USER=postgres
SOURCE_DB_PASSWORD=
SOURCE_DB_HOST=localhost
SOURCE_DB_PORT=5432

# Target Database Configuration
TARGET_DB_NAME=etl_demo_test_source
TARGET_DB_USER=postgres
TARGET_DB_PASSWORD=
TARGET_DB_HOST=localhost
TARGET_DB_PORT=5432
```

At this point, we don't know details of the Production Environment, so we will not create a `.env` file.

> ***NOTE***: It is actually unlikely that we'll ever have a `.env` file in a production environment. Instead, we would set environment variables directly on the server that will build and run the ETL pipeline.

---

#### 2.2 Create a Python .venv

Create a Python virtual environment and activate it.

```bash
python3 -m venv .venv
source .venv/bin/activate       # On Windows, use .venv\Scripts\activate
```

---

#### 2.3 Create the Development and Test Source Databases

Create the development and test source databases by running the following commands on the terminal (given you have successfully installed Postgres!):

```bash
psql -U postgres -c "CREATE DATABASE etl_demo_dev_source;"
psql -U postgres -c "CREATE DATABASE etl_demo_test_source;"
```

---

#### Step 2.4: Populate the Development Database

Populate the development database with the sample data provided in the `data/raw` folder (using the **unclean_transactions.sql** file).

> You need to make sure you are in the `etl-project` folder, rather than the `etl-project-demo` to run this command OR provide the relative link to the `data-for-demo` folder.

```bash
psql -U postgres -d etl_demo_dev_source -f data/raw/unclean_transactions.sql
```

You can check that this has happened by connecting your local database to DBeaver, navigating the connection to the `Databases` section and then checking that the `transactions` table has been created and populated.

---

### Step 3: Install the Required Dependencies

Use `pip install` to install the required dependencies.

For working with different environment variables:

- `python-dotenv`: A Python library for working with environment variables.

For Connecting to PostgreSQL databases:

- `sqlalchemy`: A PostgreSQL adapter for Python.

For Cleaning and Transforming Data:

- `pandas`: A powerful data manipulation library.

For Exploratory Data Wrangling:

- `ipykernel`: A library that allows VSCode to run Jupyter Notebooks

For Testing:

- `pytest`: A testing framework for Python.
- `pytest-cov`: A plugin for pytest that generates coverage reports.
- `pytest-mock`: A plugin for pytest that provides a mock fixture.
- `pytest-postgresql`: A plugin for pytest that provides a PostgreSQL fixture for testing.

For Linting and Code Formatting:

- `flake8`: A tool for linting Python code
  >***Top Tip: Install the Flake8 VSCode extension to pre-empt most issues!***
- `sqlfluff`: A SQL linter and formatter.

We may well add more as we go but here is the complete install command for now:

```bash
pip install python-dotenv sqlalchemy pandas pytest pytest-cov pytest-mock pytest-postgresql flake8 sqlfluff ipykernel
```

Freeze the requirements to the `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Run the project setup script to install the project as a package:

```bash
pip install -e .
```

The `-e` flag is used to install the project in "editable" mode, which means that changes to the source code will be reflected in the installed package without needing to reinstall it.

> NB: The .venv folder will not be included in the project repository and therefore the dependencies will need to be installed every time the project is cloned.  
> Since we are going to be writing a script to automate the running of the pipeline, the **setup.py** file will be used to install the project as a package.
>
> On a clean clone of the project in this state, only the following commands will be needed to set up the project:
>
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements-setup.txt
> pip install -e .
> ```

Try it yourself - delete the `.venv` you created and then run the set of commands above.

#### Why bother with this?

This will make the running of the project much simpler, both in development and when it comes to deploying the project!

We'll simply be able to run the following scripts further down the line:

```sh
# Run the project as if it were the pipeline running (development mode)
run_etl <env>  # Where <env> is replaced by the name of the environment to run in, e,g dev

# Run the tests in the project (test mode)
run_tests <test_type>
```

---

### Step 4: Review the Necessary Files and Folders

#### 4.1 Review the `env_config.py` File

As we want to be able to run the project whilst developing, be able to test the scripts with consistent values and ultimately deploy the project to production, it makes sense to utilise different environments for these situations.

We need to have a way to detect which environment should be initialised when we start the script (using the commands from the `setup.py` file).

Earlier, we created `.env` files with *environment variables* in them.  These provide the scripts with details as to things like which database to use and the login details for it.  These are for the source and target databases.

Create a `env_config.py` file in the `config/` folder to set the environment variables for the specific environments to run the scripts in.

The file is included in the repo, here is an overview.

`dotenv` allows us to load the environment variables from the `.env.xxx` files.

***Line 4*** creates a list of the acceptable environment names.

***Line 7*** declares a function that will be called at the start of the run script and receives the arguments from the command line call that initiated the script.

***Lines 8-12*** check that an acceptable environment has been passed as an argument and raises a `ValueError` if one is not.

***Line 14*** sets a variable called `env` to use in the rest of the function with the value of the argument passed in.

***Line 16*** calls a function to remove any previous environment variables set - this is good practice as it ensures a clean environment for the script to run in

***Line 17*** sets an environment variable named `ENV` to the value of the variable `env`.

> In Python, the `os.environ` object is a dictionary-like structure provided by the `os` module, which allows you to interact with the environment variables of the operating system. By assigning a value to `os.environ['ENV']`, you are creating or updating the `ENV` environment variable for the current process. This change will persist for the duration of the program's execution but will not affect the system's global environment variables or other processes.

***Line 23*** specifies which of the `.env` files to use

***Line 26*** calls the `load_dotenv` function from the `dotenv` module with the specified `.env` file and will overwrite any existing values found.

On executing this function, the values from the appropriate `.env` file will be available for use in any Python script via a call to the `os.getenv` function, using the variable name as an argument.

When we run the project, we will prefix the command with the environment variable we want to use.

```bash
run_etl dev
```

This command would set the `ENV` to be `dev` and use the `.env.dev` file to load the environment variables.

```bash
run_etl test
```

This command would set the `ENV` to be `test` and use the `.env.test` file to load the environment variables.

```bash
run_etl prod
```

This command would set the `ENV` to be `prod` and use the `.env` file to load the environment variables.

---

#### 4.2 Review the logging functionality

Part of the agreed Definition of Done is that the pipeline will log significant events, like errors.  To do this, we need to utilise Python's in-built logging functionality.

In the `utils` folder, you will find a file called `logging_utls.py`.

Review this file and work out what it does!

***Note***: This file may be added to in future features.

---

#### 4.3: Review the `db_config.py` File

View `db_config.py` file in the `config/` folder, this stores the database configuration details.

The file is included in the repo, here is an overview.

***Line 3***: Imports the `setup_logger` function from the previous section

***Line 4***: Imports the `Dict` type so that we can type-hint that the `load_db_config` function should return a Python Dictionary that has a `string` as a key and another Dictionary as the value

***Line 7***: Defines a custom `Exception` for logging purposes

***Lines 28-43***: Define the dictionary to be returned when the `load_db_config` is called.  It is dependent the `setup_env` function already being called elsewhere in the project to be able to retrieve the correct values from the system's environment variables.

***Line 45***: Calls a function to validate the configuration object

***Line 50***: Defines the validation function - this essentially checks that none of the `os.getenv` calls returned `'error'` - if they did then this is logged and an unhandled Exception is raised.  We want the pipeline to terminate if the database configuration is incorrect!

---

#### 4.4: Set Up PyTest, Coverage, Lint, Unit, Component, and Integration Testing

#### 4.4.1: Configure Test Runs

Look in the `tests` folder and you should find a file called `run_tests.py`.  The purpose of this file to allow the running of different types of tests as well as a full test run.

The first line of the method is to access the argument that has been supplied to the script.  This file configures tests to be run using the command `run_tests` followed by the type of test to be run.  

```python
def main():
    command = sys.argv[1]
    ...
```

The options defined are:

```bash
run_tests unit # Run unit tests
run_tests component # Run component tests
run_tests integration # Run integration tests
run_tests all # Run all tests
```

```python
   ...
   # Define test directories and corresponding coverage targets
    test_config = {
        'unit': {'dir': 'tests/unit_tests', 'cov': ['config']},
        'integration': {'dir': 'tests/integration_tests', 'cov': []},
        'component': {'dir': 'tests/component_tests', 'cov': []},
        'all': {'dir': 'tests', 'cov': ['config', 'etl']},
    }
    ...
```

The `test_config` dictionary defines the directories to search for tests and the units under test for coverage reports to be generated.  If additional folders are added to say unit tests, then the path from the root of the project should be added to the `'cov'` list.

> E.g. If we wanted to additionally unit test the `extract.py` file found on the path `etl/extract` then the `'unit'` key in the dictionary would be updated to include the path to the file.

```python
test_config = {
    'unit': {'dir': 'tests/unit_tests', 'cov': ['config', 'etl/extract']},
    ...
}
```

Later we will add an additional key for `'performance'` tests to allow the `run_tests performance` to be run individually.

We then check to see if a command was supplied for the test run and get the directories to test and the folders to run coverage on:

```python
   ...
   if command in test_config:
        # Access the test_config dictionary to get the test directory 
        # and coverage targets
        test_dir = test_config[command]['dir']
        cov_sources = ','.join(test_config[command]['cov'])
   ...
```

The next section builds the command to run the tests and coverage reports, based on the type of test and the coverage directories associated with it, defaulting to a standard pytest run if no coverage directories are defined.

```python
   ...
   if cov_sources:
            cov_command = (
                f'ENV=test coverage run --source={cov_sources} '
                f'--omit=*/__init__.py -m pytest --verbose {test_dir} '
                '&& coverage report -m && coverage html '
                '&& coverage report --fail-under=90'
            )
        else:
            cov_command = f'ENV=test pytest --verbose {test_dir}'
    ...
```

> NOTE: The command is configured to be run on UNIX-Like systems as most CI/CD pipelines will be running on Linux.  You will need to change the `ENV=test` to `set ENV=test` to set the environment variable to run from the Command Line on Windows and `$env:ENV="test";` to set the environment variable in PowerShell.  If you are running on Powershell in Windows, you will need to change the `&&` to `;` (removing the space before it) to run the commands sequentially.  
>
> ***BEST PRACTICE***: Assume Linux on projects but check! Set the default terminal on your Windows machine to ***GitBash*** as this allows you to run Linux commands in a Windows environment.

Each command is prefixed with the environment variable `ENV` (set to `test`) to ensure the correct environment variables are loaded and coverage is calculated for the files tested.

We run coverage on the source files defined, omitting any `__init__.py` files, and then run the tests in the directory defined.  The `verbose` flag is used to output the results of the tests to the console.  A coverage report is generated in html format and the script will fail if the total coverage of the tests is below 90%.  This will count as a failure in an automated process.

The final line of this `if` section uses the `subprocess` module to run the command and output the results to the console.

```python
   ...
   subprocess.run(cov_command, shell=True)
   ...
```

The first `elif` will run if `lint` is supplied as the argument and this will run the `flake8` process over the folders defined in the `.flake8` file.  This can be found in the root of the project.

```python
   ...
   elif command == 'lint':
        subprocess.run('flake8', shell=True)
   ...
```

The `else` statement will throw a `ValueError` which will stop the script running if an invalid command is supplied.  This will be extremely useful in an automated process to make sure that the job fails if the tests are not run correctly.

```python
   ...
   else:
        raise ValueError(f"Unknown command: {command}")
   ...
```

The final lines of the script is to call the `main` method to run the script.

```python
if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Usage: run_tests.py <unit|integration|component|all|lint>")
    else:
        main()
```

This will also throw an error if the `run_tests` command is run without a valid argument.

---

#### 4.4.2 PyTest Configuration

No additional configuration of PyTest is required.  If additional configuration is required, a `pytest.ini` file can be created in the root of the project.

#### 4.4.3 Coverage Configuration

Configuration of Coverage is required.  A `.coveragerc` file is included in the root of the project.  The options for coverage are defined in the command generated for the purposes of this walkthrough.  Information about configuring coverage can be found [here](https://coverage.readthedocs.io/en/coverage-5.5/config.html).

The configuration stops the test coverage reporter assessing whether test files are tested (why would you!) and any `__init__.py` files are excluded too.

If coverage of the whole of the testing is less than ***90%*** then testing will report as failing - this has been set inline with the project requirements.

The final part of this config file sets an output directory for HTML reports that can be viewed.

#### 4.4.4 Flake8 Configuration

A `.flake8` file has been created in the root of the project to define the rules for linting the code.  At the current time, the file has been set up to exclude a number of project folders (including the walkthrough folders) and also any folders that may contain external Python files (linting them is not OUR responsibility).  We also exclude test files from the linting process but you should endeavour to meet linting rules where possible!

#### 4.4.5 Performance Testing

Setting up performance testing will be covered later in the walkthrough.

---

---

## Running the Tests

A unit test has been created for the config.db_config module.  This test checks that the correct values are loaded from the `.env` files.

To run the test, use the following command:

```bash
run_tests unit
```

This command will run the unit tests and output the results to the console.

```terminal
============================================================================================== test session starts ===============================================================================================
platform darwin -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0 -- /Users/edwright/DFA-Repos/Digital-Futures-Academy-DE-Curriculum/etl_example/.venv/bin/python3.13
cachedir: .pytest_cache
rootdir: /Users/edwright/DFA-Repos/Digital-Futures-Academy-DE-Curriculum/etl_example
plugins: cov-6.0.0, postgresql-6.1.1, mock-3.14.0
collected 1 item                                                                                                                                                                                                 

tests/unit_tests/test_db_config.py::test_load_db_config PASSED                                                                                                                                             [100%]

=============================================================================================== 1 passed in 0.02s ================================================================================================
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
config/db_config.py       9      0   100%
---------------------------------------------------
TOTAL                     9      0   100%
Wrote HTML report to htmlcov/index.html
Name                  Stmts   Miss  Cover
-----------------------------------------
config/db_config.py       9      0   100%
-----------------------------------------
TOTAL                     9      0   100%
```

You will also find that a new folder, called `htmlcov` has been created in the root of the project.  This folder contains the coverage report in HTML format.  Open the `index.html` file in a browser to view the report - if you have the `live-server` extension installed in VSCode, you can right-click on the file and select `Open with Live Server` to view the report in your browser.

You can also ensure that this test runs if the `run_tests all` command is run.

---

### Documenting the Environment Set Up

It is good practice to have a README file that documents the environment set up.  This should include the following:

- How to set up the project.
- How to install the required dependencies.
- How to set up the databases (locally for now but how to get access to the staging, testing and production databases should be included).
- How to run the tests (including fail conditions for the pipeline - what will stop the tests completing successfully - apart from errors in the code!)
- How to run the ETL pipeline (locally for now but ultimately, how a pipeline rebuild is triggered would be here too).
- Any additional information that may be useful for someone new to the project.

### Over to You

Create a file called PROJECT_README.md in the root of your project and document the environment set up.  You should reference this document and the README.md file in the root of the project to help.

---

## Summary

The project is now set up and we are ready to tackle some of the tasks in the first user story!

---

---
