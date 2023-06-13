from fastapi import FastAPI, WebSocket, Request
from logging import getLogger

app = FastAPI()
log = getLogger("WAS")
websocket = WebSocket

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/config")
async def post_config(request: Request):
    data = await request.json()
    log.info(str(data))
    await websocket.send(data)
    return "Success"

@app.websocket_route("/ws")
async def websocket_endpoint(websocket: websocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        log.info(str(data))
        await websocket.send_text(data)
