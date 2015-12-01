import sqlite3
from bottle import route, run, template, request, get, post

@route('/todo')
@route('/todo/<status:int>')
def todo_list(status=-1):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    if (status >= 0):
        c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    else :
        c.execute("SELECT id, task, status FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    output = template('make_table', rows=result)
    return output

@get('/new')
def new_item_request():  
        return '''
        <p> Enter a new Item </p> <br/>
        <form action="/new" method="post">
            To be Done: <input name="task" type="text" />
            <input value="Save" type="submit" />
        </form>
    '''
       
@post('/new')
def new_item():

        new = request.forms.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        #return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
        return todo_list(1)

run()


