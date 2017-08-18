# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import jsonify
from flask import json
from flask import Response
from flask import request
from models.gnavi import Gnavi

app = Blueprint("api_gnavi", __name__, url_prefix="/api/gnavi")

@app.route("/category_small_search")
def gnavi_category_small_search():
    req_args = request.args.to_dict()
    gn_result = Gnavi().category_small_search(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

@app.route("/category_large_search")
def gnavi_category_large_search():
    req_args = request.args.to_dict()
    gn_result = Gnavi().category_large_search(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

@app.route("/garea_small_search")
def gnavi_garea_small_search():
    req_args = request.args.to_dict()
    gn_result = Gnavi().garea_small_search(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

@app.route("/garea_middle_search")
def gnavi_garea_middel_search():
    req_args = request.args.to_dict()
    gn_result = Gnavi().garea_middle_search(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

@app.route("/garea_large_search")
def gnavi_garea_large_search():
    req_args = request.args.to_dict()
    gn_result = Gnavi().garea_large_search(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

@app.route("/pref_search")
def gnavi_pref_search():
    req_args = request.args.to_dict()
    gn_result = Gnavi().pref_search(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

@app.route("/area_search")
def gnavi_area_search():
    req_args = request.args.to_dict()
    gn_result = Gnavi().area_search(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

@app.route("/search_rest")
def gnavi_search_rest():
    req_args = request.args.to_dict()
    gn_result = Gnavi().search_rest(**req_args)
    res = __get_response(jsonify(result=gn_result))
    return res

def __get_response(data):
    resp = Response(response=data.get_data(as_text=True),
                    status=200,
                    mimetype="application/json; charset=utf-8")
    return resp
