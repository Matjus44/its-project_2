from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from time import sleep
    
# Test 10

@given(u'Admin is in "dashboard"')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/")
    context.driver.find_element(By.XPATH, '//*[@id="input-username"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-username"]').send_keys("user")
    context.driver.find_element(By.XPATH, '//*[@id="input-password"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR,".fa-solid.fa-key").click()

@given(u'clicks on "Catalog"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="menu-catalog"]/a').click()

@when(u'clicks on the "Products" tab')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="collapse-1"]/li[2]/a').click()

@then(u'list of products should apper')
def step_impl(context):
    # Wait for the element to be present
    element_xpath = '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[2]'
    product_element = WebDriverWait(context.driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, element_xpath))
    )

    # Check if the element is clickable, which also implies it is visible
    WebDriverWait(context.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, element_xpath))
    )

    # If no exceptions were thrown by the WebDriverWait, the element is present and clickable
    assert product_element, "The product element is not present or not clickable."

#Test 11
@given(u'clicks on "sales"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="menu-sale"]/a').click()

@given(u'clicks on "Orders"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="collapse-4"]/li[1]/a').click()

@when(u'admin clicks on empty small square of the order and click on "delete"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="form-order"]/div[1]/table/tbody/tr/td[1]/input[1]').click()
    context.driver.find_element(By.XPATH,'//*[@id="button-delete"]').click()
    alert = Alert(context.driver)
    alert.accept()
    sleep(1)

@then(u'Order should not appear in order anymore')
def step_impl(context):
    # Wait for the alert to be visible
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="alert"]'))
    )
    # Retrieve the text of the alert to confirm it's the expected success message
    alert_text = context.driver.find_element(By.XPATH, '//*[@id="alert"]').text
    assert alert_text == 'Success: You have modified orders!'

#Test 12
@given(u'clicks on the "Products" tab')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="collapse-1"]/li[2]/a').click()

@when(u'Admin clicks on the "Add New" button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div/a').click()

@when(u'Fill up necessary information')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="input-name-1"]').send_keys("iPod shivler")
    context.driver.find_element(By.XPATH, '//*[@id="input-meta-title-1"]').send_keys("shivlertag")
    context.driver.find_element(By.XPATH,'//*[@id="form-product"]/ul/li[2]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-model"]').send_keys("shifflerrerermodel")
    context.driver.find_element(By.XPATH,'//*[@id="form-product"]/ul/li[11]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-keyword-0-1"]').send_keys("shifflerrererseo")

@when(u'clicks on the "Save" button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div/button/i').click()
    sleep(1)

@then(u'The product is created')
def step_impl(context):
    # Wait for the alert to be visible
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="alert"]'))
    )
    # Retrieve the text of the alert to confirm it's the expected success message
    alert_text = context.driver.find_element(By.XPATH, '//*[@id="alert"]').text
    assert alert_text == 'Success: You have modified products!'

#Test 13

@given(u'Admin is in catalog')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/")
    context.driver.find_element(By.XPATH, '//*[@id="input-username"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-username"]').send_keys("user")
    context.driver.find_element(By.XPATH, '//*[@id="input-password"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR,".fa-solid.fa-key").click()
    context.driver.find_element(By.XPATH,'//*[@id="menu-catalog"]/a').click()

@when(u'Admin clicks on the "Edit" button next to the product to be updated')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[7]/td[7]/div/a').click()

@when(u'changes the product details')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="input-name-1"]').clear()
    context.driver.find_element(By.XPATH, '//*[@id="input-name-1"]').send_keys("iPod Changed_name")

@when(u'Admin clicks on the "Save" button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div/button').click()

@then(u'The product shows the updated details')
def step_impl(context):
    # Wait for the alert to be visible
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="alert"]'))
    )
    # Retrieve the text of the alert to confirm it's the expected success message
    alert_text = context.driver.find_element(By.XPATH, '//*[@id="alert"]').text
    assert alert_text == 'Success: You have modified products!'

# Test 14

@when(u'Admin checks the checkmark next to the product to be deleted')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="form-product"]/div[1]/table/tbody/tr[10]/td[1]/input').click()

@when(u'clicks on the "Delete" button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div/button[3]').click()

@then(u'The product is deleted')
def step_impl(context):
    alert = Alert(context.driver)
    alert.accept()
    sleep(1)

#Test 15

@when(u'Admin clicks on the "Edit" buttom of "Apple Cinema 30"')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[7]/div/a').click()

@when(u'changes quantity from 990 to 988')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="form-product"]/ul/li[2]/a').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-quantity"]').clear()
    context.driver.find_element(By.XPATH,'//*[@id="input-quantity"]').send_keys("988")


@when(u'admin will click on the "Save" button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div/button/i').click()
    sleep(1)

@then(u'The product shows the updated quantity')
def step_impl(context):
    # Wait for the alert to be visible
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="alert"]'))
    )
    # Retrieve the text of the alert to confirm it's the expected success message
    alert_text = context.driver.find_element(By.XPATH, '//*[@id="alert"]').text
    assert alert_text == 'Success: You have modified products!'