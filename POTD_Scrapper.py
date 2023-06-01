import requests
from bs4 import BeautifulSoup as soup
import json
from datetime import datetime


def dateFormat(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day = date_obj.strftime('%d')
    suffix = 'th' if 11 <= int(day) <= 13 else {
        1: 'st', 2: 'nd', 3: 'rd'}.get(int(day) % 10, 'th')
    month = date_obj.strftime('%B')
    year = date_obj.strftime('%Y')
    formatted_date = f"{day}{suffix} {month} {year}"
    return formatted_date


def scrapPOTD():
    url = "https://leetcode.com/problemset/all/"
    responseData = requests.get(url)

    page_soup = soup(responseData.text, "html.parser")
    scriptsList = page_soup.find_all('script')[-1]

    scriptJSON = json.loads(scriptsList.text)
    POTD = (scriptJSON["props"]["pageProps"]["dehydratedState"]
            ["queries"][2]["state"]["data"]["dailyCodingChallengeV2"]["challenges"][-1])
    date = POTD["date"]
    link = "https://leetcode.com" + POTD["link"]
    title = POTD["question"]["title"]
    ID = POTD["question"]["questionFrontendId"]
    return {"date": dateFormat(date), "link": link, "id": ID, "title": title}
