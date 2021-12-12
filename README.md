# [fastapi-url-shortener](https://bitly.deta.dev/)

Simple yet powerful URL shortener built with [FastAPI](https://github.com/tiangolo/fastapi) and [Deta](https://github.com/deta/deta-python).

**Work is in Progress.**


## Features

- Fast and scalable
- Shorten a long URL
- Self host easily
- Connect to your own domain
- Integrate with other services using RESTful API
- Free and Open Source


## Docs

- [Swagger](https://bitly.deta.dev/docs)
- [Redoc](https://bitly.deta.dev/redoc)

## How to deploy

You are expected to have `git` installed in your system.

First of all clone the repository and move into the directory.

  ```shell
  git clone https://github.com/vidyasagar1432/fastapi-url-shortener
  cd fastapi-url-shortener
  ```

### Deploy to Heroku

Make sure you have [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.

- Create a new Heroku app
  ```shell
  heroku create
  ```

- Push the code to Heroku
  ```shell
  git push heroku main
  ```

### Deploy to Deta

Make sure you have [Deta CLI](https://docs.deta.sh/docs/cli/install) installed.

- Create a new Deta Micro
  ```shell
  deta new --python
  ```

- Deploy your local code (and dependencies) to your Deta Micro.
  ```shell
  deta deploy
  ```



### Run on Localhost
- Install dependancies from [`requirements.txt`](requirements.txt)
  ```shell
  pip install -r requirements.txt
  ```
- Run the server using [`uvicorn`](https://github.com/encode/uvicorn)
  ```shell
  uvicorn main:app --reload
  ```






## License

MIT License

Copyright (c) 2021 [Vidya Sagar](https://github.com/vidyasagar1432)