from flask import Flask, render_template, request
from file_proc import read_file, write_file

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Hi!"

@app.route('/home')
def getHome():
  return render_template('home.html', active_page = 'home')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = "123")


@app.route('/params')
def params():
  return request.args

@app.route('/post_req', methods = ['POST'])
def post_req():
  return request.args

@app.route('/read_file')
def read_from_file():
  file_content = read_file()
  return file_content

@app.route('/write_to_file', methods = ['POST'])
def write_to_file():
  request_type = request.content_type
  if request_type == 'application/json':
    contentJSON = request.get_json()
    write_file(contentJSON['data'])
    return f"Line {contentJSON['data']} added to file!"
  else:
    return f"Request {request_type} is not supported!"

@app.route('/file', methods = ['POST', 'GET'])
def fileWork():
  if request.method == 'GET':
    return read_from_file()
  elif request.method == 'POST':
    return write_to_file()
  else:
    return f"Request method {request.method} is not supported!"




if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5050, debug=True) 