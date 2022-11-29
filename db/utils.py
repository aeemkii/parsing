import os

def create_databese(c):
    query = "CREATE DATABASE students_db;"
    c.execute(query)



def db_exists(c, db_name):
    query = f"SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME='{db_name}';"
    c.execute(query)
    db=c.fetchone()
    if db is not None:
        return True
    else:
        return False
    

def clear_terminal():
    # os.system("cls||clear")
    os.system("clear")
































## if not db_exists(cursor,"students_db"):
##    create_databese(cursor)
##     print("База создалась!...")
