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
print ("Object name=" + object_name + ", Object type=" + object_type)

False