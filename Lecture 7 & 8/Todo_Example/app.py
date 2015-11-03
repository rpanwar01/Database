from bottle import default_app, run, route
from bottle import get, put, post, request, template
from bottle import static_file

from models import *

@get('/')
@get('/list')
@get('/list/<status:int>')
def get_list(status=-1):
    if (status >= 0):
        query = Todo.select().where(Todo.status == status).order_by(Todo.task.dsc())
    else:
        query = Todo.select().order_by(Todo.task.asc())
    result = []
    for todo in query:
        result.append((todo.id,todo.task,todo.status))
    return template('list_view', rows=result)

@get('/new') 
def get_new():
    return '''
        <p>Enter a new item...</p><br/>
        <form action="/new" method="post">
            To be done: <input name="task" type="text" />
            <input value="Save" type="submit" />
        </form>
    '''
    
@post('/new')
def post_new():
    task = request.forms.get('task', '').strip()
    todo = Todo.create(task = task, status = 1)
    return get_list()

@get('/edit/<id:int>')
def get_edit(id):
    todo = Todo.get(id=id)
    return template('edit_view', id=id, task=todo.task, status=todo.status)

@post('/edit/<id:int>')
def post_edit(id):
    task = request.forms.get('task', '').strip()
    status = request.GET.get('status','').strip()
    if status == 'open':
        status = 1
    else:
        status = 0
    todo = Todo.get(id=id)
    todo.task = task
    todo.status = status
    todo.save()
    return get_list()
        
@get('/delete/<id:int>')
def confirm_delete_item(id):
    todo = Todo.get(id=id)
    return template('delete_view', id=id, task=todo.task, status=todo.status)

@post('/delete/<id:int>')
def delete_item(id):
    todo = Todo.get(id=id)
    todo.delete_instance()
    return get_list()
              
@get('/static/<filename>')
def server_static(filename):
    print(filename)
    return static_file(filename, root='static')

if __name__ == "__main__":
    run(reloader = True, host="0.0.0.0")
else:
    application = default_app()