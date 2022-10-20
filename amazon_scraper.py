from bs4 import BeautifulSoup
from openpyxl import workbook
import csv
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\setup\\ChromeDriver\\chromedriver_win32\\chromedriver.exe")
book_name = input('Which Books Author Do you Want: ')
book_name = book_name.replace(' ','+')
url = f"https://www.amazon.in/s?k={book_name}&i=stripbooks&ref=nb_sb_noss"
print(url)
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')
section = soup.find('a',class_='a-size-base').text
print(section)
## Comments Below
