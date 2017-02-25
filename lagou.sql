## InnoDB引擎下会报错，还未处理好，暂时使用MyISAM引擎，报错内容：(1118, 'Row size too large (> 8126)

DROP DATABASE IF EXISTS `lagou`;
CREATE DATABASE `lagou`;

USE `lagou`;

DROP TABLE IF EXISTS `job_detail`;
CREATE TABLE `job_detail` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `jobs_positionId` int(20) unsigned DEFAULT NULL,
  `jobs_description` text,
  `jobs_addr` char(255) DEFAULT NULL,
  `jobs_positionLng` char(255) DEFAULT NULL,
  `jobs_positionLat` char(255) DEFAULT NULL,
  `jobs_positionAddress` char(255) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


LOCK TABLES `job_detail` WRITE;
UNLOCK TABLES;


DROP TABLE IF EXISTS `job`;
CREATE TABLE `job` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `businessZones` char(255) DEFAULT NULL,
  `imState` char(255) DEFAULT NULL,
  `lastLogin` char(255) DEFAULT NULL,
  `companyId` int(20) unsigned DEFAULT NULL,
  `companyShortName` char(255) DEFAULT NULL,
  `positionId` int(20) unsigned DEFAULT NULL,
  `industryField` char(255) DEFAULT NULL,
  `education` char(255) DEFAULT NULL,
  `workYear` char(255) DEFAULT NULL,
  `city` char(255) DEFAULT NULL,
  `positionAdvantage` char(255) DEFAULT NULL,
  `createTime` char(255) DEFAULT NULL,
  `salary` char(255) DEFAULT NULL,
  `positionName` char(255) DEFAULT NULL,
  `companySize` char(255) DEFAULT NULL,
  `financeStage` char(255) DEFAULT NULL,
  `companyLogo` char(255) DEFAULT NULL,
  `jobNature` char(255) DEFAULT NULL,
  `approve` char(255) DEFAULT NULL,
  `district` char(255) DEFAULT NULL,
  `companyLabelList` char(255) DEFAULT NULL,
  `score` char(255) DEFAULT NULL,
  `publisherId` int(20) unsigned DEFAULT NULL,
  `explain` char(255) DEFAULT NULL,
  `plus` char(255) DEFAULT NULL,
  `pcShow` char(255) DEFAULT NULL,
  `appShow` char(255) DEFAULT NULL,
  `deliver` char(255) DEFAULT NULL,
  `gradeDescription` char(255) DEFAULT NULL,
  `promotionScoreExplain` char(255) DEFAULT NULL,
  `firstType` char(255) DEFAULT NULL,
  `secondType` char(255) DEFAULT NULL,
  `positionLables` char(255) DEFAULT NULL,
  `companyFullName` char(255) DEFAULT NULL,
  `adWord` char(255) DEFAULT NULL,
  `formatCreateTime` char(255) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


LOCK TABLES `job` WRITE;
UNLOCK TABLES;
