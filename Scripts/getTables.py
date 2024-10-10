import liquibase_utilities as lb # this is where we are importing our liquibase_utilities helper script provided by liquibase
import sys # useful for indicating a check has been triggered

obj = lb.get_database_object() # this gets the database object the liquibase policy check is examining
status = lb.get_status() # this gets the status object of the liquibase check, used for reporting status and messages from the custom policy check


if "table" in obj.getObjectTypeName().lower():
    print (obj.getObjectTypeName().lower() + ": " + obj.getName().lower() )

if lb.is_table(obj): # function provided from liquibase utilities
    status.fired = True # indicates the custom check has been triggered
    status.message = "No tables allowed!" # set the message of the custom check, which liquibase will return
    sys.exit(1) # exit from the check