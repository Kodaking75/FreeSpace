from flask import Flask,redirect,render_template,request,session,url_for
import random
import string
import sqlite3
from pathlib import Path
from datetime import datetime,timedelta
import json
app = Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime = timedelta(days=30)
class store:
    appname = "Free Space"
def databases():
    conn = sqlite3.connect("DBASE.db")
    cursor = conn.cursor()
    command = '''CREATE TABLE IF NOT EXISTS users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME VARCHAR(15) NOT NULL,
        USERID VARCHAR(12) NOT NULL
    );'''
    newcommand = '''CREATE TABLE IF NOT EXISTS messages(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME VARCHAR(15) NOT NULL,
            USERID VARCHAR(12) NOT NULL,
            MESSAGEID VARCHAR(10) NOT NULL,
            MESSAGE TEXT NOT NULL,
            TIME TEXT NOT NULL,
            LIKES INTERGER NOT NULL
        );'''
    cursor.execute(command)
    cursor.execute(newcommand)
    conn.commit()
def useridgen(length=12):
    characters = string.digits
    newuserid = "".join(random.choice(characters) for i in range(length))
    return newuserid
def messageid(length=10):
    characters = string.digits+string.ascii_letters
    newmessage = "".join(random.choice(characters) for i in range(length))
    return newmessage
def daten():
    now = datetime.now()
    hours = now.hour
    minutes = now.minute
    return f'{hours}:{minutes}'
@app.route("/",methods=["POST","GET"])
def start():
    databases()
    if request.method == "POST":
        newuser = request.form['user']
        session["user"] = newuser
        session["userid"] = useridgen()
        ##
        newconn = sqlite3.connect("DBASE.db")
        newcursor = newconn.cursor()
        newuserd = '''INSERT INTO users(USERNAME,USERID) VALUES(?,?)'''
        addnewuser = [
            (f'{newuser}',f'{useridgen()}')
        ]
        newcursor.executemany(newuserd,addnewuser)
        newconn.commit()
        return redirect(url_for("home"))
    else:
        if "user" in session and "userid" in session:
            return redirect(url_for("home"))
        else:
            return render_template("index.html",app=store.appname)

@app.route("/home",methods=["POST","GET"])
def home():
    if "user" in session and "userid" in session:
        user = session["user"]
        userid = session["userid"]
        if request.method == "POST":
            newmsg = request.form['message']
            msgconn = sqlite3.connect("DBASE.db")
            msgcursor = msgconn.cursor()
            newmessagesend = '''INSERT INTO messages(USERNAME,USERID,MESSAGEID,MESSAGE,TIME,LIKES) VALUES(?,?,?,?,?,?)'''
            senddata = [
                (f'{user}',f'{userid}',f'{messageid()}',f'{newmsg}',f'{daten()}',f'{0}')
            ]
            msgcursor.executemany(newmessagesend,senddata)
            msgconn.commit()
            fetchconn = sqlite3.connect('DBASE.db')
            newcursor = fetchconn.cursor()
            nfetchall = '''SELECT * FROM messages'''
            newcursor.execute(nfetchall)
            rows = newcursor.fetchall()
            data = []
            for row in rows:
                data.append(
                    {
                        'ID' : row[0],
                        'USERNAME' : row[1],
                        'USERID' : row[2],
                        'MESSAGEID' : row[3],
                        'MESSAGE' : row[4],
                        'TIME' : row[5],
                        'LIKES' : row[6]
                    }
                    )
            Path("static/js/database/all.json").write_text(f"{json.dumps(data, indent=2)}")

            session["messages"] = data

                
        return render_template("home.html",app=store.appname,newuser=user,newid=userid)
    else:
        return redirect("/")
@app.route("/media")
def media():
    if "user" in session and "userid" in session:
        return render_template("media.html",app=store.appname)
    else:
        return redirect("/")
@app.route("/close")
def close():
    session.pop("user",None)
    session.pop("userid",None)
    return redirect("/")
if __name__=='__main__':
    app.run()