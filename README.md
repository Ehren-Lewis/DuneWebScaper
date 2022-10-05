
# DuneScraper
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Author: Ehren Lewis

## Table Of Contents


* [About This Project](#about-this-project)
* [How to Install](#how-to-install)
* [Usage](#usage)
* [Known Issues](#known-issues)


* [Questions](#questions)
* [License](#license)
* [Contributing](#contributing)


## About This Project

This application is a python command line web scraper that gets the scores from Rotten Tomatoes, converts the scores to one common notation, and then averages the number of appearences for each score, then presents it to the user in an easy to understand format

My motivation is that as someone that loves the movie Dune, I wanted to create an easy way for users to see the average of the scores because I myself wanted to know what the average was.

I used Python, Selenium, BeautifulSoup, and MatPlotLib. Python was used for its data processing and libraries provided that would help get the task done. Selenuim was used to automate the web scraping, allowing for the movement between each score page without any issue. BeautifulSoup was used to gather the HTML of each score page that Selenium went on to get the score information. Once the score information was gathered, MatPlotLib was then used to process the cleaned data and presented in an easy to read format.

Some challenges faced during development was Chrome. Chrome updating to a later version would cause the application to break since Selenium can only run on the chromedriver installed. Another challenge was handling unclean data. Some reviews didn't provide scores. Other reviews supplied letter grades, and other reviews used a different grading system outside of 10. Cleaning the data proved quite challenging to get it all into a common denominator.


## How to Install

1. Navigate to the code repository
2. Press the green code button, located near the about section
3. Copy either the HTTPS, Git CLI, download the zip, open with GitHub desktop, or copy the SSH link.
4. Depending on download method, use Git, executable, or the desktop application to open the content files.
5. All the content of the repository will be available after completion of the previous state.
6. Open the application into your code editor of choice
7. Navigate into the root directory
8. Run pip install -r requirements.txt
9. Run python WebScraping.py
    

## Usage

N/A



## Known Issues

Currently, there is no automatic updating for Chromedriver, as well as instances of where nothing will change from Rotten Tomatoes (no element name switches), and BeautifulSoup won't register the element at all, causing the application to break.









## Questions

You can reach me at my Github: [Ehren-Lewis](https://github.com/Ehren-Lewis)

### OR

You can reach me at my [ehrenlewis0@gmail.com](mailto:ehrenlewis0@gmail.com) pertaining any other questions you may have

## License


MIT License

Copyright (c) 2022 [Ehren Lewis]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Contributing

To contribute to this application, contact me at my Github or through my email address.
