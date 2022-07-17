# --*-- Encoding: UTF-8 --*--
#! filename: routes.py
# * 2651688427@qq.com

from flask import request
from apps import app

@app.route("/")
def index():
  return app.send_static_file("html/index.html")
