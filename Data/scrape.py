from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import csv
import time
# from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()



BASE_URL = "https://www.xwordinfo.com/Crossword?date="

md = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

TEST_URL = "https://www.xwordinfo.com/Crossword?date=1/1/1996"
driver.get(TEST_URL)

for y in range(2022, 2025):
    df = pd.DataFrame(columns=['Clue','Answer','Year', 'Month', 'Date', 'Weekday']) # creates master dataframe 
    for m in range(1, 13):
        for d in range(1, md[m]+1):
            if y == 1993:
                if m < 11:
                    continue
                if m == 11 and d < 21:
                    continue
            url = BASE_URL + str(m) + '/' + str(d) + '/' + str(y)
            weekday = date(y, m, d).weekday()
            driver.get(url)
            cluedivs = driver.find_elements(By.CLASS_NAME, 'numclue')
            for cluetype in cluedivs: 
                inner_divs = cluetype.find_elements(By.TAG_NAME, 'div')
                for i in inner_divs:
                    if len(i.text) <= 3: 
                        continue
                    clueans = i.text.split(":")

                    new_row = {'Clue': clueans[0].strip(), 'Answer': clueans[1].strip(), 'Year': y, "Month": m,
                                'Date': d, "Weekday": weekday}
                    df = df.append(new_row, ignore_index=True)
    df.to_pickle(f'{y}.pkl')
# new_row = {'Clue': 'c', 'Answer': 'a', 'Year': 'y', "Month": 'm',
#                           'Date': 'd', "Weekday": 'dkday'}
# df = df.append(new_row, ignore_index=True)



