from bs4 import BeautifulSoup
import lxml

import requests

# response = requests.get("https://news.ycombinator.com/")
# soup = BeautifulSoup(response.text, "lxml")
#
# link = soup.find_all("a", class_="storylink")
#
# # for article in link:
# #     print(article.string)
# #     print(article.get("href"))
# #     print('')
# # print(link)
#
#
# up_vote = soup.find_all(name="span", class_="score")
# up_vote_list = [score.string.split()[0] for score in up_vote]
# print(up_vote_list)
# for vote in up_vote:
#     print()
# print(up_vote)
# with open("website.html", 'r', encoding="utf-8") as file:
#     contents = file.read()
#
# # print(contents)
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup) #original
# # print(soup.title) #<title>Angela's Personal Site</title>
# # print(soup.title.name) #title
# # print(soup.title.string) #Angela's Personal Site
# # print(soup.prettify()) #美化過html
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# all_class = soup.find_all(name='h3', class_='heading')
#
# for classs in all_class:
#     print(classs.getText())
# # print(all_class)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# heading = soup.select('.heading')
# print(heading)