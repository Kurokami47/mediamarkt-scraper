# Readme.txt
app.py implements selenium but is blocked by cloudfare so if you have a paid vpn or proxy servers you can add it to the script
and implement the scraping

Running the direct_scraper.py scrapes the data from the html I manually got from the website due to site's
anti scraping mechanisms.


## Introduction

This Python script is designed to scrape product data from an online marketplace using web scraping techniques. 
Initially, we attempted automated web scraping using the `requests`, `beautifulsoup4` and 'selenium' libraries. 
However, we encountered anti-bot measures implemented by the website, specifically Cloudfare protection, which prevented 
us from directly accessing the data through automated means.

## Manual HTML Extraction

Due to the Cloudfare protection and other anti-bot mechanisms, I resorted to manually extracting the HTML content of 
the product page. I obtained the HTML content by accessing the webpage through a browser, copying the source code, 
and saving it to a file named `mediamarkt.html`. The code provided in the script reads this file and parses it using 
BeautifulSoup to extract the product's title, price, and description.

## Product Description

As the product description might be in a different language, I haven't applied any trimming or translation to the description. 
The provided script extracts the entire description as it appears in the HTML. If language processing is required, 
additional libraries or services can be utilized to handle translation or text processing.

## Web Scraping with a VPN or Proxy

If access to a paid vpn or proxy is provided it can be done I presume, BUT since its cloudfare it will be tough.

## Usage

1. Before running the script, ensure that you have the required Python libraries installed. You can install them 
using `pip install -r requirements.txt`.

2. Manually obtain the HTML content of the product page you want to scrape and save it to a file named `mediamarkt.html`.

3. Run the provided Python script. It will read the HTML content from the `mediamarkt.html` file, extract the 
product data (title, price, and description), and save the data to a CSV file named `output.csv`.

4. If you have access to a VPN or proxy server and need to scrape the product data directly from the website, 
make sure to modify the script accordingly to use the `requests` and `beautifulsoup4` libraries for web scraping.

