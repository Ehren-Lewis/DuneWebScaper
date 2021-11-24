"""
This is a webscraping/ some sort of automation project. To actually get me started, this first py will be a
brainstorming area to see what I may want to webscrape, the intentions, etc...

- After data has been scraped, clean it, analyze it, then display in matplotlib
- How should automation play a role? Maybe two separate projects?
- What libraries can I use to make this simpler?
- BeautifulSoup, Requests, MatPlotLib, Sqlite3, Pandas, Numpy


"""
"""
Second iteration: show all reviews on the website
Third iteration: filter review by the types,
fourth iterations: search by movie that you want to see the results for

feature: have a default way they want to show the data, then ask if they want a specific
way to see it (only the ones that are plausible with the dataset

"""

import pandas
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import matplotlib.pyplot as plt

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


def create_review_lists():
    score_list = []
    count = 1
    for i in small_review:
        non_split_review = i.get_text(strip=True)
        score_list.append(non_split_review)
        count += 1
    return score_list


def nan_score_adder(missing_score_list: list):
    full_review_without_missing_scores = []
    for i in missing_score_list:
        append_string = i
        if not find_char(i, "|"):
            append_string += "| Original Score: NaN"
        full_review_without_missing_scores.append(append_string.split(": ")[1])
    return full_review_without_missing_scores


def letter_score_to_number_score_converter(string_list: list):
    letter_to_number_dict = {"A+": "9.8/10", "a+": "9.8/10", "A": "9.5/10", "a": "9.5", "A-": "9.1/10", "a-": "9.1/10",
                             "B+": "8.8/10", "b+": "8.8/10", "B": "8.5/10", "b": "8.5/10", "B-": "8.1/10",
                             "b-": "8.1/10",
                             "C+": "7.8/10", "c+": "7.8/10", "C": "7.5/10", "c": "7.5/10", "C-": "7.1/10",
                             "c-": "7.1/10",
                             "D+": "6.8/10", "d+": "6.8/10", "D": "6.5/10", "d": "6.5/10", "D-": "6.1/10",
                             "d-": "6.1/10",
                             "E": "5.5/10", "e": "5.5/10"}
    full_review_without_letters = []
    for i in string_list:
        score_to_append = i
        if score_to_append != "NaN" and score_to_append.isalpha():
            score_to_append = letter_to_number_dict[score_to_append]

        full_review_without_letters.append(score_to_append)
    return full_review_without_letters


def number_score_to_common_score_converter(number_list):
    common_denominator_list = []
    x = None
    '''
    3    x
    - =  - : first numb* 10 / second numb = x
    4   10
        '''

    for numb_str in number_list:
        if numb_str == "NaN":
            common_denominator_list.append(numb_str)
            continue
        number_test = numb_str.split("/")
        first_number = float(number_test[0])
        second_number = float(number_test[1])

        if second_number == 10:
            common_denominator_list.append(f"{round(first_number, 1)}/10")
            continue
        x = (first_number * 10) / second_number
        x = round(x, 1)
        common_denominator_list.append(f"{x}/10")
    return common_denominator_list


def remove_nan_from_list(complete_list):
    data_only_list = []
    for x in complete_list:
        if x == "NaN":
            continue
        data_only_list.append(x)
    return data_only_list


def occurrences_of_scores(number_only_list):
    occurrence_dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
                       "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0}
    total_occurrence_of_score = []
    occurrence_score_start_number = []
    for score in number_only_list:
        occurrence_dict[score[0]] += 1

    for key in occurrence_dict:
        if occurrence_dict[key] != 0:
            print(key, occurrence_dict[key])
            occurrence_score_start_number.append(key)
            total_occurrence_of_score.append(occurrence_dict[key])

    return [occurrence_score_start_number, total_occurrence_of_score]


review_with_missing_scores = create_review_lists()
review_without_missing_scores = nan_score_adder(review_with_missing_scores)
non_equal_number_review = letter_score_to_number_score_converter(review_without_missing_scores)
common_denom_scores_with_nan = number_score_to_common_score_converter(non_equal_number_review)
data_without_nan = remove_nan_from_list(common_denom_scores_with_nan)
data_without_nan.sort()
graphical_list = occurrences_of_scores(data_without_nan)

df = pd.DataFrame(data_without_nan, columns=['Score'])

"""
suggestions on data representation:
stacked bar chart, bar histogram, scatter plot, 
"""

# ax.bar(scores, occurrences)
scores = graphical_list[0]
occurrences = graphical_list[1]

fig = plt.figure()
plt.bar(scores, occurrences)
plt.ylabel('Occurrences')
plt.xlabel("Score")
plt.title("Starting Value of Each Score for Dune Reviews")
plt.show()
