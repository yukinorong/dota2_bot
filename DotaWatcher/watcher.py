import json
import dota2api
from DotaWatcher import CONTEXT, CONFIG, CUSTOMERINFO
from random import randint

steamapi = CONFIG.steamapi
api = dota2api.Initialise(steamapi, raw_mode=True)


# 获取上一把比赛id
def get_last_match_id_by_userid(uid):
    return str(api.get_match_history(account_id=uid)['matches'][0]['match_id'])


# 获取比赛战绩
def get_match_detail(mid, uid):
    data = api.get_match_details(match_id=mid)
    if data:
        radiant_win = data['radiant_win']
        match_detail = [data['game_mode'], data['lobby_type'], data['radiant_score'], data['dire_score']]
        for p in data['players']:
            if p['account_id'] == int(uid):
                # print('ok')
                person_detail = [p['hero_id'],
                                 [p['item_0'], p['item_1'], p['item_2'], p['item_3'], p['item_4'], p['item_5']],
                                 p['kills'], p['deaths'], p['assists'], p.get("hero_damage", -1)]
                return [(p['player_slot'] < 5) == radiant_win, match_detail, person_detail]
        else:
            print('未知原因1')
            return 0
    else:
        print(uid, '获取比赛战绩失败, 编号为', mid)
        return 0


def parse_match_detail(mdata):
    iswin = mdata[0]

    if mdata[1][1] == 7:
        if mdata[1][0] == 22:
            game_mode = '天梯ap'
        elif mdata[1][0] == 3:
            game_mode = '天梯rd'
        else:
            print('没见过的模式', mdata)
            return 0
    elif mdata[1][1] == 0:
        if mdata[1][0] == 18:
            game_mode = '技能征召'
        elif mdata[1][0] == 22:
            game_mode = '匹配ap'
        elif mdata[1][0] == 3:
            game_mode = '匹配rd'
        else:
            print('没见过的模式', mdata)
            return 0
    else:
        print('没见过的模式', mdata)
        return 0
    if mdata[2][3] != 0:
        kda = round((mdata[2][2] + mdata[2][4]) / mdata[2][3], 1)
    else:
        kda = mdata[2][2] + mdata[2][4]

    # 情绪分类， 阴阳怪气语录和表情相关
    if mdata[0]:
        if kda > 3:
            tauntList = CONTEXT.WIN_POSTIVE
            faceid = 2
        else:
            tauntList = CONTEXT.WIN_NEGATIVE
            faceid = 5
    else:
        if kda > 2:
            tauntList = CONTEXT.LOSE_POSTIVE
            faceid = 18
        else:
            tauntList = CONTEXT.LOSE_NEGATIVE
            faceid = 36

    taunt = tauntList[randint(0, len(tauntList) - 1)]
    tips = []  # 特殊物品， 暴走，超神， 人头占比全队， 输出占比全队。
    return [mdata, iswin, game_mode, kda, taunt, faceid, tips]


# 生成阴阳句子
def constitute_sentence(uid, cdata):
    if not cdata:
        return None

    sentence1 = '[CQ:at,qq=%s] %s上一把%s比赛中使用的 %s %s[CQ:face,id=%s]' \
                % (CUSTOMERINFO.USER_DICT[uid]['qq'], CUSTOMERINFO.USER_DICT[uid]['nickname'], cdata[2],
                   CONTEXT.HEROES_LIST_CHINESE[cdata[0][2][0]], cdata[4], cdata[5])
    sentence2 = '最终战绩为%s杀%s死%s助攻，kda为%s。' % (cdata[0][2][2], cdata[0][2][3], cdata[0][2][4], cdata[3])
    sentences = [sentence1, sentence2]
    return sentences


# 数据处理
def read_lastmatch():
    with open("LASTMATCH.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_lastmatch(data):
    with open("LASTMATCH.json", "w", encoding='utf-8') as f:
        json.dump(data, f)


# 查看是否已经推送过该比赛
def check_is_sended(uid, mid):
    data = read_lastmatch()
    if data.get(uid, None) == mid:
        return True
    data[uid] = mid
    write_lastmatch(data)
    return False


def get_match_evaluation(uid):
    mid = get_last_match_id_by_userid(uid)
    if not mid:
        print("获取上一场比赛id失败")
        return None

    data = get_match_detail(mid, uid)
    if not data:
        print("获取比赛详情失败")
        return None

    if not check_is_sended(uid, mid):
        pdata = parse_match_detail(data)
        sentences = constitute_sentence(uid, pdata)
        if not sentences:
            print("组合阴阳怪气失败")
            return None
        return sentences
    print("%s 无新比赛记录" % uid)
    return None


