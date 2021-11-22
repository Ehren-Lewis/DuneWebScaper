"""
This is a webscraping/ some sort of automation project. To actually get me started, this first py will be a
brainstorming area to see what I may want to webscrape, the intentions, etc...

- After data has been scraped, clean it, analyze it, then display in matplotlib
- How should automation play a role? Maybe two separate projects?
- What libraries can I use to make this simpler?
- BeautifulSoup, Requests, MatPlotLib, Sqlite3, Pandas, Numpy


"""
import pandas
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
url = "https://www.rottentomatoes.com/m/dune_2021/reviews"
website_url = requests.get("https://www.rottentomatoes.com/m/dune_2021/reviews")

soup = BeautifulSoup(website_url.text, 'html.parser')

# print(soup.prettify())

# print(soup.find_all("div", {"class": "review_area"}))
# print(soup.find_all("div", {"class": "the_review"})) # the review itself
"""
salt=page where the buttons are
hasNextPage as to find if there are more pages, 
"""

small_review = soup.find_all("div", {"class": "small subtle review-link"})  # Score and href

score_review = soup.find_all(string=re.compile("Original Score"))  # Score

def find_char(string, character):
    return True if character in string else False


review = review_with_missing_scores = []
for i in small_review:
    non_split_review = i.get_text(strip=True)
    review_with_missing_scores.append(non_split_review)
    if find_char(non_split_review, "|"):
        review.append(non_split_review)

for i in review:
    print(i)
