from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
#driver.get('https://www.amazon.com/CHEF-iQ-Thermometer-Ultra-Thin-Monitoring/dp/B0C7JNJW2N/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.2f889ce0-246f-467a-a086-d9a721167240&dib=eyJ2IjoiMSJ9.2EzBddTDEktLY8ckTsraM27nKsa9jZ2u6fBw_GWjE7feTKdYVPdPw6K-mZz5Sd2ob4iL_yLtpEzc7hlRoGWQLLrltRGjFSnhiWPpJSbsczPRJ5wdorD3dH-bxgJSjQTKMtpq53PiEqH4TLijE17SK1zLmGU-ZraE9Bc8f6v0zamcG0Ht4kXAgsM25bTsEUIa82xMjDvXo0cAIQEefl6Xrw0zcnS8VR4jVJQdTghwfPQ.NfEUcVZpWKRdNudo9___D6wkz5Kb7jpSdhLsg-aIkVE&dib_tag=se&keywords=cooker&pd_rd_r=5510b043-4529-43db-9870-ea3fefc3192a&pd_rd_w=3og8h&pd_rd_wg=m8quc&qid=1743863776&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent   = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print (f'Price is {price_dollar.text}.{price_cent.text}')

driver.get('https:/python.org')
search_bar = driver.find_element(By.NAME , value='q')

print (search_bar.get_attribute('placeholder'))

button = driver.find_element(By.ID , value='submit')
print (button.size)

bug_link = driver.find_element(By.XPATH ,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print (bug_link.text)

driver.quit()



