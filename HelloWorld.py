
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Arrange
driver = webdriver.Chrome('C:\Learn\SeleniumDrivers\ChromeDriver\Current\chromedriver')
driver.get("http://www.python.org")
# assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()

# Act
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#Assert
assert "No results found." not in driver.page_source
driver.close()

