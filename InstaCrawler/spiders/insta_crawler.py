# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep


class InstaCrawlerSpider(Spider):
    name = 'insta_crawler'
    allowed_domains = ['instagram.com/chrishemsworth/']

    def start_requests(self):
        self.driver = webdriver.Chrome('/home/karan/Desktop/chromedriver')
        self.driver.get('https://www.instagram.com/chrishemsworth/')

        self.select = Selector(text = self.driver.page_source)

        #process all posts
        posts = self.select.xpath('//*[@class="v1Nh3 kIKUG  _bz0w"]/a/@href').extract()
        for post in posts:
            sleep(2)
            url = 'https://instagram.com/' + post
            yield Request(url, callback = self.parse_insta)
        #url = 'https://www.instagram.com/chrishemsworth/'
        #yield Request(url, callback = self.parse_insta)

    
    def parse_insta(self, response):
        # fetching profile details
        user_name = self.select.xpath('//*[@class="_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     "]/text()').extract()[0]
        name = self.select.xpath('//*[@class="rhpdm"]/text()').extract()[0]
        profile_caption = self.select.xpath('//*[@class="-vDIg"]/span/text()').extract()[0]
        #post_caption = self.select.xpath('//*[@class="C4VMK"]/span/text()').extract()[0]
        #no_of_posts = self.select.xpath('//*[@class="g47SY "]/text()').extract()[0]
        #no_of_followers = self.select.xpath('//*[@class="g47SY "]/text()').extract()[1]
        #no_of_following = self.select.xpath('//*[@class="g47SY "]/text()').extract()[2]

        yield{
            'user_name':user_name,
            'name':name,
            'profile_caption':profile_caption,
            #'post_caption':post_caption,
            #'no_of_posts':no_of_posts,
            #'no_of_followers':no_of_followers,
            #'no_of_following':no_of_following,
        }





    '''
    def parse_requests(self, response):
        # fetching profile details
        user_name = select.xpath('//*[@class="_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     "]/text()').extract()[0]
        name = select.xpath('//*[@class="rhpdm"]/text()').extract()[0]
        profile_caption = select.xpath('//*[@class="-vDIg"]/span/text()').extract()[0]
        no_of_posts = select.xpath('//*[@class="g47SY "]/text()').extract()[0]
        no_of_followers = select.xpath('//*[@class="g47SY "]/text()').extract()[1]
        no_of_following = select.xpath('//*[@class="g47SY "]/text()').extract()[2]

        yield{
            'user_name':user_name,
            'name':name,
            'profile_caption':profile_caption,
            'no_of_posts':no_of_posts,
            'no_of_followers':no_of_followers,
            'no_of_following':no_of_following
        }
    '''



