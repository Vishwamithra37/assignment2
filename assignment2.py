import flask
import platform

app = flask.Flask(__name__)

@app.route('/')
def index():

    host = flask.request.host
    hostname = platform.platform()
    return "Serving from"+"<br/>"+"Host: "+host+"<br/>"+"Hostname: "+hostname

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
