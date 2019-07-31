from fastapi_sqlalchemy.auth import authenticated
from fastapi_sqlalchemy_example.main import app

from starlette.requests import Request


@app.get('/api/config')
@authenticated()
async def get_config(request: Request) -> dict:
    return {
        "user": request.user.as_dict(),
        "scopes": request.auth.scopes,
    }
