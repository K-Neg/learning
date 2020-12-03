from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/check",response_class=HTMLResponse)
async def checkPage(request: Request):
    return templates.TemplateResponse("checkBox.html",{"request": request})