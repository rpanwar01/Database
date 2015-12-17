from bottle import default_app, run, route
from bottle import get, put, post, request, template
from bottle import static_file

from items import *

@get('/')
def home():
    return template('home')
    
@get('/signup') # or @route('/signin')
def signup():
    return '''
        <p>sign up here...</p><br/>
        <form action="/signup" method="post">
            Username: <input name="name" type="text" />
            email_id: <input name="email" type="text" />
            password: <input name="pswd" type="text" />
            <input value="Save" type="submit" />
        </form>
    '''
    
@post('/signup')
def do_signup():
    name = request.forms.get('name')
    email = request.forms.get('email')
    pswd = request.forms.get('pswd')
    signup_data(name,email,pswd)
    return "<p>Sign up completed. Please click <a href='http://localhost:8080/login?Login=login'>here</a> to login</p>"
    
    
@get('/login') # or @route('/login')
def login():
	return '''
		<form action="/login" method="post">
			Username: <input name="username" type="text" />
			Password: <input name="password" type="password" />
			<input value="Login" type="submit" />
		</form>
	'''
    
@post('/login') # or @route('/login', method='POST')
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if check_login(username, password):
		return get_list(username, -1 )
	else:
		return "<p>Login failed. Please use the valid credentials to <a href='http://localhost:8080/login'>login</a>.</p><p>Or in case of new user, please sign up <a href='http://localhost:8080/signup?Sign+up+for+a+new+account=Signup'>here</a>.</p>"
           
@get('/list')
@get('/list/<status:int>')
def get_list(user, status=-1):
    global str1
    global str2
    str1 = ""
    str2 = ""
    global uname
    items = get_items(user, status)
    results = list(db.items.aggregate( [
    {"$match": {"name": user }},
    {"$group": {"_id": "$status", "count": {"$sum": 1}}},
    ] ))
    print("result", results )
    for result in results:
        if result["_id"] == 0:
            str1 = result["count"]
            print("Completed task :", result["count"])
        if result["_id"] == 1:
            str2 = result["count"]
            print("Not completed task :", result["count"])
            
    result = []
    uname = user
    for item in items:
        result.append((item['id'],item['task'],item['status']))
    return template('list_view', rows=result, str1=str1, str2=str2, uname=uname)

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
    new_item(task,1,uname)
    return get_list(uname)

@get('/edit/<id:re:[a-z0-9]+>')
def get_edit(id):
    item = get_item(id)
    return template('edit_view', id=id, task=item['task'], status=item['status'])

@post('/edit/<id:re:[a-z0-9]+>')
def post_edit(id):
    task = request.forms.get('task', '').strip()
    status = request.GET.get('status','').strip()
    if status == 'open':
        status = 1
    else:
        status = 0
    item = get_item(id)
    item['task'] = task
    item['status'] = status
    save_item(item)
    return get_list(uname)
        
@get('/delete/<id:re:[a-z0-9]+>')
def confirm_delete_item(id):
    item = get_item(id=id)
    return template('delete_view', id=id, task=item['task'], status=item['status'])

@post('/delete/<id:re:[a-z0-9]+>')
def delete_item(id):
    discard_item(id)
    return get_list(uname)
    
@get('/deleteall')
def confirm_delete_items():
    return template('deleteall_view')

@post('/deleteall')
def delete_items():
    discard_items(uname)
    return get_list(uname)

@get('/archived')    
def get_archived():
    items = get_arc_items(uname)
    result = []
    for item in items:
        print (item)
        result.append((item['id'],item['task']))
    return template('arc_items', rows=result)
    
@get('/archive/<id:re:[a-z0-9]+>')
def add_arc_items(id):
    item = get_arc_item(id)
    save_arc_items(item, uname)
    del_arc_items(id, uname)
    return get_list(uname)
              
@get('/static/<filename>')
def server_static(filename):
    print(filename)
    return static_file(filename, root='static')

if __name__ == "__main__":
    run(reloader = True, host="0.0.0.0")
else:
    application = default_app()