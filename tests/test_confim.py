from itsdangerous import URLSafeTimedSerializer

from fastapi_sqlalchemy.models import Session
from fastapi_sqlalchemy_example import models, settings


def test_confirm(client, session):
    session = Session()
    user = models.User(username="testuser", email="recipient@example.org")
    session.add(user)
    session.commit()

    token = URLSafeTimedSerializer(str(settings.SECRET)).dumps(user.email)
    res = client.get('/confirm/' + token)
    assert res.status_code == 200
    assert res.headers.get('Content-Type').startswith('text/html')

    session.refresh(user)
    assert user.confirmed
