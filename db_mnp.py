'''DataBase manipulation for Omen'''
# Functions for writing, changing and deleting

import peewee as pw

'''
Declaration of common variable:
    self.db: variable for database object, puts in self list
'''

class dbMnp():
    '''class for DataBase manipulation'''

    def __init__(self, db_name):
        ''' Init fuction for class '''

        self.db_nm = db_name

        # In this construction we create database object
        if db_name == "static":
            self.db = pw.SqliteDatabase('db/' + db_name + '.db')

        elif db_name == "dynamic":
            self.db = pw.SqliteDatabase('db/' + db_name + '.db')

        elif db_name == "coor":
            self.db = pw.SqliteDatabase('db/' + db_name + '.db')

        else:
            print("Error!!! Invalid database name: " + db_name)

    def add_record(self, nm_table):
        self.db


#DEBUG RUN
if __name__ == "__main__":
    db_static = dbMnp("static")
    db_dynamic = dbMnp("dynamic")
    db_static.delet_record(345)
    db_dynamic.delet_record(67)

#DEBUG STOP