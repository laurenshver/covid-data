import smtplib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.worldometers.info/coronavirus/country/canada/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(20)
site_update_time = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[2]').text.title()
total_cases = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/span').text + ' Total Cases'
active_cases = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div[1]/div/div[2]/div/div[1]/div[1]').text + ' Currently Active Cases'
active_mild = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/span').text + ' Mild Condition'
active_critical = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div[1]/div/div[2]/div/div[1]/div[3]/div[2]/span').text + ' Serious Condition'
closed_cases = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div[2]/div/div[2]/div/div[1]/div[1]').text + ' Closed Cases'
recovered = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div[2]/div/div[2]/div/div[1]/div[3]/div[1]/span').text + ' Recovered/Discharged'
deaths = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/span').text + ' Deaths'
new_cases = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[8]/div/div[2]/div/div/ul/li/strong[1]').text.title()
new_deaths = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[8]/div/div[2]/div/div/ul/li/strong[2]').text.title()
driver.quit()

header = '\rCOVID-19 Data - Canada\n\n' + total_cases + '\n\n'
latest_news = 'Latest News\n' + new_cases + '\n' + new_deaths + '\n\n'
active_text = 'Active Cases\n' +active_cases+ '\n' + active_critical + '\n' + active_mild + '\n\n'
recovered_text = 'Closed Cases\n' + closed_cases + '\n' + recovered + '\n' + deaths + '\n\n'
signature = site_update_time.upper() + '\nScript by Lauren Shver\nSource: ' + url


message = header + latest_news + active_text + recovered_text + signature

receipients = ['lauren_shver@hotmail.com']
to = 'To: lauren-COVID19@outlook.com\n'
subject = 'Subject: COVID-19 Info\n'

smtpObj = smtplib.SMTP('smtp-mail.outlook.com')
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login('lauren-COVID19@outlook.com', 'covid19!Data!auto')
smtpObj.sendmail('lauren-COVID19@outlook.com', receipients, to + subject + message)
smtpObj.quit()

