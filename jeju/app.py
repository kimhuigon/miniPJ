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

        # 글 목록 전체 리스트
        all_list = list(db.post.find({}, {'_id': False}))
        return render_template('list.html', user_info=user_info, all_list=all_list)

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

@app.route("/write")
def write():
    # 글 등록페이지로 이동
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        return render_template('write.html', user_info=user_info)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))



@app.route('/add', methods=['POST'])
def add_post():
    # 글 등록
    category_receive = request.form['category_give']
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    # 사진 업로드
    file = request.files["file_give"]
    # 파일이름
    filename = file.filename.split('.')[0]
    # 확장자
    extension = file.filename.split('.')[-1]
    # 사진 저장경로
    save_to = f'static/img/{filename}.{extension}'
    file.save(save_to)
    
    # 날짜
    today = datetime.now()
    date = today.strftime('%Y.%m.%d')
    
    # 글 id값 생성
    post_list = list(db.post.find({}, {'_id': False}))
    count = len(post_list) + 1

    doc = {
        'id': count,
        'category': category_receive,
        'title': title_receive,
        'content': content_receive,
        'file': f'{filename}.{extension}',
        'date': f'{date}'
    }

    db.post.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/detail/id")
def detail_post():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        # 상세화면
        id_give = request.args.get("id_give")
        post = db.post.find_one({'id': int(id_give)})
        print(post)
        return render_template('detail.html', user_info=user_info, post=post)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route("/edit/id")
def edit_post():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        # 글 수정 / 1. 기존에 등록한 데이터를 가져온다.
        id_give = request.args.get("id_give")
        post = db.post.find_one({'id': int(id_give)})
        return render_template('edit.html', user_info=user_info, post=post)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route("/update/id", methods=['POST'])
def update_post():
    # 글 수정 / 2. 수정된 내용을 업데이트한다.
    # 글번호(id)값을 받아와서 해당되는 내용을 변경한다.
    id_give = request.form['id_give']
    category_give = request.form['category_give']
    title_give = request.form['title_give']
    content_give = request.form['content_give']

    # 사진 업로드
    file = request.files["file_give"]
    # 파일 이름
    filename = file.filename.split('.')[0]
    # 확장자
    extension = file.filename.split('.')[-1]
    # 저장경로
    save_to = f'static/img/{filename}.{extension}'
    file.save(save_to)

    # 날짜
    today = datetime.now()
    date = today.strftime('%Y.%m.%d')

    # "/add"와 동일한 방법으로 업데이트 (단, 글번호(id)는 고유값이기 때문에 변경X )
    db.post.update_one({'id': int(id_give)},
                               {'$set': {'category': category_give,
                                         'title': title_give,
                                         'content': content_give,
                                         'file': f'{filename}.{extension}',
                                         'date': f'{date}'}
                                })
    return jsonify({'msg': '수정 완료!'})

@app.route("/delete/id", methods=['POST'])
def delete_post():
    # 글 삭제
    id_give = request.form['id_give']
    db.post.delete_one({'id': int(id_give)})
    print(id_give)
    return jsonify({'msg': '삭제 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
