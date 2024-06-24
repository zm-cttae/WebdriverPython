import unittest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of

from testdata.language_selector_data import LanguageSelectorData
from componentobjects.language_selector import HealthterLanguageSelectorComponent

class HealthterLanguageSelectorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = cls.driver = webdriver.Chrome(options=options,service=service)
        cls.wait = WebDriverWait(driver, 5)
        
        cls.actionChains = ActionChains(driver)
        driver.maximize_window()
        driver.implicitly_wait(1)

    def setUp(self):
        self.driver.get(LanguageSelectorData.homepage_url)

    def test_default_title_somali(self):
        driver = self.driver
        self.assertEqual(driver.title, LanguageSelectorData.title)

    def test_gt_default_language_somali(self):
        driver = self.driver
        language_code = HealthterLanguageSelectorComponent.language_flag(driver)
        self.assertEqual(language_code.get_attribute("alt"), LanguageSelectorData.language_code_so)
    
    def test_gt_language_selector_menu(self):
        driver = self.driver

        self.util_toggle_gt_language_menu(True)

        language_options = HealthterLanguageSelectorComponent.language_options(driver)
        self.assertEqual(language_options.is_displayed(), True)

        self.util_toggle_gt_language_menu(False)

        language_options = HealthterLanguageSelectorComponent.language_options(driver)
        self.assertEqual(language_options.is_displayed(), False)

    def test_gt_language_selector_options(self):
        driver = self.driver

        self.util_toggle_gt_language_menu(True)

        language_arabic = HealthterLanguageSelectorComponent.language_arabic(driver)
        self.assertEqual(language_arabic.is_displayed(), True)
        language_english = HealthterLanguageSelectorComponent.language_english(driver)
        self.assertEqual(language_english.is_displayed(), True)
        language_french = HealthterLanguageSelectorComponent.language_french(driver)
        self.assertEqual(language_french.is_displayed(), True)
        language_amhara = HealthterLanguageSelectorComponent.language_amhara(driver)
        self.assertEqual(language_amhara.is_displayed(), True)
        language_turkish = HealthterLanguageSelectorComponent.language_turkish(driver)
        self.assertEqual(language_turkish.is_displayed(), True)
        language_swahili = HealthterLanguageSelectorComponent.language_swahili(driver)
        self.assertEqual(language_swahili.is_displayed(), True)

        self.util_toggle_gt_language_menu(False)

    def test_gt_language_option_persistence(self):
        driver = self.driver

        self.util_toggle_gt_language_menu(True)

        language_arabic = HealthterLanguageSelectorComponent.language_arabic(driver)
        language_arabic.click()

        footer_about_heading = HealthterLanguageSelectorComponent.footer_about_heading(driver)
        self.util_scroll_to_translated_element(footer_about_heading)
        self.assertEqual(footer_about_heading.text, LanguageSelectorData.about_heading_text_ar)

        driver.get(LanguageSelectorData.general_health_url)
        
        footer_about_heading = HealthterLanguageSelectorComponent.footer_about_heading(driver)
        self.util_scroll_to_translated_element(footer_about_heading)
        self.assertEqual(footer_about_heading.text, LanguageSelectorData.about_heading_text_ar)

        self.util_toggle_gt_language_menu(True)

        language_somali = HealthterLanguageSelectorComponent.language_somali(driver)
        language_somali.click()

        self.util_toggle_gt_language_menu(False)

        self.util_scroll_to_translated_element(footer_about_heading)
        self.assertEqual(footer_about_heading.text, LanguageSelectorData.about_heading_text_so)

    def util_scroll_to_translated_element(self, element):
        driver = self.driver
        wait = self.wait
        actionChains = self.actionChains

        actionChains.scroll_to_element(element).perform()
        translate_indicator = HealthterLanguageSelectorComponent.translate_indicator(driver)
        wait.until_not(visibility_of(translate_indicator))
        time.sleep(1)

    def util_toggle_gt_language_menu(self, visibility):
        driver = self.driver
        wait = self.wait

        current_language = HealthterLanguageSelectorComponent.current_language(driver)
        language_options = HealthterLanguageSelectorComponent.language_options(driver)

        if visibility:
            if not language_options.is_displayed():
                current_language.click()
            wait.until(visibility_of(language_options))
        else:
            if language_options.is_displayed():
                current_language.click()
            wait.until_not(visibility_of(language_options))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()