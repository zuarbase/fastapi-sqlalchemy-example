import fastapi
from starlette.requests import Request

from fastapi_sqlalchemy.endpoints import LoginEndpoint

from fastapi_sqlalchemy_example import settings, models
from fastapi_sqlalchemy_example.main import app

ENDPOINT = LoginEndpoint(models.User, secret=str(settings.SECRET), secure=False)


@app.get('/login')
async def login_get():
    """ Login form """
    return await ENDPOINT.on_get()


@app.post('/login')
async def login_post(
        request: Request,
        username: str = fastapi.Form(...),
        password: str = fastapi.Form(...),
):
    """ Login handler """
    return await ENDPOINT.on_post(
        request.state.session, username, password
    )
