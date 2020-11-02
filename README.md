# Starter Flask Application

### Requirements

- Homebrew
- Python 3
- Virtualenv
- Virtualenvwrapper
- MySQL server

### Running Locally

Step 1. Clone this repo

`$ git clone https://github.com/jqn/flask-boilerplate.git`

Step 2. Move into the project root directory

`$ cd flask_boilerplate`

Step 2. Create and activate a new virtual environment

`$ mkvirtualenv flask_boilerplate`

`$ workon flask_boilerplate`

Step 4. Set your environment variables

`$ vi ~/.virtualenvs/flask_boilerplate/bin/postactivate`

```bash
#!/bin/bash
# This hook is sourced after this virtualenv is activated.
export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py
export FLASK_DEBUG=True
```

Step 5. Install the project dependencies

`$ pip install -r requirements.txt`

Step 6. Create a new config.py in `instance/config.py` and add the following.
Please replace the placeholders with the correct values.

```
SECRET_KEY = 'yoursecretkey'

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=<username>,
    password=<password>,
    hostname="localhost",
    databasename="flask_boilerplate",
)
```

Step 7. Create a new database for this project

```
$ mysql -u root

$ mysql> CREATE DATABASE flask_boilerplate;
Query OK, 1 row affected (0.00 sec)
```

Step 8. Initialze the database migration

`$ flask db init`

Step 9. Create the first migration

`$ flask db migrate`

Step 10. Apply the migration to create the guest_users table in the database

`$ flask db upgrade`

Step 11. Start the server

`$ flask run`

Step 12. If installing new dependencies add them to requirements.txt and commit them to version control

`$ pip freeze > requirements.txt`

## Tips

### Externally Visible Server

`$ flask run --host=0.0.0.0`
