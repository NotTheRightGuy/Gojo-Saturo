import requests
from datetime import datetime
from utils.EmbedMaker import make_embed
from utils.sendToChannel import send_to_channel


def fetchContests():
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)
    response = response.json()
    contests = response["result"]
    return contests


def fetchAvailableContest(contests):
    available_contests = []
    for contest in contests:
        if contest["phase"] == "BEFORE":
            available_contests.append(contest)
    return available_contests


def contestAvailableToday(contests):
    today = datetime.today()
    today_contest = []
    for contest in contests:
        contest_date = datetime.fromtimestamp(
            contest["startTimeSeconds"])
        if contest_date.date() == today.date():
            today_contest.append(contest)
    return today_contest


def convert_to_formatted_date_time(input_string):
    dt = datetime.strptime(input_string, '%Y-%m-%d %H:%M:%S')
    day = dt.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = 'th'
    else:
        suffix = ['st', 'nd', 'rd'][day % 10 - 1]
    formatted_date = f"Date : {day}{suffix} {dt.strftime('%B %Y')}"
    formatted_time = f"Time : {dt.strftime('%I:%M %p')}"
    return formatted_date, formatted_time


def createEmbedOfAvailableContest(contest):
    embeds = []
    for contest in contest:
        start_time = convert_to_formatted_date_time(str(datetime.fromtimestamp(
            contest["startTimeSeconds"])))
        embed = make_embed(title=contest["name"], description=f"{start_time[0]}\n{start_time[1]}", color=0x00ff00,
                           url=f"https://codeforces.com/contests/{contest['id']}", thumbnail_url="https://assets.codeforces.com/users/kguseva/comments/cf.png")
        embeds.append(embed)
    return embeds


def embeds_provider():
    contests = fetchContests()
    available_contests = fetchAvailableContest(contests)
    today_contest = contestAvailableToday(available_contests)
    embeds = createEmbedOfAvailableContest(today_contest)
    return embeds


async def sendContestEmbed(bot, channel_id):
    embeds = embeds_provider()
    if embeds:
        print("Sending Contest for {}".format(datetime.today().date()))
    for embed in embeds:
        await send_to_channel(bot, channel_id, embed=embed)
