#! /usr/bin/env python3.6
import os
import time
from torf import Torrent
from flask import Flask, redirect, request, render_template, session, render_template_string
import subprocess
# This is your test secret API key.
app = Flask(__name__)
app.secret_key = 'tacocatlol12312121'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/download', methods=['GET', "POST"])
def download():
    session["name"] = request.form['name']
    msg = session.get("name")
    cmd = 'qobuz-dl lucky %s -n 1 --type artist -q 27 --albums-only --no-db -d H:\MusicTest' % msg
    print(cmd)
    #os.system(cmd)
    dlpath = '.\MusicTest\%s' % msg
    print(dlpath)
    t = Torrent(path=dlpath,
                trackers=['https://omega.merserver.com/announce/65e586b6bc51303e49865f7e087c48a9'],
                comment=msg)
    t.private = True
    t.generate()
    t.write('%s\%s.torrent' % (dlpath, msg))
    return render_template("download.html", name=msg)

if __name__ == '__main__':
    app.run(port=4242)