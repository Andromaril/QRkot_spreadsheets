from fastapi_users import models


class UserRead(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(models.BaseUserUpdate):
    pass