
import nextcord


def set_userinfo(bot):
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
        embed.add_field(name="Account Created On",
                        value=created_at, inline=False)
        embed.add_field(name="Joined This Server On",
                        value=joined_at, inline=False)
        embed.add_field(name="Roles", value=", ".join(roles), inline=False)
        embed.add_field(name="Status", value=user.status, inline=False)
        embed.add_field(name="User ID", value=user_id, inline=False)
        embed.add_field(name="Activity", value=user.activity, inline=False)
        await ctx.send(embed=embed)
