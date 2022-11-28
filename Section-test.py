import re


from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")  # Path to where I installed the web driver

browser.get('http://www5.austlii.edu.au/au/legis/nsw/consol_act/capva2007347/')

s_link=[]


s = browser.find_elements(By.XPATH, "html/body/pre/a")
for s in s:
    s=s.get_attribute("href")
    if s!= None:
        if s.endswith(('.html')):
            s_link.append(s)

new_link=s_link[1:len(s_link)]
# print(new_link)

driver = webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")

n=0
new=''

    
driver.get(new_link[12])



ss=driver.find_element_by_xpath("html/body").get_attribute("outerHTML")
for s in ss:
    
    new=new+s

# print(new)

section_count=[]
tag="b"
b_section="<"+ tag +">(.*?)</"+tag+">"
section = re.findall(b_section,new)
first_section=str(section[0])
for word in first_section:
    section_count=first_section.split()
    
print(section_count)        
print(len(section_count))
    


        
