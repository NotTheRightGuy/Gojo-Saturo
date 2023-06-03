import nextcord
from nextcord.ext import commands, tasks
from nextcord import Embed
import requests
from datetime import datetime, timedelta
import datetime
import pytz
import random
import time
import os
import dotenv
from POTD_Scrapper import scrapPOTD
from POTD_Solution import POTDSolution
import asyncio
from server import keep_alive

dotenv.load_dotenv()

TOKEN = os.environ.get("TOKEN")
POTD_CHANNEL = int(os.environ.get("DEV_CHANNEL"))
TIME_ZONE = os.environ.get("TIME_ZONE")

# ! Setup Logging Properly

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!",
                   description="Gojo Saturo at your service", intents=intents)


# ------------------ SLASH COMMANDS ----------------- #
@bot.slash_command(description="bow")
async def dog(interaction: nextcord.Interaction):
    user = interaction.user
    print(f"{user} issued the command /dog")
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await interaction.response.send_message(image_link)


@bot.slash_command(description="meow")
async def cat(ctx: nextcord.Interaction):
    user = ctx.user
    print(f"{user} issued the command /cat")
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()
    cat_url = data[0]['url']
    await ctx.send(cat_url)


@bot.slash_command(description="sends a message to this channel")
async def send(interaction: nextcord.Interaction, text: str):
    user = interaction.user
    print(f"{user} issued the command /send")
    await interaction.response.send_message(f"{text}")


@bot.slash_command(name="nickname", description="Change your nickname in the server")
async def nickname(ctx: nextcord.Interaction, nickname: str):
    user = ctx.user
    print(f"{user} issued the command /nickname")
    try:
        await ctx.user.edit(nick=nickname)
        await ctx.send(f"Your nickname has been changed to {nickname}")
    except nextcord.errors.Forbidden:
        await ctx.send("I don't have permission to change your nickname.")


@bot.slash_command(description="get current time")
async def timenow(interaction: nextcord.Interaction):
    user = interaction.user
    print(f"{user} issued the command /timenow")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ist = pytz.timezone(TIME_ZONE)  # e.g. America/New_York
    datetime_ist = datetime.datetime.now(ist)
    current_time = datetime_ist.strftime("%H:%M:%S")
    await interaction.response.send_message(f"Current Time is {current_time}")


@bot.slash_command(description="pong")
async def ping(ctx):
    user = ctx.user
    print(f"{user} issued the command /ping")
    start_time = time.monotonic()
    message = await ctx.send("Pong!")
    end_time = time.monotonic()
    await message.edit(content=f"Pong! Response time: {round((end_time - start_time) * 1000)} ms")


@bot.slash_command(description="rolle's dice")
async def rolldice(interaction: nextcord.Interaction):
    user = interaction.user
    print(f"{user} issued the command /rolldice")
    rolled = random.randint(1, 6)
    await interaction.send(f"*clatter* you rolled dice and you got {rolled}!")


@bot.slash_command(description="ban a user")
async def ban(ctx: nextcord.Interaction, user: nextcord.Member, reason: str = "No reason provided"):
    user = user or ctx.user
    print(f"{user} issued the command /ban")
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} has been banned from the server! Reason: {reason}!")


@bot.slash_command(description="kick a user")
async def kick(ctx: nextcord.Interaction, user: nextcord.Member, reason: str = "No reason provided"):
    user = user or ctx.user
    print(f"{user} issued the command /kick")
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} has been kicked from the server! Reason: {reason}!")


@bot.slash_command(description="Retrieves the avatar of a user.")
async def avatar(ctx, user: nextcord.Member = None):
    user = user or ctx.user
    print(f"{user} issued the command /avatar")
    avatar_url = user.avatar.url
    await ctx.send(avatar_url)


@bot.slash_command(description="alright im here to help")
async def help(interaction: nextcord.Interaction):
    user = interaction.user
    print(f"{user} issued the command /help")
    await interaction.response.send_message(f"**Hello I'm {bot.user}**\n*My commands are as follows:*\n\n`!slap !sendtochannel !codelink`\n\n*And some slash commands ;)*")


