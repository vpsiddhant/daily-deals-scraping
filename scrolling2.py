import bs4 as bs
import re
from selenium import webdriver
import time

def pauseva():
	for i in range(1,61):
		time.sleep(1)
		print i
	return

SCROLL_PAUSE_TIME = 5

url = 'https://www.flipkart.com/offers/deals-of-the-day?pk=dotd'

driver = webdriver.Firefox()
driver.get(url)           
html = driver.page_source
soup = bs.BeautifulSoup(html,"html.parser")

#last_height = driver.execute_script("return document.body.scrollHeight")

#for i in range(0,1000):
	#for j in range(0,1000):
	#	continue

#driver.execute_script("window.scrollTo(0, 1320);")
pauseva()

#scheight = .1
#while scheight < 9.9:
 #   driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
  #  scheight += .01

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5)")
pauseva()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4)")
pauseva()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
pauseva()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2)")
pauseva()

div = soup.find_all('div', attrs={'class' : 'col col-3-12'})
print len(div)

#time.sleep(SCROLL_PAUSE_TIME)


