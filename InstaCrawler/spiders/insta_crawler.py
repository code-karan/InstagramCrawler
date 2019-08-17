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
        self.select_profile = Selector(text = self.driver.page_source)
        

        #process all posts
        posts = self.select_profile.xpath('//*[@class="v1Nh3 kIKUG  _bz0w"]/a/@href').extract()
        self.post_caption_list = []
        for post in posts:
            sleep(1)
            post_url = 'https://instagram.com/' + post
            self.driver.get(post_url)
            self.select_post = Selector(text = self.driver.page_source)
            
            self.post_caption = self.select_post.xpath('//*[@class="C4VMK"]/span/text()').extract()
            self.post_caption_list.append(self.post_caption)
            
        yield Request(post_url, callback = self.parse_insta)
    
    
    def parse_insta(self, response):
        # fetching profile details
        user_name = self.select_profile.xpath('//*[@class="_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     "]/text()').extract()[0]
        name = self.select_profile.xpath('//*[@class="rhpdm"]/text()').extract()[0]
        profile_caption = self.select_profile.xpath('//*[@class="-vDIg"]/span/text()').extract()[0]
        #no_of_posts = self.driver.find_elements_by_class_name('g47SY ')[0].text
        #followers = self.driver.find_elements_by_class_name('g47SY ')[1].text
        #following = self.driver.find_elements_by_class_name('g47SY ')[2].text


        yield{
            'user_name' :user_name,
            'name' :name,
            'profile_caption ':profile_caption,
            #'no_of_posts ':no_of_posts,
            #'followers ':followers,
            #'following ':following,
            'post_caption_list ':self.post_caption_list,
        }




