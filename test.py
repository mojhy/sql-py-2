import sqlite3

DATABASE =  'table1'

def print_all_cars():
    speed = int(input("what speed: ")) 
    with sqlite3.connect(DATABASE) as db:   
        cursor = db.cursor()
        db = sqlite3.connect('table1')
        sql = "select car_name, top_speed from car where top_speed > ?;"
        cursor.execute(sql,(speed,))
        results = cursor.fetchall()

        for car in results:
            print(f'{car[0]} {car[1]}')
print_all_cars()