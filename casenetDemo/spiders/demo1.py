# Instantiate a simple BaseSpider, and access one page.
# Use XPath to get title attribute of that page,
# just to make sure we got to it correctly.

from scrapy.spider import BaseSpider
from scrapy.http import Request
# from scrapy.selector import HtmlXPathSelector

class Demo1(BaseSpider): 
	name = "demo1"
	start_urls = ["https://www.courts.mo.gov/casenet/cases/filingDateSearch.do"]

	def parse(self, response):
		pass
		# hxs = HtmlXPathSelector(response)
		# title = hxs.select("//title").extract()
		# print title