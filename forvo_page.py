from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from locator import Locator


class ForvoPage(BasePage):

    url = 'https://forvo.com/login/'

    @property
    def username(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#login')
        return BaseElement(self.driver, locator)

    @property
    def password(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#password')
        return BaseElement(self.driver, locator)

    @property
    def login_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.button')
        return BaseElement(self.driver, locator)

    @property
    def keyword_button(self):
        locator = Locator(
            by=By.CSS_SELECTOR, value='ul.word-play-list-icon-size-l:nth-child(1) > li:nth-child(1) > a:nth-child(2)')
        return BaseElement(self.driver, locator)

    @property
    def agree_button(self):
        locator = Locator(
            by=By.CSS_SELECTOR, value='.css-flk0bs')
        return BaseElement(self.driver, locator)

    @property
    def pronounciation(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.phonetics')
        return BaseElement(self.driver, locator)

    @property
    def download_button(self):
        locator = Locator(
            # by=By.XPATH, value="//*[@id='en_uk']/following-sibling::*/div/div/p[3]")
            by=By.XPATH, value="//header[@id='ru']/following-sibling::*/li[1]/div/div[1]/p[3]")
        return BaseElement(self.driver, locator)
