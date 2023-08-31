import nextcord


def set_avatar(bot):
    @bot.slash_command(description="Retrieves the avatar of a user.")
    async def avatar(ctx, user: nextcord.Member = None):
        user = user or ctx.user
        print(f"{user} issued the command /avatar")
        avatar_url = user.avatar.url
        await ctx.send(avatar_url)
