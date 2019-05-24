# -*- coding: utf-8 -*-
import scrapy
import itertools
from bitcoininfo1.items import Bitcoininfo1Item


class SpideroneSpider(scrapy.Spider):
	"""
	The spider crawls through the various pages in order to scrape the posts from
	the following URLs.
	"""
	name = 'spiderone'
	allowed_domains = ['bitcointalk.org/']
	start_urls = ['https://bitcointalk.org/index.php?topic=20333.0']
	page_count = 0
	
	def parse(self, response):
		"""
		Method to crawl through different urls.
		returns: After every successful crawl, 'parse_call' callback method is invoked.
		"""
		page_urls = response.xpath('.//a[@class = "navPages"]/@href')
		page_urls = page_urls[:40]
		#page_nos = page_nos[:40]
		for page in page_urls:
			#print (page.extract())
			yield scrapy.Request(url = response.urljoin(page.extract()), callback=self.parse_all, dont_filter=True)

	def parse_all(self, response):
		"""
		Method to parse the post content, author name, subject, url and post number.
		returns: Yeilds an item object which is written into a json file.
		"""
		SpideroneSpider.page_count += 1
		posts = response.xpath('//div[@class="post"]') 
		author_names = response.xpath('//td[@class="poster_info"]/b/a/text()')
		subjects = response.xpath('//div[@class="subject"]/a/text()')
		#time = response.xpath('//div[@class="smalltext"]/text()').re(r'.*PM|AM')
		message_numbers = response.xpath('//a[@class="message_number"]/text()')
		
		for txt, author, subject, msg_no in itertools.zip_longest(posts, author_names, subjects, message_numbers):
			item = Bitcoininfo1Item()
			item['post'] = txt.select("text()").extract()
			item['page_number'] = SpideroneSpider.page_count
			item['url'] = response.url
			item['author'] = author.extract()
			item['subject'] = subject.extract()
			#item['time'] = post_time
			item['message_number'] = msg_no.extract()
			yield item