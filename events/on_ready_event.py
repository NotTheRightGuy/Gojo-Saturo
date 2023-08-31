import nextcord


async def on_ready_event(bot):
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="with your feelings"))
    print("================================================================")
    print(f"Logged in as: {bot.user.name}\nid: {bot.user.id}")
    print("================================================================")
    print(f"Nextcord Version: {nextcord.__version__}")
    print("================================================================")
