# Use Selenium to handle the search form, and again
# use the title XPath to make sure we got to the 
# right page.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
# from selenium import selenium
# from selenium.selenium import selenium
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import Select
# import time
# import datetime
 
class Demo2(BaseSpider):
    _timeout = 5
    name = "demo2"
    start_urls = ["https://www.courts.mo.gov/casenet/cases/filingDateSearch.do"]
    
    # def __init__(self,  **kwargs):
    #     self.driver = webdriver.Firefox()
    #     driver = self.driver
    #     driver.implicitly_wait(30)
    #     driver.get("https://www.courts.mo.gov/casenet/cases/filingDateSearch.do")

    #     Select(driver.find_element_by_id("courtId")).select_by_visible_text("Fine Collection Center")

    #     now = datetime.datetime.now()
    #     nowstring = now.strftime("%m/%d/%Y")
    #     date_el = driver.find_element_by_id('inputVO.startDate')
    #     date_el.send_keys(nowstring)

    #     driver.find_element_by_id("findButton").click()

    #     super(Demo2, self).__init__()
    
    def parse(self, response):
		hxs = HtmlXPathSelector(response)
		title = hxs.select("//title").extract()
		print title