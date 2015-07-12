 #!/usr/local/bin/python

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, getopt

# driver.get("http://stormcenter.oncor.com/default.html")
def main(argv):
	inputfile = ''
	outputfile = ''
	try:
	  opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
	  print 'test.py -i <inputfile> -o <outputfile>'
	  sys.exit(2)
	for opt, arg in opts:
	  if opt == '-h':
	     print 'test.py -i <inputfile> -o <outputfile>'
	     sys.exit()
	  elif opt in ("-i", "--ifile"):
	     inputfile = arg
	     print 'in- ' +inputfile
	  elif opt in ("-o", "--ofile"):
	     outputfile = arg
	     print 'out-' + outputfile
	f = file(outputfile, 'w')
	sys.stdout = f

	county_outages_button = None
	driver = webdriver.Chrome()
	# driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
	driver.implicitly_wait(10)

	driver.get(inputfile)

# assert "Storm Center" in driver.title

	summarytab = driver.find_element_by_xpath("//li[@id='summary_tab']/a")
	summarytab.click()

	# try:
	#     county_outages_button = WebDriverWait(driver, 20).until(
	#         # EC.presence_of_element_located((By.ID, "simpleoutagereport_link"))
	#         EC.presence_of_element_located((By.XPATH, '//*[@id="simpleoutagereport_link"]'))
	#     )
	# finally:
	#     driver.quit()
# county_outages_button = driver.find_element_by_id('simpleoutagereport_link')
# county_outages_button.click()
	# WebDriverWait(driver, 500)
	# driver.switch_to_frame(0)
	# county_frame = driver.find_element_by_id("_yuiResizeMonitor")
# iframe = driver.find_elements_by_tag_name('iframe')
# print >> f, ("iframe: {}",  repr(iframe))
	# while len(iframe) < 2:
	# 	WebDriverWait(driver, 100)
# driver.switch_to.frame(iframe[1])

	# WebDriverWait(driver, 100)
	# driver.switch_to.frame(county_frame)
	print >> f, ("driver.current_url: {}",  driver.current_url)

	WebDriverWait(driver, 100)
	textTable = ''
# while len(textTable) < 1000:
# 	outputTable = driver.find_element_by_id('outageReportTable')
# 	textTable = outputTable.get_attribute('innerHTML')
# 	print >> f, ('outageReportTable')
# 	# print(textTable)
# 	outputTotalTable = driver.find_element_by_id('outageReportTotalTable')
# 	text = outputTotalTable.get_attribute('innerHTML')
# 	print>> f,  ('outageReportTotalTable')
# 	print >> f, (text)
	# WebDriverWait(driver, 500)
# customer_outage_total = None
# customer_outage_total = driver.find_element_by_xpath('//*[@id="outageReportTotalTable"]/tbody/tr/td[2]')
	# try:
	#     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
	#     WebDriverWait(driver, 10).until(customer_outage_total = driver.find_element_by_xpath('//*[@id="colTotal2"]'))

	# finally:
	#     print "Unexpected error:", sys.exc_info()[0]
	#     driver.quit()
	# print("customer_outage_total: {}", repr(driver.find_element_by_xpath('//*[@id="outageReportTotalTable"]/tbody/tr/td[0]')))
	customer_outage_total = driver.find_element_by_id('num_custs_text')
	print >> f, ("customer_outage_total: {}, {}", repr(customer_outage_total), customer_outage_total.text)

	driver.close()

if __name__ == "__main__":
    main(sys.argv[1:])
# elem = driver.find_element_by_name("q")

# elem.send_keys("pycon")

# elem.send_keys(Keys.RETURN)

# assert "No results found." not in driver.page_source
