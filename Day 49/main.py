from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import environ
import time

load_dotenv()

# --- User credentials from .env ---
ACCOUNT_EMAIL = environ.get("LINKEDIN_EMAIL")
ACCOUNT_PASSWORD = environ.get("LINKEDIN_PASSWORD")
PHONE = environ.get("LINKEDIN_PHONE")

def abort_application(driver):
    try:
        close_btn = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_btn.click()
        time.sleep(2)
        discard_btns = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
        if len(discard_btns) > 1:
            discard_btns[1].click()
    except NoSuchElementException:
        pass

def login_linkedin(driver):
    driver.get("https://www.linkedin.com/jobs/search?keywords=&location=India")
    time.sleep(2)
    try:
        reject_btn = driver.find_element(By.CSS_SELECTOR, 'button[action-type="DENY"]')
        reject_btn.click()
    except NoSuchElementException:
        pass
    time.sleep(2)
    sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_btn.click()
    time.sleep(5)
    driver.find_element(By.ID, "username").send_keys(ACCOUNT_EMAIL)
    pwd_field = driver.find_element(By.ID, "password")
    pwd_field.send_keys(ACCOUNT_PASSWORD)
    pwd_field.send_keys(Keys.ENTER)
    input("Solve the Captcha manually, then press Enter to continue...")

def apply_to_jobs(driver):
    time.sleep(5)
    listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    for listing in listings:
        print("Opening job listing...")
        listing.click()
        time.sleep(2)
        try:
            apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
            apply_btn.click()
            time.sleep(5)
            phone_input = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
            if phone_input.get_attribute("value") == "":
                phone_input.send_keys(PHONE)
            submit_btn = driver.find_element(By.CSS_SELECTOR, "footer button")
            if submit_btn.get_attribute("data-control-name") == "continue_unify":
                abort_application(driver)
                print("Complex application detected, skipping.")
                continue
            print("Submitting application...")
            submit_btn.click()
            time.sleep(2)
            try:
                close_btn = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                close_btn.click()
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            abort_application(driver)
            print("No application button found, skipping.")
            continue

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    try:
        login_linkedin(driver)
        apply_to_jobs(driver)
        time.sleep(5)
    finally:
        pass

if __name__ == "__main__":
    main()
