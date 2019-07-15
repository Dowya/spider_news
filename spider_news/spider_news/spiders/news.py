from scrapy import CrawlSpider,Request



class news(CrawlSpider):
	name ="news"
	start_urls = []
	

	def parse(self,response):
		pass
