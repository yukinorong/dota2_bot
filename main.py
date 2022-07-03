from DotaWatcher import watcher
from WebSocket import client
from JsonManager import JsonManager
import asyncio
import time

if __name__ == '__main__':
    config = JsonManager.getConfig()
    gid = config["common_group_qq"]
    uid = config["common_manager_qq"]
    while True :
        time.sleep(60)
        for uid in JsonManager.getCustomerInfo()["USER_DICT"].keys():
            sentences = watcher.get_match_evaluation(uid)
            if sentences:
                asyncio.run(client.send_group_msg(gid, "\n".join(sentences)))


