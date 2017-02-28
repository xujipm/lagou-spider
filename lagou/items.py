# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsPositionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    businessZones = scrapy.Field()
    imState = scrapy.Field()
    lastLogin = scrapy.Field()
    companyId = scrapy.Field()
    companyShortName = scrapy.Field()
    positionId = scrapy.Field()
    industryField = scrapy.Field()
    education = scrapy.Field()
    workYear = scrapy.Field()
    city = scrapy.Field()
    positionAdvantage = scrapy.Field()
    createTime = scrapy.Field()
    salary = scrapy.Field()
    positionName = scrapy.Field()
    companySize = scrapy.Field()
    financeStage = scrapy.Field()
    companyLogo = scrapy.Field()
    jobNature = scrapy.Field()
    approve = scrapy.Field()
    district = scrapy.Field()
    companyLabelList = scrapy.Field()
    score = scrapy.Field()
    publisherId = scrapy.Field()
    explain = scrapy.Field()
    plus = scrapy.Field()
    pcShow = scrapy.Field()
    appShow = scrapy.Field()
    deliver = scrapy.Field()
    gradeDescription = scrapy.Field()
    promotionScoreExplain = scrapy.Field()
    firstType = scrapy.Field()
    secondType = scrapy.Field()
    positionLables = scrapy.Field()
    companyFullName = scrapy.Field()
    adWord = scrapy.Field()
    formatCreateTime = scrapy.Field()


class JobDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobs_positionId = scrapy.Field()
    jobs_description = scrapy.Field()
    jobs_addr = scrapy.Field()
    jobs_positionLng = scrapy.Field()
    jobs_positionLat = scrapy.Field()
    jobs_positionAddress = scrapy.Field()


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()


class InterviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    i_positionId = scrapy.Field()
    i_tagArray = scrapy.Field()
    i_id = scrapy.Field()
    i_portrait = scrapy.Field()
    i_username = scrapy.Field()
    i_userId = scrapy.Field()
    i_isAnonymous = scrapy.Field()
    i_isInterview = scrapy.Field()
    i_noInterviewReason = scrapy.Field()
    i_noInterviewType = scrapy.Field()
    i_usefulCount = scrapy.Field()
    i_myScore = scrapy.Field()
    i_describeScore = scrapy.Field()
    i_interviewerScore = scrapy.Field()
    i_companyScore = scrapy.Field()
    i_comprehensiveScore = scrapy.Field()
    i_content = scrapy.Field()
    i_evaluation = scrapy.Field()
    i_positionId = scrapy.Field()
    i_positionName = scrapy.Field()
    i_companyName = scrapy.Field()
    i_positionType = scrapy.Field()
    i_hrId = scrapy.Field()
    i_orderId = scrapy.Field()
    i_companyId = scrapy.Field()
    i_replyCount = scrapy.Field()
    i_isAllowReply = scrapy.Field()
    i_tags = scrapy.Field()
    i_type = scrapy.Field()
    i_status = scrapy.Field()
    i_source = scrapy.Field()
    i_createTime = scrapy.Field()
