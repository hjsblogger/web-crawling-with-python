import sys
sys.path.append(sys.path[0] + "/..")

from urllib.parse import urljoin
from config.config import IGNORE_FRAGMENTS, PRODUCT_URL_PATTERN, BASE_DOMAIN

def is_valid_product_url(url, base_domain):
    # Check if URL is a valid product URL.
    # Avoid URLs containing IGNORE_FRAGMENTS ==> '#mz', '#cart', '#section'
    return (
        # The raw product URLs are extracted during the crawling process
        # Teh product meta-data from the product pages are further sraped by the scraper
        # https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=79
        # PRODUCT_URL_PATTERN = "product&product_id"
        PRODUCT_URL_PATTERN in url
        and url.startswith(base_domain)
        # URL should not contain any of the values like '#mz', '#cart', '#section'
        and not any(fragment in url for fragment in IGNORE_FRAGMENTS)
    )

def make_absolute_url(base_url, href):
    # Convert relative URL to absolute URL
    # More information on urljoin - https://docs.python.org/3/
    # library/urllib.parse.html#urllib.parse.urljoin
    return urljoin(base_url, href)