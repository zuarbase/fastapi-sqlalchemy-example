#!/usr/bin/env python3
import os
import subprocess

import sqlalchemy
import click
import alembic

from fastapi_sqlalchemy.models import BASE, Session

from fastapi_sqlalchemy_example import models, settings


@click.group()
def cli():
    pass


def alembic_config():
    """ Generate a Config instance from alembic.ini """
    from alembic.config import Config
    path = os.path.join(os.path.dirname(settings.__file__), 'alembic.ini')
    return Config(path)


@cli.command()
def initdb():
    cfg = alembic_config()

    sqlalchemy_url = cfg.get_main_option('sqlalchemy.url')
    engine = sqlalchemy.create_engine(sqlalchemy_url)
    BASE.metadata.create_all(engine)

    alembic.command.stamp(cfg, "head")


@cli.command()
def migrate():
    cfg = alembic_config()
    return alembic.command.upgrade(cfg)


@cli.command(context_settings=dict(
    ignore_unknown_options=True
))
@click.argument('uvicorn_args', nargs=-1, type=click.UNPROCESSED)
def runserver(uvicorn_args):
    cmd = [
        'uvicorn', 'fastapi_sqlalchemy_example.main:app', '--debug'
    ] + list(uvicorn_args)
    subprocess.run(" ".join(cmd), shell=True, check=True)


@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def createuser(username, password):
    session = Session()
    user = models.User(username=username)
    user.password = password
    session.add(user)
    session.commit()


@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def setpassword(username, password):
    session = Session()
    user = models.User.get_by_username(session, name=username)
    if not user:
        raise click.BadParameter("Not found", param="username")
    user.password = password
    session.commit()


if __name__ == '__main__':
    cli()
