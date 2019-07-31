from fastapi_sqlalchemy.endpoints import RegisterEndpoint


def test_register_get(client):
    res = client.get('/register')
    assert res.status_code == 200
    assert res.headers.get('Content-Type').startswith('text/html')


def test_register_post(client, session, mocker):
    stub = mocker.patch.object(RegisterEndpoint, 'send_email_confirmation')

    username = 'testuser'
    recipient = 'recipient@example.com'
    res = client.post('/register', data={
        'username': username,
        'password': 'passw0rd',
        'email': recipient
    })
    assert res.status_code == 200
    stub.assert_called_once_with(
        'http://testserver', recipient, username=username
    )
