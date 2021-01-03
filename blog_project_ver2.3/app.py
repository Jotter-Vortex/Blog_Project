from bson import ObjectId
from flask import Flask, render_template, jsonify, request, sessions
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient                 # pymongo를 import하기
{??}                                   # 현재 시간을 가져오기 위함.
{??}

app = Flask(__name__)

{??}
client = MongoClient('mongodb://changjin:0001@13.209.47.213', 27017)        # mongoDB는 27017 포트로 돌아감
db = client.my_invent                            # 'my_invent'라는 이름의 db를 생성함
## 이메일기능을 담당하는 부분
{??}

## HTML을 주는 부분
@app.route('/')                                 # home 주소
def home():
   return {??}emplate('{??}')

@app.route('/{??}')                                 # home 주소
def getmemo_main():
   return {??}late('{??}')

@app.route('{??}                            # about 주소
def about():
{??}
@app.route({??}
   return {??}ender_template('totem.html')

@app.route('/board')                                 # board 주소
def board():{??}
### GET 요청으로 클라이언트에 값을 보내겠다.
@app.route('/board/writing_page/write', methods=['GET'])
def show_board():
    writings = {??}s=['POST'])
def board_delete():
    # 1. 클라이언트로부터 데이터를 받기
    wid = request.form['index_give']
    # 2. DB에 {??}ss'})
    #, 'msg':'POST 연결되었습니다!'})

@app.route('/board/writing_page/write', methods=['POST'])                                 # writing 주소
def board_write():
    title_r{??}]

    extension = file.filename.split('.')[-1]

    #### 시간을 나누는 방법.
    toda{??}
    return jsonify({'msg': '저장 완료!'})


## API 역할을 하는 부분 (서버)
@app.route('/login', methods=['POST'])
def login():
    # 1. 클라이언트로부터 데이터를 받기
    id = request.form['ID'] # 클라이언트로부터 title을 받을 부분
    pw = re{??}form['content_give'] # 클라이언트로부터 content를 받을 부분
    # 2. mongoDB에 데이터 넣기'
    nowtime = str(datetime.now())           # 현재 시간을 가져옵니다. 최초 메모를 쓸때 사용됩니다.
    nowtime = nowtime.split('.')
    db.notepad.insert_one({'title' : title_receive, 'content' : content_receive, 'time' : nowtime[0]})
    return jsonify({'result': 'success'})
    #, 'msg':'POST 연결되었습니다!'})

@app.route('/memo', methods=['GET'])
def init_notepad():      # 처음 새로고침시에 DB에 있는 값을 모두 가져와서 cards를 만드는 함수
    # DB에서 모든 데이터 조회해오기(Read)
    result = list(db.notepad.find({}))
    for i in range(len(result)):
        result[i]['_id'] = str(result[i]['_id'])       # DB에서 받아온 _id 값은 type이 ObjectId이기 때문에 형변환
                                                        # 을 해줘야 json형식으로 클라이언트에게 보낼 수 있다.
    print(result)
    # notepads라는 키 값으로 result 정보 보내주기
    return jsoni{??}
def fetch_notepad():
    # 1. 클라이언트로부터 데이터를 받기
    index_receive = request.form['index_receive'] # 클라이언트로부터 index 받을 부분
    # 2. DB에서 데이터를 조회하기요
    # _id 값을 검색하고 싶을때는 string으로는 검색할 수 없음. 따라서 ObjectId라는 함수를 이용해야함
    tclist = list({??} Obj{??}e)}))
    tclist[0]['_id'] = str(tclist[0]['_id'])        # _id는 type이 string이 아니라 ObjectId. 형변환 필요함
    print(tclist[0])
    return jsonify({'result': 'success', 'notepads' : tclist})
    #, 'msg':'POST 연결되었습니다!'})

## API 역할을 하는 부분 (서버)
@app.route('/rewrite', methods=['POST'])
def post_notepad():
    # 1. 클라이언트로부터 데이터를 받기
    index{??}orm['content_ne{??}
    # 2. DB에 데이터를 찾기
    db.{??{??}'})


if __name__ == '__main__':
   app.r{??}