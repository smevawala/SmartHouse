from flask import Flask, render_template, redirect, url_for
import db

app = Flask(__name__)


@app.route('/')
def smartapp():
    D = db.Database('db.db')
    print "Database connected"
    entries = D.GetOutlets()
    return render_template('smartapp.html', entries=entries)


@app.route('/toggle/<rowid>/<state>')
def toggle(rowid=None, state=None):
    if state == "1":
        st = True
    else:
        st = False
    print rowid, st
    D = db.Database('db.db')
    D.UpdateState(rowid, state)
    return redirect(url_for('smartapp'))


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
