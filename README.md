# Starter Flask Application

### Requirements

- Homebrew
- Python 3
- Virtualenv
- Virtualenvwrapper
- MySQL server

### Running Locally

Step 1. Clone this repo

`$ git clone https://github.com/jqn/microservices.git`

Step 2. Move into the project root directory

`$ cd microservices`

Step 2. Create and activate a new virtual environment

`$ mkvirtualenv microservices`

`$ workon microservices`

Step 4. Set your environment variables

`$ vi ~/.virtualenvs/microservices/bin/postactivate`

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
    databasename="microservices",
)
```

Step 7. Create a new database for this project

```
$ mysql -u root

$ mysql> CREATE DATABASE microservices;
Query OK, 1 row affected (0.00 sec)
```

Step 8. Initialze the database migration

`$ flask db init`

Step 9. Create the first migration

`$ flask db migrate`

Step 10. Apply the migration to create the guest_users table in the database

`$ flask db upgrade`

Step 11. Create an admin user.

```
$ flask shell

>>> from app.models import Employee

>>> from app import db

>>> admin = Employee(email="admin@admin.com",username="admin",password="admin2016",is_admin=True)

>>> db.session.add(admin)

>>> db.session.commit()
```

Step 12. Start the server

`$ flask run`

## Tips

If installing new dependencies add them to requirements.txt and commit them to version control

`$ pip freeze > requirements.txt`

### Externally Visible Server

`$ flask run --host=0.0.0.0`

### Features

- AWS EC2
