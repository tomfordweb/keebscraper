import scrapy

from scraper.items import EbayProduct
class EbaySpider(scrapy.Spider):
	
	name = "ebay-search"
	allowed_domains = ["ebay.com"]
	start_urls = ["https://www.ebay.com"]

	# Allow a custom parameter (-a flag in the scrapy command)
	def __init__(self, search=""):
		self.search_string = search

	def parse(self, response):
		# Extrach the trksid to build a search request	
		trksid = response.css("input[type='hidden'][name='_trksid']").xpath("@value").extract()[0]       
		
		# Build the url and start the requests
		yield scrapy.Request("http://www.ebay.com/sch/i.html?_from=R40&_trksid=" + trksid +
							 "&_nkw=" + self.search_string.replace(' ','+') + "&_ipg=200", 
							 callback=self.parse_link)

	# Parse the search results
	def parse_link(self, response):
		# Extract the list of products 
		results = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')

		# Extract info for each product
		for product in results:		
			item = EbayProduct()
			name = product.xpath('.//*[@class="s-item__title"]//text()').extract_first()
			# Sponsored or New Listing links have a different class
			if name == None:
				name = product.xpath('.//*[@class="s-item__title s-item__title--has-tags"]/text()').extract_first()			
				if name == None:
					name = product.xpath('.//*[@class="s-item__title s-item__title--has-tags"]//text()').extract_first()			
			if name == 'New Listing':
				name = product.xpath('.//*[@class="s-item__title"]//text()').extract()[1]

			# If this get a None result
			if name == None:
				name = "ERROR"
			item['name'] = name
			item['price'] = product.xpath('.//*[@class="s-item__price"]/text()').extract_first()
			item['status'] = product.xpath('.//*[@class="SECONDARY_INFO"]/text()').extract_first()
			# seller_level = product.xpath('.//*[@class="s-item__etrs-text"]/text()').extract_first()
			# location = product.xpath('.//*[@class="s-item__location s-item__itemLocation"]/text()').extract_first()
			product_url = product.xpath('.//a[@class="s-item__link"]/@href').extract_first()
			item['url'] = product_url

			# Set default values
			stars = 0
			ratings = 0

			stars_text = product.xpath('.//*[@class="clipped"]/text()').extract_first()
			if stars_text: stars = stars_text[:3]
			ratings_text = product.xpath('.//*[@aria-hidden="true"]/text()').extract_first()
			if ratings_text: ratings = ratings_text.split(' ')[0]
			item['stars'] = stars
			item['ratings'] = ratings

			# Go to the product details page
			data = {'summary_data': item}
			if product_url != None:
				yield item
				# yield scrapy.Request(product_url, meta=data, callback=self.parse_product_details)

		# Get the next page
		next_page_url = response.xpath('//a[@class="pagination__next"]/@href').extract_first()
		if next_page_url != None and False == str(next_page_url).endswith("#"):
			yield scrapy.Request(next_page_url, callback=self.parse_link)

	# Parse details page for each product
	def parse_product_details(self, response):
		data = response.meta['item']

		data['unique_identifier'] = response.xpath('//h2[@itemprop="gtin13"]/text()').extract_first()

		yield data