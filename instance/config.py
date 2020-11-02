SECRET_KEY = 'yoursecretkey'

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="root",
    hostname="localhost",
    databasename="microservices",
)
