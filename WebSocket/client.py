import websockets
import json

websocket_path = "ws://localhost:9877/api"

async def send_private_msg(uid, msg):
    async with websockets.connect(websocket_path) as websocket:
        data = {}
        data["action"] = "send_private_msg"
        data["params"] = {}
        data["params"]["user_id"] = uid
        data["params"]["message"] = msg
        jdata = json.dumps(data, ensure_ascii=False)
        await websocket.send(jdata)
        await websocket.recv()

async def send_group_msg(gid, msg):
    async with websockets.connect(websocket_path) as websocket:
        data = {}
        data["action"] = "send_group_msg"
        data["params"] = {}
        data["params"]["group_id"] = gid
        data["params"]["message"] = msg
        jdata = json.dumps(data, ensure_ascii=False)
        await websocket.send(jdata)
        await websocket.recv()