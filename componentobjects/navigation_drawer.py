from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class HealthterNavigationDrawerComponent:
    @staticmethod
    def button_open_drawer(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value=".smart-head-main .offcanvas-toggle")
    
    @staticmethod
    def panel_drawer(driver: WebDriver):
        return driver.find_element(by=By.ID, value="off-canvas")

    @staticmethod
    def toggle_general(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value="#menu-item-2472 > .chevron")

    @staticmethod
    def anchor_cancer(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value="#menu-item-2473 a")

    @staticmethod
    def button_close_drawer(driver: WebDriver):
        return driver.find_element(by=By.CSS_SELECTOR, value="#off-canvas a.close")