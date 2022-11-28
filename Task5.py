

import re


from selenium import webdriver
from selenium.webdriver.common.by import By
# browser =webdriver.Chrome()

browser = webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")  # Path to where I installed the web driver

browser.get('https://itcodefair.cdu.edu.au/data-science-challenge/')


driver= webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")

##~~~~~~~~~~~~~~~~~~`get legislation urls~~~~~~~~~~~~~~~~~~~~`####
urls=[]

u=browser.find_elements(By.XPATH, "//div[@class='elementor-widget-container']//table//tbody//tr//td//p//a")
for url in u:
    url=url.get_attribute('innerHTML')
    urls.append(url)
# print(urls)

            
##~~~~~~~~~~~~~~~~~~`get each legislation 's endnote link ~~~~~~~~~~~~~~~~~~~~`####            
endnote_link=[]
for u in urls:
    driver.get(u)
    a=driver.find_elements(By.XPATH, "html/body/pre/a")
    # print(endnote)
    for each in a:
        each= each.get_attribute("href")
        if each!= None:
            if each.endswith(('endnotes')):
                endnote_link.append(each)
    
# print(endnote_link)

##~~~~~~~~~~~~~~~~~~`get each legislation 's title ~~~~~~~~~~~~~~~~~~~~`####
for l in endnote_link:
    titlelist=[]
    amend_list=[]
    yearlist=[]
    
    if 'nt' in l:
        driver.get(l)
        title=driver.find_element_by_xpath("html/body/h3").text
        title_split=title.split()
        new_title=title_split[0:-4]
        new_title=(' '.join(new_title)).lower()
        
        # print(new_title)
    
        abbr= driver.find_elements(By.XPATH, "html//body//p//table//tbody//tr//td//p//b//i[contains(text(), new_title )]")
        for element in abbr:
            text=element.text
            titlelist.append(text)
        # print(len(titlelist))   
        for li in titlelist:
            li=li.split()
            new_li=li[-1]
            yearlist.append(new_li)
        # print(yearlist)
    elif  'vic' in l:
        driver.get(l)
        
    
        b_list= driver.find_elements(By.XPATH, "html//body//p//font//b")
        for b in b_list:
            b=b.text
            if  b != 'Family Violence Protection Act 2008':
              titlelist.append(b)
        amend_list=titlelist[18:]
        # print(amend_list)
        # print(len(amend_list))
        for al in amend_list:
            
            new_li=al[-4:]
            yearlist.append(new_li)
        # print(yearlist)
        
    else:
        driver.get(l) 
        b_list= driver.find_elements(By.XPATH, "html/body/p/font/b")
        for b in b_list:
            b=b.text
            
            if 'Act' in b:
                titlelist.append(b)
        # print(len(titlelist))
        for li in titlelist:
            new=li.split()
            for y in new:
                if y.isnumeric():
                    if len(y)==4:
                        yearlist.append(y)
        print(yearlist)
                    
            
            
            
            
      
           
            
                
    

        
driver.quit()
browser.quit()