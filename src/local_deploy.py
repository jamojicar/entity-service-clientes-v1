import aws_lambda_wsgi
from flask import Flask
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy
from zpy.api.flask.cloud_handlers import aws_lambda
import os
from zpy.utils.files import add_source_to_path

current_dir = os.getcwd().replace('\\src\\', '\\src\\contexts')
add_source_to_path(current_dir)

app = Flask(__name__)
CORS(app)

from api.routes import app

with app.app_context():
    import api.routes


def handler(event, context):
    return aws_lambda_wsgi.response(app, event, context)


if __name__ == '__main__':
    app.run()