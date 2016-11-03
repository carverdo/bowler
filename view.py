#!/usr/bin/env python
"""DOC STRING"""
from flask import Flask, render_template
app = Flask(__name__)
__author__ = 'donal'
__project__ = 'bowler'

@app.route('/')
def hello_world():
    return render_template('main_page.html')