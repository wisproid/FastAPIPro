from enum import Enum
from {{cookiecutter.project_slug}}.schemas import BaseModelSchema
from pydantic import Field

class UserRole(Enum):
    A = "reg"
    B = "adm"

class AddUserSchema(BaseModelSchema):
    username: str = Field(max_length=10)
    name: str
    role: UserRole