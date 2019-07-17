#!/usr/bin/env python3
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

from flask import Flask
from flask import jsonify

# test data
dummy0 = {
    "photo_group": "乃木坂46",
    "photo_member": "樋口日奈",
    "photo_costume": "2019 summer concert 1",
    "photo_type": "ヨリ",
    "photo_number": 1,
    "photo_folder": "summer concert",
    "photo_tag": []
}

dummy1 = {
    "photo_group": "乃木坂46",
    "photo_member": "樋口日奈",
    "photo_costume": "2019 summer concert 1",
    "photo_type": "チュウ",
    "photo_number": 3,
    "photo_folder": "summer concert",
    "photo_tag": []
}

dummy2 = {
    "photo_group": "乃木坂46",
    "photo_member": "樋口日奈",
    "photo_costume": "2019 summer concert 1",
    "photo_type": "ヒキ",
    "photo_number": 1,
    "photo_folder": "summer concert",
    "photo_tag": []
}

photos = [dummy0, dummy1, dummy2]

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/photos/all', methods=['GET'])
def photos_all():
    return jsonify(photos)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]

