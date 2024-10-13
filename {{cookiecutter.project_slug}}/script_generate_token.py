#!/usr/bin/env python3
import os
from datetime import datetime, timedelta, timezone
import jwt
import sys

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

print(JWT_SECRET_KEY)
print(JWT_ALGORITHM)
print(JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
print(sys.argv[1])
print(sys.argv[2])

access_token_expires = timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
access_token = create_access_token(
    data={"sub": sys.argv[1], "type": sys.argv[2]}, expires_delta=access_token_expires
)

# dotenv run python script_generate_token.py heri m2m
print(access_token)