from peewee import *

database = SqliteDatabase('todo.db')

class BaseModel(Model):
    class Meta:
        database = database

class Todo(BaseModel):
    status = BooleanField()
    task = CharField()
    class Meta:
        db_table = 'todo'

#query = Todo.select()
#for todo in query:
#    print (todo.task)

#query = Todo.select().where(Todo.status)
#for todo in query:
#    print (todo.task)
    
query = Todo.select().where(Todo.status).order_by(Todo.task.asc())
for todo in query:
    print (todo.task)
