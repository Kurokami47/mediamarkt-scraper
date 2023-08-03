from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://www.mediamarkt.es/es/product/_secadora-aeg-t7dbg841-bomba-de-calor-8-kg-a-blanco-1455590.html'

driver = webdriver.Chrome() 

try:
    driver.get(url)
    # Sleep to allow the page to load (you can adjust the time as needed)
    time.sleep(10)

    # Get the page source after JavaScript execution
    page_source = driver.page_source

    # Parse the page source using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    # Extracting the title, price, and description
    title_element = soup.find('h1', class_='sc-hLBbgP')
    title = title_element.text.strip() if title_element else "Title not found"

    price_element = soup.find('span', {'data-test': 'branded-price-whole-value'})
    price = price_element.text.strip() if price_element else "Price not found"

    description_element = soup.find('div', class_='index-styled__StyledPdpContentArea-sc-55a771f1-0 hkjvvF')
    description = description_element.text.strip() if description_element else "Description not found"

    # Create a DataFrame
    data = {
        'Title': [title],
        'Price': [price],
        'Description': [description]
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('output.csv', index=False)

    # Print the DataFrame
    print(df)

finally:
    driver.quit()
