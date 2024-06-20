from flask import Flask,request
import json
from flask_cors import CORS
import pymysql
app = Flask(__name__)

CORS(app)  # 允许所有域名进行跨域请求

host = 'localhost'
user = 'root'
password = '123456'
database = 'test'

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/test',methods = ["POST"])
def test():  # put application's code here
    data = request.get_json()
    print(data)
    # 数据库
    db = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM user')
    results = cursor.fetchall()
    db.close()
    json_data = {"return_data": data['data'],"database":results}
    return json.dumps(json_data)
if __name__ == '__main__':
    app.run()
