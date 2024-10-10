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

### Retrieve index object
object_type = database_object.getObjectTypeName().lower()
object_name = database_object.getName().lower()
# print ("Object name=" + object_name + ", Object type=" + object_type)

### Are we executing this script on a uniqueconstraint object?
if "foreignkey" in object_type:

    print ("Foreign Key name=" + object_name + ", Object type=" + object_type)

    # ### If there is a foreign key, then ...
    fk_name_current = object_name
    fk_name_expected = "xfk"
    
    ### if the current primary key name not what we expected ...
    if fk_name_expected not in fk_name_current:
        liquibase_status.fired = True       # indicates the custom check has been triggered

        # set the message of the custom check, which liquibase will return
        status_message = "Found foreign key name " + f"{fk_name_current}" + " which did not start with " + f"{fk_name_expected}"
        liquibase_status.message = status_message

        sys.exit(1)     # exit from the check

### No foreign keys found in the database. 
### For this object we will not trigger this check
False