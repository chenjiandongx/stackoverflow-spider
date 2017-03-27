import scrapy
from stackoverflow.spiders.items import StackoverflowItem


class StackoverflowSpider(scrapy.Spider):

    name = "stackoverflow"

    def start_requests(self):

        urls = ['http://stackoverflow.com/questions?page={page}&sort=votes&pagesize=50'.format(page=page)
                for page in range(11, 21)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        for index in range(1, 51):
            sel = response.xpath('//*[@id="questions"]/div[{index}]'.format(index=index))
            item = StackoverflowItem()
            item['votes'] = sel.xpath('div[1]/div[2]/div[1]/div[1]/span/strong/text()').extract()
            item['answers'] = sel.xpath('div[1]/div[2]/div[2]/strong/text()').extract()
            item['views'] = "".join(sel.xpath('div[1]/div[3]/@title').extract()).split()[0].replace(",", "")
            item['questions'] = sel.xpath('div[2]/h3/a/text()').extract()
            item['links'] = "".join(sel.xpath('div[2]/h3/a/@href').extract()).split("/")[2]
            item['tags'] = sel.xpath('div[2]/div[2]/a/text()').extract()
            yield item
