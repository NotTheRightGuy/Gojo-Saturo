from utils.LC_POTD import LC_POTD
from utils.sendToChannel import send_to_channel as sendToChannel
from utils.LC_Solution import LC_Solution
from utils.EmbedMaker import make_embed


async def sendPOTD(bot, channel_id):
    POTD = LC_POTD()
    print("Sending Leetcode POTD for {}".format(POTD["date"]))
    embed = make_embed(title=POTD["id"] + " | " + POTD["date"], url=POTD["link"], color=0xff0000,
                       thumbnail_url="https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png", additonal_fields=[
        {
            "name": POTD["title"],
            "value":  POTD["link"],
        }])
    await sendToChannel(bot, channel_id, embed=embed)
    return POTD["id"]


async def sendSolution(bot, channel_id, id):
    print("Sending Leetcode Solution for {}".format(id))
    solution = LC_Solution(id)
    await sendToChannel(bot, channel_id, solution)
