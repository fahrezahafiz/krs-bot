from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import WebDriverException

# constants
# path to webdriver
BASE_URL = "https://krs.simak.ipb.ac.id"
PATH = 'C:\Program Files (x86)\msedgedriver.exe'
USERNAME = ''
PASSWORD = ''

# initialize webdriver
driver = webdriver.Edge(PATH)


def login(username: str, password: str):
    """
        Login menuju krs.simak.ipb.ac.id kemudian standby di page /krs
    """
    driver.get(BASE_URL)

    # login
    uname_field = driver.find_element_by_id('input-username')
    uname_field.send_keys(username)
    pwd_field = driver.find_element_by_id('input-password')
    pwd_field.send_keys(password, Keys.RETURN)

    # wait for page to load then click "Isi KRS" button
    btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/krs"]')))
    btn.click()


if __name__ == '__main__':
    login(USERNAME, PASSWORD)

    print('Commands\n(q: quit, r: reload)')
    while True:
        arg = input("> ")
        if arg == 'q':
            driver.quit()
            break
        elif arg == 'r':
            try:
                driver.refresh()
            except WebDriverException:
                break

    # time.sleep(5)
    # driver.quit()

