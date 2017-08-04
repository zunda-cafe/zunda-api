# -*- coding: utf-8 -*-
from flask import Blueprint

app = Blueprint("test", __name__, url_prefix="/")

@app.route('')
def index():
	return "Hi it's working!"

