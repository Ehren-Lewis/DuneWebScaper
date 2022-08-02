from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, NoSuchElementException
import functools
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


"""
This is a webscraping/ some sort of automation project. To actually get me started, this first py will be a
brainstorming area to see what I may want to webscrape, the intentions, etc...

- What libraries can I use to make this simpler?
- BeautifulSoup, Requests, MatPlotLib, Sqlite3, Pandas, Numpy


"""
"""
Second iteration: show all reviews on the website : done 
Third iteration: filter review by the types : done
Fourth iteration: add more ways to represent data : wip
Fifth iteration: search by movie that you want to see the results for
Sixth iteration: Create a Gui, ask which data (maybe how much they want), 
and how they would like to present the data
"""


def find_char(string: str, character: str):
    return True if character in string else False


def nan_score_adder(missing_score_list: list):  # no errors at all
    full_review_without_missing_scores = []
    for i in missing_score_list:
        append_string = i
        if not find_char(append_string, "Original Score"):
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
    print(number_list)
    common_denominator_list = []
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



def new_number_score_to_common_score_converter(number_list):
    only_number = []
    for i in range(len(number_list)):
        if (number_list[i] != "NaN"):
            only_number.append(number_list[i])



    common_denominator_list = []
    for numb_str in only_number:
        new_str = numb_str
        if len(new_str) == 1 and new_str.isnumeric():
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
        except IndexError as e:
            continue

        finally:
            try:
                if second_number == 10:
                    common_denominator_list.append(f"{round(first_number, 1)}/10")
                    continue
                x = (first_number * 10) / second_number
                x = round(x, 1)
                common_denominator_list.append(f"{x}/10")
            except TypeError as e:
                print(new_str)
                print(numb_str)


    return common_denominator_list

#  Testing new code
def remove_nan_from_list(complete_list):
    data_only_list = []
    for x in complete_list:
        if x == "NaN":
            continue
        data_only_list.append(x)
    return data_only_list


# look at fixing this one for data representation
def occurrences_of_scores(number_only_list):
    count = 0
    test_occurrence_dict = {}
    total_occurrence_of_score = []
    occurrence_score_start_number = []
    for score in number_only_list:
        if score in test_occurrence_dict:
            test_occurrence_dict[score] += 1
        elif score not in test_occurrence_dict:
            test_occurrence_dict[score] = 0
        count += 1

    for key in test_occurrence_dict:
        if test_occurrence_dict[key] != 0:
            occurrence_score_start_number.append(key)
            total_occurrence_of_score.append(test_occurrence_dict[key])

    return [occurrence_score_start_number, total_occurrence_of_score, count]  # look a fi  # look atf

"""
suggestions on data representation:
stacked bar chart, bar histogram, scatter plot, 
pie chart, 
"""


def been_called(func):
    @functools.wraps(func)
    def is_it_called(*args, **kwargs):
        is_it_called.has_been_called = True
        return func(*args, **kwargs)

    is_it_called.has_been_called = False
    return is_it_called


def how_big_data_size():
    data_size = ''
    while not data_size.isnumeric():
        data_size = input("How big would you like the dataset to be? (whole numbers only)")

    return int(data_size)


