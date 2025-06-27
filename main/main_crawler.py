# Took some cues from https://github.com/xukai92/crawlerfromscratch

import sys
sys.path.append(sys.path[0] + "/..")

import logging
from crawler.ecommerce_crawler import Crawler
from config.config import BASE_DOMAIN, OUTPUT_CRAWL

""" Configure logging """
# Set the default Log Level to INFO
def setup_logs():
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )

""" The Main Crawler """
def crawler():
    setup_logs()

    # Fetch the crawled domain from the config file 
    start_urls = [BASE_DOMAIN]
    crawler = Crawler(urls=start_urls, base_domain=BASE_DOMAIN)
    
    #### Discover product URLs #####
    # 
    # product_urls = crawler.discover_product_urls(BASE_DOMAIN)
    # logging.info("Discovered Product URLs:")
    # for url in product_urls:
    #     print(url)

    #### Run general crawl ####
    crawler.run()
    logging.info("Crawling Complete\n\n")
    logging.info(f"Crawled URLs saved to file: {OUTPUT_CRAWL}\n")
    for url in crawler.get_visited_urls():
        print(url)
    
    # Save the crawled URLs in a JSON file
    # This will be input to the scraping logic
    crawler.save_urls(OUTPUT_CRAWL)

if __name__ == '__main__':
    crawler()