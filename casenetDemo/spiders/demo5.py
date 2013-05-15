# Create a FormRequest and send it post data from the
# URLs we've scraped. Give it a callback to handle the
# violation field we've added in the Item.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from selenium import selenium
from selenium.selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from casenetDemo.items import CasenetdemoItem
import re
import time
import datetime
 
class Demo5(BaseSpider):
    _timeout = 5
    name = "demo5"
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

        super(Demo5, self).__init__()
    
    def parse(self, response):
        driver = self.driver

        links = []

        links.extend(driver.find_elements_by_xpath("//td[@class='td1']/a"))
        links.extend(driver.find_elements_by_xpath("//td[@class='td2']/a"))

        for link in links:

            text = link.get_attribute("href")
            split_text = re.findall(r"[\w']+", text)
            caseno = split_text[2].replace("'", "")
            courtno = split_text[3].split('\'')[1]

            # item = FormRequest(url="https://www.courts.mo.gov/casenet/cases/charges.do",
            #     formdata={'inputVO.caseNumber': caseno, 'inputVO.courtId': courtno},
            #     method="POST",
            #     callback=self.get_client_violation)
            # item.meta['caseno'] = caseno
            # item.meta['courtno'] = courtno

            # yield item

    # def get_client_violation(self, response):
    #     item = CasenetdemoItem()

    #     item['caseno'] = response.meta['caseno']
    #     item['courtno'] = response.meta['courtno']

    #     hxs = HtmlXPathSelector(response)
    #     violation = hxs.select("//td[@class='detailData']").extract()
    #     violation = violation[0]
    #     violation = str(violation.encode('ascii', 'ignore'))
    #     violation = violation.lstrip('<td style="width: 84%" colspan="5" class="detailData">')
    #     violation = violation.split(" <i>")
    #     violation = violation[0]

    #     item['violation'] = violation
    #     return item