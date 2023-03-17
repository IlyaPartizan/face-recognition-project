from preset import dbname, picturesfolder
import sqlite3, datetime
from PIL import Image

def get_user(user_id):
    if user_id:
        con = sqlite3.connect(dbname)
        cur = con.cursor()
        cur.execute("SELECT * from people WHERE id = ?", (str(user_id),))
        result = cur.fetchone()
        con.close()
        return result
    else:
        return None

def get_users():
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("SELECT * from people")
    result = cur.fetchall()
    con.close()
    return result

def delete_event(event_id):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("DELETE FROM events WHERE id = ?", (str(event_id),))
    con.commit()
    con.close()

def get_events():
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("SELECT * from events")
    result = cur.fetchall()
    con.close()
    return result

def get_event(event_id=None, user_id=None):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    if event_id:
        cur.execute("SELECT * from events WHERE id = ?", (str(event_id),))
    elif user_id:
        cur.execute("SELECT * from events WHERE subject = ?", (str(user_id),))
    else:
        return None
    result = cur.fetchone()
    con.close()
    return result

def register_entrance(subject_id):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("INSERT INTO events(subject, entrance) VALUES(?,?)", (str(subject_id), datetime.datetime.now()))
    con.commit()
    con.close()

def register_exit(subject_id):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("UPDATE events SET exit = ? WHERE subject = ?", (datetime.datetime.now(), str(subject_id)))
    con.commit()
    con.close()

def register_unknown():
    current = get_stat()['unknown']
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("UPDATE stat SET amount = ? WHERE type = ?", (current+1, 'unknown'))
    con.commit()
    con.close()

def reset_unknown():
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("UPDATE stat SET amount = ? WHERE type = ?", (0, 'unknown'))
    con.commit()
    con.close()

def get_stat():
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("SELECT * from stat")
    result = cur.fetchall()
    res = {}
    for i in result:
        res[i[1]] = i[2]
    con.close()
    return res
