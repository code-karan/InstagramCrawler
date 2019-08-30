# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep

# paste username of profile to be scraped
# ---------Here 👇️👇️--------------------
user_id = 'thisisbillgates'

#---------------------------------------------------


class InstaCrawlerSpider(Spider):
    name = 'insta_crawler'
    global user_id
    allowed_domains = ['instagram.com/{}/'.format(user_id)]

    def start_requests(self):
        global user_id
        #opt = webdriver.ChromeOptions()
        #opt.add_extension("/home/karan/Desktop/InstaCrawler/Block-image_v1.1.crx")
        #browser = webdriver.Chrome(chrome_options=opt)
        self.driver = webdriver.Chrome('/home/karan/Desktop/chromedriver')

        # get profile page
        self.driver.get('https://www.instagram.com/{}'.format(user_id))
        
        
        
        #scroll through an infinite page

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_list = []
        self.post_caption_list = []

        while True:
                # Scroll down to bottom
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                sleep(3)
                # assign page source
                self.select_profile = Selector(text = self.driver.page_source)

                # fetch all posts
                sleep(1)
                posts = self.select_profile.xpath('//*[@class="v1Nh3 kIKUG  _bz0w"]/a/@href').extract()
                
                #self.post_likes_list = []
                for post in posts:
                    sleep(1)
                    post_url = 'https://instagram.com/' + post
                    self.driver.get(post_url)
                    
                    #fetch post caption
                    self.select_post = Selector(text = self.driver.page_source)
                    self.post_caption = self.select_post.xpath('//*[@class="C4VMK"]/span/text()').extract()
                    #self.post_caption = self.driver.find_element_by_xpath('//*[@class="C4VMK"]/span').text
                    self.post_caption_list.append(self.post_caption)

                    #self.post_likes = self.driver.find_element_by_xpath('//*[@class="_0mzm- sqdOP yWX7d    _8A5w5    "]/span').text
                    #self.post_likes_list.append(self.post_likes)

                    yield Request(post_url, callback = self.parse_insta)


                #done with posts
                scroll_list.append(last_height)

                # back to profile page
                self.driver.get('https://www.instagram.com/{}'.format(user_id))


                # scroll to last height
                for scroll in scroll_list:
                    self.driver.execute_script("window.scrollTo(0, {});".format(scroll))
                    sleep(4)
                    self.driver.execute_script("window.scrollTo(0, {});".format(scroll+1095))
                    sleep(3)
                    self.driver.execute_script("window.scrollTo(0, {});".format(scroll+2190))
                    sleep(3)
                    self.driver.execute_script("window.scrollTo(0, {});".format(scroll+3285))
                    sleep(3)
                    self.driver.execute_script("window.scrollTo(0, {});".format(scroll+4380))
                    sleep(3)
                    self.driver.execute_script("window.scrollTo(0, {});".format(scroll+5475))


                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
        
    
    
    def parse_insta(self, response):
        # fetching profile details
        user_name = self.select_profile.xpath('//*[@class="_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     "]/text()').extract()[0]
        name = self.select_profile.xpath('//*[@class="rhpdm"]/text()').extract()[0]
        profilePic_link = self.driver.find_element_by_class_name("_6q-tv")
        profile_caption = self.select_profile.xpath('//*[@class="-vDIg"]/span/text()').extract()
        #no_of_posts = self.driver.find_elements_by_class_name('g47SY ')[0].text
        #followers = self.driver.find_elements_by_class_name('g47SY ')[1].text
        #following = self.driver.find_elements_by_class_name('g47SY ')[2].text
        posts_fetched = len(self.post_caption_list)


        yield{
            'user_name' :user_name,
            'name' :name,
            'profile_caption ':profile_caption,
            #'no_of_posts ':no_of_posts,
            #'followers ':followers,
            #'following ':following,
            'profilePic_link ':profilePic_link.get_attribute("src"),
            'post_caption_list ':self.post_caption_list,
            'no of posts fetched ':posts_fetched,
            #'post_likes_list ':self.post_likes_list,
        }




