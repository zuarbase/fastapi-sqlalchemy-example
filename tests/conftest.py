
import pytest

from starlette.testclient import TestClient

from fastapi_sqlalchemy import models
from fastapi_sqlalchemy_example.main import app


@pytest.fixture(scope='function', name='session')
def session_fixture():

    # Drop all tables ...
    models.BASE.metadata.reflect(bind=app.bind)
    models.BASE.metadata.drop_all(bind=app.bind)

    # and recreate
    models.BASE.metadata.create_all(bind=app.bind)
    session = models.Session()

    yield session
    session.close()


@pytest.fixture(scope='function', name='client')
def client_fixture():
    return TestClient(app)
