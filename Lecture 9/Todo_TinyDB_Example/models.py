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