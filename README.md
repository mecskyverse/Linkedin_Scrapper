# linkedin-scraper

This Scrapy project contains 2 seperate spiders:

| Spider  |      Description      |
|----------|-------------|
| `linkedin_website_scrape` |  Scrapes data from google search  
| `linkedin_people_profile` |  Scrapes people data from LinkedIn people profile pages. | 



## ScrapeOps Proxy
This LinkedIn spider uses [ScrapeOps Proxy](https://scrapeops.io/proxy-aggregator/) as the proxy solution. ScrapeOps has a free plan that allows you to make up to 1,000 requests per month, but can be easily scaled up to millions of pages per month if needs be.

You can [sign up for a free API key here](https://scrapeops.io/app/register/main).


## Here are the steps to setup project
`git clone https://github.com/mecskyverse/Linkedin_Scrapper.git`<br/>
Change the directory to linkedin: `cd linkedin`<br/>
Create a Python Virtual Environment: `python3 -m venv venv`<br/>
Activate the Python Virtual Environment: `source venv/bin/activate`<br/>
Install Scrapy using pip: `pip install scrapy scrapeops-scrapy pandas openpyxl scrapeops-scrapy-proxy-sdk`<br/>
Listing the scrapy projects `scrapy list`<br/>
Firstly run crawler for scraping search result from google: `scrapy crawl linkedin_website_crawl`<br/>
then run another crawler for scanning those search results on linkedin: `scrapy crawl linkedin_people_profile`<br/>



Then activate the ScrapeOps Proxy by adding your API key to the `SCRAPEOPS_API_KEY` in the ``settings.py`` file.

```python

SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}


```
