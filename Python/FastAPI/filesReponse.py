from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "video.mp4"
app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(some_file_path)