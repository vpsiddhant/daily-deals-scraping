# daily-deals-scraping
I am making a API/website/csv where I display daily amazon and flipkart sales by scraping their webpage

You need selenium and BeautifulSoup to run this program
You also need firefox to run this program
You also need geckodrivers to run selenium for firefox

sudo pip install selenium
sudo pip install bs4

flipkart.py scrapes the daily flipkart deals and inserts in a csv
amazon.py scrapes all amzon deals and inserts in a csv, but since amazon has 313 pages of deals dont run it unless you have lot of time
amazon_scraping_first_page.py scrapes the deals from first page of amazon
