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
  line = request.form.get('data')
  write_file(line)
  return f"Add line '{line}' to file."


if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5050, debug=True) 