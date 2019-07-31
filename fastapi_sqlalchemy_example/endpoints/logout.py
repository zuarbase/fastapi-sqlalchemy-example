from fastapi_sqlalchemy.endpoints import LogoutEndpoint

from fastapi_sqlalchemy_example.main import app

ENDPOINT = LogoutEndpoint()


@app.post('/logout')
async def login_post(
):
    """ Logout handler """
    return await ENDPOINT.on_post()
