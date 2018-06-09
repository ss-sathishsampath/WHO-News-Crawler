
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 02:21:35 2018

@author: Sathish Sampath(ss.sathishsampath@gmail.com)

"""

from mechanize import Browser
from bs4 import BeautifulSoup as BS
import schedule
import time

total_news = []
url = "http://www.who.int/news-room/releases" 

def crawler():
    global url
    global total_new
    agent = Browser()
    agent.addheaders = [('User-agent', 'Firefox')]
    agent.set_handle_robots(True)  
    agent.set_handle_refresh(False) 
    
    agent_data = agent.open(url)
    soup = BS(agent_data.read(), "lxml")
    
    for row in soup.find_all('div',attrs={"class" : "list-view--item vertical-list-item"}):   
        link = row.find('a')['href']
        date = row.find('span',attrs={"class" : "timestamp"}).text
        text = row.find('p',attrs={"class" : "heading text-underline"}).text
        if {"date": date, "news":text, "link": link} not in total_news:
            total_news.append({"date": date, "news": text, "link": link})


schedule.every().day.at("07:30").do(crawler)



while 1:
    schedule.run_pending()
    time.sleep(1)