import pytest
from app.routes import app, db
from app.models import Todo

@pytest.fixture
def client():
    with app.app_context():
        db.drop_all()
        db.create_all()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_add_todo(client):
    response = client.post('/add', data={'title': 'Task 1'}, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        todo = Todo.query.filter_by(title='Task 1').first()
        assert todo is not None
        assert not todo.completed

def test_edit_todo(client):
    with app.app_context():
        todo = Todo(title='Old')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id
    response = client.post(f'/edit/{todo_id}', data={'title': 'New'}, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        updated = Todo.query.get(todo_id)
        assert updated.title == 'New'

def test_toggle_todo(client):
    with app.app_context():
        todo = Todo(title='Toggle')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id
    response = client.get(f'/toggle/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        toggled = Todo.query.get(todo_id)
        assert toggled.completed

def test_delete_todo(client):
    with app.app_context():
        todo = Todo(title='Delete')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id
    response = client.get(f'/delete/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        assert Todo.query.get(todo_id) is None
