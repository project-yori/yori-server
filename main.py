import datetime
import logging
import os
import json

from flask import Flask
from flask_cors import CORS
import sqlalchemy

app = Flask(__name__)

logger = logging.getLogger()

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username=db_user,
        password=db_pass,
        database=db_name,
        query={
            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
            }
        )
    )

@app.route('/photo', methods=['GET'])
def index():
    db = connect_to_cloudsql()
    result = db.execute("select * from photos")
    return json.dumps([dict(data) for data in result])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
