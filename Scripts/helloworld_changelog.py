### Helpers come from Liquibase
import liquibase_utilities

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

    # Print index of all "create" in sql_list
    create_list = [i for i, x in enumerate(sql_list) if x.lower() == "create"] 
    print ("Create list:" + str(create_list) )

    # Print index of all "insert" in sql_list
    # insert_list = [i for i, x in enumerate(sql_list) if x.lower() == "insert"] 
    # print ("Insert list:" + str(insert_list) )

    # # Print index of all "alter" in sql_list
    # alter_list = [i for i, x in enumerate(sql_list) if x.lower() == "alter"] 
    # print ("Alter list:" + str(alter_list) )

### Default return code
False