# Basic Django Project
Basic django project setup with poetry and Docker

## Setup

Build project:
- Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/).

Try next commands with `sudo` if you get permission errors.
- `docker-compose build`.
- `docker-compose up -d`.
- Server will run in port 8080.


## Install new dependencies
This project uses [poetry](https://python-poetry.org/). as a dependency manager.
- `poetry shell`.
- `poetry add {dependency_name}`.


## Create new apps
1) Create a folder in `my_project/apps/` with the app name.
1) Run `python manage.py startapp {app_name} my_project/apps/{folder_name}`.



