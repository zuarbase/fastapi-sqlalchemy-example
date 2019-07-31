def test_config(client):
    res = client.get('/')
    assert res.status_code == 200
