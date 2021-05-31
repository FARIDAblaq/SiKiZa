from sqlite3.dbapi2 import connect
from flask import Flask, render_template, url_for, request, redirect
import sqlite3 
from sqlite3 import Error


conn = sqlite3.connect('req.db')
print("connected to database")
sql_create_users_table = 'CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, firstname text NOT NULL, lastname text NOT NULL,email text NOT NULL);'
conn.execute(sql_create_users_table)
print("table created succcesfully")



sikiza = Flask(__name__) 

@sikiza.route('/')
def Intro_Page():
    return render_template('index.html')


@sikiza.route('/home')
def Home_Page():
    return render_template('home.html')

@sikiza.route('/new')
def api():
    return render_template('api_request.html')

@sikiza.route('/new_request', methods=['POST', 'GET'])
def new_request():
    if request.method == 'POST':
        try:
            firstname = request.form['fname']
            lastname = request.form['lname']
            email = request.form['email']

            with sqlite3.connect('req.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO USERS (firstname,lastname,email) VALUES (?,?,?)", (firstname,lastname,email))
                conn.commit()
                msg = 'recorded Successfully'

        except:
            conn.rollback()
            msg = 'error inserting data'
        
        finally:
            return render_template("results.html",msg=msg)
            conn.close()

if __name__ == '__main__':
    sikiza.run(debug=True)
