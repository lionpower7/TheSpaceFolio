from flask import Flask, render_template, request
import os
from os.path import basename

#basedir gets the current working directory (where app.py is)
basedir = os.path.abspath(os.path.dirname(file))
#parentdir gets the previous directory of the basedir
parentdir = os.path.abspath(os.path.join(basedir, os.pardir))

app = Flask(name, template_folder=parentdir+"/templates/",
static_folder=parentdir+"static",
static_url_path=parentdir+"static")

from app import routes