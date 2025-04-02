import requests
from bs4 import BeautifulSoup

# Fetch the webpage
response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text

# Parse the HTML
soup = BeautifulSoup(yc_webpage, 'html.parser')


# Print the title of the page
print(soup.title.text)

# Extract the first article title
article_tag     = soup.find('span', class_='titleline').find('a')
article_link    = article_tag.getText()
article_vote    = article_tag.get('href')
article_upvote  = soup.find(name='span' , class_='score').getText()
print(article_tag)
print(article_link)
print(article_vote)
print(article_upvote)