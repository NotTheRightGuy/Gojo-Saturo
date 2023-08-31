from bs4 import BeautifulSoup as soup
import requests


def LC_Solution(id):
    if len(str(id)) < 4:
        id = "0" * (4 - len(str(id))) + str(id)
    url = f"https://walkccc.me/LeetCode/problems/{id}/"
    response = requests.get(url)
    page_soup = soup(response.text, "html.parser")
    solution = page_soup.find("code").text
    return f"**Solution : **\n```cpp\n{solution}```"
