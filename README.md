# Async ODM Integration in FastAPI with MongoDB

We use Docker Compose to launch the whole backend stack, so please make sure that [Docker](https://www.docker.com/) is installed.

## Development

To start MongoDB server in Docker for local development and testing, make sure to provide the following variables:

Recommend using [direnv](https://github.com/direnv/direnv) for management of environment variables.

  ```
  DEBUG=True
  MONGO_HOST=127.0.0.1
  MONGO_USERNAME=
  MONGO_PASSWORD=
  MONGO_DB=
  ```

- To start the whole stack, run:

  ```
  $ make up
  ```

- To take down the stack, run:

  ```
  $ make down
  ```

- To view logs for a specific service, use `logs-{service}`. You can also customize the number of log lines to display with the `log_lines` argument:

  ```
  $ make logs-api log_lines=50
  ```