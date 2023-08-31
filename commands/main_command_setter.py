from . import avatar
from . import cat
from . import dog
from . import helper
from . import ping
from . import userinfo


def setup_all_commands(bot):
    avatar.set_avatar(bot)
    cat.set_cat(bot)
    dog.set_dog(bot)
    helper.set_helper(bot)
    ping.set_ping(bot)
    userinfo.set_userinfo(bot)
