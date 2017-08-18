# -*- coding: utf-8 -*-
from flask import Flask

from view import gnavi_api
from view import yahoo_map_api
from view import test

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

modules_define = [gnavi_api.app, yahoo_map_api.app, test.app, ]
for ap in modules_define:
    app.register_blueprint(ap)

if __name__ == "__main__":
    app.debug = True
    app.run()
