import seleniumwire
from selenium.webdriver import EdgeOptions, FirefoxOptions, SafariOptions, ChromeOptions
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.remote.webdriver import VirtualAuthenticatorOptions
import selenium
from seleniumwire import webdriver
from PIL import Image


link = "https://profile.w3schools.com/"
user_name = '//*[@id="modalusername"]'
pass_field = '//*[@id="current-password"]'
login_button = '//*[@id="root"]/div/div/div[4]/div[1]/div/div[4]/div[1]/button'
edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.page_load_strategy = 'eager' # normal, eager, none
edge_options.add_argument('start-maximized')
# edge_options.add_argument('headless')
# edge_options.add_argument('disable-gpu')
# edge_options.add_argument("--proxy_server=%s" % proxy)
# edge_options.add_argument("--user_agent=%s" % user_agent)
sel_wire_options = {
    'request_storage_base_dir': r'C:\Users\dmcfa\Desktop\selenium_wire_storage',
    'exclude_hosts': ['google-analytics.com'],
    'disable_encoding': True
}
with seleniumwire.webdriver.Edge(options=edge_options, seleniumwire_options=sel_wire_options) as driver:
    wait = WebDriverWait(driver, 30)
    driver.get(link)
    user_name_field = wait.until(ec.presence_of_element_located((By.XPATH, user_name)))
    password_field = wait.until(ec.presence_of_element_located((By.XPATH, pass_field)))
    login = wait.until(ec.presence_of_element_located((By.XPATH, login_button)))
    user_name_field.send_keys("dmcfarland8031@gmail.com")
    password_field.send_keys("Fuck@pass30.com")
    login.click()
    

    virt_auth_options = VirtualAuthenticatorOptions(
        protocol="ctap2", # "ctap1/u2f", "ctap2" or "ctap2_1"
        transport="Transport.INTERNAL", # .INTERNAL indicates that the Authenticator is stored on client device
        has_resident_key=True, # Set as True so that the server requests a discoverable public key without client supplying an id first.
        has_user_verification=True, # Set to True to validate user verification through pin/password. Must be True for is_user_verified to work.
        is_user_consenting=True, # Set as True so user automatically consents to Virtual Authentication
        is_user_verified=True # Set to true so user verification always succeeds.
    )
    driver.add_virtual_authenticator(options=virt_auth_options)