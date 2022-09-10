import httpx

import main
import user


def topLogin(data: list) -> None:
    endpoint = main.webhook_discord_url

    rewards: user.Rewards = data[0]
    login: user.Login = data[1]
    bonus: user.Bonus or str = data[2]

    messageBonus = ''
    nl = '\n'

    if bonus != "No Bonus":
        messageBonus += f"__{bonus.message}__{nl}```{nl.join(bonus.items)}```"

        if bonus.bonus_name is not None:
            messageBonus += f"{nl}__{bonus.bonus_name}__{nl}{bonus.bonus_detail}{nl}```{nl.join(bonus.bonus_camp_items)}```"

        messageBonus += "\n"

    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO 每日签到 - " + main.fate_region,
                "description": f"Fate/Grand Order 自动签到.\n\n{messageBonus}",
                "color": 563455,
                "fields": [
                    {
                        "name": "等级",
                        "value": f"{rewards.level}",
                        "inline": True
                    },
                    {
                        "name": "呼符",
                        "value": f"{rewards.ticket}",
                        "inline": True
                    },
                    {
                        "name": "圣晶石",
                        "value": f"{rewards.stone}",
                        "inline": True
                    },
                    {
                        "name": "连续登录天数",
                        "value": f"{login.login_days}",
                        "inline": True
                    },
                    {
                        "name": "总计登录天数",
                        "value": f"{login.total_days}",
                        "inline": True
                    },
                    {
                        "name": "总友情点",
                        "value": f"{login.total_fp}",
                        "inline": True
                    },
                    {
                        "name": "友情点增量",
                        "value": f"+{login.add_fp}",
                        "inline": True
                    },
                    {
                        "name": "最大AP",
                        "value": f"{login.act_max}",
                        "inline": True
                    }
                ],
                "thumbnail": {
                    "url": "https://grandorder.wiki/images/thumb/3/3d/Icon_Item_Saint_Quartz.png/200px-Icon_Item_Saint_Quartz.png"
                }
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    httpx.post(endpoint, json=jsonData, headers=headers)


def drawFP(servants, missions) -> None:
    endpoint = main.webhook_discord_url

    message_mission = ""
    message_servant = ""

    if len(servants) > 0:
        servants_atlas = httpx.get(
            f"https://api.atlasacademy.io/export/JP/basic_svt_lang_en.json").json()

        svt_dict = {svt["id"]: svt for svt in servants_atlas}

        for servant in servants:
            svt = svt_dict[servant.objectId]
            message_servant += f"`{svt['name']}` "

    if len(missions) > 0:
        for mission in missions:
            message_mission += f"__{mission.message}__\n{mission.progressTo}/{mission.condition}\n"

    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO Daily Bonus - " + main.fate_region,
                "description": "Scheluded Friend Point Fate/Grand Order.\n\n",
                "color": 5750876,
                "fields": [
                    {
                        "name": "Gacha Result",
                        "value": f"{message_servant}",
                        "inline": False
                    }
                ],
                "thumbnail": {
                    "url": "https://i.imgur.com/LJMPpP8.png"
                }
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    httpx.post(endpoint, json=jsonData, headers=headers)


def buy_bronze_fruit(buy_num: int, current_num: int) -> None:
    endpoint = main.webhook_discord_url

    jsonData = {
        "content": None,
        "embeds": [
            {
                "title": "FGO 每日签到 - " + main.fate_region,
                "description": f"自动购买青铜果实{buy_num}个\n\n",
                "color": 5750876,
                "fields": [
                    {
                        "name": "当前青铜果实数量",
                        "value": str(current_num),
                        "inline": False
                    }
                ]
            }
        ],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    httpx.post(endpoint, json=jsonData, headers=headers)
