def test_config(client):
    res = client.get('/api/config')
    assert res.status_code == 200
    assert res.json() == {}
