import bs4 as bs
import re
from selenium import webdriver

url = 'https://www.flipkart.com/offers/deals-of-the-day?pk=dotd'

driver = webdriver.Firefox()
driver.get(url)           
html = driver.page_source
soup = bs.BeautifulSoup(html,"html.parser")

last_height = driver.execute_script("return document.body.scrollHeight"
