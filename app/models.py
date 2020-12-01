# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class VehicleVehicle(db.Model):
    __tablename__ = 'vehicle_vehicle'

    id = db.Column(db.Integer, primary_key=True)
    dealer_name = db.Column(db.String(255, 'utf8mb4_general_ci'))
    address = db.Column(db.String(255, 'utf8mb4_general_ci'))
    city = db.Column(db.String(255, 'utf8mb4_general_ci'))
    state = db.Column(db.String(255, 'utf8mb4_general_ci'))
    zip = db.Column(db.String(255, 'utf8mb4_general_ci'))
    stock_number = db.Column(db.String(255, 'utf8mb4_general_ci'))
    vin = db.Column(db.String(255, 'utf8mb4_general_ci'),
                    nullable=False, unique=True)
    year = db.Column(db.String(4, 'utf8mb4_general_ci'))
    make = db.Column(db.String(255, 'utf8mb4_general_ci'))
    model = db.Column(db.String(255, 'utf8mb4_general_ci'))
    series = db.Column(db.String(255, 'utf8mb4_general_ci'))
    vehicle_body = db.Column(db.String(255, 'utf8mb4_general_ci'))
    trim = db.Column(db.String(255, 'utf8mb4_general_ci'))
    new_used = db.Column(db.String(255, 'utf8mb4_general_ci'))
    cpo = db.Column(db.String(255, 'utf8mb4_general_ci'))
    photos = db.Column(db.String(collation='utf8mb4_general_ci'))
    description = db.Column(db.String(collation='utf8mb4_general_ci'))
    mileage = db.Column(db.Integer)
    engine = db.Column(db.String(255, 'utf8mb4_general_ci'))
    transmission = db.Column(db.String(255, 'utf8mb4_general_ci'))
    drive = db.Column(db.String(255, 'utf8mb4_general_ci'))
    fuel = db.Column(db.String(255, 'utf8mb4_general_ci'))
    options = db.Column(db.String(collation='utf8mb4_general_ci'))
    image_date = db.Column(db.String(255, 'utf8mb4_general_ci'))
    vehicle_type = db.Column(db.String(255, 'utf8mb4_general_ci'))
    tag_line = db.Column(db.String(255, 'utf8mb4_general_ci'))
    color_exterior = db.Column(db.String(255, 'utf8mb4_general_ci'))
    color_interior = db.Column(db.String(255, 'utf8mb4_general_ci'))
    brakes = db.Column(db.String(255, 'utf8mb4_general_ci'))
    seats = db.Column(db.String(255, 'utf8mb4_general_ci'))
    warranty = db.Column(db.String(255, 'utf8mb4_general_ci'))
    vehicle_condition = db.Column(db.String(255, 'utf8mb4_general_ci'))
    price_retail = db.Column(db.String(255, 'utf8mb4_general_ci'))
    price_internet = db.Column(db.String(255, 'utf8mb4_general_ci'))
    price_wholesale = db.Column(db.String(255, 'utf8mb4_general_ci'))
    price_book_retail = db.Column(db.String(255, 'utf8mb4_general_ci'))
    latitude = db.Column(db.Numeric(10, 8), nullable=False)
    longitude = db.Column(db.Numeric(11, 8), nullable=False)
    data_tier = db.Column(db.SmallInteger, nullable=False)
    account_id = db.Column(db.ForeignKey('employees.id'),
                           nullable=False, index=True)
    photo_count = db.Column(db.Integer, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
