from flask import Flask
from flask import request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost:27017')
db=client.sensor_data

print("done establishing connection!")

@app.route('/sensor',methods = ['POST', 'GET'])
def sensor():
   if request.method == 'POST':
        # print (request.is_json)
        content = request.json
        print(content)
        db.sensor_datas.insert_one(content)
        fivestar = db.sensor_datas.find()
        for i in fivestar:
            print(i)
        return "done"
   else:
        return "error"

if __name__ == "__main__":
    app.run(host= '0.0.0.0')