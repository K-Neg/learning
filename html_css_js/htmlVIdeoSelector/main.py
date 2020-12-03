import io
import time
import datetime as dt
from threading import Event, Thread
from pathlib import Path
import json
import uvicorn
import random


from fastapi import FastAPI, Response, WebSocket, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.testclient import TestClient
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocket, WebSocketDisconnect

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


def damit():
    return random.randint(0, 100)


##### Main interface class
# ROUTES


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "views/hist.html", {"request": request, "objectives": beta}
    )


@app.get("/video_viewer")
def video_viewer():
    return StreamingResponse(
        self.gen_camera(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )


@app.get("/hist", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "/hist.html", {"request": request, "navigation": beta}
    )


@app.get("/update", response_class=JSONResponse)
async def update():
    data = {"x": damit(), "y": damit()}
    return JSONResponse(data)


@app.get("/movie/{id}")
def movie_selector(id: int):
#    path = "videos/" + str(id) + ".mp4"
	path = "videos/4.mp4"
	file_like = open(path, mode="rb")
	return StreamingResponse(file_like, media_type="video/mp4")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)


@app.websocket("/ws2")
async def websocket_updata(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            # await websocket.send_json({"x": damit(), "y":damit()})

            data = await websocket.receive_text()
            print(data)
            await websocket.send_text(f"Message text was: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)


# WEBSOCKET MANAGER - Accept new connection and disconnect
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)


manager = ConnectionManager()

alfa = {"name": ["10x", "20x", "40x"], "value": ["o1", "o2", "o3"]}


beta = list(
    [
        {"name": "v1", "href": "selectMovie('1')"},
        {"name": "v2", "href": "selectMovie('2')"},
        {"name": "v3", "href": "selectMovie('3')"},
        {"name": "v4", "href": "selectMovie('4')"},
    ]
)
