from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\msedgedriver.exe"

driver = webdriver.Edge(PATH)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver.get("https://techwithtim.net")
    print(driver.title)

    search = driver.find_element_by_name('s')
    search.send_keys('test')
    search.send_keys(Keys.RETURN)

    # time.sleep(5)
    # driver.quit()

