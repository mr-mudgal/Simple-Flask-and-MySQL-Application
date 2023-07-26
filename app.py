"""This module is our main file of the application, this files creates a server and configure CSS, HTML files along
with routes to every HTML page"""

# importing all the necessary modules
import mysql.connector
from flask import Flask

from routers.routes import router

# creating app (server)
app = Flask(__name__)
app.register_blueprint(router)

# connecting to the database
mydb = mysql.connector.connect(host="localhost", user="root", password="MySQL@1", database='users')
cur = mydb.cursor()
cur.execute('user users')


@app.errorhandler(404)
def not_found(e):
	return '<h1>PAGE NOT FOUND, <button><a href="/hello">Click to go to Home Page</a></button></h1>'


if __name__ == "__main__":
	app.run(debug=True)
