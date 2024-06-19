from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class HealthterLanguageSelectorComponent:
    @staticmethod
    def language_code(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".gt-lang-code")

    @staticmethod
    def language_options(driver: WebDriver):
      return driver.find_element(by=By.CSS_SELECTOR, value=".gt_options")

    @staticmethod
    def language_arabic(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".nturl[data-gt-lang='ar']")

    @staticmethod
    def language_english(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".nturl[data-gt-lang='en']")

    @staticmethod
    def language_french(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".nturl[data-gt-lang='fr']")

    @staticmethod
    def language_amhara(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".nturl[data-gt-lang='am']")

    @staticmethod
    def language_turkish(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".nturl[data-gt-lang='tr']")

    @staticmethod
    def language_swahili(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".nturl[data-gt-lang='sw']")

    @staticmethod
    def language_somali(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".nturl[data-gt-lang='so']")

    @staticmethod
    def footer_about_heading(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value="footer .widget-about h5.heading")

    @staticmethod
    def translate_indicator(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".VIpgJd-ZVi9od-aZ2wEe-wOHMyf")

    @staticmethod
    def current_language(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".gt-current-lang")