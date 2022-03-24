import scrapy


class MedalsSpider(scrapy.Spider):
    name = 'medals'
    allowed_domains = ['fi.wikipedia.org']
    start_urls = ['https://fi.wikipedia.org/wiki/Olympialaiset']

    def parse(self, response):
        
        filename = 'olympialaiset.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
