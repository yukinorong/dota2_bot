from DotaWatcher import watcher, CUSTOMERINFO, CONFIG
from WebSocket import client
import asyncio

if __name__ == '__main__':
    gid = CONFIG.common_group_qq
    uid = CONFIG.common_manager_qq

    for uid in CUSTOMERINFO.USER_DICT.keys():
        sentences = watcher.get_match_evaluation(uid)
        if sentences:
            # asyncio.run(client.send_private_msg(uid, "\n".join(sentences)))
            asyncio.run(client.send_group_msg(gid, "\n".join(sentences)))


