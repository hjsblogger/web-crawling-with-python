#Beautiful Soup Official Documentation - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Import the locators file
import sys
import json
import logging
import requests
from bs4 import BeautifulSoup
import argparse
from pprint import pprint
sys.path.append(sys.path[0] + "/../..")

def setup_logs():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )

def load_urls(filename):
    # Load URLs from a JSON file created by the crawler
    try:
        with open(filename, 'r') as f:
            urls = json.load(f)
        logging.info(f"Loaded {len(urls)} URLs from {filename}")
        return urls
    except Exception as e:
        logging.info(f"Failed to load URLs from {filename}: {e}")
        return []
    
def print_scrapped_content(meta_data):
        for elem_info in meta_data:
            logging.info(elem_info)

# Scraping logic is based on the existing implementation
# https://github.com/hjsblogger/web-scraping-with-python/
# blob/main/tests/beautiful-soup/test_ecommerce_scraping.py#L14

def scrap_ecommerce(url) -> list:
    response = requests.get(url)

    if response.status_code != 200:
        logging.info(f"Unable to fetch the page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    meta_data_arr = []

    name = soup.find('h1', class_='h3')
    brand = soup.find("span", class_='ls-label', string="Brand:")

    price = soup.find("h3", class_='price-new mb-0')
    avail_stock = soup.find(class_='badge badge-success')
    out_stock = soup.find(class_='badge badge-danger')

    if avail_stock:
        stock_txt = avail_stock.get_text(strip=True)
    elif out_stock:
        stock_txt = out_stock.get_text(strip=True)
    else:
        stock_txt = "Stock info. unavailable"

    # Create a dictionary of the meta-data of the items on e-commerce store
    meta_data_dict = {
        'product name': name.get_text(strip=True),
        # Find the immediate sibling <a> tag and print the text
        'product brand': brand.find_next_sibling("a").get_text().strip(),
        'product price': price.get_text(strip=True),
        'product availability': stock_txt
    }
    
    meta_data_arr.append(meta_data_dict)
    return meta_data_arr

if __name__ == '__main__':
    setup_logs()
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--filename',
        type=str,
        default="ecommerce_crawled_urls.json",
        help="Path to the JSON file containing URLs to scrape"
    )
    args = parser.parse_args()
    input_url = args.filename

    visited_urls = load_urls(input_url)
    # Count the number of remaining URLs
    url_size = len(visited_urls)
    for iteration in range(1,url_size):
        meta_data_arr = scrap_ecommerce(url = visited_urls[iteration])
        logging.info("\nProduct Page = " + visited_urls[iteration])
        print_scrapped_content(meta_data_arr)

    logging.info(f"\nScraping Complete")