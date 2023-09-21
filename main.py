# This document is a cheat sheet for selenium and beautiful soup. There is no functioning code in this page.
# Selenium:
# Selenium imports:
    from selenium.webdriver import EdgeOptions, FirefoxOptions, SafariOptions, ChromeOptions
    from selenium.common import NoSuchElementException, ElementNotInteractableException
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.by import By
    import selenium


# Selenium driver options: https://selenium-python.readthedocs.io/api.html
        proxy = "Proxy Address Here"
        user_agent = "User agent string here"
    # Exceptions imported on line 5 to be used in WebDriverWait
        exceptions_list = [NoSuchElementException, ElementNotInteractableException]
    # EdgeOptions() constructor and its import statement, line 4, change depending on which browser you are using.
    # EX: EdgeOptions(), SafariOptions(), FirefoxOptions()
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('headless')
    # disable-gpu stops the browser from loading images, increasing speed and decreasing necessary bandwidth.
        edge_options.add_argument('disable-gpu')
        edge_options.add_argument("--proxy_server=%s" % proxy)
        edge_options.add_argument("--user_agent=%s" % user_agent)
    # Use with instead of explicitly closing driver with driver.close()

# Selenium common Wait Strategies: https://selenium-python.readthedocs.io/waits.html#implicit-waits:
        with selenium.webdriver.Edge(options=edge_options) as driver:
    # Implicitly wait is a general pause statement specific to the selenium webdriver.
            driver.implicitly_wait(10)
    # WebDriverWait constructor, imported on line 6, are used to more effectively wait for changes to DOM.
            wait = WebDriverWait(driver=driver,  # driver defined in the with statement.
                                 timeout=30,  # adjust for longer wait times.
                                 poll_frequency=.20,  # Change frequency of change to selector.
                                 ignored_exceptions=exceptions_list  # list of exceptions to ignore while waiting imported
                                 )
# Selenium Common Locator Strategies:
"""Available Locators: ID = "id", NAME = "name", XPATH = "xpath", LINK_TEXT = "link text", 
PARTIAL_LINK_TEXT = "partial link text", TAG_NAME = "tag name", CLASS_NAME = "class name", 
CSS_SELECTOR = "css selector" """
            returned_object = driver.find_element(By.XPATH, "Put locater value here")
            returned_list = driver.find_elements(By.CLASS_NAME, "Put locater value here")
    # Including a wait strategy in a selector statement:
        # Most expected_conditions take a tuple formated as (By.locator, "selector value")
        # ec is an alias for expected_conditions imported on line 7 and By is imported on line 8
                returned_object1 = wait.until(ec.presence_of_element_located((By.XPATH, "Put locater value here")))
                returned_list1 = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "Put locater value here")))
        # until not triggers if expected_condition returns false.
                returned_object2 = wait.until_not(ec.text_to_be_present_in_element((By.LINK_TEXT, "Put locator value here"),
                                                                              text_= "Some text in element" ))