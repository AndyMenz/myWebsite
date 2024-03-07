from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField


class loginForm(FlaskForm):
    username=StringField('Username')
    password=PasswordField('Password')

class registerForm(FlaskForm):
    lastname=StringField('Last Name')
    othernames=StringField('Other Names')
    email=StringField("Email")
    password=PasswordField('Password')

class shopForm(FlaskForm):
    item =SelectField('Select Item', choices=[(1,'Tshirt'),(2,'Jeans'),(3,'Shoes')])
    brand=SelectField('Select Brand', choices=[(1, 'Nike'),(2,'Addidas'),(3,'Puma'),(4,'NewBalance')])
    size=StringField("Size")