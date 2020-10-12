import uvicorn
from pathlib import Path
import numpy as np

from fastapi import FastAPI, Response, WebSocket, BackgroundTasks, Request
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
port = 8000

templates = Jinja2Templates(directory="static")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)


def randomPoints():
    return np.random.randint(1, 10, size=2)


##### Main interface class
class Interface:
    # def __init__(self)

    # ROUTES
    def start(self):
        @app.get("/")
        def index(request: Request):
            return templates.TemplateResponse(
                "/index.html",
                {"request": request},
            )

        @app.get("/graph", response_class=HTMLResponse)
        async def get(request: Request):
            return templates.TemplateResponse(
                "/graph.html",
                {"request": request},
            )

        @app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await manager.connect(websocket)

            try:
                while True:
                    await websocket.send_text(str(randomPoints()))
                    data = await websocket.receive_text()
                    print(data)
                    # print(randomPoints())
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

if __name__ == "__main__":
    Interface().start()
    uvicorn.run("__main__:app", host="0.0.0.0", port=port, log_level="info")
