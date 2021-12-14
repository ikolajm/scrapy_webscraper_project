import scrapy

class PostsSpider(scrapy.Spider):
    name = 'items'

    start_urls = [
        'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1',
        'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=2'
    ]

    def parse(self, response):
        for item in response.css('div.col-sm-4'):
            yield {
                'title': item.css('.thumbnail .caption h4 a.title::text')[0].get(),
                'price': item.css('.thumbnail .caption h4.price::text')[0].get(),
                'description': item.css('.thumbnail .caption p.description::text')[0].get()
            }