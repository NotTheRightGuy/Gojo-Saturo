import requests
import nextcord


def set_dog(bot):
    @bot.slash_command(description="bow")
    async def dog(interaction: nextcord.Interaction):
        user = interaction.user
        print(f"{user} issued the command /dog")
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        image_link = response.json()["message"]
        await interaction.response.send_message(image_link)
