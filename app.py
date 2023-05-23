from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/", methods=['post'])
def application_submitted():
  data = request.form
  return render_template('application_submited.html', application=data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)