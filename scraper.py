import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://ta.wikipedia.org/wiki/%E0%AE%AE%E0%AF%81%E0%AE%A4%E0%AE%B2%E0%AE%BE%E0%AE%AE%E0%AF%8D_%E0%AE%87%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AE%B0%E0%AE%BE%E0%AE%9C_%E0%AE%9A%E0%AF%8B%E0%AE%B4%E0%AE%A9%E0%AF%8D'  # Replace with the URL you want to scrape

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'lxml')

    # Extract data (example: all paragraphs)
    data = []
    for p in soup.find_all('p'):
        data.append(p.get_text())

    # Export to a text file with UTF-8 encoding
    with open('data.txt', 'w', encoding='utf-8') as text_file:
        for paragraph in data:
            text_file.write(paragraph + '\n\n')  # Each paragraph separated by a newline

    print('Data has been exported to data.txt')
else:
    print('Failed to retrieve the webpage')
