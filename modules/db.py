from os import error
import sqlite3
try:
    connection = sqlite3.connect('SikiZa.db')
    cursor = connection.cursor()
    # #query = """SELECT sqlite_version()"""
    query = """ CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL                       
    )"""
    # query = "DROP TABLE users"
    # query = """ INSERT INTO interns (user_id,first_name,last_name,email)
    #          VALUES(1, "Chantelle" , "Osafo", "cosafo@gmail.com", "+2330241578805", "Ashesi University")"""
    
    cursor.execute(query)
    # print ("Table Sucessfully created")
except connection.Error as error:
    print("Error creating Table" , error)
finally:
    if connection:
        connection.close()