import scrapy
from net_a_porterscrapyer.items import NetAPorterscrapyerItem

class EcomSpider(scrapy.Spider):

	#name of the spider
	name = "ecommerce"
	
	#lookup urls 
	def start_requests(self):
		urls = [
				'https://www.net-a-porter.com/en-in/shop/shoes',
				#'',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	#this parse fuction will use upper link to scrap data from them use css selector	
	def parse(self, response):
		item = NetAPorterscrapyerItem()
		for products in response.css('div.ProductItem24.ProductList52__productItem'):
				item['name'] = products.css('span.ProductItem24__name::text').get().replace('+','')
				item['brand'] = products.css('span.ProductItem24__designer::text').get()
				item['original_price'] = float(products.css('span[itemprop="price"]::text').get().replace('$', '').replace(',',''))
				item['sale_price'] = float(products.css('span[itemprop="price"]::text').get().replace('$', '').replace(',',''))
				item['image_url'] = products.css('div.Image18__imageContainer img::attr(src)').get()
				item['product_page_url'] = products.css('div.ProductItem24__p meta::attr(content)').get()
				item['product_category'] ='footwear'

				yield item

		#this next page variable will find the next page link when the next 
		#page is available then call the parse function to extract the page information until reached the end.
		next_page = response.css('a.Pagination7__next').attrib['href']
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)
