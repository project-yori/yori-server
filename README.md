# yori-server

## Local Development

### Prerequisite

- Python 3

### Run Development Server

- Create and activate environment
  ```
  python3 -m venv venv
  . venv/bin/activate
  ```

- Install Flask locally (if you haven't)
  ```
  pip install Flask
  ```

- Run
  ```
  env FLASK_APP=main.py flask run
  ```

## Deploy

Before deploy to gcloud, you have to install gcloud sdk. ([Install guide](https://cloud.google.com/sdk/docs/quickstarts))

### Deploy Command

```
gcloud deploy
```

