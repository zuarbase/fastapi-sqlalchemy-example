import fastapi
from starlette.requests import Request

from fastapi_sqlalchemy.endpoints import ConfirmEndpoint

from fastapi_sqlalchemy_example import settings, models
from fastapi_sqlalchemy_example.main import app

ENDPOINT = ConfirmEndpoint(
    user_cls=models.User,
    secret=str(settings.SECRET),
)


@app.get('/confirm/{token}')
async def confirm_get(
        request: Request,
        token: str
):
    """ confirmation of email link """
    return await ENDPOINT.on_get(request.state.session, token)
