### Helpers come from Liquibase
import sys
import liquibase_utilities
import re

def find_string_index(lst, schemaChar):
    result = 0
    for i, string in enumerate(lst):
        if schemaChar in string:
            result = i
            # result.append((i, string.index(schemaChar)))
    return result

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

    schemaString = "."

    index = find_string_index(sql_list, schemaString)
    # print ("Schema found at index " + str(index) + ": " + str(sql_list[index]) )

    if (index != 0):
        # Found schema prefix
        # Now check if the schema is "public". If not public, then trigger the check
        publicString = "public"
        if not re.search(publicString, sql_list[index]):

            liquibase_status.fired = True       # indicates the custom check has been triggered

            # set the message of the custom check, which liquibase will return
            status_message = "No schema prefix allowed. Found schema prefix: [ " + f"{sql_list[index]}" + " ] in the changeset."
            liquibase_status.message = status_message

            sys.exit(1)     # exit from the check

### Default return code
False