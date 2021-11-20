'''
Going to Ethically Scrap From https://news.ycombinator.com/news or Hacker News
'''

import requests
from bs4 import BeautifulSoup
from pprint import pprint

responce = requests.get(r'https://news.ycombinator.com/news')
soup = BeautifulSoup(responce.text, 'html.parser')

# print(soup.find(id='score_29288618'))

links = soup.select(".titlelink")
votes = soup.select(".span")
subtext = soup.select(".subtext")


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_link(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[0].get_text()
        href = item.get('href', None)
        # href = links[0].get('href', None) # Also could have bee there
        vote = subtext[idx].select('.score')
        if len(vote):
            point = int(vote[0].get_text().replace('points', ''))
        else:
            point = 0
        if point > 99:
            hn.append({
                'title': title,
                'link': href,
                'votes': point
            })

    return sort_by_votes(hn)


pprint(create_custom_link(links, subtext))


# -> find will find when it first appeared
# -> find_all will find everywhere it occurred
# -> select is css selector
