import asyncio
import websockets
import json
import re
from JsonManager import JsonManager
from JsonManager.customerInfoManager import *

robot_qq = JsonManager.getConfig()["robot_qq"]

def message_manager(data):
    # 1 命令 (群聊中艾特 或 私聊）
    return command_check(data)

    # 2 互动
    # 2.1 搞点东西

def command_check(data):
    command = ""
    if data["message_type"] == "group":
        mo = re.match(r'\[CQ:at,qq=([0-9]+)\]\s(.*)', data["message"])
        if mo and mo.group(1) == robot_qq:
            command = mo.group(2)
            print("[command_check] ", command)
    elif data["message_type"] == "private":
        command = data["message"]
    else:
        return

    # 校验命令
    matchobj = re.match(r'^(find|delete)\s?(user|manager)\s([0-9]+)$', command)
    if matchobj:
        return command_manager(matchobj.group(1), matchobj.group(2), [matchobj.group(3)])

    matchobj = re.match(r'^(create|update)\s?(user|manager)\s([0-9]+)\s(\S+)\s([0-9]+)$', command)
    if matchobj:
        return command_manager(matchobj.group(1), matchobj.group(2), [matchobj.group(3), matchobj.group(4), matchobj.group(5)])

async def server(websocket):
    async for message in websocket:
        data = json.loads(message)
        if data.get('post_type', None) and data['post_type'] == 'message':
            print("[server] ", data)
            ret = message_manager(data)
            print("[server] ret=", ret)

async def main():
    async with websockets.serve(server, "localhost", 9876):
        await asyncio.Future()
