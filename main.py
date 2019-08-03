import datetime
import logging
import os
import json

from flask import Flask
from flask_cors import CORS
import sqlalchemy
import requests

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


if os.getenv('GAE_ENV') == 'standard':
    import google.cloud.logging
    client = google.cloud.logging.Client('yori-server')
    client.setup_logging(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_name = os.environ.get('DB_NAME')
cloud_sql_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
slack_webhook_url = os.environ.get('SLACK_WEBHOOK_URL')

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


# TODO:
# We should create a package and move this into __init__.py of that package
def notify():
    logger.info('will notify {}'.format(slack_webhook_url))
    print('will notify {}'.format(slack_webhook_url))
    if slack_webhook_url:
        project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
        gae_version = os.environ.get('GAE_VERSION')
        gae_instance = os.environ.get('GAE_INSTANCE')
        message = 'Launch {0}. GAE_VERSION: {1} on GAE_INSTANCE: {2}'.format(
            project_id, gae_version, gae_instance)
        logger.info(message)
        requests.post(slack_webhook_url, json={'text': message})


# TODO:
# We should create a package and move this into that package
@app.route('/photo', methods=['GET'])
def index():
    result = db.execute('select * from photos')
    return json.dumps([dict(data) for data in result])


# TODO:
# We should create a package and move this into __init__.py of that package
notify()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
