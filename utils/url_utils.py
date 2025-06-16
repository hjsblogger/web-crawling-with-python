import sys
sys.path.append(sys.path[0] + "/..")

from urllib.parse import urljoin
from config.config import IGNORE_FRAGMENTS, PRODUCT_URL_PATTERN, BASE_DOMAIN

def is_valid_product_url(url, base_domain):
    """Check if URL is a valid product URL."""
    return (
        PRODUCT_URL_PATTERN in url
        and url.startswith(base_domain)
        and not any(fragment in url for fragment in IGNORE_FRAGMENTS)
    )

def make_absolute_url(base_url, href):
    """Convert relative URL to absolute URL."""
    return urljoin(base_url, href)