import scrapy
from scrapy.crawler import CrawlerRunner
from crochet import setup
import requests
from scrapy.http import TextResponse

setup()

url ='https://www.google.co.in'
url='https://www.tesco.com/groceries/en-GB/search?query=sensodyne&icid=tescohp_sws-1_m-ft_in-sensodyne_out-sensodyne&viewAll=promotion&promotion=offers'

print("Started")
r=requests.get(url)
print("Started 1")
response = TextResponse(r.url, body=r.text, encoding="utf-8")
print("Done"+response)
d = response.css('a').extract()
print(d)