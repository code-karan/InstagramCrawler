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
        url = 'https://www.instagram.com/chrishemsworth/'
        #self.driver.get('https://www.instagram.com/chrishemsworth/')
        

        #process all posts
        '''
        posts = self.select.xpath('//*[@class="v1Nh3 kIKUG  _bz0w"]/a/@href').extract()
        for post in posts:
            sleep(1)
            post_url = 'https://instagram.com/' + post
            self.driver.get(post_url)  
            yield Request(post_url, callback = self.parse_posts)
        '''
        
        
        yield Request(url, callback = self.parse_profile)


    '''
    def parse_posts(self, response):
        
        #post_caption = self.select.xpath('//*[@class="C4VMK"]/span/text()').extract()
        #post_caption = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span/text()')
        #post_caption = self.driver.find_element_by_class_name("C4VMK").find_element_by_tag_name('span')
        yield{
            'post_caption':post_caption,
        }
    '''
    
    
    def parse_profile(self, response):
        # fetching profile details
        user_name = self.select.xpath('//*[@class="_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     "]/text()').extract()[0]
        name = self.select.xpath('//*[@class="rhpdm"]/text()').extract()[0]
        profile_caption = self.select.xpath('//*[@class="-vDIg"]/span/text()').extract()[0]
        no_of_posts = self.driver.find_elements_by_class_name('g47SY ')[0].text
        followers = self.driver.find_elements_by_class_name('g47SY ')[1].text
        following = self.driver.find_elements_by_class_name('g47SY ')[2].text

        yield{
            'user_name':user_name,
            'name':name,
            'profile_caption':profile_caption,
            'no_of_posts':no_of_posts,
            'followers':followers,
            'following':following,
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



