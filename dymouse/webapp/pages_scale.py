from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_wtf import Form
import os
from blueprint_scale import app

"""
Dymo USB Scale
Pages

This file defines Flask routes
that lead to pages.
"""

@app.route('/')
def index():
    return render_template('index.html')


