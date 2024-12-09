from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('Then I expect that message is decoded as "{msg}"')
def step_impl(context, msg):
    decoded = context.driver.find_element(By.ID, "decoded_message")
    p = decoded.find_element(By.CSS_SELECTOR,"p")
    assert p == msg