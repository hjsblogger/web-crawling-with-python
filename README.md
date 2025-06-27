# Web Crawling with Python

<img width="1000" height="500" alt="cover-image" src="https://github.com/user-attachments/assets/840330c8-b856-4376-9148-5466b57ab3f3">
<div align="center">Image generated using Grok</a></div>
<br/>

In this 'Web Crawling with Python' repo, we have covered the following scenario:

Unique links from [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/) are crawled using Beautiful Soup. Content (i.e., product meta-data) from the crawled content is than scraped with Beautiful Soup. I have a detailed blog & repo on **Web Scraping with Python**, details below:

* [Blog - Web Scraping with Python](https://www.lambdatest.com/blog/web-scraping-with-python/)
* [Repo - Web Scraping with Python](https://github.com/hjsblogger/web-scraping-with-python)

## Pre-requisites for test execution

**Step 1**

Create a virtual environment by triggering the *virtualenv venv* command on the terminal

```bash
virtualenv venv
```
<img width="1418" alt="VirtualEnvironment" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/89beb6af-549f-42ac-a063-e5f715018ef8">

**Step 2**

Navigate the newly created virtual environment by triggering the *source venv/bin/activate* command on the terminal

```bash
source venv/bin/activate
```

Follow steps(3) and (4) for performing web scraping on LambdaTest Cloud Grid:

**Step 3**

Run the *make install* command on the terminal to install the desired packages (or dependencies) - Beautiful Soup,urrlib3, etc.

```bash
make install
```

<img width="1413" alt="make-install" src="https://github.com/user-attachments/assets/9780b589-86cc-43d0-ab88-7bbccfef8663" />

With this, all the dependencies and environment variables are set. We are all set for web crawling with Beautiful Soup (bs4).

## Web Crawling using Beautiful Soup

Follow the below mentioned steps to for crawling the [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

**Step 1**

Trigger the command ```make clean``` to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="cover-image" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1baf2aeb-fab1-4207-8547-4c07a70074c2">
<br/>

**Step 2**

Trigger the ```make crawl-ecommerce-playground``` command on the terminal to crawl the LambdaTest E-Commerce Playground

<img width="939" alt="web-crawling-1" src="https://github.com/user-attachments/assets/e748ea89-5e5a-43df-8b19-13ba6d78d5e0" />

<img width="1154" alt="web-crawling-2" src="https://github.com/user-attachments/assets/79fbc9d5-a060-4411-96ed-b452b4ebdb19" />

As seen above, the content from LambdaTest E-commerce playground was crawled successfully! Fifty five unique product links are now available to be scraped in the exported JSON file (i.e., ecommerce_crawled_urls.json)

**Step 3**

Now that we have the crawled information, trigger the ```make scrap-ecommerce-playground``` command on the terminal to scrap the product information (i.e., product name, product price, product availability, etc.) from the exported JSON file.

<img width="1181" alt="web-scraping-1" src="https://github.com/user-attachments/assets/238d6d34-388b-4671-9249-e0e1358b90b2" />

<img width="1153" alt="web-scraping-2" src="https://github.com/user-attachments/assets/a2f06f81-c2a1-45b1-851e-fb35debb8dcf" />

Also, all the 55 links on are scraped without any issues!

## Have feedback or need assistance?
Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)<br/>
<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)