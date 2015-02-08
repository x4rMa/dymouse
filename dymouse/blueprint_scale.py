from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, jsonify

"""
Dymo USB Scale
Flask blueprint

This file defines a Flask blueprint,
which is a URL prefix for the 
REST API.
"""

app = Flask(__name__)
#blueprint_scale = Blueprint('scale',__name__,template_folder='templates')
#app.register_blueprint(blueprint_scale,url_prefix='/scale')

