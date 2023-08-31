import nextcord
from nextcord.ext import commands

def init_bot():
    intents = nextcord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", description="Gojo Saturo at your service", intents=intents)
    return bot
