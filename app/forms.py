from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,FileField,TextAreaField,SelectField, SubmitField
from wtforms.validators import InputRequired, Length 
from flask_wtf.file import FileField, FileRequired, FileAllowed

# Add any form classes for Flask-WTF here

""" Create a form class called MovieForm that has three (3) fields
and appropriate validation rules. A String field called 'title' for the Movie Title,
TextArea field called 'description' that requires a user to fill in a brief description
or summary of the movie and a FileField called 'poster' that only allows images of
a movie poster to be uploaded. """

class MovieForm(FlaskForm):

    title = StringField('Title', validators=[InputRequired(), Length(min=1, max=100)])
    description = TextAreaField('Description',validators=[InputRequired()] ) 
    poster = FileField('Poster', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])