@bot.slash_command(description="Ask a question to 8 ball")
async def eightball(ctx, question: str):
    user = ctx.user
    print(f"{user} issued the command /eightball")
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                 "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "Outlook not so good.", "My sources say no.", "Very doubtful."]
    await ctx.send(random.choice(responses))


@bot.slash_command(name="userinfo", description="Get detailed information about a user.")
async def userinfo(ctx: nextcord.Interaction, user: nextcord.Member = None):
    user = user or ctx.user
    print(f"{user} issued the command /userinfo")
    if user is None:
        user = ctx.user

    # Get information about the user
    username = str(user)
    created_at = user.created_at.strftime("%Y-%m-%d \n*%H:%M:%S* UTC")
    joined_at = user.joined_at.strftime("%Y-%m-%d \n*%H:%M:%S* UTC")
    roles = [role.mention for role in user.roles if role !=
             ctx.guild.default_role]
    if len(roles) == 0:
        roles = ["None"]
    user_id = str(user.id)
    avatar_url = user.avatar.url

    embed = nextcord.Embed(title="User Information", color=0x00ff00)
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Username", value=username, inline=False)
    embed.add_field(name="Account Created On", value=created_at, inline=False)
    embed.add_field(name="Joined This Server On",
                    value=joined_at, inline=False)
    embed.add_field(name="Roles", value=", ".join(roles), inline=False)
    embed.add_field(name="Status", value=user.status, inline=False)
    embed.add_field(name="User ID", value=user_id, inline=False)
    embed.add_field(name="Activity", value=user.activity, inline=False)
    await ctx.send(embed=embed)


@bot.slash_command()
async def mute(ctx: nextcord.Interaction, user: nextcord.Member):
    user = user or ctx.user
    print(f"{user} issued the command /mute")
    if ctx.user.guild_permissions.administrator:
        try:
            await user.edit(mute=True)
        except:
            await ctx.send("user is not connected to any voice channel.")
        else:
            await ctx.send(f"{user.display_name} has been muted.")
    else:
        await ctx.send("You do not have permission to use this command.")


@bot.slash_command()
async def unmute(ctx: nextcord.Interaction, user: nextcord.Member):
    user = user or ctx.user
    print(f"{user} issued the command /unmute")
    if ctx.user.guild_permissions.administrator:
        try:
            await user.edit(mute=False)
        except:
            await ctx.send("user is not connected to any voice channel.")
        else:
            await ctx.send(f"{user.display_name} has been unmuted.")
    else:
        await ctx.send("You do not have permission to use this command.")


# ------------------- COMMANDS ! ------------------- #

@bot.command()
async def slap(ctx, members: commands.Greedy[nextcord.Member], *, reason='no reason'):
    user = ctx.author
    print(f"{user} issued the command !slap")
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')


# ------------------- TASKS LOOP ------------------- #

@tasks.loop(hours=24)
async def POTD():
    print("POTD task started")
    POTD = scrapPOTD()
    solution = POTDSolution(POTD["id"])
    channel = bot.get_channel(POTD_CHANNEL)
    embed = Embed(
        title="Leetcode | Problem of the Day | " + POTD["date"], color=0xff0000, url=POTD["link"])
    embed.set_thumbnail(url="https://i.ibb.co/2MRPBBw/ASPDC.jpg")
    embed.add_field(name=POTD["id"], value=POTD["title"], inline=False)
    embed.set_footer(text="Happy Coding!")
    await channel.send(embed=embed)
    await asyncio.sleep(100)
    print("POTD solution task started")
    await channel.send(solution)


@POTD.before_loop
async def before_POTD():
    hour, minute = 1, 20
    await bot.wait_until_ready()
    now = datetime.datetime.now()
    future = datetime.datetime(now.year, now.month, now.day, hour, minute)
    if now.hour >= hour and now.minute >= minute:
        future += datetime.timedelta(days=1)
    await asyncio.sleep((future-now).seconds)


# ------------------- EVENTS ------------------- #

@bot.event
async def on_ready():
    print(f"{bot.user} is ready to fight!")
    print("------")
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="with your feelings"))
    POTD.start()

if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)
