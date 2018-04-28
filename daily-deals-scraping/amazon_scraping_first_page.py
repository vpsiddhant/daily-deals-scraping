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

print len(name)
#GETTING THE DISCOUNT PERCENTAGE

div2 = soup.find_all('div', attrs = {'class' : 'a-row dealDetailContainer'})
discount = []
for i in range(0,len(div2)):
	item = div2[i].findAll('span', attrs={'class':'a-size-base a-color-base inlineBlock unitLineHeight'},text= True)

	discount.append(item[1])

discount2 = []
for i in range(0,len(discount)):
	stringva = str(discount[i])
	start = stringva.find('(')
	end = stringva.find(')')
	price = stringva[start + 1:end]
	discount2.append(price)

filename = "amazon.csv"

f = open(filename,"w")

headers = "Product , Deals \n"

f.write(headers)
for i in range(0,len(discount2)):
	#print name[i] + " , " + discount2[i]
	f.write(name[i].encode('utf-8').strip().replace(","," ") + "," + discount2[i].encode('utf-8').strip().replace(","," ") + "\n")




f.close()
driver.close()
