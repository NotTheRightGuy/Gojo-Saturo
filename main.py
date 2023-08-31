from events.on_ready_event import on_ready_event
from commands import main_command_setter as commands_main
from scheduler.LeetCode import sendPOTD
from scheduler.LeetCode import sendSolution
from scheduler.Codeforces import sendContestEmbed
from nextcord.ext import tasks
from dotenv import load_dotenv
from discordBot import init_bot
import os
import asyncio


load_dotenv()
TOKEN = os.environ.get("TOKEN")
POTD_CHANNEL = os.environ.get("POTD_CHANNEL")
CONTEST_CHANNEL = os.environ.get("CONTEST_CHANNEL")

bot = init_bot()


# =========Importing Commands=======
commands_main.setup_all_commands(bot)


# =========Tasks Loop=========
@tasks.loop(hours=24)
async def sendPOTDLoop():
    problem_id = await sendPOTD(bot, POTD_CHANNEL)
    await asyncio.sleep(43200)  # ! Sleeping for 12 hours
    await sendSolution(bot, POTD_CHANNEL, problem_id)


@tasks.loop(hours=24)
async def sendContestLoop():
    await sendContestEmbed(bot, CONTEST_CHANNEL)


@bot.event
async def on_ready():
    await on_ready_event(bot)
    sendPOTDLoop.start()
    sendContestLoop.start()


if __name__ == "__main__":
    bot.run(TOKEN)
