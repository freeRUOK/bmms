# --*-- Encoding: UTF-8 --*--
#! filename: __init__.py
# * 2651688427@qq.com

from flask import Flask
from datetime import timedelta
import os

app = Flask("__name__")
app.config["SECRET_KEY"] = os.urandom(24)
#app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta()

from apps import routes
