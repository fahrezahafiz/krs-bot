from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import WebDriverException
from selenium.webdriver.support.ui import Select
import numpy as np

import time
import re

# constants
# path to webdriver
BASE_URL = "https://krs.simak.ipb.ac.id"
PATH = 'C:\Program Files (x86)\msedgedriver.exe'
USERNAME = 'fahreza_12'
PASSWORD = '279654066abc'
COURSE_IDS = [
    'IKK233',
    'EKO201',
]

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


def enroll_sc(target_ids):
    # loop through targets
    for target in target_ids:
        print('TARGET: {}'.format(target))
        # get list of course objects
        dd_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'multiselect__select')))
        dd_btn.click()
        sc_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.multiselect__content')))
        # sc_dropdown = driver.find_element_by_css_selector('ul.multiselect__content')
        courses = sc_dropdown.find_elements_by_tag_name('li')

        # extract course ids
        courses_text = [c.text for c in courses]
        courses_id = [c_text.split('\n')[1].split(' - ')[0] for c_text in courses_text if len(c_text) > 1]

        # click on course
        idx = courses_id.index(target)
        print('Memilih course {}\n'.format(courses[idx].text))
        courses[idx].click()

        # TODO: pick schedule

        # save course
        save_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-sm')))
        save_btn.click()
        time.sleep(1)


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
        elif arg == 'p':
            enroll_sc(COURSE_IDS)

    # time.sleep(5)
    # driver.quit()
