# l'ORM scelto da LElio e' Peewee fa un sacco di cose e somiglia all' ORM di django
# Peewee si preoccupa del mapping delle tabelle del database
# i tipi di dato delle varie tabelle - 
# informarsi su PENTAHO

#definizione del modello -  partiamo da un DB vuoto
#
# http://docs.peewee-orm.com/en/latest/index.html


import peewee
import datetime
db = peewee.SqliteDatabase('test.db')
class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)
    class Meta:
        database = db
        db_table = 'notes'
Note.create_table(Note)
note1 = Note.create(text='Went to the cinema')
note1.save()
note2 = Note.create(text='Exercised in the morning',
        created=datetime.date(2018, 10, 20))
note2.save()
note3 = Note.create(text='Worked in the garden',
        created=datetime.date(2018, 10, 22))
note3.save()
note4 = Note.create(text='Listened to music')
note4.save()

#Note.drop_table()  # cancella la tabella
#leggere il pdf quando arrivera' per le ultime cose fatte
#da fare


