import requests

# from raspoznavanie import name_taker

# def id_taker(id):
#    return id

def register_entrance(user_id):
   return requests.post('http://127.0.0.1:5000/api/register_entrance', json={'user_id':user_id})

def register_exit(user_id):
   return requests.post('http://127.0.0.1:5000/api/register_exit', json={'user_id':user_id})

def delete_event(user_id):
   return requests.post('http://127.0.0.1:5000/api/delete_event', json={'user_id':user_id})

# uid = int(json.dumps(name_taker))
def id_taker(uid):
   with open ("zapros.txt", 'r', encoding='utf-8') as zapr:
      DB_request = zapr.read(1)
   if int(DB_request) == 1:
         resp = register_entrance(uid)
   elif int(DB_request) == 2:
         resp = register_exit(uid)
   elif int(DB_request) == 3:
         resp = delete_event(uid)


