from fastapi.requests import Request
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer

import jwt
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel

from {{cookiecutter.project_slug}}.config import settings

## Avoid showing username and password in swagger-ui
## to get a token. Show single field Authorization: Bearer <token> instead
security_bearer_as_key = APIKeyHeader(name="Authorization", auto_error=False)


class TokenData(BaseModel):
    username: str | None = None
    usertype: str | None = None


async def get_token_data(
    request: Request, token: str = Depends(security_bearer_as_key)
):
    token = await OAuth2PasswordBearer("token", auto_error=False).__call__(request)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        username: str = payload.get("sub")
        usertype: str = payload.get("type")
        if username is None or usertype is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    return token_data