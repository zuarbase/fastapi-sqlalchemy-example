""" application main """
import logging

from fastapi_sqlalchemy import FastAPI_SQLAlchemy, middleware, auth
from fastapi_sqlalchemy_example import models

from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.staticfiles import StaticFiles

from . import settings


logger = logging.getLogger(__name__)


def make_app() -> FastAPI_SQLAlchemy:
    """ Create an ASGI Application
    """
    logging.basicConfig()
    logging.getLogger('fastapi_sqlalchemy').setLevel(logging.INFO)

    myapp = FastAPI_SQLAlchemy(
        str(settings.DATABASE_URL),
        title='FastAPI-SQLAlchemy Example',
        version='0.0.0'
    )
    myapp.add_middleware(
        AuthenticationMiddleware,
        backend=auth.PayloadAuthBackend(user_cls=models.User)
    )
    myapp.add_middleware(middleware.JwtMiddleware, secret=str(settings.SECRET))
    myapp.add_middleware(middleware.SessionMiddleware)
    return myapp


app = make_app()
app.router.default = StaticFiles(directory='static', html=True)
