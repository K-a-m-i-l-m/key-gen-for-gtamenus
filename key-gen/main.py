import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Add Options.
options = webdriver.ChromeOptions()


# Add adblocker to Options.
options.add_extension('./ublock.crx')


# Add Browser.
driver = webdriver.Chrome(options=options)


# Delay for the Adblocker to load.
time.sleep(1)

# Repeat.
for i in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    try:
        # Access Website.
        driver.get("https://linkvertise.com/249307/GravityLicense")

        # Delay
        time.sleep(1)

        # Click the "Access with Free button in Linkvertise"
        driver.find_element_by_class_name('lv-dark-btn').click()

        # Delay before restarting.
        time.sleep(1)
    except:
        # Waiting a Amount of time if a error is happened ( Should prevent from linkvertise delays )
        time.sleep(18)
