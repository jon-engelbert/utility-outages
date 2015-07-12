 #!/usr/local/bin/python

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()

driver.get("http://stormcenter.oncor.com/default.html")

assert "Oncor Storm Center" in driver.title

summarytab = driver.find_element_by_xpath("//li[@id='summary_tab']/a")
summarytab.click()

# try:
#     county_outages_button = WebDriverWait(driver, 10).until(
#         # EC.presence_of_element_located((By.ID, "simpleoutagereport_link"))
#         EC.presence_of_element_located((By.XPATH, '//*[@id="simpleoutagereport_link"]'))
#     )
# finally:
#     driver.quit()
county_outages_button = driver.find_element_by_xpath('//*[@id="simpleoutagereport_link"]')
county_outages_button.click()
WebDriverWait(driver, 10)

driver.quit()

# elem = driver.find_element_by_name("q")

# elem.send_keys("pycon")

# elem.send_keys(Keys.RETURN)

# assert "No results found." not in driver.page_source
