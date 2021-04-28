import requests
import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup

##function takes in array of youtube links
def youtubeViews(input):
	videos = input
	views = []
	for video in videos:
		if type(video) == str:
			video = video.split("\n")
			for url in video:
				url = url.split(" ")
				for link in url:
					output = scrape(link)
					if output:
						views.append(output)
	return views

def scrape(link):
	if link[0:5] == 'https':
		soup = BeautifulSoup(requests.get(link).text, 'lxml')
		return soup.find(itemprop="interactionCount")['content']
	return None

##test
monthlyResponses = "Core_Affiliate_February.csv"
monthlyResponsesDf = pd.read_csv("inputs/" + monthlyResponses)
x = monthlyResponsesDf["If your primary platform is YouTube, please link all new Core videos for the month of February below. "]
print(youtubeViews(x))
