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

# score_review = soup.find_all(string=re.compile("Original Score"))  # Score


def find_char(string: str, character: str):
    return True if character in string else False


def add_nan_for_missing_scores(score_list: list):
    for score in score_list:
        pass


review = []  # for calculations
review_with_missing_scores = []  # for dataframe
count = 1

for i in small_review:
    non_split_review = i.get_text(strip=True)
    review_with_missing_scores.append(non_split_review)

    if find_char(non_split_review, "|"):
        review.append((count, non_split_review.split(" ")[4]))

    count += 1

full_review_without_missing_scores = []

for i in review_with_missing_scores:
    append_string = i
    if not find_char(i, "|"):
        append_string += "| Original Score: NaN"
    full_review_without_missing_scores.append(append_string.split(": ")[1])


full_review_without_letters = []

def letter_score_to_number_score_converter(string_list: list):
    # instad of if checks, find different way to check the value of score_to_append
    for i in string_list:
        score_to_append = i
        if score_to_append != "NaN" and score_to_append.isalpha():
            if score_to_append == "A" or score_to_append == "a":
                score_to_append = "9.5/10"
            elif score_to_append == "B" or score_to_append == "b":
                score_to_append = "8.5/10"
            elif score_to_append == "C" or score_to_append == "c":
                score_to_append = "7.5/10"
            elif score_to_append == "D" or score_to_append == "d":
                score_to_append = "6.5/10"

        full_review_without_letters.append(score_to_append)




def number_score_to_common_score_converter():
    pass


df = pd.DataFrame(full_review_without_missing_scores, columns=["Score"])

# print(df)

letter_score_to_number_score_converter(full_review_without_missing_scores)

df_new = pd.DataFrame(full_review_without_letters, columns=['Score'])
print(df_new)