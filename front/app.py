from flask import Flask, render_template, request, Blueprint
import json
import urllib

endpoint = 'http://34.22.70.234:8080/pastebin/api'

app = Flask(__name__)

bp = Blueprint('mybp', __name__, 
               static_folder='static',
               static_url_path='/pastebin/static',
               template_folder='templates',
               url_prefix='/pastebin')

@bp.route('/', methods=['GET'])
@bp.route("/index.html", methods=['GET'])
def get_index():
    print("start getindex")
    count_users = 0
    url = f'{endpoint}/users/'
    data = None
    headers = {'Accept': 'application/json'}
    method = 'GET'
    req = urllib.request.Request(url=url,
                                 data=data,
                                 headers=headers,
                                 method=method)
    with urllib.request.urlopen(req) as f:
        data = json.loads(f.read())
        count_users = len(data)

    count_pastes = 0
    url = f'{endpoint}/pastes/'
    data = None
    headers = {'Accept': 'application/json'}
    method = 'GET'
    req = urllib.request.Request(url=url,
                                 data=data,
                                 headers=headers,
                                 method=method)
    with urllib.request.urlopen(req) as f:
        data = json.loads(f.read())
        count_pastes = len(data)

    return render_template('index.html', 
                           count_users=count_users,
                           count_pastes=count_pastes)

@bp.route('/createuser', methods=['GET'])
@bp.route('/createuser', methods=['POST'])
def create_user():
    if request.method == 'POST':
       url = f'{endpoint}/users/'
       data = {'username' : request.form['username'],
               'password' : request.form['password']}
       data = json.dumps(data).encode("utf-8")
       headers = {'Accept': 'application/json',
                  'Content-Type': 'application/json'}
       method = 'POST'

       req = urllib.request.Request(url=url,
                                    data=data,
                                    headers=headers,
                                    method=method)
       
       with urllib.request.urlopen(req) as f:
           data = json.loads(f.read())
           username = data['username']
           user_key = data['id']
           user_pastes = data['pastes']

           return render_template('create_user.html',username=username)
    else:
        return render_template('create_user.html')


@bp.route('/createpaste', methods=['GET'])
@bp.route('/createpaste', methods=['POST'])
def create_paste():
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       url = f'{endpoint}/users/{username}/paste/?password={password}'
       data = {'title' : request.form['title'],
               'content' : request.form['content']}
       data = json.dumps(data).encode("utf-8")
       headers = {'Accept': 'application/json',
                  'Content-Type': 'application/json'}
       method = 'POST'

       req = urllib.request.Request(url=url,
                                    data=data,
                                    headers=headers,
                                    method=method)
       with urllib.request.urlopen(req) as f:
           data = json.loads(f.read())

           return render_template('create_paste.html',username=username)

    else:
        return render_template('create_paste.html')

@bp.route('/<username>/pastes', methods=['GET'])
def get_user_pastes(username):
    print("start get pastes for user")
    
    url = f'{endpoint}/users/{username}/pastes/?skip=0&limit=100'
    data = None
    headers = {'Accept': 'application/json'}
    method = 'GET'
    req = urllib.request.Request(url=url,
                                 data=data,
                                 headers=headers,
                                 method=method)

    with urllib.request.urlopen(req) as f:
        data = json.loads(f.read())
        count_pastes = len(data)

    return render_template('user_pastes.html',
                           username = username,
                           count_pastes=count_pastes,
                           pastes = data)

app.register_blueprint(bp)

