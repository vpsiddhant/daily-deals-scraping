import bs4 as bs
import re
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

url_part_1 = "https://www.amazon.in/gp/goldbox/ref=gbps_ftr_s-4_9f70_page_"
url_part_2= "1"

url_part_3= "?tag=googinabkkenshoo-21&ascsubtag=a114bce1-fe84-4eef-9499-48f8c0f66d32&gb_f_GB-SUPPLE=page:2,sortOrder:BY_SCORE,dealsPerPage:32&pf_rd_p=c03a86b1-0b29-4f8f-b42f-5ef1f2019f70&pf_rd_s=slot-4&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=H4VKT0VGVHW1830R7TZD&ie=UTF8"

url = url_part_1 + url_part_2 +url_part_3

#HEADLESS BROWSER
options = Options()
options.set_headless(headless=True)

driver = webdriver.Firefox(firefox_options=options)
driver.get(url)

#GETTING SOURCE CODE OF THE WEBPAGE
html = driver.page_source
soup = bs.BeautifulSoup(html,"html.parser")

#GETTING THE NAME OF THE ITEM
div = soup.find_all('div', attrs={'class' : 'a-row dealContainer dealTile'})

name = []
for i in range(0,len(div)):
	item = div[i]

	name.append(item.div.div.img["alt"])


#discount = bs.BeautifulSoup(str(div[0]),"html.parser")
div2 = soup.find('div', attrs = {'class' : 'a-row priceBlock unitLineHeight'})

soup2 = bs.BeautifulSoup(div2[0],"html.parser")
span = soup2.find('span', attrs={'class' : 'a-size-base a-color-base inlineBlock unitLineHeight'})

print span



