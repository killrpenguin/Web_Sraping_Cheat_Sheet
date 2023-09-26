# Selenium imports:
from selenium.webdriver import EdgeOptions, FirefoxOptions, SafariOptions, ChromeOptions
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import seleniumwire
from seleniumwire import webdriver
import selenium

import pytest

# Common Selenium driver options: https://selenium-python.readthedocs.io/api.html
link = "Webpage link string you want to scrape."
proxy_variable = "Proxy address string you pass to selenium in add_arguments."
user_agent_variable = "User agent you supply to selenium in add_arguments."

# Exceptions imported on line 3 to be used in WebDriverWait
exceptions_list = [NoSuchElementException, ElementNotInteractableException]

# EdgeOptions() constructor and its import statement, line 2, change depending on which browser you are using.
# EX: EdgeOptions(), SafariOptions(), FirefoxOptions() Modify its behavior with the add_arguments method.
edge_options = EdgeOptions()
# Page load strategy applies to the entire session. Eager and None don't work well without an explicit wait strategy.
edge_options.page_load_strategy = "eager" # default = normal, faster = eager, fastest = none
edge_options.use_chromium = True
edge_options.add_argument("headless")
edge_options.add_argument("start-maximized")
# disable-gpu stops the browser from loading images, increasing speed and decreasing necessary bandwidth.
edge_options.add_argument("disable-gpu")
edge_options.add_argument("--proxy_server=%s" % proxy_variable)
edge_options.add_argument("--user_agent=%s" % user_agent_variable)

# Use seleniumwire for more control over requests, responses and headers.
# Use with instead of explicitly closing driver with driver.close() after scraping.
with seleniumwire.webdriver.Edge(options=edge_options) as driver:
    # Common browser actions.
        driver.get(link)
        driver.get("www.webpagetoscrape.com")
        driver.refresh()
        driver.back()
        driver.forward()
        print(f"{driver.page_source}") # Display page source.
        print(f"{driver.current_url}") # Display url in address bar.
    # Cookies in the current session.
        driver.add_cookie({"name": "cookie_value"})
        print(driver.get_cookie("cookie name"))
        print(driver.get_cookies())
    # Store screenshot as bytes. Use PIL to convert and save bytes as image.
        screenshot = driver.get_screenshot_as_png()
    # Store screenshot as .png image
        driver.save_screenshot("File name here. MUST include .png extention")
        element.screenshot("File name here. MUST include .png extention")
    # Execute JavaScript. This command will scroll to the bottom of the screen.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Execute a Javascript "?.click()" on a JS path supplied by Chrome Elements page.
        # JS Path supplied by Chrome: document.querySelector("#main > div:nth-child(3) > a.w3-right.w3-btn")
        driver.execute_script('document.querySelector("#main > div:nth-child(3) > a.w3-right.w3-btn")?.click()')


# Selenium common Wait Strategies: https://selenium-python.readthedocs.io/waits.html#implicit-waits:
# Implicitly wait is a general pause statement specific to the selenium webdriver.
driver.implicitly_wait(10)  # int in seconds to wait.
# WebDriverWait constructor, imported on line 4, is used to more effectively wait for changes to DOM.

wait = WebDriverWait(driver=driver,  # driver defined in the with statement.
                     timeout=30,  # adjust for longer wait times.
                     poll_frequency=.20,  # Change frequency of change to selector.
                     ignored_exceptions=exceptions_list
                     # list of exceptions to ignore while waiting for timeout to expire
                     )

# Selenium Common Locator Strategies:
# XPATH and Class_Name are the two best options for selecting a specific element on a webpage.

"""Available Locators: ID = "id", NAME = "name", XPATH = "xpath", LINK_TEXT = "link text",
PARTIAL_LINK_TEXT = "partial link text", TAG_NAME = "tag name", CLASS_NAME = "class name",
CSS_SELECTOR = "css selector" """

returned_object = driver.find_element(By.XPATH, "Put locater value here")
returned_list = driver.find_elements(By.CLASS_NAME, "Put locater value here")

# Including a wait strategy in a selector statement:
# Most expected_conditions take a tuple formated as (By.locator, "selector value")
# ec is an alias for expected_conditions imported on line 5 and By is imported on line 6

returned_object1 = wait.until(ec.presence_of_element_located((By.XPATH, "Put locater value here")))
returned_list1 = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "Put locater value here")))

# .until_not() triggers if expected_condition returns false.
returned_object2 = wait.until_not(ec.text_to_be_present_in_element((By.LINK_TEXT, "Put locator value here"),
                                                                   text_="Some text in element"))

# Interacting with elements like buttons, dropdowns, radials, text boxes, etc.
# Button interaction.
click_button_without_waiting = driver.find_element(By.XPATH, "Submit button xpath")
click_button_without_waiting.click()
click_button_after_loading = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "button class name")))
click_button_without_waiting.click()
hover_mouse_over_button = wait.until(ec.presence_of_element_located((By.XPATH, "Element xpath")))
ActionChains(driver=driver).move_to_element(hover_mouse_over_button).perform()


# Input text into form field or text box.
# First locate the text box and then use .send_keys() method to interact with the element.
locate_text_box = wait.until(ec.presence_of_element_located((By.XPATH, "Xpath of text box")))
locate_text_box_without_wait = driver.find_element(By.XPATH, "Xpath of text box")
locate_text_box.send_keys("Text you would input goes here.")
send_keys_text_input = "It can be anything you would type or a predefined string"
locate_text_box_without_wait.send_keys(send_keys_text_input)

# Use Keys, imported on line 7, and its predefined methods to input special keyboard actions like arrow keys, enter or shift.
locate_text_box.send_keys(Keys.ARROW_DOWN)
locate_text_box.send_keys(Keys.ENTER)

# Dropdown menu interaction:
# Selenium documentation suggests using pytest instead of my example. This example is copied right from their GitHub.
select_element = driver.find_element(By.NAME, "single_disabled")
select = Select(select_element)
with pytest.raises(NotImplementedError):
    select.select_by_value("disabled")
# Select the dropdown if it isn't disabled. wait.until_not() returns false when the elements value!= disabled
# This is my workaround for checking enabled/disabled status of a dropdown.
dropdown = wait.until_not(ec.text_to_be_present_in_element_attribute((By.XPATH, "Put locator value here"),
                                                                             "value", "disabled"))
# Select a single dropdown option:
select = Select(dropdown)
# Dropdown menu's visible options.
select.select_by_visible_text("Four")
# Text in the select elements value attribute.
select.select_by_value("two")
# Int in the select elements index attribute.
select.select_by_index(3)
# apply the selected option in selenium:
assert dropdown.is_selected()

# Select multiple dropdown options simultaneously. Copied from Selenium GitHub
select = Select(dropdown)
# Select all options by first finding all of the available options
option_elements = wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, "option")))
# select.options returns a list of all options belonging to the dropdown.
option_list = select.options
# Apply all options in selenium
assert option_elements == option_list

# .all_selected_options() returns a list of options that have been preselected by the page or by you.
selected_option_list = select.all_selected_options
expected_selection = ["egg_element", "sausage_element"]
if all(expected_selection) in selected_option_list:
    assert selected_option_list == expected_selection
else:
    select.deselect_by_value("some text")
    assert not dropdown.is_selected()
