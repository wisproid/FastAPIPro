from fastapi import WebSocket, WebSocketDisconnect
from fastapi.routing import APIRouter
import asyncio

from {{cookiecutter.project_slug}}.utils.websocket_manager import manager as ws_manager

import logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1")

@router.websocket("/ws/{room_id}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, client_id: str):
    logger.info("websocket listen")
    await ws_manager.connect(websocket)
    try:
        # first message is auth token
        data = None
        try:
            # Wait for a message from the client with a timeout
            data = await asyncio.wait_for(websocket.receive_text(), timeout=5)
        except asyncio.TimeoutError:
            await ws_manager.send_personal_message("401 Unauthorized", websocket)
            logger.info(f"Disconnect client {client_id}")
            ws_manager.disconnect(websocket)
        if data:
            if data == "ABCDabcd12345":
                await ws_manager.send_personal_message("200", websocket)
                while True:
                    data = await websocket.receive_text()
                    # await ws_manager.send_personal_message(f"You wrote: {data}", websocket)
                    await ws_manager.broadcast(f"Client #{client_id} says: {data}")
            else:
                await ws_manager.send_personal_message("401 Unauthorized", websocket)
                logger.info(f"Disconnect client {client_id}")
                ws_manager.disconnect(websocket)
    except WebSocketDisconnect:
        logger.info(f"Client #{client_id} disconnected")
        ws_manager.disconnect(websocket)
        # await manager.broadcast(f"Client #{client_id} left the chat")
