from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=true")
        chrome_options.add_argument("--window-size=1920x1080")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_django_initial_startup_html(self):
        self.browser.get(self.live_server_url)
        self.assertEquals("Success!", self.browser.title)
