# -*- coding: utf-8 -*-


        
#目录页+详情页
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from job51.items import Job51Item

class CominfoSpider(CrawlSpider):
    name = 'cominfo'
    #beijing
    # start_urls = ['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #shanghai
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=020000&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #GuangZhou
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=030200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #shenzhou
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #wuhan
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=180200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #XiAn
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=200200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #HangZhou
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=080200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #NanJing
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=070200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #chenggu
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=090200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #chongqing
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=060000&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #dongguan
    # start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=030800&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #Dalian
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=230300&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #ShenYang
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=230200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #SuZhou
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=070300&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #KunMing
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=250200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #ChangSha
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=190200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #HeFei
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=150200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #ningbo
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=080300&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #ZhengZhou
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=170200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #TianJin
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=050000&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #QingDao
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=120300&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #Jinan
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=120200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #HaErBin
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=220200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #ChangChun
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=240200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #FuZhou
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=110200&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #ZhuSanJiao
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=01&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    #Beijing
    start_urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9']
    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        #提取了下一页的标签，不断提取直至无法取得下一页的标签
        Rule(LinkExtractor(allow=(r'http://search.51job.com/list/230300,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,[0-9]+?.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')),follow=True),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=(r'http://jobs.51job.com/all/co[0-9]*.html')), callback='parse_item'),
    )
    count=0
    def parse_item(self, response):
        #self.log('Hi, this is an item page! %s' % response.url)
        #print(response.body)
        count += 1
        item = Job51Item()
        item['company_url']=response.url
        # item['company_name']=response.xpath('//div[@class="in "]/title/text()').extract[0]
        #item['company_name']=response.xpath('/html/head/title/text()').extract[0] 报错
        #item['company_name']=response.xpath('/html/head/title/text()')  正确
        #item['company_name']=response.xpath('//div[@class="in "]/h1/@title')
        #正确应用text()与extract() 
        cname=response.xpath('//div[@class="in "]/h1/@title | //div[@class="in img_on"]/h1/@title')
        #item['company_name']=cname[0].extract()  与下面语句效果相同
        item['company_name']=cname.extract()[0]
        caddress=response.xpath('//p[@class="fp"]/text()').extract()
        cadstr="".join(caddress)
        item['company_address']=cadstr.strip().replace(" ","")
        cinfolist=response.xpath('//div[@class="in"]/p/text()').extract()
        cinfostr="".join(cinfolist)
        #如果需要换行，或者需要正常在网页上显示，去掉下面的后处理过程
        cinfo=cinfostr.strip().replace(" ","").replace('\xa0','')
        item['company_info']=cinfo
        
        yield item
        

        #pass
