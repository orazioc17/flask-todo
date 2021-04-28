from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from flask_login import login_required, current_user

from app import create_app
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from app.firestore_service import delete_todo, update_todo, get_todos, put_todo


app = create_app()


to_dos = ['Comprar cafe', 'Hacer solicitud de compra', 'Estudiar platzi ctm']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    flash('Nombre de usuario registrado con exito')

    return response


#Las rutas  en flask por defecto solo aceptan get, por lo que si queremos POST debemos agregarlo
@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()

    context = {
        'user_ip':user_ip,
        'to_dos':get_todos(user_id=username),
        'username':username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form,
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)

        flash('Tu tarea se creo con exito!')

        return redirect(url_for('hello'))

    return render_template('hello.html', **context)


#Esto son rutas dinamicas  en Flask
@app.route('/todos/delete/<todo_id>', methods=['GET', 'POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))


@app.route('/todos/update/<todo_id>/<int:done>', methods=['GET','POST'])
def update(todo_id, done):
    user_id = current_user.id

    update_todo(user_id=user_id, todo_id=todo_id, done=done)

    return redirect(url_for('hello'))