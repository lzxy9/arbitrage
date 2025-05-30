from bs4 import BeautifulSoup
import requests

url = "https://www.sportsbet.com.au/betting/live-betting"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all li elements with the specific class
items = soup.find_all('li', class_='cardOuterItem_fn8ai8t')

with open('output.txt', 'w', encoding='utf-8') as f:
    for item in items:
        item_text = item.text.strip()  # Gets all text content and removes extra whitespace
        f.write(item_text + '\n')  # Write to file with a newline