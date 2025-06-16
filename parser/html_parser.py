import sys
sys.path.append(sys.path[0] + "/..")

from bs4 import BeautifulSoup
from utils.url_utils import make_absolute_url, is_valid_product_url

def extract_linked_urls(base_url, html):
    """Extract all linked URLs from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a', href=True):
        yield make_absolute_url(base_url, link['href'])

def extract_product_urls(base_url, html, base_domain):
    """Extract product-specific URLs from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    product_links = set()
    for a_tag in soup.select("a[href]"):
        href = a_tag['href']
        absolute_url = make_absolute_url(base_url, href)
        if is_valid_product_url(absolute_url, base_domain):
            product_links.add(absolute_url)
    return list(product_links)