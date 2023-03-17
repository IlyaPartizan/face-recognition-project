from flask import Flask, render_template, request, make_response
from db import *
app = Flask(__name__)

users = get_users()
for i in range(len(users)):
    users[i] = (users[i][0], users[i][1], users[i][2], '/static/pictures/' + str(users[i][0]) + '.jpg')

@app.route('/')
def index():
    events = get_events()
    for i in range(len(events)):
        event = events[i]
        user = users[event[1]-1]
        event = (user[1], user[2], event[2], event[3], '/static/pictures/' + str(user[0]) + '.jpg')
        events[i]=event
    stat = get_stat()
    return render_template('index.html', events=events, stat=stat)

@app.route('/users')
def get_usrs():
    return render_template('users.html', users=users)

@app.route('/api/register_entrance', methods=['POST'])
def reg_ent():
    request_data = request.get_json()
    if "user_id" in request_data.keys():
        user_id = request_data["user_id"]
    else:
        return make_response('No user id', 204)
    usr = get_user(user_id)
    evnt = get_event(user_id=user_id)
    if evnt:
        return make_response('That event already exist', 400)
    if not(usr):
        return make_response('Wrong user id', 400)
    register_entrance(user_id)
    return 'OK'

@app.route('/api/register_exit', methods=['POST'])
def reg_exit():
    request_data = request.get_json()
    if "user_id" in request_data.keys():
        user_id = request_data["user_id"]
    else:
        return make_response('No user id', 204)
    usr = get_user(user_id)
    evnt = get_event(user_id=user_id)
    if not(evnt):
        return make_response('Wrong user id', 400)
    if not(usr):
        return make_response('Wrong user id', 400)
    if evnt[3]:
        return make_response('Already satisfied', 208)
    register_exit(user_id)
    return 'OK'

@app.route('/api/register_unknown')
def reg_un():
    register_unknown()
    return 'OK'

@app.route('/api/reset_unknown')
def res_un():
    reset_unknown()
    return 'OK'

@app.route('/api/delete_event', methods=['POST'])
def del_event():
    request_data = request.get_json()
    if "user_id" in request_data.keys():
        user_id = request_data["user_id"]
    else:
        return make_response('No user id', 204)
    event_id = request.args.get('event_id')
    result = get_event(event_id, user_id)
    if result:
        delete_event(result[0])
        return 'OK'
    else:
        return make_response('Wrong user or event id', 400)

@app.route('/api/get_events', methods=['GET'])
def get_ev():
    return get_events()

@app.route('/api/get_users', methods=['GET'])
def get_us():
    return get_users()

@app.route('/api/get_stat')
def get_un():
    return get_stat()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
