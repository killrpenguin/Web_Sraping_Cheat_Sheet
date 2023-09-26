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
from selenium.webdriver.remote.webdriver import Credential
import selenium
from seleniumwire import webdriver


link = "https://webauthn.io/"
authenticate_button = '//*[@id="login-button"]'
edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.page_load_strategy = 'normal'  # normal, eager, none
edge_options.add_argument('start-maximized')
# edge_options.add_argument('headless')
# edge_options.add_argument('disable-gpu')
# edge_options.add_argument("--proxy_server=%s" % proxy)
# edge_options.add_argument("--user_agent=%s" % user_agent)
sel_wire_options = {
    'request_storage_base_dir': r'C:\Users\dmcfa\Desktop\selenium_wire_storage',
    'disable_encoding': True
}
with seleniumwire.webdriver.Edge(options=edge_options, seleniumwire_options=sel_wire_options) as driver:
    wait = WebDriverWait(driver, 30)
    virt_auth_options = VirtualAuthenticatorOptions(
        protocol="ctap2",  # Options are"ctap1/u2f", "ctap2" or "ctap2_1"
        transport="internal",  # INTERNAL indicates that the Authenticator is stored on client device
        has_resident_key=True,
        # Set as True so that the server requests a discoverable public key without client supplying an id first.
        has_user_verification=True,
        # Set to True to validate user verification through pin/password. Must be True for is_user_verified to work.
        is_user_consenting=True,  # Set as True so user automatically consents to Virtual Authentication
        is_user_verified=True  # Set to true so user verification always succeeds.
    )
    driver.add_virtual_authenticator(options=virt_auth_options)
    credential = Credential(
        credential_id="",
        is_resident_credential=True,
        rp_id="",
        user_handle="test123",
        private_key= ,
        sign_count=0
    )
    driver.add_credential(credential=credential)
    driver.get(link)
    test_auth = wait.until(ec.presence_of_element_located((By.XPATH, authenticate_button)))
    test_auth.click()
    print(driver.get_credentials())
    wait.until(ec.title_contains("WebAuthn.io"))