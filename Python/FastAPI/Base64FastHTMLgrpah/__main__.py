import io
import time
from threading import Event, Thread
import uvicorn

import io
import base64

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()

port = 5563

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


class Interface:

    def get_frame(self):
            """Return the current frame."""
            # wait for a signal from the thread
            self.event.wait()
            self.event.clear()
            return self.frame

    def frames(self):
        
            time.sleep(2)

            stream = io.BytesIO()
            
            fig.savefig(stream, format='png',box_inches='tight')
            stream.seek(0)
        
            # return current frame
            stream.seek(0)
            yield stream.read()

            # reset stream for next frame
            stream.seek(0)
            stream.truncate()

   

    def frames2(self):
        
            time.sleep(2)

            stream2 = io.BytesIO()
            for _ in camera.capture_continuous(stream2, 'jpeg',
                                                 use_video_port=True):

                    # return current frame
                stream2.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream2.seek(0)
                stream2.truncate()

    def framemap(self):
        """FrameMap background thread."""
        frames = self.frames()
        for frame in frames:
            self.frame = frame
            self.event.set()  # send signal to client
            time.sleep(0.01)
        self.thread = None

    def gen_camera(self):
        """Generate the video"""
        while True:
            frame = self.get_frame()
            yield (b"--frame\r\n" b"Content-Type: image/PNG\r\n\r\n" + frame + b"\r\n")


    def __init__(self):
        self.frame = None
        self.event = Event()

    def start(self):
        @app.get("/", response_class=HTMLResponse)
        def index():
            """Route to the main page"""
            return """<html>
                        <head>
                            <title>Video Streaming </title>
                        </head>
                        <body>
                            <h1>Video Streaming </h1>
                            <img src="http://0.0.0.0:5151/video_viewer">
                        </body>
                    </html>"""

        @app.get("/base1", response_class=HTMLResponse)
        def base1():
            encoded = fig_to_base64(fig)
            my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
            return my_html

        @app.get("/video")
        def video():
            """Route to the video"""
            return StreamingResponse(media_type="multipart/x-mixed-replace; boundary=frame")

        @app.get("/video_viewer")
        def video_viewer():
            """Route to the video"""
            return StreamingResponse(self.gen_camera(), media_type="multipart/x-mixed-replace; boundary=frame")

        self.thread = Thread(target=self.framemap)
        self.thread.start()

       


        
if __name__ == "__main__":
    Interface().start()
    uvicorn.run("__main__:app", host="0.0.0.0", port=port, log_level="info")
