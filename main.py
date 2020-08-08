from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# constants
# path to webdriver
PATH = "C:\Program Files (x86)\msedgedriver.exe"
BASE_URL = "https://krs.simak.ipb.ac.id"
USERNAME = 'fahreza_12'
PASSWORD = '279654066abc'

# initialize webdriver
driver = webdriver.Edge(PATH)


def login(username: str, password: str):
    """
        Login menuju krs.simak.ipb.ac.id kemudian standby di page /krs
    """
    driver.get(BASE_URL)

    # login
    username_field = driver.find_element_by_id('input-username')
    username_field.send_keys(username)
    password_field = driver.find_element_by_id('input-password')
    password_field.send_keys(password, Keys.RETURN)

    # wait for page to load then click "Isi KRS" button
    btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/krs"]')))
    btn.click()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    login(USERNAME, PASSWORD)

    print('Commands\n(q: quit, r: reload)')
    while True:
        arg = input("> ")
        if arg == 'q':
            driver.quit()
            break
        elif arg == 'r':
            driver.refresh()

    # time.sleep(5)
    # driver.quit()

