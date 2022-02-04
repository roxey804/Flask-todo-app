from flask import render_template, jsonify
from app import app
from app.models import Todo
from app import db
import requests
import jsonify

@app.route("/")
def hello_world():
    return "<p>This is the welcome page of the app</p>"


@app.route("/hello")
def hello():
    return render_template('index.html')


@app.route("/api")
def get_api_docs():
    return render_template('swaggerui.html')


@app.route("/todo", methods=['POST'])
def create_todo():
    description = requests.get('description')
    priority = requests.get('priority')
    todo1 = Todo(description=description, priority=priority)
    db.session.add(todo1)
    db.session.commit()
    return "Todo created"


@app.route("/todos", methods=['GET'])
def get_all_todos():
    """Return all todos from the db"""
    todos = Todo.query.all()
    return render_template('todos.html', todos=todos)


@app.route("/todo/<int:todo_id>", methods=['GET'])
def get_individual_todo(todo_id):
    """Return individual todo from the db"""
    todo = Todo.query.filter_by(id=todo_id).first()
    return f'Todo:  {todo_id, todo.description}'
    #return render_template('todos.html', todos=todo)


#RN todo delete method not working
@app.route("/todo/delete/<int:todo_id>", methods=['DELETE'])
def delete_individual_todo(todo_id):
    """Delete the Todo item with the specified id"""
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return 'Todo deleted ' #maybe f string as above


# rntodo The below doesn't work, how can i show all info withouth using  a templete? jsonify?
#  tuple?
# The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list.
# @app.route('/all')
# def show_all():
#     all_todos = Todo.query.all()
#     return tuple(all_todos)


#----Error handler routes--------#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

def catch_500_error():
    pass