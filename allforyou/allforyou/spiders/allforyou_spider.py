import scrapy
import re
from time import gmtime, strftime
from allforyou.items import AllforyouItem

class allForYou(scrapy.Spider):
	name = "allforyou"
	allowed_domains = ["allforyou.sg"]
	start_urls = ["http://www.allforyou.sg/"]
	ctr=0

	def parse(self, response):
		for href in response.css("div.span2.categorybox-span >  div.categorybox.thumbnail > div.thumb >  a::attr('href')"):
			url = response.urljoin(href.extract())
			print url
			yield scrapy.Request(url, callback=self.parse_all_items)

	def parse_all_items(self, response):
		for hrefitem in response.css("div.FeaturedHeader >  h2 >  a::attr('href')"):
			urlitem = response.urljoin(hrefitem.extract())
			yield scrapy.Request(urlitem, callback=self.parse_item_pages)

	def parse_item_pages(self, response):
		max_pages=0
		for sel in response.css("div.pager > a.individual-page::text"):
			max_pages=int(sel.extract())	
		print max_pages
		print response.urljoin('')

		for i in range(max_pages+1):
			yield scrapy.Request(response.urljoin('?pagenumber=%d'%(i+1)), callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		for sel in response.xpath("//div[contains(@class, 'prod-data')]"):
			item = AllforyouItem()
			self.ctr+=1
			print response
			item['crawl_time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			item['urls'] = sel.xpath("@data-imgurl").extract()	
			item['image'] = sel.xpath("@data-imgurl").extract()		
			item['out_of_stock'] = sel.xpath("@data-outofstock").extract()
			item['title'] = sel.xpath("@data-name").extract()
			item['offer'] = sel.xpath("@data-hasoffers").extract()	
			item['retailer_sku_code'] = sel.xpath("@id").extract()
			item['sku'] = sel.xpath("@data-newprodid").extract()
			item['desc'] = sel.xpath("@data-desc").extract()
			item['price'] = sel.xpath("@data-price").extract()
			print self.ctr
			#item['categories'] = cat[x:]
			yield item

# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.selector import Selector
# from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

# from allforyou.items import AllforyouItem
# from allforyou.pipelines import AllforyouPipeline


# class AllforyouSpider(CrawlSpider):

#     name = 'allforyou'
#     allowed_domains = ['allforyou.sg']
#     start_urls = ['https://allforyou.sg/']
#     rules = [
#             Rule(LxmlLinkExtractor(allow=''),
#             callback='parse_item',
#             follow=True)
#     ]

#     _item = AllforyouItem()

#     pipeline = set([
#         AllforyouPipeline
#     ])

#     def parse_item(self, response):
#         sel = Selector(response)
#         categories = list()
#         breadcrumbs = sel.xpath('//ul[@id="content_breadcrumb"]/li/a/img')
#         for crumb in breadcrumbs:
#             categories.append(crumb.xpath('@title').extract()[0])

#         if categories:
#             items = list()
#             item_boxes = sel.xpath('//div[@class="prod-data"]')
#             for box in item_boxes:
#                 item = AllforyouItem()
#                 item['urls'] = response.url or None
#                 item['categories'] = str(categories) or None
#                 item['image'] = box.xpath('@data-imgurl').extract() or None
#                 item['description'] = box.xpath('@data-desc').extract()
#                 item['offer'] = box.xpath('@data-offername').extract()
#                 item['price'] = box.xpath('@data-price').extract() or None
#                 item['out_of_stock'] = box.xpath('@data-outofstock').extract()
#                 item['title'] = box.xpath('@data-name').extract() or None
#                 item['old_price'] = box.xpath('@data-oldprice').extract() or None
#                 item['sku'] = box.xpath('@id').extract() or None
#                 items.append(item)
#             return items