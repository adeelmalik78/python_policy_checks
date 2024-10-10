### Helpers come from Liquibase
import sys
import liquibase_utilities
import re

### Retrieve log handler
### Ex. liquibase_logger.info(message)
liquibase_logger = liquibase_utilities.get_logger()

### Retrieve status handler
liquibase_status = liquibase_utilities.get_status()

### Retrieve database object
database_object = liquibase_utilities.get_database_object()

### Retrieve index object
object_type = database_object.getObjectTypeName().lower()
object_name = database_object.getName().lower()
# print ("Object name=" + object_name + ", Object type=" + object_type)

### Are we executing this script on a index object?
if "table" in object_type:

    print ("Table name=" + object_name + ", Object type=" + object_type)

    # ### If there is a table, then ...
    table_name_current = object_name
    table_name_expected = "[*#+-]"
    
    ### if the current table name not what we expected ...
    if re.search(table_name_expected, table_name_current):
    # if table_name_expected not in table_name_current:
        liquibase_status.fired = True       # indicates the custom check has been triggered

        # set the message of the custom check, which liquibase will return
        status_message = "Found table name " + f"{table_name_current}" + " which did not agree with TABLE naming convention " + f"{table_name_expected}"
        liquibase_status.message = status_message

        sys.exit(1)     # exit from the check

### No unique constraints found in the database. 
### For this object we will not trigger this check
False