def selenium_initializer():
    full_review_list = []
    # s = Service("C:/Webdriver/bin/chromedriver.exe")
    s = Service("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    with webdriver.Chrome(service=s) as driver:
        driver.get("https://www.rottentomatoes.com/m/dune_2021/reviews")

        @been_called
        def all_critics():
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[1]/a').click()
                return_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/nav/button[2]/span')
            except Exception as e:
                print(e)
            else:
                return return_button

        @been_called
        def top_critics():
            try:
                # driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[2]/a').click()
                # button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/nav[1]/button[2]/span')
                button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/nav[1]/button[2]/span')
            except NoSuchElementException as e:
                print(e)
            else:
                return button

        @been_called
        def all_audience():
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[3]/a').click()
                button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[3]/button[2]')
            except Exception as e:
                print(e)
            else:
                return button

        @been_called
        def verified_audience():
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[1]/ul/li[4]/a').click()
                button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/nav[3]/button[2]/span')
            except Exception as e:
                print(e)
            else:
                return button

        def critic_parser(parser_info):
            append_list = []
            review_info = parser_info.find_all("div", {"class": "small subtle review-link"})
            for i in review_info:
                append_list.append(i.get_text(strip=True))
            return append_list

        def audience_parser(parser_info):
            append_list = []
            review_info = parser_info.find_all('span', {"class": "star-display"})
            for star in review_info:
                full_stars = star.findAll('span', {'class': 'star-display__filled'})
                half_stars = star.findAll('span', {'class': 'star-display__half'})
                out_of = len(full_stars) + len(half_stars) * .5
                append_list.append(f"{out_of * 2}/10")
            return append_list

        final_button = top_critics()
        global full_review
        full_review = False

        while True:
            html = driver.page_source
            soup_2 = BeautifulSoup(html, 'html.parser')

            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable(final_button))
            except TimeoutException:
                if not final_button.is_displayed():
                    full_review = True
                if len(full_review_list) == 0:
                    driver.close()
                    break
                return full_review_list

            if all_critics.has_been_called or top_critics.has_been_called:
                for individual_review in critic_parser(soup_2):
                    full_review_list.append(individual_review)
                try:
                    final_button.click()
                except ElementNotInteractableException:
                    driver.close()
                    break

            elif all_audience.has_been_called or verified_audience.has_been_called:
                for other_review in audience_parser(soup_2):
                    full_review_list.append(other_review)
                try:
                    final_button.click()
                except ElementNotInteractableException:
                    driver.close()
                    break


def bar_graph_data_representation(proper_list):
    scores = proper_list[0]
    occurrences = proper_list[1]
    plt.figure()
    plt.bar(scores, occurrences)
    plt.ylabel('Occurrences')
    plt.xlabel("Score")
    plt.title("Starting Value of Each Score for Dune Reviews")
    plt.show()


def pie_chart_representation(proper_list):
    scores = proper_list[0]
    sizes = [x / proper_list[2] for x in proper_list[1]]
    plt.figure()
    plt.pie(sizes, labels=scores, autopct='%1.1f%%')
    plt.show()


review_with_missing_scores = selenium_initializer()
print(review_with_missing_scores)
review_without_missing_scores = nan_score_adder(review_with_missing_scores)
non_equal_number_review = letter_score_to_number_score_converter(review_without_missing_scores)
# common_denom_scores_with_nan = new_number_score_to_common_score_converter(non_equal_number_review)
data_without_nan = new_number_score_to_common_score_converter(non_equal_number_review)
sorted_data = sorted(data_without_nan, key=lambda x: (len(x), x))

graphical_list = occurrences_of_scores(sorted_data)

df = pd.DataFrame(sorted_data, columns=['Score'])

bar_graph_data_representation(graphical_list)
# pie_chart_representation(graphical_list)


def search_with_selenium(movie_to_search="Dune"):
    s = Service("C:/Webdriver/bin/chromedriver.exe")

    # movie_to_search = input("What movie would you like to search for?")

    search_url = f'https://www.rottentomatoes.com/search?search={movie_to_search}'

    with webdriver.Chrome(service=s) as driver:
        driver.get(search_url)
        driver.implicitly_wait(10)
        try:
            driver.find_element(By.XPATH,
                            '//*[@id="main-page-content"]/div/section[1]/search-page-result-container/nav/ul/li[2]').click()
        except NoSuchElementException:
            driver.close()
            print("sorry, there were no results to display")
            return



        html_info = driver.page_source
        soup_info = BeautifulSoup(html_info, 'html.parser')

        movie_names = soup_info.find_all('a', {'class': 'unset'})
        movie_name_test = soup_info.find_all('a', {'data-qa': 'thumbnail-link'})
        href_list = []
        src_list = []
        names_list = []
        return_list = []

        for movie in movie_name_test:
            src = movie.contents[1]
            src_list.append(src.attrs['src'])
            href_list.append(movie['href'])
            names_list.append(src.attrs['alt'])

        for i in range(len(href_list)):
            return_list.append((names_list[i], href_list[i], src_list[i]))


        return return_list

        driver.implicitly_wait(10)

# search_with_selenium()



