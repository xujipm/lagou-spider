# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from lagou.items import JobsPositionItem, JobDetailItem, CompanyItem
import pymysql
from scrapy.exceptions import DropItem
from configparser import ConfigParser


class LagouPipeline(object):
    cfg = ConfigParser()
    cfg.read('config.py')
    host = cfg.get('db-server', 'host')
    db = cfg.get('db-server', 'db')
    usr = cfg.get('db-server', 'usr')
    passwd = cfg.get('db-server', 'passwd')

    def __init__(self):
        self.cursor = ""
        self.conn = ""

    def open_spider(self, spider):
        self.conn = pymysql.connect(host=self.host,
                                    user=self.usr,
                                    password=self.passwd,
                                    database=self.db,
                                    port=3306,
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, JobsPositionItem):
            table = "job"
        elif isinstance(item, JobDetailItem):
            table = "job_detail"
        elif isinstance(item, CompanyItem):
            pass

        sql = "INSERT INTO `" + table + "` ("
        sqlValues = ") VALUES ("
        dic = {}
        for k in item:
            sql = sql + "`" + k + "`, "
            sqlValues = sqlValues + "%(" + k + ")s, "
            dic[k] = str(item[k])
        sql = sql[:-2] + sqlValues[:-2] + ")"
        self.cursor.execute(sql, dic)
        self.conn.commit()
        raise DropItem()

        return item
