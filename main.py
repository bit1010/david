#!/usr/bin/python3

import os
from io import BytesIO
from flask import Flask, render_template
from flask import Flask, request, Response
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')

app = Flask(__name__)


@app.route("/")
def home():

    return render_template('index.html', image_file="david.jpg")


@app.route("/hello")
def hello():

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    text = '안녕하세요. 인공지능 로봇 David입니다. 무엇을 도와 드릴까요?'
    gTTS(text, "com", lang).write_to_fp(fp)

    # return Response(fp.getvalue(), mimetype='audio/mpeg')
    return render_template('audio.html', audiodata=fp.getvalue())


if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
