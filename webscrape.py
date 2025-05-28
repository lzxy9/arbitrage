from bs4 import BeautifulSoup
import requests

url = "https://www.sportsbet.com.au/betting/live-betting"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all li elements with the specific class
items = soup.find_all('li', class_='cardOuterItem_fn8ai8t')

for item in items:
    # Extract data from each item as needed
    print(item.text)  # Gets all text content
    # Or find specific elements within each li
    # price = item.find('span', class_='price-class').text