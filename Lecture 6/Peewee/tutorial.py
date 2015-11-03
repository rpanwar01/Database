from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()
    class Meta:
        database = db # This model uses the "people.db" database.

		
class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()
    class Meta:
        database = db # this model uses the "people.db" database		
    
db.connect
db.create_tables([Person, Pet])

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
grandma.name = 'Grandma L.'
grandma.save()  # Update grandma's name in the database.

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

herb_mittens.delete_instance()

uncle_bob = Person.create(name='Bob', birthday=date(1950, 5, 5), is_relative=False)
herb_fido.owner = uncle_bob
herb_fido.save()
bob_fido = herb_fido # rename our variable for clarity

grandma = Person.select().where(Person.name == 'Grandma L.').get()
We can also use the equivalent shorthand Model.get():

grandma = Person.get(Person.name == 'Grandma L.')

for person in Person.select():
    print(person.name, person.is_relative)

query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))
for pet in query:
    print(pet.name, pet.owner.name)

for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

for pet in Pet.select().where(Pet.owner == uncle_bob):
    print(pet.name)

for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print(pet.name)

for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)

for person in Person.select():
    print(person.name, person.pets.count(), 'pets')
    for pet in person.pets:
        print('    ', pet.name, pet.animal_type)



Finally, let’s do a complicated one. Let’s get all the people whose birthday was either:

before 1940 (grandma)
after 1959 (bob)

d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))
...

    

query = (Person
         .select()
         .where((Person.birthday > d1940) & (Person.birthday < d1960)))
for person in query:
    print(person.name, person.birthday)

expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'g')
for person in Person.select().where(expression):
    print (person.name)

db.close()