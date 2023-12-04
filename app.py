from flask import Flask, jsonify, request, render_template
import os, requests
from agcut_machine import agcut_machine
from rpcm_machine import rpcm_machine
from mark_machine import mark_machine
from auto_press import auto_press
from plate_chamfer import plate_chamfer
from jd_stantion import st_weld_machine

app = Flask(__name__, static_url_path='/static')

app.register_blueprint(agcut_machine.rpcm_ag, url_prefix='/rpcag')
app.register_blueprint(rpcm_machine.rpcm_s300, url_prefix='/rpcm')
app.register_blueprint(mark_machine.mark_machine, url_prefix='/mark')
app.register_blueprint(auto_press.auto_press, url_prefix='/press')
app.register_blueprint(plate_chamfer.plate_chamfer, url_prefix='/pchamfer')
app.register_blueprint(st_weld_machine.st_weld_machine, url_prefix='/stantion') # 정동 로봇 용접 1호기(stantion)-GET방식

# Error Handler -------------------------------------------------->>
app.debug = False
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('server.log', maxBytes=1000000, backupCount=10) 
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>404 Error</h1>", 404

@app.errorhandler(500)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>Server Error</h1>", 500

# 자동 실행 ------------------------------------------------------->>
# @app.before_first_request
# def before_first_request():
#     print ("firt Run Ok --------------------------------------->>>") 

# @app.before_request
# def before_request():
#     print ("Excute Ok ----------------------------------------->>>") 

# @app.after_request
# def after_request(response):
#     print ("Response Ok --------------------------------------->>>")
#     return response

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8282", debug=True)

