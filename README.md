# Simple-Flask-and-MySQL-Application
This is the simple Python Flask application, it uses MySQL, as database, and perform various operations on database, on various routes.

To run the application in your system the steps are divided into two parts:
- First part mentions the database setup and editing the _app.py_ accordingly.
- Second part mentions the actual application execution.

## First Part - Setting up the Database
1. This application works with the MySQL database, it is required to download and setup the MySQL database in your system.
2. In _routes.py_ in **routers directory**, at line 8, edit following parameter with your MySQL details, without the angular brackets, in string format:<br/>_host=<'YOUR MySQL HOST NAME'>_<br/>_user=<'YOUR MySQL USERNAME'>_<br/>_password=<'YOUR MySQL PASSWORD>_. <br/>
> **DO NOT CHANGE database='users'**
3. Save the file changes.
4. Now, run command ```python3 db_create.py``` in the terminal of the root directory of the project.
5. This would display the result - **10 rows, Sample Data added to database successfully!**, and your database is ready with table and 10 sample entries.
   On error it would print the error caused while creating the database, or table or inserting entries.
users database have a users table with four fields, they are as follows with their dataype and constraints:<br/>**id** _: integer type, primary key and auto_increment_<br/>**name** _: varchar (string) type, not null_<br/>**email** _: varchar type, not null_<br/>**role** _: varchar type, not null_
<br/>

## Second Part - Running the Flask Application

1. Clone or Download the project in your system-
   * For clone using the GitHub Command Line Interface, execute the command -> ```gh repo clone mr-mudgal/Simple-Flask-and-MySQL-Application``` in the GitHub CLI terminal.
   * For clone using the URL, execute the command -> ```git clone https://github.com/mr-mudgal/Simple-Flask-and-MySQL-Application.git``` in the native terminal.
   * For Download, click the green code button above and select option Download zip, to begin your download, once it is finished unzip the zip file.
2. Open the terminal in the root directory of the project & execute the command -> ```pip install -r requirements.txt``` , to download all the required modules (dependencies) for the project.
    > If pip not install, install pip using command<br/>-> for linux: ```sudo apt install python3-pip```
<br/>-> for windows: ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```<br/>then run command -> ```python get-pip.py```
    If you face and path error in windows or linux, make sure to add pip to system enviornment variable.
3. Now to run your Flask application, execute the command -> ```flask run``` or ```python3 app.py```
    This would start the server in non-debug mode, to run in the debug mode, un-comment the line number 20 in the app.py and comment the line number 21.
4. Open a new tab in the browser and paste http://127.0.0.1:5000/hello in the url section above.
   This would give you a white screen, showing "Hello, World!" in the corner.
5. Replace ['/hello'](http://127.0.0.1:5000/hello) with ['/users'](http://127.0.0.1:5000/users) in the url, this would give you the list of users, in the HTML table format, with their _ID, NAME, EMAIL_ & _ROLE_.
6. Add ['/id'](http://127.0.0.1:5000/users/id) after ['/users'](http://127.0.0.1:5000/users) in the url, where _id_ = any user _ID_ displayed in the above url webpage, this would give you the details of that specific user only.
7. Replace ['/users'](http://127.0.0.1:5000/users) or ['/users/id'](http://127.0.0.1:5000/users/id) with ['/new_user'](http://127.0.0.1:5000/new_user) in the url, this would display a HTML Form to enter user's _NAME, EMAIL_ & _ROLE_ in the form and click the submit button.
   On submitting the form, it would redirect you to the ['/users'](http://127.0.0.1:5000/users) url, where you could see the newly added user in the bottom, with their ID.
8. On any wrong url (like: http://127.0.0.1:5000/asdhfjkads), it would take you to the webpage, showing **'Page Not Found'** and a button which would redirect you to the homepage of the application, ['/hello'](http://127.0.0.1:5000/hello).
9. On any database operation error, it would display the error in the browser.

## Snippets from the Running Application
Home Page!
<img width="1352" src="https://github.com/user-attachments/assets/7ef6f0ce-530c-4602-b0f0-f9bb8cf3d125" />

All Users Page!
<img width="1352" src="https://github.com/user-attachments/assets/2b7141a1-f58a-4aea-9904-83b82b9341f0" />

One User Details Page!
<img width="1352" src="https://github.com/user-attachments/assets/92b00572-f06c-4969-989a-aac7dc3e2f9b" />

404 Error Page!
<img width="1352" src="https://github.com/user-attachments/assets/235e76a4-616b-49d0-ab83-bdc610992699" />


## How to contribute
1. To contribute in the project, first raise an issue describing why you want to contribute to the project or get a pull request or want to fork the project. 
2. On approval you need to first FORK the project, and then create new branch and start contributing what you wanted.
3. After you are done (with atleast one, functionable, upgraded feature/functionality solved), create a pull request to the main branch of the project.
4. After success full review and everything good, your contribution would be merged into the main branch, mentioning you for the contribution.
<br/>

### THANK YOU !

### [```@mr-mudgal```](https://github.com/mr-mudgal)
