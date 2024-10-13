from fastapi import Depends
from fastapi.routing import APIRouter, Request
from sqlalchemy.ext.asyncio import AsyncSession

from {{cookiecutter.project_slug}}.utils.jwt_auth import get_token_data
from {{cookiecutter.project_slug}}.db import get_db_async_session

import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1")


@router.get("/user/me")
async def get_gw_modbus_reg_val(
    request: Request, sn: str, 
    reg_no=int,
    db_session: AsyncSession = Depends(get_db_async_session), 
    token_data=Depends(get_token_data)
):
    return False
