from flask import Blueprint

#El url_prefix hara que todas las rutas que empiecen con '/auth' seran redirigidas a este blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

#Se importa aqui abajo para que despues de que creemos los blueprints importemos todos los views y configuremos la app, porque ahora la app se configura desde create_app directamente y no desde main.py
from . import views