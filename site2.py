from flask import Flask, render_template
import db

app = Flask(__name__)



@app.route('/')
def hello(entries=None):
    D=db.Database('db.db')
    print "hi"
    entries=D.GetOutlets()
    return render_template('hello.html', entries=entries)

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')