import json
import logging
import requests
import sys
import argparse

sys.path.append(sys.path[0] + "/..")

from utils.url_utils import is_valid_product_url
from parser.html_parser import extract_linked_urls, extract_product_urls

class Crawler:
    def __init__(self, urls=None, base_domain=None):
        self.visited_urls = []
        self.urls_to_visit = urls or []
        self.base_domain = base_domain

    def download_url(self, url):
        """Download HTML content of a given URL."""
        logging.info(f'Downloading: {url}')
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"Failed to download {url}: {e}")
            return None

    def add_url_to_visit(self, url):
        """Add URL to queue if not visited or queued."""
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def discover_product_urls(self, url):
        """Discover product-specific URLs on a page."""
        logging.info(f'Discovering product URLs on: {url}')
        html = self.download_url(url)
        if html:
            product_urls = extract_product_urls(url, html, self.base_domain)
            # Only mark as visited if not already visited
            if url not in self.visited_urls:
                self.visited_urls.append(url)
            return product_urls
        # Only mark as visited if not already visited
        if url not in self.visited_urls:
            self.visited_urls.append(url)
        return []

    def crawl(self, url):
        """Crawl a single URL and queue linked product URLs."""
        # Skip if already visited
        if url in self.visited_urls:
            logging.info(f"Skipping already visited URL: {url}")
            return

        html = self.download_url(url)
        if html:
            for linked_url in extract_linked_urls(url, html):
                if is_valid_product_url(linked_url, self.base_domain):
                    self.add_url_to_visit(linked_url)
        # Mark as visited after processing
        self.visited_urls.append(url)

    def run(self):
        """Run crawler until queue is empty."""
        while self.urls_to_visit:
            current_url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {current_url}')
            self.crawl(current_url)

    def get_visited_urls(self):
        """Return list of visited URLs."""
        return self.visited_urls
    
    def save_urls(self, filename):
        """Save visited URLs to a JSON file."""
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--filename',
            type=str,
            default="ecommerce_crawled_urls.json",
            help="Path to the JSON file containing URLs to scrape"
        )
        args = parser.parse_args()
        filename = args.filename
        try:
            with open(filename, 'w') as f:
                json.dump(self.visited_urls, f, indent=2)
            logging.info(f"Saved {len(self.visited_urls)} URLs to {filename}")
        except Exception as e:
            logging.error(f"Failed to save URLs to {filename}: {e}")