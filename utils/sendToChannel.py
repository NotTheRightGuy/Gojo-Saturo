async def send_to_channel(bot, channel_id, message=None, embed=None):
    channel = bot.get_channel(int(channel_id))

    if embed:
        await channel.send(embed=embed)
    elif message:
        await channel.send(message)
    else:
        raise ValueError("Either a message or an embed must be provided.")
