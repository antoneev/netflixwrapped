from selenium import webdriver
from getpass import getpass
import time
import csv 

email = input('Enter your email : ')
pwd = getpass('Enter your password : ')

driver = webdriver.Chrome('/Users/antoneev/documents/projects/chromedriver')

driver.get('https://www.netflix.com/login')

#Login

time.sleep(4)

emailadd = driver.find_element_by_name('userLoginId')
emailadd.send_keys(email)

password = driver.find_element_by_name('password')
password.send_keys(pwd)

login = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
login.click()

time.sleep(2)

#Opening 101 pages
#I found 2020 to start and 2019 to end on page 101 after looking through the links 

#getting all results and saving into an array
results = []
i = 0
while i <= 101:
    #changes pg=0-n where n is 101 in this case
    link = 'https://www.netflix.com/api/shakti/vbb0b093a/viewingactivity?pg='+str(i)+'&pgSize=20&guid=NDDK7TQH7FCP3LVKZVQ6DTVRQI&_=1607439903768&authURL=1607439402662.%2FtRYmugjyc2c5ITNc7tzlAca54s%3D'
    driver.execute_script('window.open("{}","_blank");'.format(link))
    driver.switch_to.window(driver.window_handles[-1])
    output = driver.find_element_by_tag_name('body').text
    results.append(output)
    time.sleep(2)
    i += 1

#exit driver
driver.quit()

#saving results into a text file
f= open("allresults.txt","w+")
for j in range(len(results)):
    f.write(results[j])
f.close()   

