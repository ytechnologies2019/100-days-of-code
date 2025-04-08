from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Python.org homepage
driver.get("https://www.python.org/")

# Get all event times using plural `find_elements`
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_name  = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')
# Print each time
events = {

}

for n in range(len(event_times)):
    events[n] = {
        'time' : event_times[n].text ,
        'name' : event_name[n].text
    }

    print(events)

# for time in event_times:
#     print(time.text)
#
# for name in event_name:
#     print (name.text)

# Close the browser
driver.quit()
