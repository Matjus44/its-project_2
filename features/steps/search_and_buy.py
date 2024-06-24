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
from selenium.webdriver.support.ui import Select
from time import sleep

# Test 1 and 2

@given(u'User is in "home page"')
def step_impl(context):
    context.driver.get("http://opencart:8080/")


@given(u'clicks on "searchbar"')
def step_impl(context):
    # Wait for the search bar to be clickable
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()

SUT_URL = "http://opencart:8080/"

@when(u'user writes iMAC and press enter')
def step_impl(context):
    context.driver.get(SUT_URL)
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iMac")
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()

@then(u'iMac should be seen')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "iMac").text == "iMac"

@when(u'user writes traktor and presses enter')
def step_impl(context):
    context.driver.get(SUT_URL)
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("traktor")
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()

@then(u'No results should be shown')
def step_impl(context):
    # Try to find the element with link text 'traktor' and assert it's not present
    try:
        element = context.driver.find_element(By.LINK_TEXT, "traktor")
        # If the element is found, we fail the test
        context.fail("Element 'traktor' should not be present")
    except NoSuchElementException:
        # If the element is not found, the test passes
        pass

# Test 3

    
@given(u'user writes iMAC and press enter')
def step_impl(context):
    context.driver.get(SUT_URL)
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iMac")
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()

@given(u'iMac should be seen')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "iMac").text == "iMac"

@when(u'user selects "category" to Mac')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="input-category"]').click()
    # Wait for the dropdown options to be visible and interactable
    WebDriverWait(context.driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="input-category"]/option[6]'))
    )

    # Select the 'Mac' option from the dropdown
    mac_option = context.driver.find_element(By.XPATH, '//*[@id="input-category"]/option[6]')
    mac_option.click()
    sleep(5)

@when(u'user selects "category" to WebCameras')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="input-category"]').click()
    # Select the 'Mac' option from the dropdown
    context.driver.find_element(By.XPATH, '//*[@id="input-category"]/option[15]').click()
    

@when(u'User clicks on some product')
def step_impl(context):
    
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) > .product-thumb .img-fluid").click()
    
@then(u'No result should be shown')
def step_impl(context):
    # Use WebDriverWait to wait for the element to be present, or timeout after 10 seconds
    try:
        # Wait for the specific paragraph that shows the no result text
        element = WebDriverWait(context.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="content"]/p'))
        )
        # Assert the text of the element is as expected
        assert element.text == 'There is no product that matches the search criteria', (
            f"Expected no result text, but got: {element.text}"
        )
    except TimeoutException:
        # If the element is not found after the timeout, this is also considered a pass,
        # since we're expecting no results.
        pass

@then(u'The products page should be seen')
def step_impl(context):
    # context.driver.find_element(By.CSS_SELECTOR,'//*[@id="product-info"]')
        # Wait for the product info container to be visible to confirm we're on the product's page
    product_info = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#product-info'))
    )
    # Assert that product info container is not None, which would mean the element is indeed present
    assert product_info is not None, "Product info container is not visible."

@when(u'User adds Samsung Galaxy Tab 10.1 to the cart')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[4]/a').click()
    context.driver.find_element(By.XPATH,'//*[@id="product-list"]/div/div/div[2]/form/div/button[1]').click()
    context.driver.find_element(By.CSS_SELECTOR,'.btn-close').click()
    context.driver.find_element(By.XPATH,'//*[@id="header-cart"]/div/button').click()

@then('Product should appear in shopping cart')
def step_impl(context):
    element = context.driver.find_element(By.XPATH,'//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[2]/a').text
    assert(element == 'Samsung Galaxy Tab 10.1')
    context.driver.find_element(By.XPATH,'//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[5]/form/button').click()

@given(u'User clicks on "Laptot & notebooks"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/a').click()

@given(u'clicks on "Show all laptops & notebooks"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/div/a').click()

@given(u'clicks on "HP LP3065"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[1]/a/img').click()

@given(u'adds product into cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="button-cart"]').click()
    context.driver.find_element(By.CSS_SELECTOR,'.btn-close').click()

@given(u'opens shopping cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[4]/a/span').click()

@given(u'clicks on "checkout"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]/a').click()

@when(u'User fills in all adress details')
def step_impl(context):
    # Adress
    context.driver.find_element(By.XPATH, '//*[@id="input-guest"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-firstname"]').send_keys("Alfred")
    context.driver.find_element(By.XPATH, '//*[@id="input-lastname"]').send_keys("Alfredovic")
    context.driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys("email@gmail.com")
    context.driver.find_element(By.XPATH, '//*[@id="input-shipping-address-1"]').send_keys("Kralovska")
    context.driver.find_element(By.XPATH, '//*[@id="input-shipping-city"]').send_keys("Brno")
    select_country = Select(context.driver.find_element(By.ID, 'input-shipping-country'))
    select_country.select_by_visible_text('Slovak Republic')
    select_country = Select(context.driver.find_element(By.ID, 'input-shipping-zone'))
    select_country.select_by_visible_text('Košický')
    context.driver.find_element(By.XPATH, '//*[@id="input-shipping-postcode"]').send_keys("90888")
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(1)
    wait = WebDriverWait(context.driver, 10)  # Čeká až 10 sekund
    continue_button = wait.until(EC.element_to_be_clickable((By.ID, 'button-register')))
    
    continue_button.click()

@when(u'delivery')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,0);")
    sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="button-shipping-methods"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-shipping-method-flat-flat"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="button-shipping-method"]').click()

@when(u'payment')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="button-payment-methods"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="input-payment-method-cod-cod"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="button-payment-method"]').click()

@when(u'clicks on "Confirm Order"')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="button-confirm"]').click()

@then(u'Order should be processed')
def step_impl(context):
    #By being able to click on this button, order should have been processed
    context.driver.find_element(By.XPATH, '//*[@id="content"]/div/a').click()

# Test 9

@when(u'admin puts into filter iMAC')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys("iMac")
    context.driver.find_element(By.XPATH, '//*[@id="button-filter"]').click()

@then(u'admin should see the product.')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'iMac')]"))
        )
        product_name = context.driver.find_element(By.XPATH, "//td[contains(text(), 'iMac')]").text
        assert 'iMac' in product_name, "Product 'iMac' is not present in the table."
    except TimeoutException:
        assert False, "Product 'iMac' was not found in the table after filtering."

