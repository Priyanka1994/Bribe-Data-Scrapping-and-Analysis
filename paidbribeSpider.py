# -*- coding: utf-8 -*-
import scrapy


class paidbribebotSpider(scrapy.Spider):
    name = 'paidbribebot'
    allowed_domains = ['http://www.ipaidabribe.com/']
    start_urls = ['http://www.ipaidabribe.com/reports/all?page=%s' % page for page in range(0,120)]

    def parse(self, response):
        #extracting the content using css selectors
        title = response.css('.heading-3').xpath('./a/@title').getall()
        amount = response.css('.paid-amount').xpath('./span/text()').getall()
        department = response.css('.transaction').xpath('./a/@title').getall()
        transDetail = response.css('.unique-reference').xpath('text()').getall()
        views = response.css('.views').xpath('text()').getall()
        city = response.css('.location').xpath('text()').getall()
        date = response.css('.date').xpath('text()').getall()

        #Give the extracted content row wise
        for item in zip(title,amount,department,transDetail,views,city,date):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'amount' : item[1],
                'department' : item[2],
                'transDetail' : item[3],
                'views' : item[4],
                'city' : item[5],
                'date' : item[6],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
        
        
            
            
      
        
 
