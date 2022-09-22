from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient('mongodb://3.36.123.144', 27017, username="test", password="test")
db = client.LoginJeju


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('list.html', user_info=user_info)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    email_receive = request.form['email_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,  # 아이디
        "password": password_hash,  # 비밀번호
        "email": email_receive,  # 이메일!
        "profile_name": username_receive,  # 프로필 이름 기본값은 아이디
        "profile_pic": "",  # 프로필 사진 파일 이름
        "profile_pic_real": "profile_pics/profile_placeholder.png",  # 프로필 사진 기본 이미지
        "profile_info": ""  # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

@app.route('/post', methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    contnet_receive = request.form['content_give']
    category_receive = request.form['category_give']
    file = request.files["file_give"]

    post_list = list(db.diary.find({}, {'_id': False}))
    count = len(post_list) + 1

    today = datetime.now()
    # mytime =
    date = today.strftime('%Y.%m.%d')

    filename = file.filename.split('.')[0]

    extension = file.filename.split('.')[-1]

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    post_list = list(db.post.find({}, {'_id': False}))
    count = len(post_list) + 1

    doc = {

        'id': count,
        'title': title_receive,
        'content': contnet_receive,
        'category': category_receive,
        'file': f'{filename}.{extension}',
        'date': f'{date}',
    }

    db.post.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route('/post', methods=['GET'])
def show_diary():
    posts = list(db.post.find({}, {'_id': False}))
    return jsonify({'all_post': posts})


@app.route('/post/done', methods=['POST'])
def diary_done():
    num_receive = request.form['num_give']
    db.post.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})

    return jsonify({'result': 'success', 'msg': '삭제완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
