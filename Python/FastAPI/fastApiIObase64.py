#https://stackoverflow.com/questions/49015957/how-to-get-python-graph-output-into-html-webpage-directly

import uvicorn
from pathlib import Path
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import fastapi
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

import io
import base64

s = pd.Series([1, 2, 3])
fig, ax = plt.subplots()
s.plot.bar()
fig.savefig('my_plot.png')

def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())

encoded = fig_to_base64(fig)
my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))

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


if __name__ == "fastApiIObase64":
    Interface().start()
    uvicorn.run("fastApiIObase64:app", host="0.0.0.0", port="8001", log_level="info")
