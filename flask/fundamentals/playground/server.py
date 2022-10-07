from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/play/')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<string:color>')
def index(num=3, color='green'):
    return render_template("index.html", box="", times=num, color=color)	


if __name__=="__main__":
    app.run(debug=True)