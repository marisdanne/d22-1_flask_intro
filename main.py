from flask import Flask, render_template

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

if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5050, debug=True) 