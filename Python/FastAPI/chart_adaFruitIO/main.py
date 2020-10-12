from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


@app.get("/")
async def main():
    return FileResponse("static/views/index.html")


@app.get("/config")
async def get(request: Request):
    return templates.TemplateResponse(
        "views/index.html",
        {
            "request": request,
        },
    )