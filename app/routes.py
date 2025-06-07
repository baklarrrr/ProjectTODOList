from flask import render_template, request, redirect, url_for, abort
from . import create_app, db
from .models import Todo

app = create_app()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    if title:
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    if not todo:
        abort(404)
    title = request.form.get('title')
    if title:
        todo.title = title
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    if not todo:
        abort(404)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    if not todo:
        abort(404)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()
