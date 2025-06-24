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
        # Download HTML content of a given URL
        logging.info(f'Downloading: {url}')
        try:
            response = requests.get(url)
            response.raise_for_status()
            # Return the HTML content if the response status is 200 (i.e. HTTP_OK)
            return response.text
        except requests.RequestException as e:
            # In case of issues, return an exception
            logging.error(f"Failed to download {url}: {e}")
            return None

    def add_url_to_visit(self, url):
        # Add URL to queue if not visited or queued
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    # Replicated this logic from 
    # https://github.com/hjsblogger/web-scraping-with-python
    # Start - Ignore this code block
    def discover_product_urls(self, url):
        # Discover product-specific URLs on a page
        logging.info(f'Discovering product URLs on: {url}')
        html = self.download_url(url)
        # Now that the HTML content is ready, let's extract the meta-data from the pages
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
    # End - Ignore this code block

    def crawl(self, url):
        # Crawl a single URL and queue linked product URLs
        # Skip if already visited
        if url in self.visited_urls:
            logging.info(f"Skipping already visited URL: {url}")
            return

        # Once the have the response as 200, the next set of steps
        # in crawling are executed 
        html = self.download_url(url)
        if html:
            for linked_url in extract_linked_urls(url, html):
                if is_valid_product_url(linked_url, self.base_domain):
                    # Append the URL to the Visit List
                    # print(f'Linked URL:{linked_url}')
                    self.add_url_to_visit(linked_url)
        # Mark the input URL as visited so that we do not revisit it again
        self.visited_urls.append(url)

    def run(self):
        while self.urls_to_visit:
            # Run crawler until queue is empty
            current_url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {current_url}')
            # Crawl using the core logic
            self.crawl(current_url)

    def get_visited_urls(self):
        # Return list of visited URLs
        return self.visited_urls
    
    def save_urls(self, filename):
        # Save visited URLs to a JSON file
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