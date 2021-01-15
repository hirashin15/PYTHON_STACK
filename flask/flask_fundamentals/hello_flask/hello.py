from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def level_1():
  return render_template('index.html', repeat=3)

@app.route('/play/<num>')
def level_2(num):
  return render_template('index.html', repeat=int(num))



if __name__=="__main__":
  app.run(debug=True)

