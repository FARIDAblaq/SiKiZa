from flask import Flask, render_template, request, url_for,redirect
from os import error
import sqlite3
from sqlite3.dbapi2 import Cursor




try:
    connection = sqlite3.connect('SikiZa.db')
    cursor = connection.cursor()
    
    query = """ CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL                       
    )"""

   
    
    # query = "DROP TABLE users"
    cursor.execute(query)

    # print ("Table Sucessfully created")

except connection.Error as error:
    print("Error creating Table" , error)


app = Flask(__name__)

@app.route('/')
def open_form():
    return render_template('templates/api_request.html')

@app.route('/insert', methods = ['POST', 'GET'])
def insertdata():
    if request.method == 'POST':
        f_name = request.form['fname']
        l_name = request.form['lname']
        email = request.form['email']
        query1 = """ INSERT INTO users (user_id,first_name,last_name,email)
                VALUES(?,?,?,?)"""
        cursor.execute(query1, f_name,l_name,email)
        connection.commit()
        print("inserted successfully")
        connection.close()


        
