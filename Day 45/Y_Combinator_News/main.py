from bs4 import BeautifulSoup
import requests

# Send a GET request to Hacker News homepage
response = requests.get("https://news.ycombinator.com/")
yc_news_webpage = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(yc_news_webpage, "html.parser")

# Find all article title containers
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

# Extract the text and link for each article
for article_tag in articles:
    a_tag = article_tag.find("a")
    text = a_tag.getText()
    link = a_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

# Extract upvotes for each article
score_tags = soup.find_all(name="span", class_="score")
article_upvotes = [int(score.getText().split()[0]) for score in score_tags]

# Find the article with the most upvotes
max_upvotes = max(article_upvotes)
max_index = article_upvotes.index(max_upvotes)

# Print the article with the highest upvotes
print(f"Article Name: {article_texts[max_index]}\nArticle Link: {article_links[max_index]}\nUpvotes: {max_upvotes}")
