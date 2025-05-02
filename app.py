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
    print('N_ID:   Number:  Do i like it?  Unbiased rating? ')
    for number in results:
        print(f"     {number[0]:<10}{number[1]:<15}{number[2]:<28} {number[3]}")
    #end of loop
    db.close()

def print_all_likes():
    """prints all likes"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from number_ratings where do_i_like_it = 'y';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    print('N_ID:   Number:  Unbiased rating? ')
    for number in results:
        print(f"     {number[0]:<10}{number[1]:<17} {number[3]}")
    #end of loop
    db.close()
def print_all_dislikes():
    """prints all dislikes"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from number_ratings where do_i_like_it = 'n';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    print('N_ID:   Number:  Unbiased rating? ')
    for number in results:
        print(f"     {number[0]:<10}{number[1]:<17} {number[3]}")
    #end of loop
    db.close()
#main code

while True:
    user_input = input(' \nwhat would you like to do. \ncall all numbers \nCall what I like \nCall what I disike \nExit \n')
    if user_input == "1":
        print_all()
    elif user_input == '2':
        print_all_likes()
    elif user_input == '3':
        print_all_dislikes()
    elif user_input == '4':
        break
    else:
        print('!That is not an option!\n')
