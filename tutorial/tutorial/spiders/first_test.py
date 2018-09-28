import scrapy


class BlogSpider(scrapy.Spider):
    name = "blogspider"

    # shortcut verison to start_requests method
    # start_urls = ["https://www.webscraper.io/test-sites/tables"]
    def start_requests(self):
        urls = ["https://www.webscraper.io/test-sites/tables"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url
        filename = "spider1.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log("Saved file %s" % filename)
