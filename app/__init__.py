from flask import Flask, render_template, request
import os
from os.path import basename


dir_path = os.path.dirname(os.path.realpath(__file__))
parentdir = dir_path = os.path.dirname(os.path.realpath(dir_path))

print('PARENTDIR: {}'.format(parentdir))

app = Flask('asdd', template_folder=parentdir+"/templates",
static_folder=parentdir+"/static",
static_url_path=parentdir+"/static")

from app import routes