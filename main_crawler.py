import sys
sys.path.append(sys.path[0] + "/..")

import logging
from crawler.ecommerce_crawler import Crawler
from config.config import BASE_DOMAIN

def setup_logging():
    """Configure logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def crawler():
    """Main execution function."""
    setup_logging()
    start_urls = [BASE_DOMAIN]
    crawler = Crawler(urls=start_urls, base_domain=BASE_DOMAIN)
    
    # Discover product URLs
    # product_urls = crawler.discover_product_urls(BASE_DOMAIN)
    # logging.info("Discovered Product URLs:")
    # for url in product_urls:
    #     print(url)

    # Run general crawl
    crawler.run()
    logging.info("Crawling Complete")
    for url in crawler.get_visited_urls():
        print(url)
    
    # Save the crawled URLs in a JSON file
    # This will be input to the scraping logic
    crawler.save_urls("ecommerce_crawled_urls.json")

if __name__ == '__main__':
    crawler()