from selenium.webdriver import EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import seleniumwire
from seleniumwire import webdriver
import selenium
from dataclasses import dataclass


@dataclass
class Listings:
    link: str


listing_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/div[1]/div/h2/a"
link = "https://www.moxfield.com/decks/HYT9YcG0bEK1UMvmEEXtTA"
proxy = "http://134.195.101.34:8080"

class Job_Scraper:
    def __init__(self):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("headless")
        edge_options.add_argument("start-maximized")
        edge_options.page_load_strategy = "eager"
        edge_options.add_argument("disable-gpu")
        edge_options.add_argument("--proxy_server=%s" % proxy)
        self.driver = webdriver.Edge(options=edge_options)


jobs = Job_Scraper()

jobs.driver.get(link)
print(jobs.driver.page_source)