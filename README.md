# Seshat  

[![All Contributors](https://img.shields.io/github/contributors/sorkhemiri/seshat)](#contributors-)
![Issues](https://img.shields.io/github/issues/sorkhemiri/seshat)
![Pull Requests](https://img.shields.io/github/issues-pr/sorkhemiri/seshat?)
![Forks](https://img.shields.io/github/forks/sorkhemiri/seshat)
![Stars](https://img.shields.io/github/stars/sorkhemiri/seshat)
![License](https://img.shields.io/github/license/sorkhemiri/seshat)
### Expense Management Application
Seshat is a personal expense management application.

Technologies and databases:

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Python 3.8](https://www.python.org/downloads/release/python-3812/)
* [FastAPI 0.68](https://github.com/tiangolo/fastapi/releases/tag/0.68.2)
* [Postgres 13](https://github.com/docker-library/postgres/blob/a83005b407ee6d810413500d8a041c957fb10cf0/13/alpine/Dockerfile)
* [Redis 6](https://github.com/docker-library/redis/blob/84c36a0967bcfa8a9c39cb899464785c5f2cf5ef/6.2/alpine/Dockerfile)


### Getting started

For simplifying the running the project in **development environment**, use the `Makefile` which is included in the project root folder:

`make build`

**WARNING**: do not use Makefile for deployment on production server.

### Running the tests

To run the tests in the project's root folder run this command:

`make test`

### Contributing in this project

If you want to contribute in this project, make sure to read the [CONTRIBUTING.md](CONTRIBUTING.md) first.
