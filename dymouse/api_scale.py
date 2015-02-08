from flask import Flask, render_template, request, Response, redirect, url_for, jsonify, session
from blueprint_scale import app
import numpy as np
import time

"""
Dymo USB Scale
API

This file defines a REST API 
by defining Flask routes.
"""



# Contents:
# ---------------------
# * Scale API



# Scale API:
# ---------------------
# * Read [g by default]
# /scale/read/
#
# * Read in oz mode [oz]
# /scale/read/
# 
# * Read in lb mode [lb,oz]
# /scale/read/

@app.route('/read')
@app.route('/read/')
def read_mass():
    pass



