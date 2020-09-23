import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
Bsoup = BeautifulSoup(res.text, 'html.parser')
stories = Bsoup.select('.storylink')
subtext = Bsoup.select('.subtext')



def Top_Scrapped_Hnews(stories, subtext):

    Topnews = []

    for index, items in enumerate(stories):
        title = items.getText()
        links = items.get('href', None)
        score = subtext[index].select('.score')
        if len(score):
            sscore = int(score[0].getText().replace(' points',''))
            Topnews.append({'Title ': title,'Links ': links,'Points ': sscore})
    return sorted(Topnews, key = lambda k:k['Points '],reverse=True )

pprint.pprint(Top_Scrapped_Hnews(stories,subtext))
