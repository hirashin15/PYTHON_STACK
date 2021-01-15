from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def createChecker():
  return render_template('index.html', width=int(8), height=int(8))

@app.route('/4')
def createChecker2():
  return render_template('index.html', width=int(8), height=int(4))

@app.route('/<width>/<height>')
def createChecker3(width, height):
  return render_template('index.html', width=int(width), height=int(height))

@app.route('/<width>/<height>/<color1>/<color2>')
def createChecker4(width, height, color1, color2):
  return render_template('index.html', width=int(width), height=int(height), color1=color1, color2=color2)

if (__name__ == "__main__"):
  app.run(debug=True)