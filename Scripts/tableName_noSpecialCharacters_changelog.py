### Helpers come from Liquibase
import sys
import liquibase_utilities
import re

### Retrieve log handler
### Ex. liquibase_logger.info(message)
liquibase_logger = liquibase_utilities.get_logger()

### Retrieve status handler###
liquibase_status = liquibase_utilities.get_status()

### Retrieve all changes in a changeset
changes = liquibase_utilities.get_changeset().getChanges()

### Loop through all changes
for change in changes:

    ### Split sql into a list of strings to remove whitespace
    sql_list = liquibase_utilities.generate_sql(change).split()

    # Get index of all "create" in sql_list. Result will look like this [0] or [0,30]
    create_list = [i for i, x in enumerate(sql_list) if x.lower() == "create"] 
    # print ("Create list:" + str(create_list) )

    # Get index of all "rename" in sql_list. Result will look like this [0] or [0,30]
    rename_list = [i for i, x in enumerate(sql_list) if x.lower() == "rename"] 

    # If there is a CREATE statement in the changeset ...
    if len(create_list) > 0:
        for create_loc in create_list:
            # If we find TABLE immediately after CREATE ... as in CREATE TABLE ...
            #    then very next index will contain the table name.
            if sql_list[create_loc + 1].lower() == "table":
                table_name_current = sql_list[create_loc + 2].lower()
                table_name_expected = "[*#+-]"

                print ("CREATE table name is " + table_name_current)

                if re.search(table_name_expected, table_name_current):
                    # if table_name_expected not in table_name_current:
                    liquibase_status.fired = True       # indicates the custom check has been triggered

                    # set the message of the custom check, which liquibase will return
                    status_message = "CREATE table name " + f"{table_name_current}" + " contains one of these special characters " + f"{table_name_expected}"
                    liquibase_status.message = status_message

                    sys.exit(1)     # exit from the check

   # If there is a RENAME statement in the changeset ...
    if len(rename_list) > 0:
        for rename_loc in rename_list:
            # If we find TABLE immediately after RENAME ... as in RENAME TABLE ...
            #    then very next index will contain the table name.
            if sql_list[rename_loc + 1].lower() == "table":
                table_name_current = sql_list[rename_loc + 2].lower()
                table_name_expected = "[*#+-]"

                print ("RENAME table name is " + table_name_current)

                if re.search(table_name_expected, table_name_current):
                    # if table_name_expected not in table_name_current:
                    liquibase_status.fired = True       # indicates the custom check has been triggered

                    # set the message of the custom check, which liquibase will return
                    status_message = "RENAME table name " + f"{table_name_current}" + " contains one of these special characters " + f"{table_name_expected}"
                    liquibase_status.message = status_message

                    sys.exit(1)     # exit from the check

### Default return code
False