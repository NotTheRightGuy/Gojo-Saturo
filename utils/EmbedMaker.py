from nextcord import Embed


def make_embed(title="", description=None, color=None, url="", thumbnail_url="", additonal_fields=[]):
    """
    Makes an embed with the given parameters

    Args:
        title (str, optional): Title of the embed. Defaults to "".
        description (str, optional): Description of the embed. Defaults to "".
        color (str, optional): Color of the embed. Defaults to "".
        url (str, optional): URL of the embed. Defaults to "".
        thumbnail_url (str, optional): Thumbnail URL of the embed. Defaults to "".
        additonal_fields (list, optional): List of dictionaries containing the fields to be added. Defaults to [].

    Returns:
        Embed: The embed with the given parameters

    """
    embed = Embed(title=title, description=description, color=color, url=url)
    embed.set_thumbnail(url=thumbnail_url)
    for field in additonal_fields:
        embed.add_field(name=field["name"],
                        value=field["value"], inline=True)
    embed.set_footer(text="Happy Coding!")
    return embed
