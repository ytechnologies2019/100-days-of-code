from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print (element.text)
driver.quit()