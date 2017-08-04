# -*- coding: utf-8 -*-
from flask import Flask

from view import gnavi_api

application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False

modules_define = [gnavi_api.app]
for app in modules_define:
    application.register_blueprint(app)

if __name__ == "__main__":
    application.debug = True
    application.run()
