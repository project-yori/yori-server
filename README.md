# yori-server

## Local Development

### Prerequisite

- Python 3
- [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy)

### Run Development Server

- Create environment (This is only needed for the first time)

  ```sh
  python3 -m venv venv
  ```

- Activate environment

  ```sh
  . venv/bin/activate
  ```

- Install Flask and other dependencies locally (if you haven't)

  ```sh
  pip install -r requirements.txt
  ```

- Install and launch [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy)

  ```sh
  cloud_sql_proxy -dir=/tmp/cloudsql -instances=yori_instance_name=tcp:3306
  ```

- Launch server

  ```sh
  env FLASK_APP=main.py DB_USER=username DB_PASS=password DB_NAME=database_name CLOUD_SQL_CONNECTION_NAME=yori_instance_name flask run
  ```

  or if you want to enable network access to local server (especially when you are developing yori-view)

  ```sh
  env FLASK_APP=main.py DB_USER=username DB_PASS=password DB_NAME=database_name CLOUD_SQL_CONNECTION_NAME=yori_instance_name flask run --host=0.0.0.0
  ```

  If setting environments bothers you, write them in your dotfiles.

## Deploy

Before deploy to gcloud, you have to install gcloud sdk. ([Install guide](https://cloud.google.com/sdk/docs/quickstarts))

- Create a `secret.yaml` (if you haven't) and set your own environment variable
  **NOTICE: do not upload your `secret.yaml` to repository**

  ```yaml
  env_variables:
    CLOUD_SQL_CONNECTION_NAME: your-connection-name
    DB_USER: your-account
    DB_PASS: your-password
    DB_NAME: your-database
    SLACK_WEBHOOK_URL: slack-webhook-url
  ```

- Deploy Command

  ```sh
  gcloud app deploy
  ```
