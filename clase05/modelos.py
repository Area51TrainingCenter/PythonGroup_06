from pony.orm import *

db = Database()


class Ingrediente(db.Entity):
    nombre = Required(str)


db.bind('sqlite', 'db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


