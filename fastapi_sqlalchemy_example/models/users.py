from fastapi_sqlalchemy import models
from fastapi_sqlalchemy.models import mixins


class User(models.User, mixins.ConfirmationMixin):
    pass
