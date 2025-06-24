# Domain on which the web crawler would be run
BASE_DOMAIN = "https://ecommerce-playground.lambdatest.io"

# The raw product URLs are extracted during the crawling process
# Teh product meta-data from the product pages are further sraped by the scraper
# https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=79
PRODUCT_URL_PATTERN = "product&product_id"

# Ignore adding pages with the below pattern 
IGNORE_FRAGMENTS = ('#mz', '#cart', '#section')