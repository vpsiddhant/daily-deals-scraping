import bs4 as bs
import re
from selenium import webdriver

url = 'https://www.flipkart.com/offers/deals-of-the-day?pk=dotd'

driver = webdriver.Firefox()
driver.get(url)           
html = driver.page_source
soup = bs.BeautifulSoup(html,"html.parser")


driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
div = soup.find_all('div', attrs={'class' : 'col col-3-12'})
print len(div[0])
