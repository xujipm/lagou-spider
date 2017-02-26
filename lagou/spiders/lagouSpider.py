# -*- coding: utf-8 -*-
# author: xujipm

import scrapy
import json
from scrapy.http import FormRequest, Request
from lagou.items import JobsPositionItem, JobDetailItem


class LagouspiderSpider(scrapy.Spider):
    # name = "lagouSpider"
    name = "lagou"
    allowed_domains = ["lagou.com"]
    # start_urls = ['http://lagou.com/']
    keywords = ["产品经理", "数据产品经理"]
    citys = ["成都", "北京", "厦门"]
    first = "true"
    pn = 1
    kdFlag = 0
    cityFlag = 0
    kd = keywords[kdFlag]
    city = citys[cityFlag]
    isEnd = False

    def start_requests(self):
        return [FormRequest(url="https://www.lagou.com/jobs/positionAjax.json?" +
                            "px=default&city=" + self.city +
                            "&needAddtionalResult=false",
                            formdata={'first': self.first,
                                      'pn': str(self.pn), 'kd': self.kd},
                            callback=self.job_parse)]

    def job_parse(self, response):
        self.logger.info("获取到：job_parse(self, response)")
        try:
            self.logger.info("我错了try")
            jdata = json.loads(response.text)
            if not(jdata['success']):
                self.logger.error('jobs获取失败')
            else:
                for result in jdata['content']['positionResult']['result']:
                    jobsItem = JobsPositionItem()
                    for k in result:
                        # self.logger.info(k + ": " + str(result[k]))
                        # jobsItem.add_value(k, result[k]) ## 不知道啥不能用了
                        jobsItem[k] = result[k]
                    yield jobsItem
                    yield Request(url="https://www.lagou.com/jobs/" +
                                  str(result['positionId']) + ".html",
                                  callback=self.jobDetail_parse)
                totalCount = jdata['content']['positionResult']['totalCount']
                resultSize = jdata['content']['positionResult']['resultSize']
                # TODO 暂不清楚为啥会有0，为0的时候先强制修改为15好了
                if resultSize == 0:
                    resultSize = 15
                self.pn = self.pn + 1

                if self.pn - 1 > totalCount / resultSize:
                    self.logger.info(self.kd + "_" + self.city + "的jobs抓取完毕")
                    self.pn = 1

                    if self.kdFlag < len(self.keywords) - 1:
                        if self.cityFlag < len(self.citys) - 1:
                            self.kdFlag = self.kdFlag + 1
                            self.kd = self.keywords[self.kdFlag]
                            self.logger.info("开始切换关键词抓取" + self.kd + self.city)
                        else:
                            self.logger.error("让我出现就是你的不对了～")

                    if self.kdFlag == len(self.keywords) - 1:
                        if self.cityFlag < len(self.citys) - 1:
                            self.kdFlag = 0
                            self.cityFlag = self.cityFlag + 1
                            self.kd = self.keywords[self.kdFlag]
                            self.city = self.citys[self.cityFlag]
                            self.logger.info("开始切换城市抓取" + self.kd + self.city)
                        else:
                            self.logger.info("不错哟～，全部抓取完毕")
                            self.isEnd = True
                if not self.isEnd:
                    yield FormRequest(url="https://www.lagou.com/jobs/positionAjax.json?" +
                                      "px=default&city=" + self.city +
                                      "&needAddtionalResult=false",
                                      formdata={'first': self.first,
                                                'pn': str(self.pn), 'kd': self.kd},
                                      callback=self.job_parse)
        except:
            self.logger.info("我错了except")
            yield Request(url=response.url,
                          formdata=response.formdata,
                          meta={"change_proxy": True},
                          callback=self.job_parse)

    def jobDetail_parse(self, response):
        try:
            self.deal_jobDetail_parse(response)
            jobDetailItem = JobDetailItem()
            jobDetailItem['jobs_positionId'] = response.xpath('//*[@id="jobid"]/@value').extract()[0]
            jobDetailItem['jobs_description'] = response.xpath('//*[@id="job_detail"]/dd[2]/div').extract()[0]
            jobDetailItem['jobs_addr'] = response.xpath('//*[@id="job_detail"]/dd[2]/div').extract()[0]
            jobDetailItem['jobs_positionLng'] = response.xpath('//*[@id="job_detail"]/dd[3]/input[1]/@value').extract()[0]
            jobDetailItem['jobs_positionLat'] = response.xpath('//*[@id="job_detail"]/dd[3]/input[2]/@value').extract()[0]
            jobDetailItem['jobs_positionAddress'] = response.xpath('//*[@id="job_detail"]/dd[3]/input[3]/@value').extract()[0]
            yield jobDetailItem
        except:
            yield Request(url=response.url,
                          meta={"change_proxy": True},
                          callback=self.jobDetail_parse)


    def company_parse(self, response):
        pass
