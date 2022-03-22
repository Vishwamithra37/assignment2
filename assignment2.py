import flask
import platform
import time
import pymongo as pym

app = flask.Flask(__name__)
dbcon=pym.MongoClient("mongodb://devC:27017",serverSelectionTimeoutMS=3000)
db=dbcon["assignment2"]
dac=db["counting_incoming_requests"]

@app.route('/')
def index():

    host = flask.request.host
    hostname = platform.platform()
    Time=time.strftime("%H:%M:%S")
    dac.insert_one({"host":host,"hostname":hostname,"time":Time})
    totalcount=dac.count_documents({})
    return "Serving from"+"<br/>"+"Host: "+host+"<br/>"+"Hostname: "+hostname+"<br/>"+"Time: "+Time+"<br/>"+"Total Requests: "+str(totalcount)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
