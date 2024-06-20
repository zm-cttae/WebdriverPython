import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of

from componentobjects.navigation_drawer import HealthterNavigationDrawerComponent

class HealthterNavigationDrawerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = cls.driver = webdriver.Chrome(options=options,service=service)
        cls.wait = WebDriverWait(driver, 5)
        driver.get("https://healthter.org/")
        driver.maximize_window()
        driver.implicitly_wait(1)

    def setUp(self):
        self.driver.get("https://healthter.org/")

    def test_navigation_drawer_open(self):
        driver = self.driver
        wait = self.wait

        button_open_drawer = HealthterNavigationDrawerComponent.button_open_drawer(driver)
        button_open_drawer.click()

        panel_drawer = HealthterNavigationDrawerComponent.panel_drawer(driver)
        wait.until(visibility_of(panel_drawer))
        self.assertEqual(panel_drawer.is_displayed(), True)

    def test_navigation_drawer_submenu(self):
        driver = self.driver
        wait = self.wait

        button_open_drawer = HealthterNavigationDrawerComponent.button_open_drawer(driver)
        button_open_drawer.click()

        toggle_general = HealthterNavigationDrawerComponent.toggle_general(driver)
        toggle_general.click()

        anchor_cancer = HealthterNavigationDrawerComponent.anchor_cancer(driver)
        wait.until(visibility_of(anchor_cancer))
        anchor_cancer.click()

        self.assertEqual(driver.current_url, "https://healthter.org/qeybta/caafimaad-guud/kansar/")

    def test_navigation_drawer_close(self):
        driver = self.driver
        wait = self.wait

        button_open_drawer = HealthterNavigationDrawerComponent.button_open_drawer(driver)
        button_open_drawer.click()

        panel_drawer = HealthterNavigationDrawerComponent.panel_drawer(driver)
        wait.until(visibility_of(panel_drawer))

        button_close_drawer = HealthterNavigationDrawerComponent.button_close_drawer(driver)
        button_close_drawer.click()

        wait.until_not(visibility_of(panel_drawer))
        self.assertEqual(panel_drawer.is_displayed(), False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()