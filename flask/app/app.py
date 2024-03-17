from flask import Flask

import uuid
import os
import re


app = Flask(__name__)

# @app.after_request
# def add_hostname_header(response):
#     env_host = str(os.environ.get('HOSTNAME'))
#     hostname = re.findall('[a-z]{3}-\d$', env_host)
#     if hostname:
#             response.headers["SP-LOCATION"] = hostname
#     return response

@app.route('/')
def get_uuid():
    return str(uuid.uuid4())
	

	