import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML content from the file
with open('mediamarkt.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

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
