import scrapy
from scrapy.linkextractors import LinkExtractor
import pandas as pd

# This spider will help us in scraping the google search data for that particular company name and post and we will further scrape top 10 search results from linkedin
class LinkedJobsSpider(scrapy.Spider):
    name = "linkedin_website_scrape"   
    def start_requests(self):
        company_name = input("Enter company name: ")
        post = input("Enter post: ")

        company_name = company_name.replace(" ", "+")
        post = post.replace(" ", "+")
        # Limiting the url for only search related to linkedin
        linkedin_website_url = f"https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+AND+%22{post}%22+AND+%22{company_name}%22&source=desktop"
        
        yield scrapy.Request(url=linkedin_website_url, callback=self.parse_url)
            

    def parse_url(self, response):
        df = pd.DataFrame()
        xlink = LinkExtractor()
        link_list=[]
        for link in xlink.extract_links(response):
        # here we will filter out pure links and will save them in output.csv
         if 'linkedin.com' in link.url  and 'google.com' not in link.url:
            print(len(str(link)),link.url,link,"\n")
            link_list.append(link.url)
            
        print('length ', len(link_list))
        df['links']=link_list
        df.to_csv(f"output.csv")