"""This module would create a database named: users, and create a table inside it with the same name.
This module also adds, 10 rows, as a sample data in the database."""

# import mysql connector for creating and executing, connection and queries respectively
import mysql.connector

# connect with mysql, with your credentials i.e., host, user and password
conn = mysql.connector.connect(host="localhost", user="root", password="MySQL@1")
# create a cursor which would be used to execute the queries
cur = conn.cursor()

try:
	# create a database using cursor
	cur.execute('CREATE DATABASE users')
	# closing the connection to connect with the newly created database

	conn.close()
except Exception as e:
	print(e)
finally:
	try:
		# connect with mysql, with your previous credentials and connect to newly created database
		conn = mysql.connector.connect(host="localhost", user="root", password="MySQL@1", database="users")
		# create a cursor which would be used to execute the queries on the specific database
		cur = conn.cursor()

		try:
			# create a table with columns and their properties
			cur.execute(
				'CREATE TABLE users(''id INT AUTO_INCREMENT PRIMARY KEY,''name VARCHAR(50) NOT NULL,''email VARCHAR('
				'50) NOT NULL, ''role VARCHAR(20) NOT NULL)')
		except Exception as e:
			print(e)
		finally:
			# query to insert sample data
			QUERY = "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)"
			# list of tuples, containing values, that would be inserted in the database, as a sample data
			VALUES = [
				('Ram', 'ram@gmail.com', 'Employee'),
				('Shyam', 'shyam@gmail.com', 'Employee'),
				('Rohit', 'rohit@gmail.com', 'Employee'),
				('Rocky', 'rocky@gmail.com', 'Employee'),
				('Rishi', 'rishi@gmail.com', 'Employee'),
				('Osama', 'osama@gmail.com', 'Employee'),
				('Dhananjay', 'dhananjay@gmail.com', 'Admin'),
				('Soumya', 'soumya@gmail.com', 'Assistant'),
				('Karishma', 'karishma@gmail.com', 'Assistant'),
				('Sherdil', 'sherdil@gmail.com', 'Admin')
			]

			# executing the command to insert all the values in the desired table
			cur.executemany(QUERY, VALUES)
			# committing the execution so that, the modifications are affected in database, even after the
			# connection is close
			conn.commit()
			print('10 rows, Sample Data added to database successfully!')
			# closing the connection
			conn.close()
	except Exception as e:
		print(e)
