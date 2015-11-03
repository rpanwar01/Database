from peewee import *

database = SqliteDatabase('Chinook_Sqlite.sqlite', **{})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Artist(BaseModel):
    artistid = PrimaryKeyField(db_column='ArtistId')
    name = UnknownField(db_column='Name', null=True)  # NVARCHAR(120)

    class Meta:
        db_table = 'Artist'

class Album(BaseModel):
    albumid = PrimaryKeyField(db_column='AlbumId')
    artistid = ForeignKeyField(db_column='ArtistId', rel_model=Artist, to_field='artistid')
    title = UnknownField(db_column='Title')  # NVARCHAR(160)

    class Meta:
        db_table = 'Album'

class Employee(BaseModel):
    address = UnknownField(db_column='Address', null=True)  # NVARCHAR(70)
    birthdate = DateTimeField(db_column='BirthDate', null=True)
    city = UnknownField(db_column='City', null=True)  # NVARCHAR(40)
    country = UnknownField(db_column='Country', null=True)  # NVARCHAR(40)
    email = UnknownField(db_column='Email', null=True)  # NVARCHAR(60)
    employeeid = PrimaryKeyField(db_column='EmployeeId')
    fax = UnknownField(db_column='Fax', null=True)  # NVARCHAR(24)
    firstname = UnknownField(db_column='FirstName')  # NVARCHAR(20)
    hiredate = DateTimeField(db_column='HireDate', null=True)
    lastname = UnknownField(db_column='LastName')  # NVARCHAR(20)
    phone = UnknownField(db_column='Phone', null=True)  # NVARCHAR(24)
    postalcode = UnknownField(db_column='PostalCode', null=True)  # NVARCHAR(10)
    reportsto = ForeignKeyField(db_column='ReportsTo', null=True, rel_model='self', to_field='employeeid')
    state = UnknownField(db_column='State', null=True)  # NVARCHAR(40)
    title = UnknownField(db_column='Title', null=True)  # NVARCHAR(30)

    class Meta:
        db_table = 'Employee'

class Customer(BaseModel):
    address = UnknownField(db_column='Address', null=True)  # NVARCHAR(70)
    city = UnknownField(db_column='City', null=True)  # NVARCHAR(40)
    company = UnknownField(db_column='Company', null=True)  # NVARCHAR(80)
    country = UnknownField(db_column='Country', null=True)  # NVARCHAR(40)
    customerid = PrimaryKeyField(db_column='CustomerId')
    email = UnknownField(db_column='Email')  # NVARCHAR(60)
    fax = UnknownField(db_column='Fax', null=True)  # NVARCHAR(24)
    firstname = UnknownField(db_column='FirstName')  # NVARCHAR(40)
    lastname = UnknownField(db_column='LastName')  # NVARCHAR(20)
    phone = UnknownField(db_column='Phone', null=True)  # NVARCHAR(24)
    postalcode = UnknownField(db_column='PostalCode', null=True)  # NVARCHAR(10)
    state = UnknownField(db_column='State', null=True)  # NVARCHAR(40)
    supportrepid = ForeignKeyField(db_column='SupportRepId', null=True, rel_model=Employee, to_field='employeeid')

    class Meta:
        db_table = 'Customer'

class Genre(BaseModel):
    genreid = PrimaryKeyField(db_column='GenreId')
    name = UnknownField(db_column='Name', null=True)  # NVARCHAR(120)

    class Meta:
        db_table = 'Genre'

class Invoice(BaseModel):
    billingaddress = UnknownField(db_column='BillingAddress', null=True)  # NVARCHAR(70)
    billingcity = UnknownField(db_column='BillingCity', null=True)  # NVARCHAR(40)
    billingcountry = UnknownField(db_column='BillingCountry', null=True)  # NVARCHAR(40)
    billingpostalcode = UnknownField(db_column='BillingPostalCode', null=True)  # NVARCHAR(10)
    billingstate = UnknownField(db_column='BillingState', null=True)  # NVARCHAR(40)
    customerid = ForeignKeyField(db_column='CustomerId', rel_model=Customer, to_field='customerid')
    invoicedate = DateTimeField(db_column='InvoiceDate')
    invoiceid = PrimaryKeyField(db_column='InvoiceId')
    total = UnknownField(db_column='Total')  # NUMERIC(10,2)

    class Meta:
        db_table = 'Invoice'

class Mediatype(BaseModel):
    mediatypeid = PrimaryKeyField(db_column='MediaTypeId')
    name = UnknownField(db_column='Name', null=True)  # NVARCHAR(120)

    class Meta:
        db_table = 'MediaType'

class Track(BaseModel):
    albumid = ForeignKeyField(db_column='AlbumId', null=True, rel_model=Album, to_field='albumid')
    bytes = IntegerField(db_column='Bytes', null=True)
    composer = UnknownField(db_column='Composer', null=True)  # NVARCHAR(220)
    genreid = ForeignKeyField(db_column='GenreId', null=True, rel_model=Genre, to_field='genreid')
    mediatypeid = ForeignKeyField(db_column='MediaTypeId', rel_model=Mediatype, to_field='mediatypeid')
    milliseconds = IntegerField(db_column='Milliseconds')
    name = UnknownField(db_column='Name')  # NVARCHAR(200)
    trackid = PrimaryKeyField(db_column='TrackId')
    unitprice = UnknownField(db_column='UnitPrice')  # NUMERIC(10,2)

    class Meta:
        db_table = 'Track'

class Invoiceline(BaseModel):
    invoiceid = ForeignKeyField(db_column='InvoiceId', rel_model=Invoice, to_field='invoiceid')
    invoicelineid = PrimaryKeyField(db_column='InvoiceLineId')
    quantity = IntegerField(db_column='Quantity')
    trackid = ForeignKeyField(db_column='TrackId', rel_model=Track, to_field='trackid')
    unitprice = UnknownField(db_column='UnitPrice')  # NUMERIC(10,2)

    class Meta:
        db_table = 'InvoiceLine'

class Playlist(BaseModel):
    name = UnknownField(db_column='Name', null=True)  # NVARCHAR(120)
    playlistid = PrimaryKeyField(db_column='PlaylistId')

    class Meta:
        db_table = 'Playlist'

class Playlisttrack(BaseModel):
    playlistid = ForeignKeyField(db_column='PlaylistId', rel_model=Playlist, to_field='playlistid')
    trackid = ForeignKeyField(db_column='TrackId', rel_model=Track, to_field='trackid')

    class Meta:
        db_table = 'PlaylistTrack'
        primary_key = CompositeKey('playlistid', 'trackid')

