### Helpers come from Liquibase
import sys
import liquibase_utilities

### Retrieve log handler
### Ex. liquibase_logger.info(message)
liquibase_logger = liquibase_utilities.get_logger()

### Retrieve status handler
liquibase_status = liquibase_utilities.get_status()

### Retrieve database object
database_object = liquibase_utilities.get_database_object()

### Retrieve database object type and object name
object_type = database_object.getObjectTypeName().lower()
object_name = database_object.getName().lower()
print ("Object name=" + object_name + ", Object type=" + object_type)

### Are we executing this script on a table object?
if "table" in database_object.getObjectTypeName().lower():

    ### Get table name
    table_name = database_object.getName().lower()

    ### Get primary key for the table, if there is one ...
    pk_object = database_object.getPrimaryKey()

    ### If there is a primary key for this table, then ...
    if pk_object != None:
        pk_name_current = pk_object.getName()
        pk_name_expected = "xpk_" + f"{table_name}"
        
        ### if the current primary key name not what we expected ...
        if pk_name_expected not in pk_name_current:
            liquibase_status.fired = True       # indicates the custom check has been triggered
 
            # set the message of the custom check, which liquibase will return
            status_message = "Found primary key name " + f"{pk_name_current}" + " which did not match what was expected: " + f"{pk_name_expected}"
            liquibase_status.message = status_message

            sys.exit(1)     # exit from the check

### No primary key found in the table object. 
### For this table object we will not trigger this check
False