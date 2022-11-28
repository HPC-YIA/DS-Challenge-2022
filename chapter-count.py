import re
import pip._vendor.requests

from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
# browser =webdriver.Chrome()
browser = webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")  # Path to where I installed the web driver

browser.get('http://classic.austlii.edu.au/au/legis/nt/consol_act/dafva2007254/')

page_text = browser.find_element_by_xpath("html/body/pre").text
# print(page_text)


index_list=[]

c= browser.find_elements(By.XPATH, "//b[contains(text(), 'CHAPTER ')]")
for element in c:
    text=element.text
    # print(text)
    
    index_list.append(text)
print(index_list)

n=0

for x in range(0,len(index_list)):
    total=[]
    if n<len(index_list)-1:
        
        start= page_text.index(index_list[n])
        end = page_text.index(index_list[n+1])
        part= page_text[start:end]
        
        words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
        for word in words:  
            if word.isalpha():
                total.append(word)
        # print(word)
        # print(total)
        print(len(total))
           
        
    else: 
        n == len(index_list)-1
        start= page_text.index(index_list[n])
        end = len(page_text)
        part= page_text[start:end]   
        words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
        for word in words:  
            if word.isalpha():
                total.append(word)
        # print(total)
        print(len(total))
    n=n+1   
    

