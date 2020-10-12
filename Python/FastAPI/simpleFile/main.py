from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse


import io
import base64

some_file_path = "my_plot.png"
fig = open(some_file_path, mode="rb")
#encoded = fig_to_base64(fig)
#my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))

app = FastAPI()

def fig_to_base64(fig):
    img = io.BytesIO()
    fig = open(some_file_path, mode="rb")
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())


@app.get("/")
async def main():
    return FileResponse("html1.html")

async def fake_video_streamer():
    for i in range(10):
        #yield b"some fake video bytes"
        file_like = open(some_file_path, mode="rb")
        encoded = fig_to_base64(fig)
        yield (b"" + encoded)





@app.get("/a")
async def main():
    return StreamingResponse(fake_video_streamer(),media_type="multipart/x-mixed-replace; boundary=frame")


@app.get("/b")
def stremFile():
    file_like = open(some_file_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")

@app.get("/c")
def video_viewer():
	file_like2 = open(some_file_path, mode="rb")
	return StreamingResponse(file_like2, media_type="multipart/x-mixed-replace; boundary=frame")


	  #  while True:
         #   frame = self.get_frame()
         #   yield (b"--frame\r\n" b"Content-Type: image/PNG\r\n\r\n" + frame + b"\r\n")