from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import time
import functools

"""
This is a webscraping/ some sort of automation project. To actually get me started, this first py will be a
brainstorming area to see what I may want to webscrape, the intentions, etc...

- After data has been scraped, clean it, analyze it, then display in matplotlib
- How should automation play a role? Maybe two separate projects?
- What libraries can I use to make this simpler?
- BeautifulSoup, Requests, MatPlotLib, Sqlite3, Pandas, Numpy


"""
"""
Second iteration: show all reviews on the website : done 
Third iteration: filter review by the types : wip
Fourth iteration: add more ways to represent data
Fifth iterations: search by movie that you want to see the results for
"""


def find_char(string: str, character: str):
    return True if character in string else False


def nan_score_adder(missing_score_list: list):  # no errors at all
    full_review_without_missing_scores = []
    for i in missing_score_list:
        append_string = i
        if not find_char(i, "Original Score"):
            append_string += "| Original Score: NaN"
        full_review_without_missing_scores.append(append_string.split(": ")[1])
    return full_review_without_missing_scores


def letter_score_to_number_score_converter(string_list: list):  # no more errors
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
        try:
            if score_to_append != "NaN" and score_to_append[0].isalpha():
                score_to_append = letter_to_number_dict[score_to_append]
        except KeyError:
            if score_to_append[2:] == 'plus':
                score_to_append = letter_to_number_dict[f"{score_to_append[0]}+"]
            elif score_to_append[2:] == 'minus':
                score_to_append = letter_to_number_dict[f"{score_to_append[0]}-"]
            full_review_without_letters.append(score_to_append)
        except Exception as e:
            print(e)
        else:
            full_review_without_letters.append(score_to_append)
    return full_review_without_letters


def number_score_to_common_score_converter(number_list):
    common_denominator_list = []
    # for numb_str in number_list:
    #     if numb_str == "NaN":
    #         common_denominator_list.append(numb_str)
    #         continue
    #     elif len(numb_str) == 1 and numb_str.isalpha():
    #         common_denominator_list.append(f"{numb_str}/10")
    #         continue
    #     number_test = numb_str.split("/")
    #     try:
    #         first_number = float(number_test[0])
    #     except IndexError as e:
    #         print(e, numb_str, 'first number')
    #     except ValueError as e:
    #         print(e, numb_str, 'first number')
    #
    #     try:
    #         second_number = float(number_test[1])
    #     except IndexError as e:
    #         print(e)
    #         print(numb_str)
    #     except ValueError as e:
    #         print(e)
    #         print(numb_str)
    #
    #     if second_number == 10:
    #         common_denominator_list.append(f"{round(first_number, 1)}/10")
    #         continue
    #     x = (first_number * 10) / second_number
    #     x = round(x, 1)
    #     common_denominator_list.append(f"{x}/10")
    # print(number_of_errors)
    # return common_denominator_list

    for numb_str in number_list:
        new_str = numb_str
        if new_str == "NaN":
            common_denominator_list.append(new_str)
            continue
        elif len(new_str) == 1 and new_str.isnumeric():
            common_denominator_list.append(f"{new_str}/10")
            continue
        first_number = None
        second_number = None
        try:
            number_test = new_str.split("/")
            first_number = float(number_test[0])
            second_number = float(number_test[1])
        except ValueError:
            if find_char(new_str, "out of"):
                out_of_string = new_str.split(" ")
                first_number = float(out_of_string[0])
                second_number = float(out_of_string[-1])
        finally:
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
            occurrence_score_start_number.append(key)
            total_occurrence_of_score.append(occurrence_dict[key])

    return [occurrence_score_start_number, total_occurrence_of_score]


"""
suggestions on data representation:
stacked bar chart, bar histogram, scatter plot, 
"""


def been_called(func):
    @functools.wraps(func)
    def is_it_called(*args, **kwargs):
        is_it_called.has_been_called = True
        return func(*args, **kwargs)

    is_it_called.has_been_called = False
    return is_it_called





def selenium_initializer():
    full_review_list = []
    count = 0
    s = Service("C:/Webdriver/bin/chromedriver.exe")

    with webdriver.Chrome(service=s) as driver:
        new_url = driver.get("https://www.rottentomatoes.com/m/dune_2021/reviews")
        """
        try:  # top critics rating
             driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[2]/a').click()
        except Exception as e:
            print(e)
        try: # by all critics
            driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[1]/a').click()
        except Exception as e:
            print(e)
        """

        @been_called
        def all_critics():
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[3]/a').click()
            except Exception as e:
                print(e)

        @been_called
        def top_critics():
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[4]/a').click()
            except Exception as e:
                print(e)

        @been_called
        def all_audience():
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[3]/a').click()
            except Exception as e:
                print(e)

        @been_called
        def verified_audience():
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[4]/a').click()
            except Exception as e:
                print(e)

        while True:  # change to has next page instead
            html = driver.page_source
            soup_2 = BeautifulSoup(html, 'html.parser')
            """
            if all_critics.has_been_called or top_critics.has_been_called:
                small_review_2 = soup_2.find_all("div", {"class": "small subtle review-link"})  # for critics
                for _ in small_review_2:
                    count += 1
                    non_split_review_2 = _.get_text(strip=True)
                    full_review_list.append(non_split_review_2)

            elif all_audience.has_been_called or verified_audience.has_been_called: 
                new_souped_data = soup_2.find_all('span', {"class": "star-display"})  # for audience
                for i in new_souped_data:
                    full_stars = i.findAll('span', {'class': 'star-display__filled'})
                    half_stars = i.findAll('span', {'class': 'star-display__half'})
                    out_of = len(full_stars) + len(half_stars) * .5
                    print(f"{out_of}/5")
            """
            break

            """
            try:  # where the next may be, works with critics, not audience
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/nav/button[2]').click()
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[3]/button[2]/span').click()
                time.sleep(.1)
            except ElementNotInteractableException:
                print(f"{count} first count")
                return full_review_list
            """

            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[3]/button[2]/span').click()
                time.sleep(.1)
            except ElementNotInteractableException:
                print(f"{count} first count")
                return full_review_list


def bar_graph_data_representation(proper_list):
    scores = proper_list[0]
    occurrences = proper_list[1]
    plt.figure()
    plt.bar(scores, occurrences)
    plt.ylabel('Occurrences')
    plt.xlabel("Score")
    plt.title("Starting Value of Each Score for Dune Reviews")
    plt.show()

# review_with_missing_scores = selenium_initializer()
# review_without_missing_scores = nan_score_adder(review_with_missing_scores)
# non_equal_number_review = letter_score_to_number_score_converter(review_without_missing_scores)
# common_denom_scores_with_nan = number_score_to_common_score_converter(non_equal_number_review)
# data_without_nan = remove_nan_from_list(common_denom_scores_with_nan)
# data_without_nan.sort()
# graphical_list = occurrences_of_scores(data_without_nan)
#
# df = pd.DataFrame(data_without_nan, columns=['Score'])


# print(len(review_with_missing_scores))
# print(len(review_without_missing_scores))
# print(len(non_equal_number_review))
# print(len(common_denom_scores_with_nan))
# print(len(data_without_nan))
