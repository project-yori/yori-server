# yori-server

## Local Development

### Prerequisite

- Python 3

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

- Run

  ```sh
  env FLASK_APP=main.py flask run
  ```

## Deploy

Before deploy to gcloud, you have to install gcloud sdk. ([Install guide](https://cloud.google.com/sdk/docs/quickstarts))

### Deploy Command

```
gcloud deploy
```
