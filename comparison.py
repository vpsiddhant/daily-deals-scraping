from bs4 import BeautifulSoup as soup
from urllib2 import urlopen


my_url = "https://www.flipkart.com/offers/deals-of-the-day?pk=dotd"

client = urlopen(my_url)
page_html = client.read()
client.close()

page_soup = soup(page_html, "html.parser")

#print page_soup.body
#print page_soup.find_all('div',{"class":"col col-3-12"})

#print len(page_soup.find_all("div", class_="col col-3-12"))

#print len(page_soup.findAll("div",{'class':"col col-3-12"}))

print page_soup.find_all('div', attrs={'class' : 'col col-3-12'})
