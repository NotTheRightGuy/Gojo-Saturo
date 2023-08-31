import nextcord


def set_helper(bot):
    @bot.slash_command(description="alright im here to help")
    async def helper(interaction: nextcord.Interaction):
        user = interaction.user
        print(f"{user} issued the command /help")
        await interaction.response.send_message(f"**Hello I'm {bot.user}**\n*My commands are as follows:*\n\n`!slap !sendtochannel !codelink`\n\n*And some slash commands ;)*")
