from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumDemo:
    # Define driver as a class attribute
    driver = webdriver.Chrome()

    def OpenWebsite(self, link):
        # Website name
        self.driver.get(link)
        # Maximize window
        self.driver.maximize_window()
        print("Website title: ", self.driver.title)

    def ChromeTest(self):
        # Find element by ID
        # element_by_id = self.driver.find_element(By.ID, "my-id")
        # print("Search box is present: ", element_by_id.is_displayed())
        #
        # Find element by name
        element_by_name = self.driver.find_element(By.NAME, "q")
        print("Name is present: ", element_by_name.is_displayed())

        # # Find element by partial link text
        # element_by_partial_link_text = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Georgia")
        # print("Partial link is present: ", element_by_partial_link_text.is_displayed())
        #
        # # Find element by tag name
        # element_by_tag_name = self.driver.find_element(By.TAG_NAME, "my-tag-name")
        # print("Partial link is present: ", element_by_tag_name.is_displayed())
        #
        # # Find element by class name
        # element_by_class_name = self.driver.find_element(By.CLASS_NAME, "my-class-name")
        # print("Partial link is present: ", element_by_class_name.is_displayed())
        #
        # # Find element by CSS selector
        # element_by_css_selector = self.driver.find_element(By.CSS_SELECTOR, "my-css-selector")
        # print("Partial link is present: ", element_by_css_selector.is_displayed())

        # Find element by XPath or use (By.XPATH)
        search_box = self.driver.find_element(By.XPATH, "//*[@name='q']")
        print("Search box is present: ", search_box.is_displayed())
        # Write in input
        search_box.send_keys("Automation WebDriver")
        # Click submit
        search_box.submit()
        # Find element using class name
        search_results = self.driver.find_elements(By.CLASS_NAME, "g")
        # Print amount of elements found in the page with that class name
        print(f"Number of search results: {len(search_results)}")
        # Find element using text
        tools_links = self.driver.find_elements(By.LINK_TEXT, "Images")
        # Which text in the list (first one in here)
        tools_links[0].click() if tools_links else print("No Images link found")
        # Wait 3 seconds before quiting.
        time.sleep(3)
        self.driver.quit()


seleniumTests = SeleniumDemo()
seleniumTests.OpenWebsite("https://training.openspan.com/login")
# https://www.google.com
# https://training.openspan.com/login
# seleniumTests.ChromeTest()
# seleniumTests.TrainTest()


# search_results = driver.find_elements (By XPATH, "//div[@class='viewport']//div[1]/li")
# print(len(search_results))
# for results in search_results:
# if "New York (JFK)" in results.text:
# results.click()
# time.sleep(6)
