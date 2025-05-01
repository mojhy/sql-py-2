import sqlite3

db = sqlite3.connect('table2.db')
cursor = db.cursor()
sql = "select * from number_ratings;"
cursor.execute(sql)
results = cursor.fetchall()

print(results)

db.close()