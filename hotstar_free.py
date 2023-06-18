# live cricket for free
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('/Users/sunilg/Desktop/HotstarFree/chromedriver')
# For Google chrome browser in mac OS
# driver = webdriver.Chrome(service=s)


# For brave browser driver in mac OS
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(service=s, options=brave_options)

# Maximize the browser window to full screen
driver.maximize_window()

# Open the Hotstar website
match_url = "https://www.hotstar.com/in/shows/west-indies-vs-usa/1540023743/live/watch?filters=content_type%3Dsport_live"
driver.get(match_url)

while True:
    # Delete all cookies
    driver.delete_all_cookies()

    # Reload the page
    driver.refresh()

    # Wait for 5 minutes
    time.sleep(290)  # 300 seconds = 5 minutes
    print("running")

# Close the browser when you're done
# driver.quit()
