# FastAPI boilerplate

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pylint](https://img.shields.io/badge/Pylint-enabled-brightgreen)](https://pylint.org/)

This is a simple fastapi boilerplate with db migration and ORM support.

## Local env setup

This section describes tools and configurations needed to make local environment ready to develop and run the application locally.

### Prerequisites

Following tech stacks are required to get the local env up and running.

- [Python 3.9](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/front.html#installation)
- [PostgresSQL](https://www.postgresql.org/)

---

### Installation

This is an installation example for Mac users. Please check out official documentations of those above prerequisites for `windows/linux`. It's assumed that [Homebrew](https://brew.sh) is installed in the machine.

```sh
# Install python and it's ecosystem
$ brew install python3

# Install pipenv: a tool for python packaging
$ brew install pipenv
```

**Install Postgres:** There are two options for installing postgres.

**Option 1:** Installing in the machine

- Download from [here](https://www.postgresql.org/download/) and install it.

**Option 2:** Using docker containers

- Make sure `docker` and `docker-compose` are installed in the machine. Latest docker package (docker for Mac) comes with `docker-compose` bundled in it though.

---

### Configuration and Running

- Rename `env.sample` --> `.env`
- Fill out the env variables in the file from a team member.

Choose one of the following options to run the application

- **Option 1:** Start the postgres app and create a database called `payment` from the UI. Execute following commands from the root of the project.

  ```sh
  # To create and enable virtual env for the project.
  $ pipenv shell

  # Install dependencies
  $ pipenv install

  # Make start script executable
  $ chmod +x start

  # start the project
  ./start
  ```

- **Option 2:** Run a docker container using compose file.

  ```sh
  # To start the DB engine in a daemon mode
  $ docker-compose up -d

  # To stop the DB engine
  $ docker-compose down

  # To stop the DB engine and remove the data volumes:
  $ docker-compose down -v
  ```

Once service is up and running successfully hover over the following url for the API documentation:
[localhost:9000/docs](http://127.0.0.1:9000/docs)

---

### Alembic and migrations
Alembic can view the status of the database and compare against the table metadata in the application, generating the `obvious` migrations based on a comparison.

If new models are added alembic would be able to detect it. Run the following commands to create new migration version using `--autogenerate` option.

```sh
# Tpo autogenerate new version
$ alembic --config migrations/alembic.ini revision --autogenerate -m "<commit_message>"

# upgrade to the latest version
$ alembic --config migrations/alembic.ini upgrade head

```

## Tests

**TODO:**

- Add tests

## Deployment

**TODO:**

- Add CI/CD configuration
- Document deployment processes.

## Roadmap

State the roadmap of the project

## License
[MIT LICENSE](./LICENSE)

## Credit

I've taken inspirations from these following two libraries while making this boiler plate.

- [SKB's boilerplate](https://github.com/skb1129/fastapi-boilerplate)
- [Thales Bruno's boilerplate](https://github.com/thalesbruno/fastapi-boilerplate)
