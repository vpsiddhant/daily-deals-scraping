import bs4 as bs
import re
from selenium import webdriver
import time

def pauseva():
	for i in range(1,16):
		time.sleep(1)
		print i
	return

SCROLL_PAUSE_TIME = 5

url = 'https://www.flipkart.com/offers/deals-of-the-day?pk=dotd'

driver = webdriver.Firefox()
driver.get(url)           

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5)")
pauseva()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4)")
pauseva()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
pauseva()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2)")
pauseva()

html = driver.page_source
soup = bs.BeautifulSoup(html,"html.parser")

div = soup.find_all('div', attrs={'class' : 'iUmrbN'})
print div[0]

