# Basic Django Project
Basic django project setup with poetry and Docker

## Setup

Build project:
- Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/).

Try next commands with `sudo` if you get permission errors.
- `docker-compose build`.
- `docker-compose up -d`.
- Server will run in port 8000.

### Requirements

This projects requires python 3.11.
Python 3 can be installed with [pyenv](https://github.com/pyenv/pyenv).

1. Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for installing pyenv
2. See which python versions are available: `pyenv install --list`
3. Install python 3. Example: `pyenv install 3.11.1` (3.11.1 or higher)
4. `pyenv shell 3.11.1`
5. `poetry shell`


## Install new dependencies
This project uses [poetry](https://python-poetry.org/). as a dependency manager.
- `poetry shell`.
- `poetry add {dependency_name}`.


## Create new apps
1. Create a folder in `my_project/apps/` with the app name.
2. Run `python manage.py startapp {app_name} my_project/apps/{folder_name}`.
3. Add the app to you LOCAL_APPS in the `base.py`.
4. Add the apps urls in `settings/urls.py`.



