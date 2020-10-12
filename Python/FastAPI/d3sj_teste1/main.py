# https://stackoverflow.com/questions/34578507/d3js-chart-update-triggered-on-websocket-message
# https://medium.com/@benjaminmbrown/real-time-data-visualization-with-d3-crossfilter-and-websockets-in-python-tutorial-dba5255e7f0e

from fastapi import FastAPI
from fastapi.websockets import WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, Response, WebSocket, BackgroundTasks, Request
from fastapi.staticfiles import StaticFiles
from pathlib import Path

import json

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)


def getJson():
    with open("myjson.json") as json_file:
        data = json.load(json_file)

        print(data)

        print(type(data))

        return data


@app.get("/")
async def main():
    return FileResponse("static/html2.html")


@app.get("/2")
async def p2():
    return FileResponse("static/html2.html")


@app.get("/3")
async def p3():
    return FileResponse("static/html3.html")


@app.get("/4")
async def p4():
    return FileResponse("static/html4.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            if str(data) == "abc":
                print("send")
                await websocket.send_json(getJson())

    except WebSocketDisconnect:
        manager.disconnect(websocket)


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)


manager = ConnectionManager()