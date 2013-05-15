from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from selenium import selenium
from selenium.selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
# from casenetDemo.items import CasenetdemoItem
import time
import datetime
# import re
 
class Demo4(BaseSpider):
    _timeout = 5
    name = "demo4"
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

        super(Demo4, self).__init__()
    
    def parse(self, response):
        driver = self.driver

        links = []

        links.extend(driver.find_elements_by_xpath("//td[@class='td1']/a"))
        links.extend(driver.find_elements_by_xpath("//td[@class='td2']/a"))

        # for link in links:

        #     text = link.get_attribute("href")
        #     split_text = re.findall(r"[\w']+", text)
        #     caseno = split_text[2].replace("'", "")
        #     courtno = split_text[3].split('\'')[1]

        #     item = CasenetdemoItem()

        #     item['caseno'] = caseno
        #     item['courtno'] = courtno

        #     yield item
