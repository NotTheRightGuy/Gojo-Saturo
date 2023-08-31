import requests
import nextcord


def set_cat(bot):
    @bot.slash_command(description="meow")
    async def cat(ctx: nextcord.Interaction):
        user = ctx.user
        print(f"{user} issued the command /cat")
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        cat_url = data[0]['url']
        await ctx.send(cat_url)
