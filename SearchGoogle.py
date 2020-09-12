#Search for "jhdsfkjfhskdfjhdskjfhskjfhkajhdsjkfhkdsj987897898979" in Google.com 
# and see if you "did not match any documents" in page source


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# # Arrange
driver = webdriver.Chrome('C:\Learn\SeleniumDrivers\ChromeDriver\Current\chromedriver')
driver.get("https://www.google.com/")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()

# # Act
elem.send_keys("jhdsfkjfhskdfjhdskjfhskjfhkajhdsjkfhkdsj987897898979")
elem.send_keys(Keys.RETURN)

# #Assert
assert "did not match any documents." in driver.page_source
# driver.close()

