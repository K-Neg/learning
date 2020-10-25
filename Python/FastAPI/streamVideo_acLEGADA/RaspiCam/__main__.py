import io
import time
import datetime as dt
from threading import Event, Thread
from pathlib import Path
import uvicorn

from src import cameraFunctions
from src import Serial_file
from src import utils as utils

from fastapi import FastAPI, Response, WebSocket, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.testclient import TestClient
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocket, WebSocketDisconnect

app = FastAPI()

# mounts a static directory for file indexation
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

# WEB APP port
port = 5151
local_ip = utils.ip_check()

# JINJA2 as HTML render
templates = Jinja2Templates(directory="templates")

##### Main interface class
class Interface:
    def __init__(self, camera, serial):
        self.camera = camera
        self.Serial = serial

    # CAMERA FUNCTIONS
    def gen_camera(self):
        """Generate the video"""
        while True:
            frame = self.camera.image_encode()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n"
            )

    # ROUTES
    def start(self):
        @app.get("/", response_class=HTMLResponse)
        def index(request: Request):
            return templates.TemplateResponse(
                "views/home.html",
                {"request": request, "ip": str(local_ip), "port": str(port)},
            )

        @app.get("/control")
        def jon(request: Request):
            return templates.TemplateResponse(
                "views/control.html",
                {
                    "request": request,
                    "ip": str(local_ip),
                    "port": str(port),
                    "stuff": dict(myjson),
                },
            )

        # Config and Help page
        @app.get("/config")
        async def get(request: Request):
            return templates.TemplateResponse(
                "views/config.html",
                {"request": request, "ip": str(local_ip), "port": str(port)},
            )

        @app.get("/video_viewer")
        def video_viewer():
            return StreamingResponse(
                self.gen_camera(),
                media_type="multipart/x-mixed-replace; boundary=frame",
            )

        @app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await manager.connect(websocket)

            try:
                while True:
                    data = await websocket.receive_text()
                    self.Serial.send_msg(data)
                    print(f"Mesagem enviada: {data}")

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

myjson = utils.getJson()


# Start server
if __name__ == "__main__":
    Camera = cameraFunctions.camera()
    Camera.daemon = True
    Camera.start()
    Serial = Serial_file.SerialCom("/dev/ttyUSB0", 9600)
    Serial.daemon = True
    Serial.start()
    Interface(Camera, Serial).start()
    uvicorn.run("__main__:app", host="0.0.0.0", port=port, log_level="info")
