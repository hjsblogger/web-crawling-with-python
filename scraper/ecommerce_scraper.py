#Beautiful Soup Official Documentation - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Import the locators file
import sys
import json
import logging
import requests
from bs4 import BeautifulSoup
import argparse
from pprint import pprint
sys.path.append(sys.path[0] + "/..")

#  @hjsblogger - This is only for reference
#  The URLs will be added from the scraping logic

def setup_logging():
    """Configure logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def load_urls(filename):
    """Load URLs from a JSON file created by the crawler."""
    try:
        with open(filename, 'r') as f:
            urls = json.load(f)
        print(f"Loaded {len(urls)} URLs from {filename}")
        return urls
    except Exception as e:
        print(f"Failed to load URLs from {filename}: {e}")
        return []
    
def print_scrapped_content(meta_data):
        for elem_info in meta_data:
            print(elem_info)

visited_urls = [
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=36",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=40",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=28",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=30",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=47",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=107",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=106",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=105",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=104",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=103",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=102",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=101",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=100",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=99",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=98",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=42",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=36",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=29",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=32",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=34",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=31",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=45",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=41",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=33",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=49",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=43",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=46",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=48",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=44",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=90",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=50",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=89",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=88",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=97",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=96",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=95",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=94",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=93",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=92",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=91",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=87",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=86",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=85",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=84",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=55",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=63",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=66",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=53",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=40",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=68",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=69",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=28",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=30",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=47",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=107",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=106",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=105",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=104",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=103",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=102",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=101",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=100",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=99",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=98",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=42",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=54",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=76",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=77",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=78",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=79",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=36",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=29",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=32",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=34",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=31",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=45",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=41",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=33",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=49",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=43",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=46",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=48",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=44",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=90",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=50",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=89",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=88",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=97",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=96",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=95",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=94",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=93",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=92",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=91",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=87",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=86",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=85",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=84",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=55",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=63",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=66",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=53",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=68",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=69",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=54",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=76",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=77",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=78",
    "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=79"
]


def scrap_ecommerce(url) -> list:
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Unable to fetch the page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # rows = soup.select('.product-layout.product-grid.no-desc.col-xl-4.col-lg-4.col-md-4.col-sm-6.col-6')
    # print(len(rows))

    meta_data_arr = []

    # for row in rows:
    # link = soup.find("a", class_='carousel d-block slide')
    # name = soup.find("h3", class_='title')
    # price = soup.find("span", class_='price-new')

    name = soup.find('h1', class_='h3')
    brand = soup.find("span", class_='ls-label', string="Brand:")
    # if brand:
    #     brand_tag = brand.find_next_sibling("a")  
    #     if brand_tag:
    #         print(brand_tag.text.strip())  # Output: HTC

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
        'product name': name.get_text(),
        # Find the immediate sibling <a> tag and print the text
        'product brand': brand.find_next_sibling("a").get_text().strip(),
        'product price': price.get_text(),
        'product availability': stock_txt
    }
    
    meta_data_arr.append(meta_data_dict)
    return meta_data_arr

# Pagination - 1:5
# Page 1: https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57&page=1
# Page 5: https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57&page=5
# if __name__ == '__main__':
#     for iteration in range(1,2):
#         test_url = locators.test_bs4_url + "&page=" + str(iteration)
#         meta_data_arr = scrap_ecommerce("https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=36")
#         print('\n')
#         # print("Product Page = " + test_url)
#         print("*********************************************************************************************************\n")
#         helpers.print_scrapped_content(meta_data_arr)

if __name__ == '__main__':
    # url_size = len(visited_urls)
    # urls = load_urls("ecommerce_crawled_urls.json")
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--filename',
        type=str,
        default="ecommerce_crawled_urls.json",
        help="Path to the JSON file containing URLs to scrape"
    )
    args = parser.parse_args()
    
    urls = args.filename
    url_size = len(urls)  # Get the number of URLs
    logging.info(f"Total URLs to scrape: {url_size}")
    for iteration in range(1,url_size):
        # test_url = locators.test_bs4_url + "&page=" + str(iteration)
        print(visited_urls[iteration])
        meta_data_arr = scrap_ecommerce(url = visited_urls[iteration])
        # print("Product Page = " + test_url)
        print_scrapped_content(meta_data_arr)