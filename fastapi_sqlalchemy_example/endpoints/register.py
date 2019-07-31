import fastapi
from starlette.requests import Request

from fastapi_sqlalchemy.endpoints import RegisterEndpoint

from fastapi_sqlalchemy_example import settings, models
from fastapi_sqlalchemy_example.main import app

ENDPOINT = RegisterEndpoint(
    user_cls=models.User,
    sender=settings.EMAIL_SENDER,
    secret=str(settings.SECRET),

    email_server=settings.EMAIL_SERVER,
    email_port=settings.EMAIL_PORT,
    email_use_ssl=settings.EMAIL_USE_SSL,
    email_use_tls=settings.EMAIL_USE_TLS,
    email_login=settings.EMAIL_LOGIN,
    email_password=settings.EMAIL_PASSWORD,
)


@app.get('/register')
async def register_get():
    """ registration form """
    return await ENDPOINT.on_get()


@app.post('/register')
async def register_post(
        request: Request,
        username: str = fastapi.Form(...),
        email: str = fastapi.Form(...),
        password: str = fastapi.Form(...),
        confirm_password: str = fastapi.Form(None),
):
    """ Login handler """
    base_url = request.url.scheme + '://' + request.url.netloc
    return await ENDPOINT.on_post(
        base_url, request.state.session,
        username=username, email=email,
        password=password, confirm_password=confirm_password
    )
