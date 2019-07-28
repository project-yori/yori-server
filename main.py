# Copyright 2018 Google LLC
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

import datetime
import logging
import os
import json

from flask import Flask
import sqlalchemy

app = Flask(__name__)

logger = logging.getLogger()

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        db = sqlalchemy.create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
    else:
        db = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername='mysql+pymysql',
                host="127.0.0.1",
                username=db_user,
                password=db_pass,
                database=db_name
            )
        )
    return db

@app.route('/photo', methods=['GET'])
def index():
    db = connect_to_cloudsql()
    result = db.execute("select * from photos")
    return json.dumps([dict(data) for data in result])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)