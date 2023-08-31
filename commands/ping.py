import time


def set_ping(bot):
    @bot.slash_command(description="pong")
    async def ping(ctx):
        user = ctx.user
        print(f"{user} issued the command /ping")
        start_time = time.monotonic()
        message = await ctx.send("Pong!")
        end_time = time.monotonic()
        await message.edit(content=f"Pong! Response time: {round((end_time - start_time) * 1000)} ms")
