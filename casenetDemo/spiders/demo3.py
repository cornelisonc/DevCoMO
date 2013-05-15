from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from selenium import selenium
from selenium.selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import datetime
 
class Demo3(BaseSpider):
    _timeout = 5
    name = "demo3"
    start_urls = ["https://www.courts.mo.gov/casenet/cases/filingDateSearch.do"]
    
    def __init__(self,  **kwargs):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("https://www.courts.mo.gov/casenet/cases/filingDateSearch.do")

        Select(driver.find_element_by_id("courtId")).select_by_visible_text("Fine Collection Center")

        now = datetime.datetime.now()
        nowstring = now.strftime("%m/%d/%Y")
        date_el = driver.find_element_by_id('inputVO.startDate')
        date_el.send_keys(nowstring)

        driver.find_element_by_id("findButton").click()

        super(Demo3, self).__init__()
    
    def parse(self, response):
        driver = self.driver

        links = []

        links.extend(driver.find_elements_by_xpath("//td[@class='td1']/a"))
        links.extend(driver.find_elements_by_xpath("//td[@class='td2']/a"))

        print links
        
        # for link in links:

        #     text = link.get_attribute("href")
        #     print text
