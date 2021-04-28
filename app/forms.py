from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    #El parametro que se le pasa es la etiqueta o label
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    #wtf va a manejar esa contraseña encriptandola y demas, sin tener que preocuparnos nosotros de eso
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class TodoForm(FlaskForm):
    description = StringField('Descripcion', validators=[DataRequired()])
    submit = SubmitField('Crear')


class DeleteTodoForm(FlaskForm):
    submit_field = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit_field = SubmitField('Actualizar')
