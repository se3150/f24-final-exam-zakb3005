from behave import given, when, then
from behave_webdriver.steps import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('I expect that message is encoded as "{msg}"')
def step_impl(context, msg):
    decoded = context.driver.find_element(By.ID, "decoded_message")
    p = decoded.find_element(By.CSS_SELECTOR,"p")
    assert p == msg