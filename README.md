# lagou-spider
拉勾网招聘信息抓取/spider框架


# 功能说明
抓取拉勾网上的招聘信息和职位详情

# 使用方法

1. 安装spider  `pip install spider` 
2. 安装pymysql依赖包  `pip install pymysql`
3. 编辑`lagou/spiders/lagouSpider.py`中的`keywords`、`citys`，分别代表需要抓取的职位关键词和城市
4. 将`lagou/lagou.sql`导入到mysql数据库中
5. 命令行执行爬虫命令，例如`scrapy crawl lagou`，注意：该命令需要在lagou文件夹下执行

