from db import DB
db = DB()
db.register_entrance(1)
db.register_exit(1)
db.register_entrance(3)
print(db.get_events())
db.commit()
