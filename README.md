
This repository contains test cases for Custom Policy Checks.

# Links
| Description | Source |
|-------------|--------|
| Latest Liquibase build (Download `liquibase-<version>.zip`) | [GitHub.com](https://github.com/liquibase/liquibase/releases/latest)
| Documentation | [doc.liquibase.com](https://docs.liquibase.com/liquibase-pro/policy-checks/custom-policy-checks/checks-python-package.html)
| Checks jar file | [Maven Repository](https://mvnrepository.com/artifact/org.liquibase.ext/liquibase-checks)
| Python code reference | [W3Schools.com](https://www.w3schools.com/python/default.asp)
| SQL parse module reference | [ReadTheDocs.io](https://sqlparse.readthedocs.io/en/latest/)
| Python helper scripts (included with build) | [GitHub.com](https://github.com/liquibase/liquibase-checks/tree/main/scripting/liquibase_checks_python/src/liquibase_checks_python)
| GraalPy (required for local virtual environment) | [GitHub.com](https://github.com/oracle/graalpython/releases)
| GraalPy reference | [Medium.com](https://medium.com/graalvm/graalpy-quick-reference-0488b661a57c)
| venv reference | [Python.org](https://docs.python.org/3/library/venv.html)

# Pre-Execution Steps
1. Clone the repo to ensure you have all available updated files.<br>
     ```
     git clone git@github.com:adeelmalik78/python_policy_checks.git
     ```
1. Java 17 or higher is required. 
1. Download and extract the `liquibase-<version>.zip` file.
1. Ensure this property (*liquibase-checks-enabled*) is set to enable custom policy checks.<br>
* *Environment variable*: `LIQUIBASE_COMMAND_CHECKS_RUN_CHECKS_SCRIPTS_ENABLED='true'`<br>
* *liquibase.properties:* `checks-scripts-enabled=true`<br>
* *CLI:* `--checks-scripts-enabled=true`<br>

# Tutorials
There are two tutorials provided in this repo. These are a great starting point to learn from a helloworld example:
1. [Python Custom Policy Checks Tutorial for Database Checks](Tutorial/PythonCustomPolicyChecksTutorialforDatabaseChecks.pdf)
1. [Python Custom Policy Checks Tutorial for Changelog Checks](Tutorials/PythonCustomPolicyChecksTutorialforDatabaseChecks.pdf)

# Observations
1. Recommend all non-custom policy checks be disabled for testing.
1. SQL changelogs are available in the [changelog.sql](changelog.sql) file.
1. [IMPORTANT] Python scripts are called ONCE FOR EACH CHANGESET (changelog scope) or ONCE FOR EACH DATABASE OBJECT (database scope). Changesets may contain multiple SQL statements.
1. The `print()` function can be used to display debugging messages (instead of just liquibase_logger). This works regardless of log_level. Additionally, `f strings` automatically convert variables for printing and remove the need for concatenation to build a string of static and dynamic text.
    ```python
    my_int = 123
    my_str = "Hello World!"
    print(f"{my_str} My variable is: {my_int}")
    ```
    f strings can also be used wherever strings are expected.
    ```
    my_int = 123
    liquibase_status.message = f"My variable is: {my_int}"
    ```
1. Arguments defined at check creation/modification can be passed in to scripts. See [varchar_max_size.py](Scripts/varchar_max_size.py) for an example.
1. Error messages can be customized by adding a string to be replaced when defining the custom policy check. See [table_names_uppercase.py](Scripts/table_names_uppercase.py) for an example.
1. Values can be saved/retrieved between check runs using a cache. See [create_index_count.py](Scripts/create_index_count.py) for an example.
1. The latest Python helper scripts can be imported into your main python file to access available functions. Note you may need to ask #devops for access to the repository to view them.
    ```python
    import liquibase_utilities
    import liquibase_changesets

    print(liquibase_changesets.get_labels(liquibase_utilities.get_changeset()))
    ```
1. LoadData change types are not supported. [DAT-17893](https://datical.atlassian.net/browse/DAT-17893)
1. Having the commercial Mongo extension in the lib directory will cause some relational change types to behave incorrectly (e.g., createIndex). [DAT-17901](https://datical.atlassian.net/browse/DAT-17901)
1. Environment variables can be accessed using the os module.
    ```
    import os

    print(os.environ.get("LIQUIBASE_COMMAND_URL"))
    ```

# Running Local Python Environment
To use a local Python environment, versus the built-in one, follow these steps.<br>
1. Download and extract GraalPy.
1. Add \<install dir\>/bin (or \<install dir\>\bin for Windows) to your path.
1. Create a Python virtual environment and directory structure. Once created the environment can be moved to a different folder (provided the Liquibase environment variable is also updated). Use GitBash for Windows to execute these commands.
    ```
    graalpy -m venv <virtual env path>
    ```
1. Activate the environment to install modules to the local virtual environment.<br>
    *Linux*
    ```
    source <virtual env path>/bin/activate
    ```
    *Windows*
    ```
    source <virtual env path>/Scripts/activate
    ```
1. Install Python modules. Sqlpare is required.
    ```
    graalpy -m pip install sqlparse
    ```
1. Deactive the environment (exit or run bin/deactivate). Deactivate on Windows may throw an error (safe to close the GitBash window).
1. Configure Liquibase to point to the new virtual environment.<br>
    *Linux*
    ```
    LIQUIBASE_SCRIPT_PYTHON_EXECUTABLE_PATH="<virtual env path>/bin/python"
    ```
    *Windows*
     ```
    LIQUIBASE_SCRIPT_PYTHON_EXECUTABLE_PATH='<virtual env path>\Scripts\python.exe'
    ```
1. Run checks as normal. To revert back to the built-in environment, unset the environment variable.

# Configuration Steps
**Note:** script path includes name of script file
1. [**TableNamesMustBeUppercase**](Scripts/table_names_uppercase.py)

    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | TableNamesMustBeUppercase |
    | Severity | 0-4 |
    | Description | TableNamesMustBeUppercase |
    | Scope | changelog |
    | Message | Table \_\_TABLE_NAME\_\_ must be UPPERCASE. |
    | Type | python |
    | Path | Scripts/table_names_uppercase.py |
    | Args |  |
    | Snapshot | false |
1. [**VarcharMaxSize**](Scripts/varchar_max_size.py)
    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | VarcharMaxSize |
    | Severity | 0-4 |
    | Description | VarcharMaxSize |
    | Scope | database |
    | Message | Column \_\_COLUMN_NAME\_\_ exceeds \_\_COLUMN_SIZE\_\_. |
    | Type | python |
    | Path | Scripts/varchar_max_size.py |
    | Args | VARCHAR_MAX=255 |
    | Snapshot | false |
1. [**PKNamingConvention**](Scripts/pk_names.py)
    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | PKNamingConvention |
    | Severity | 0-4 |
    | Description | PKNamingConvention |
    | Scope | database |
    | Message | Primary key name \_\_CURRENT_NAME\_\_ must include table name (\_\_NAME_STANDARD\_\_). |
    | Type | python |
    | Path | Scripts/pk_names.py |
    | Args | |
    | Snapshot | false |
1. [**UCNamingConvention**](Scripts/xak.py)
    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | UCNamingConvention |
    | Severity | 0-4 |
    | Description | Unique constraint name must be in the form of xak_tablename |
    | Scope | DATABASE |
    | Message |  |
    | Type | PYTHON |
    | Path | Scripts/uc_names.py |
    | Args |  |
    | Snapshot | false |
1. [**PKNamingConventionPG**](Scripts/pk_names_pg.py)
    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | PKNamingPostgreSQL |
    | Severity | 0-4 |
    | Description | Name must be in the form of tablename_pkey |
    | Scope | DATABASE |
    | Message | Primary key name \_\_CURRENT_NAME\_\_ must include table name.  Please use (\_\_NAME_STANDARD\_\_) instead. |
    | Type | PYTHON |
    | Path | Scripts/pk_names_pg.py |
    | Args | STANDARD=pkey |
    | Snapshot | false |
1. [**CreateIndexCount**](Scripts/create_index_count.py)
    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | CreateIndexCount |
    | Severity | 0-4 |
    | Description | CreateIndexCount |
    | Scope | changelog |
    | Message | Table \_\_TABLE_NAME\_\_ would have \_\_INDEX_COUNT\_\_ indexes. |
    | Type | python |
    | Path | Scripts/create_index_count.py |
    | Args | MAX_INDEX=2 |
    | Snapshot | true |
1. [**FKNamingConvention**](Scripts/fk_names.py)
    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | FKNamingConvention |
    | Severity | 0-4 |
    | Description | FKNamingConvention |
    | Scope | changelog |
    | Message | Foreign key name \_\_NAME_CURRENT\_\_ must include parent and child table names (\_\_NAME_STANDARD\_\_). |
    | Type | python |
    | Path | Scripts/fk_names.py |
    | Args | |
    | Snapshot | false |
1. [**PKTablespace**](Scripts/pk_tablespace.py)
    ```
    % liquibase checks customize --check-name=CustomCheckTemplate
    ```
    | Prompt | Response |
    |--------|----------|
    | Short Name | PKTablespace |
    | Severity | 0-4 |
    | Description | PKTablespace |
    | Scope | changelog |
    | Message | Primary key name \_\_PK_NAME\_\_ must include explicit tablespace definition. |
    | Type | python |
    | Path | Scripts/pk_tablespace.py |
    | Args | |
    | Snapshot | false |
# Contact Liquibase
#### Liquibase sales: https://www.liquibase.com/contact
#### Liquibase support: https://support.liquibase.com/knowledge
