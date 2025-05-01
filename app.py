#made by harrison - numbers go brrrr
#imports
import sqlite3

#constants and varibles
DATABASE = "table2.db"

# functions
def print_all():
    """prints all number ratings nicely"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from number_ratings;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    for number in results:
        print(results)
    #end of loop

#main code
print_all()

db.close()