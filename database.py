##################### FOR ADDING SEPARATE INCLUDE PATH ######################
# only required if module was downloaded to another path
import sys
sys.path.append('/home/neil/.local/lib/python3.8/site-packages')
#############################################################################

import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="neil",
        password="verysecret",
        database="classicmodels"
    )

    print(mydb)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    mydb.close()