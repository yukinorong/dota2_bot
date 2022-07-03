import asyncio
import websockets
import json
from DotaWatcher import CONFIG

robot_qq = CONFIG.robot_qq
at_string = "[CQ:at,qq="+robot_qq+"]"

def message_manager(data):
    # 1 命令 (群聊中艾特 或 私聊）
    command_check(data)

    # 2 互动
    # 2.1 搞点东西

def command_check(data):
    command = ""
    if at_string in data["message"] and data["message_type"] == "group":
        command = data["message"].split(at_string)[1].strip()
    elif data["message_type"] == "private":
        command = data["message"]
    else :
        return

    if "user" in command:
        # 1.1 添加账号
        user_change(command)
    elif "manager" in command:
        # 1.2 添加权限
        manager_change(command)


def user_change(command):
    order, info = command.split("user")
    if order == "create":
        uid, nickname, qq = info.split()
        print(order, uid, nickname, qq)
        pass
    elif order == "update":
        uid, nickname, qq = info.split()
        print(order, uid, nickname, qq)
        pass
    elif order == "delete":
        uid = info.split()[0]
        print(order, uid)
        pass
    elif order == "find":
        uid = info.split()[0]
        print(order, uid)
        pass
    else :
        print("order error")


def manager_change(command):
    order, info = command.split("manager")
    if order == "create":
        uid, nickname, qq = info.split()
        print(order, uid, nickname, qq)
        pass
    elif order == "update":
        uid, nickname, qq = info.split()
        print(order, uid, nickname, qq)
        pass
    elif order == "delete":
        uid = info.split()[0]
        print(order, uid)
        pass
    elif order == "find":
        uid = info.split()[0]
        print(order, uid)
        pass
    else:
        print("order error")





    # 2.2 聊天








async def server(websocket):
    async for message in websocket:
        data = json.loads(message)
        if data.get('post_type', None) and data['post_type'] == 'message':
            print(data)
            message_manager(data)


async def main():
    async with websockets.serve(server, "localhost", 9876):
        await asyncio.Future()

asyncio.run(main())