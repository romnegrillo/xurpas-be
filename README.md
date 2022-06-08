# Xurpas Backend Test

## Setting up the environment:
- Install Python 3.8 or later here: https://www.python.org/.
- Install pip. Follow this guide: https://pip.pypa.io/en/stable/installation/ 
- Install virtualenv to separate project dependencies by the command:
```
pip install virtualenv
```
- Clone this repository and cd to its root directory.
- Create a virtual environment, you can name it anything, example `django_env` by running 
the command :
```
virtualenv django_env
````
- Activate the virtual environment by the command (this is assuming you use Windows):
```
django_env/Scripts/activate
```
- Install the modules that this project uses by running the command:
```
pip install -r requirements.txt
```

#

## Running the server:
- To start running the server, simply run the command:
```
python manage.py runserver
```
- It will have an output the the server is currently running at `localhost:8000`.
- Open the browser and navigate to `localhost:8000/users/all/` and you should see an interface that says you are not authenticated to that endpoint. This means the server is working.
- To stop the server just press `Ctrl + C`.
#

## Endpoint list:
- List all users (GET): `localhost:8000/users/all/`
- Create user (POST): `localhost:8000/users/create/`
- Read user (GET): `localhost:8000/users/<int:id>/`
- Update user (PUT or PATCH): `localhost:8000/users/update/<int:id>/`
- Delete user (DELETE): `localhost:8000/users/delete/<int:id>/`
- Delete multiple users (POST): `localhost:8000/users/delete/multiple/`

#

## Testing using the graphical built in Django API interface:
- Django has built-in  graphical interface for testing the API just like Postman.
- You first need to be authenticated by navigating to
`localhost:8000/admin` and enter the username and password. 
- Username: romnegrillo
- Password: xurpas
- Then you can visit the endpoints in the browser directly to test.

![Endpoint UI Test](/sample_outputs/endpoint_ui_test.png)

#

## Testing using Python scripts:
- I've created one script per each endpoint in `py_client` folder, you just need to run it using the command 
```
python <script_name>.py
```
- Each requires to obtain an authentication token using the same username and password.

Script names:
- list_user.py
- create_user.py
- read_user.py
- update_user.py
- delete_user.py
- delete_multiple_user.py

![Endpoint Script Test](/sample_outputs/endpoint_script_test.png)

#

## Seeding the database models:
- You can populate the database by using the command:
```
python manage.py seed --number 10
```
The command above will populate the database with 10 records with random data that corresponds to each defined datatype.

#

## Changing between MySQL and SQLite3:
- I coded it initially on sqlite3 since it's built-in in Django.
- But I've setup MySQL as well as per the requirements, you just need to change the variable `DATABASE` in `settings.py` between the two versions included there then;
- You need to import the schema I've exported. It is named `xurpas_mysql_dump` in the root folder of this repository. The schema name for import should be `xurpas`.

![SQL Notes](/sample_outputs/sql_notes.png)











