# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'


    start_urls = [
        'https://www.amazon.com/s?bbn=1&rh=n%3A283155%2Cn%3A%211000%2Cn%3A1%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1588077484&rnid=1250225011&ref=lp_1_nr_p_n_publication_date_0'
    ]
    def parse(self, response):

        items = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        while '\n' in product_author:
                        product_author.remove('\n')
                        print(product_author)
        product_price = response.css('.sg-col-24-of-28:nth-child(8) .a-spacing-mini .a-price-fraction , .sg-col-24-of-28:nth-child(8) .a-spacing-mini .a-price-whole , .a-spacing-top-small+ .a-spacing-top-mini .a-spacing-mini:nth-child(1) .a-price-fraction , .a-spacing-top-small+ .a-spacing-top-mini .a-spacing-mini:nth-child(1) .a-price-whole , .sg-col-24-of-28:nth-child(5) .a-spacing-top-small .a-price-fraction , .sg-col-24-of-28:nth-child(5) .a-spacing-top-small .a-price-whole , .sg-col-24-of-28:nth-child(3) .a-spacing-mini:nth-child(1) .a-price-fraction , .sg-col-24-of-28:nth-child(3) .a-spacing-mini:nth-child(1) .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
