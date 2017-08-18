# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import jsonify
from flask import json
from flask import Response
from flask import request
from models.yahoo_map import YahooMap

app = Blueprint("api_yahoo_map", __name__, url_prefix="/api/yahoo_map")

@app.route("/geo_coder")
def geo_coder():
    req_args = request.args.to_dict()
    yh_result = YahooMap().geo_coder(**req_args)
    res = __get_response(jsonify(result=yh_result))
    return res

def __get_response(data):
    resp = Response(response=data.get_data(as_text=True),
                    status=200,
                    mimetype="application/json; charset=utf-8")
    return resp
