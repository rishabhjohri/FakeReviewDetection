import requests 
from bs4 import BeautifulSoup

#import time
#import random as rand 

import pandas as pd

review_dict = {'name':[], 'date':[], 'rating':[], 'review':[]}

for page in range(0,23): #Remember to update the number of pages 
    url = 'https://www.metacritic.com/game/switch/pokemon-sword/user-reviews?page='+str(page)
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = requests.get(url, headers = user_agent)
    #time.sleep(rand.randint(3,30)) 
    soup = BeautifulSoup(response.text, 'html.parser')
    for review in soup.find_all('div', class_='review_content'):
        if review.find('div', class_='name') == None:
                       break 
        review_dict['name'].append(review.find('div', class_='name').find('a').text)
        review_dict['date'].append(review.find('div', class_='date').text)
        review_dict['rating'].append(review.find('div', class_='review_grade').find_all('div')[0].text)
        if review.find('span', class_='blurb blurb_expanded'):
            review_dict['review'].append(review.find('span', class_='blurb blurb_expanded').text)
        else:
            review_dict['review'].append(review.find('div', class_='review_body').find('span').text)

sword_reviews = pd.DataFrame(review_dict)  
