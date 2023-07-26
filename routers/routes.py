# importing all the required module and variables
from flask import Blueprint, render_template, request, redirect

from app import cur, mydb

router = Blueprint('router', __name__)


@router.route('/hello')
def hello():
	"""This function simply return 'Hello, World!' string."""
	
	return 'Hello, World!'


@router.route('/users')
def showusers():
	"""This function show all the users saved in the database in the form of HTML table."""
	
	try:
		# execute the query with the cursor created in the app.py file
		cur.execute('SELECT * FROM users')
		data = cur.fetchall()

		# render the html template with the data passed to it
		return render_template('showUsers.html', users=data)

	# return error in case of any failure
	except Exception as e:
		return str(e)


@router.route('/new_user', methods=['GET', 'POST'])
def insertuser():
	"""This function insert the user when a POST request is received from the browser, else on the GET request, 
 it renders the webpage with form to be filled in order to insert the user in the database."""
	
	# if it's a post request, then execute this code block
	if request.method == 'POST':
		# get data from the input fields of the form for saving the details in database
		name = request.form['name']
		email = request.form['email']
		role = request.form['role']

		try:
			# execute the query with the cursor created in the app.py file
			cur.execute('INSERT INTO users (name, email, role) VALUES (%s, %s, %s)', (name, email, role))
			mydb.commit()

			# redirect the user to another webpage to show the details
			return redirect('/users')

		# return error in case of any failure
		except Exception as e:
			return str(e)

	# if it's a get request, then return the form filling webpage
	else:
		return render_template('insertUser.html')


@router.route('/users/<userid>')
def showuser(userid):
	"""This function fetch only one user by matching their id passed from url into database and display the user 
 in the webpage."""

	try:
		# execute the query with the cursor created in the app.py file
		cur.execute(f'SELECT * FROM users WHERE id={userid}')
		data = cur.fetchone()

		# render the html template with the data passed to it
		return render_template('showUsers.html', users=data)
	
	# return error in case of any failure
	except Exception as e:
		return str(e)
