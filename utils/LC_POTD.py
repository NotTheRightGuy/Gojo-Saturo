import requests
from bs4 import BeautifulSoup as soup
import json
from . import dateFormater


def LC_POTD():
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
    return {"date": dateFormater.dateFormater(date), "link": link, "id": ID, "title": title}
