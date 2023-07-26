from flask import Blueprint, render_template, request, redirect

from app import cur, mydb

router = Blueprint('router', __name__)


@router.route('/hello')
def hello():
	return 'Hello, World!'


@router.route('/users')
def showusers():
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
	# if its a post request, then execute this code block
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

	# if its a get request, then return the form filling webpage
	else:
		return render_template('insertUser.html')


@router.route('/users/<userid>')
def showuser(userid):
	try:
		conn = mysql.connector.connect(host='localhost', user='root', password='MySQL@1', database='users')
		cur = conn.cursor()
		cur.execute(f'SELECT * FROM users WHERE id={userid}')
		data = cur.fetchone()
		conn.close()

		return render_template('showUsers.html', users=data)

	except Exception as e:
		return str(e)
