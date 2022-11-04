/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80025
Source Host           : localhost:3306
Source Database       : equipment_mg

Target Server Type    : MYSQL
Target Server Version : 80025
File Encoding         : 65001

Date: 2022-11-04 15:50:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cabinet
-- ----------------------------
DROP TABLE IF EXISTS `cabinet`;
CREATE TABLE `cabinet` (
  `cab_id` int NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `cab_num` varchar(45) NOT NULL COMMENT '''机柜编号''',
  `cab_name` varchar(45) NOT NULL COMMENT '''机柜名称''',
  `room_id` int unsigned NOT NULL COMMENT '机房ID',
  `is_use` int DEFAULT '1' COMMENT '是否使用,1:使用，0:未使用',
  `pdu_num` int DEFAULT NULL COMMENT 'PDU数量',
  `count_position` int DEFAULT NULL,
  `free` int DEFAULT NULL COMMENT '剩余U数',
  `comment` varchar(45) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`cab_id`),
  UNIQUE KEY `cab_id_UNIQUE` (`cab_id`),
  KEY `roomid` (`room_id`),
  KEY `cab_name` (`cab_name`),
  KEY `cab_num` (`cab_num`),
  CONSTRAINT `roomid` FOREIGN KEY (`room_id`) REFERENCES `machine_room` (`room_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb3 COMMENT='机柜信息';

-- ----------------------------
-- Records of cabinet
-- ----------------------------
INSERT INTO `cabinet` VALUES ('1', 'A01', 'A01', '1', '1', '2', '42', null, null);
INSERT INTO `cabinet` VALUES ('3', 'A02', 'A02', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('4', 'A03', 'A03', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('5', 'A04', 'A04', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('6', 'A05', 'A05', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('7', 'A06', 'A06', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('8', 'A07', 'A07', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('9', 'A08', 'A08', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('10', 'A09', 'A09', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('11', 'A10', 'A10', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('12', 'B01', 'B01', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('13', 'B02', 'B02', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('14', 'B03', 'B03', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('15', 'B04', 'B04', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('16', 'B05', 'B05', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('17', 'B06', 'B06', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('18', 'B07', 'B07', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('19', 'B08', 'B08', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('20', 'B09', 'B09', '1', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('21', 'B10', 'B10', '1', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('22', 'C01', 'C01', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('23', 'C02', 'C02', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('24', 'C03', 'C03', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('25', 'C04', 'C04', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('26', 'C05', 'C05', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('27', 'C06', 'C06', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('28', 'C07', 'C07', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('29', 'C08', 'C08', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('30', 'C09', 'C09', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('31', 'C10', 'C10', '1', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('32', 'D01', 'D01', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('33', 'D02', 'D02', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('34', 'D03', 'D03', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('35', 'D04', 'D04', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('36', 'D05', 'D05', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('37', 'D06', 'D06', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('38', 'D07', 'D07', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('39', 'D08', 'D08', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('40', 'D09', 'D09', '1', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('41', 'D10', 'D10', '1', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('48', 'A01', 'A01', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('49', 'A02', 'A02', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('50', 'A03', 'A03', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('51', 'A04', 'A04', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('52', 'A05', 'A05', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('53', 'A06', 'A06', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('54', 'A07', 'A07', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('55', 'A08', 'A08', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('56', 'A09', 'VMAX 10K', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('57', 'A10', 'VMAX 10K', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('58', 'B01', 'B01', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('59', 'B02', 'B02', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('60', 'B03', 'B03', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('61', 'B04', 'B04', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('62', 'B05', 'B05', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('63', 'B06', 'B06', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('64', 'B07', 'B07', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('65', 'B08', 'B08', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('66', 'B09', 'B09', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('67', 'B10', 'B10', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('68', 'C01', 'C01', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('69', 'C02', 'C02', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('70', 'C03', 'C03', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('71', 'C04', 'C04', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('72', 'C05', 'C05', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('73', 'C06', 'C06', '2', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('74', 'C07', 'C07', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('75', 'C08', 'C08', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('76', 'C09', 'C09', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('77', 'C10', 'C10', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('78', 'D01', 'D01', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('79', 'D02', 'D02', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('80', 'D03', 'D03', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('81', 'D04', 'D04', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('82', 'D05', 'D05', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('83', 'D06', 'D06', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('84', 'D07', 'D07', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('85', 'D08', 'D08', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('86', 'D09', 'D09', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('87', 'D10', 'D10', '2', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('88', 'A01', 'A01', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('89', 'A02', 'A02', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('90', 'A03', 'A03', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('91', 'A04', 'A04', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('92', 'A05', 'A05', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('93', 'A06', 'A06', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('94', 'A07', 'A07', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('95', 'A08', 'A08', '3', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('96', 'A09', 'A09', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('97', 'A10', 'A10', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('98', 'B01', 'B01', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('99', 'B02', 'B02', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('100', 'B03', 'B03', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('101', 'B04', 'B04', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('102', 'B05', 'B05', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('103', 'B06', 'B06', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('104', 'B07', 'B07', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('105', 'B08', 'B08', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('106', 'B09', 'B09', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('107', 'B10', 'B10', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('108', 'C01', 'C01', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('109', 'C02', 'C02', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('110', 'C03', 'C03', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('111', 'C04', 'C04', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('112', 'C05', 'C05', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('113', 'C06', 'C06', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('114', 'C07', 'C07', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('115', 'C08', 'C08', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('116', 'C09', 'C09', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('117', 'C10', 'C10', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('118', 'D01', 'D01', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('119', 'D02', 'D02', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('120', 'D03', 'D03', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('121', 'D04', 'D04', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('122', 'D05', 'D05', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('123', 'D06', 'D06', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('124', 'D07', 'D07', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('125', 'D08', 'D08', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('126', 'D09', 'D09', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('127', 'D10', 'D10', '3', '0', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('128', 'KF01', 'KF01', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('129', 'KF02', 'KF02', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('130', 'KF03', 'KF03', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('131', 'KF04', 'KF04', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('132', 'KF05', 'KF05', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('133', 'KF06', 'KF06', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('134', 'KF07', 'KF07', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('135', 'KF08', 'KF08', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('136', 'KF09', 'KF09', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('137', 'KF10', 'KF10', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('138', 'KF11', 'KF11', '4', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('139', 'A11', '波分机柜', '2', '1', null, '42', null, '（电信、中信）');
INSERT INTO `cabinet` VALUES ('150', 'A01', 'A01', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('151', 'A02', 'A02', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('152', 'A03', 'A03', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('153', 'A04', 'A04', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('154', 'A05', 'A05', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('155', 'A06', 'A06', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('156', 'A07', 'A07', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('157', 'A08', 'A08', '5', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('158', 'C01', 'C01', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('159', 'C02', 'C02', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('160', 'C03', 'C03', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('161', 'C04', 'C04', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('162', 'C05', 'C05', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('163', 'C06', 'C06', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('165', 'A01', 'A01', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('166', 'A02', 'A02', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('167', 'A03', 'A03', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('168', 'A04', 'A04', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('169', 'A05', 'A05', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('170', 'A06', 'A06', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('171', 'C07', 'C07', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('172', 'C08', 'C08', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('173', 'C09', 'C09', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('174', 'B01', 'B01', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('175', 'B02', 'B02', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('176', 'B03', 'B03', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('177', 'B04', 'B04', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('178', 'B05', 'B05', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('179', 'B06', 'B06', '25', '1', null, '42', null, null);
INSERT INTO `cabinet` VALUES ('180', 'B07', 'B07', '25', '1', null, '42', null, null);

-- ----------------------------
-- Table structure for cab_position
-- ----------------------------
DROP TABLE IF EXISTS `cab_position`;
CREATE TABLE `cab_position` (
  `id` int NOT NULL AUTO_INCREMENT,
  `num` int NOT NULL COMMENT 'U位编号',
  `position_name` char(11) NOT NULL COMMENT 'U位名称',
  `use` varchar(255) DEFAULT NULL COMMENT '用途',
  `is_frame` int DEFAULT NULL COMMENT '是否为配线架',
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `position_num` (`position_name`),
  KEY `id` (`id`),
  KEY `id_2` (`id`),
  KEY `num` (`num`),
  KEY `num_2` (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb3 COMMENT='U位表';

-- ----------------------------
-- Records of cab_position
-- ----------------------------
INSERT INTO `cab_position` VALUES ('1', '1', '01U', '', null, null);
INSERT INTO `cab_position` VALUES ('2', '2', '02U', null, null, null);
INSERT INTO `cab_position` VALUES ('3', '3', '03U', null, null, null);
INSERT INTO `cab_position` VALUES ('4', '4', '04U', null, null, null);
INSERT INTO `cab_position` VALUES ('5', '5', '05U', null, null, null);
INSERT INTO `cab_position` VALUES ('6', '6', '06U', null, null, null);
INSERT INTO `cab_position` VALUES ('7', '7', '07U', null, null, null);
INSERT INTO `cab_position` VALUES ('8', '8', '08U', null, null, null);
INSERT INTO `cab_position` VALUES ('9', '9', '09U', null, null, null);
INSERT INTO `cab_position` VALUES ('10', '10', '10U', null, null, null);
INSERT INTO `cab_position` VALUES ('11', '11', '11U', null, null, null);
INSERT INTO `cab_position` VALUES ('12', '12', '12U', null, null, null);
INSERT INTO `cab_position` VALUES ('13', '13', '13U', null, null, null);
INSERT INTO `cab_position` VALUES ('14', '14', '14U', null, null, null);
INSERT INTO `cab_position` VALUES ('15', '15', '15U', null, null, null);
INSERT INTO `cab_position` VALUES ('16', '16', '16U', null, null, null);
INSERT INTO `cab_position` VALUES ('17', '17', '17U', null, null, null);
INSERT INTO `cab_position` VALUES ('18', '18', '18U', null, null, null);
INSERT INTO `cab_position` VALUES ('19', '19', '19U', null, null, null);
INSERT INTO `cab_position` VALUES ('20', '20', '20U', null, null, null);
INSERT INTO `cab_position` VALUES ('21', '21', '21U', null, null, null);
INSERT INTO `cab_position` VALUES ('22', '22', '22U', null, null, null);
INSERT INTO `cab_position` VALUES ('23', '23', '23U', null, null, null);
INSERT INTO `cab_position` VALUES ('24', '24', '24U', null, null, null);
INSERT INTO `cab_position` VALUES ('25', '25', '25U', null, null, null);
INSERT INTO `cab_position` VALUES ('26', '26', '26U', null, null, null);
INSERT INTO `cab_position` VALUES ('27', '27', '27U', null, null, null);
INSERT INTO `cab_position` VALUES ('28', '28', '28U', null, null, null);
INSERT INTO `cab_position` VALUES ('29', '29', '29U', null, null, null);
INSERT INTO `cab_position` VALUES ('30', '30', '30U', null, null, null);
INSERT INTO `cab_position` VALUES ('31', '31', '31U', null, null, null);
INSERT INTO `cab_position` VALUES ('32', '32', '32U', null, null, null);
INSERT INTO `cab_position` VALUES ('33', '33', '33U', null, null, null);
INSERT INTO `cab_position` VALUES ('34', '34', '34U', null, null, null);
INSERT INTO `cab_position` VALUES ('35', '35', '35U', null, null, null);
INSERT INTO `cab_position` VALUES ('36', '36', '36U', null, null, null);
INSERT INTO `cab_position` VALUES ('37', '37', '37U', null, null, null);
INSERT INTO `cab_position` VALUES ('38', '38', '38U', null, null, null);
INSERT INTO `cab_position` VALUES ('39', '39', '39U', null, null, null);
INSERT INTO `cab_position` VALUES ('40', '40', '40U', null, null, null);
INSERT INTO `cab_position` VALUES ('41', '41', '41U', null, null, null);
INSERT INTO `cab_position` VALUES ('42', '42', '42U', null, null, null);

-- ----------------------------
-- Table structure for cmd_file
-- ----------------------------
DROP TABLE IF EXISTS `cmd_file`;
CREATE TABLE `cmd_file` (
  `cmd_id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `cmd_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '命令集名称',
  `cmd` varchar(255) DEFAULT NULL COMMENT '命令内容',
  PRIMARY KEY (`cmd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of cmd_file
-- ----------------------------
INSERT INTO `cmd_file` VALUES ('1', '日期', 'date\r\nhostname\r\nuname\r\nls\r\nhostname\r\nuname');

-- ----------------------------
-- Table structure for machine_check_user
-- ----------------------------
DROP TABLE IF EXISTS `machine_check_user`;
CREATE TABLE `machine_check_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `cmd_id` int DEFAULT NULL COMMENT '命令集合id',
  `comment` varchar(255) DEFAULT NULL COMMENT '备注',
  `machine_id` int NOT NULL COMMENT '主机id',
  PRIMARY KEY (`id`),
  KEY `machine_check_user_FK` (`machine_id`),
  CONSTRAINT `machine_check_user_FK` FOREIGN KEY (`machine_id`) REFERENCES `machine_infos` (`machine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='设备巡检用户信息';

-- ----------------------------
-- Records of machine_check_user
-- ----------------------------

-- ----------------------------
-- Table structure for machine_infos
-- ----------------------------
DROP TABLE IF EXISTS `machine_infos`;
CREATE TABLE `machine_infos` (
  `machine_id` int NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `machine_name` char(255) DEFAULT NULL COMMENT '设备名称',
  `machine_sort_name` char(255) DEFAULT NULL COMMENT '分类名称',
  `machine_sn` char(255) DEFAULT NULL COMMENT '序列号',
  `machine_factory` char(255) DEFAULT NULL COMMENT '设备厂商',
  `model` char(255) DEFAULT NULL COMMENT '型号',
  `machine_roomid` int unsigned DEFAULT NULL COMMENT '机房ID',
  `cabinet_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '机柜编号',
  `start_position` int DEFAULT NULL COMMENT '开始U位',
  `end_position` int DEFAULT NULL COMMENT '结束U位',
  `factory_date` date DEFAULT '2000-01-01' COMMENT '出产日期',
  `end_ma_date` date DEFAULT '2000-01-01' COMMENT '到保日期',
  `work_are` char(255) DEFAULT NULL COMMENT '业务类型：1生产，2电渠，3灾备，4开发',
  `run_state` int DEFAULT '1' COMMENT '运行状态:1运行，2下线，3关机，4下架，5未加电',
  `machine_admin` char(255) DEFAULT NULL COMMENT '管理员',
  `app_admin` char(255) DEFAULT NULL COMMENT '应用管理员',
  `mg_ip` char(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '管理IP地址',
  `app_ip1` char(255) DEFAULT NULL COMMENT '业务IP1',
  `bmc_ip` char(255) DEFAULT NULL COMMENT 'bmc IP',
  `install_date` date DEFAULT NULL COMMENT '上架安装时间',
  `uninstall_date` date DEFAULT NULL COMMENT '下架时间',
  `single_power` int DEFAULT '0' COMMENT '是否单电源：0：否，1：是',
  `comments` char(255) DEFAULT NULL COMMENT '备注',
  `asset_id` varchar(100) DEFAULT NULL COMMENT '资产编号',
  PRIMARY KEY (`machine_id`),
  KEY `room_id` (`machine_roomid`),
  KEY `sort_name` (`machine_sort_name`),
  KEY `s_position` (`start_position`),
  KEY `e_position` (`end_position`),
  KEY `fr_cabinet_name` (`cabinet_name`),
  CONSTRAINT `e_position` FOREIGN KEY (`end_position`) REFERENCES `cab_position` (`num`),
  CONSTRAINT `machine_infos_ibfk_1` FOREIGN KEY (`machine_sort_name`) REFERENCES `machine_sort` (`sort_name`) ON UPDATE CASCADE,
  CONSTRAINT `room_id` FOREIGN KEY (`machine_roomid`) REFERENCES `machine_room` (`room_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `s_position` FOREIGN KEY (`start_position`) REFERENCES `cab_position` (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=1629 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of machine_infos
-- ----------------------------
INSERT INTO `machine_infos` VALUES ('1000', 'A类第三方入侵防御系统1', '安全设备', '02050297D193000001', '迪普', 'IPS2000-GS', '2', 'B01', '38', '38', '2019-05-01', null, null, '4', '肖申波', null, '172.251.0.94', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1001', 'A类第三方入侵防御系统2', '安全设备', '02050297D193000004', '迪普', 'IPS2000-GS', '2', 'B02', '38', '38', '2019-05-01', null, null, '4', '肖申波', null, '172.251.0.95', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1002', 'C类第三方入侵检测系统1', '安全设备', '19-11-L-0218', '绿盟', 'NIDS NX3 N1600A', '2', 'B01', '26', '27', '2019-05-01', null, null, '4', '肖申波', null, '172.251.0.75', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1003', 'D类第三方入侵检测系统1', '安全设备', '19-11-L-0217', '绿盟', 'NIPS NX3 N1600A', '2', 'B02', '17', '18', '2019-05-01', null, null, '4', '肖申波', null, '172.251.0.64', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1004', '骨干交换区入侵检测系统1', '安全设备', '19-11-J-0214', '绿盟', 'NIDS NX3 N2010A', '2', 'A05', '13', '14', '2019-05-01', null, null, '4', '肖申波', null, '172.251.0.3', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1005', '生产外联前置入侵检测系统1', '安全设备', '19-11-J-0213', '绿盟', 'NIDS NX3 N2010A', '2', 'B01', '19', '20', '2019-05-01', null, null, '4', '肖申波', null, '172.251.0.44', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1006', '业务接入交换机（全光）', '交换机', '210235A1TXH18C000291', 'H3C', 'S6800', '1', 'B01', '8', '8', '2019-05-01', null, null, '4', '肖申波', null, '172.251.2.3', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1007', '业务接入交换机（全光）', '交换机', '210235A1TXH18C000166', 'H3C', 'S6800', '1', 'B02', '8', '8', '2019-05-01', null, null, '4', '肖申波', null, '172.251.2.3', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1008', '业务接入交换机（全光）', '交换机', '210235A1TXH18C000208', 'H3C', 'S6800', '2', 'C01', '12', '12', '2019-05-01', null, null, '4', '肖申波', null, '172.251.2.1', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1009', '业务接入交换机（全光）', '交换机', '210235A1TXH18C000110', 'H3C', 'S6800', '2', 'C01', '10', '10', '2019-05-01', null, null, '4', '肖申波', null, '172.251.2.1', null, null, null, '2022-08-15', null, null, null);
INSERT INTO `machine_infos` VALUES ('1343', '显示套件', '其它设备', '107830R', 'IBM', '显示套件', '1', 'A01', '17', '17', null, null, null, '1', '胡运秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1344', 'OA X86虚拟化 ESX6', 'X86服务器', '06L2028', 'IBM', 'X3850 X5', '1', 'A05', '5', '8', '2012-07-30', null, '1', '1', '晏良/张杭', null, '192.168.230.61', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1345', 'X86虚拟化 ESX5', 'X86服务器', '06L2033', 'IBM', 'X3850 X5', '1', 'A05', '9', '12', '2012-07-31', null, '1', '1', '张杭/晏良', null, '192.168.230.34', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1346', '图形前端服务器（双活）1', 'X86服务器', '2102310YPY10J4000697', '华为', 'H22M-03 RH2288 V3', '1', 'A05', '26', '27', '2018-07-13', null, '1', '1', '晏良', null, '6.4.1.71', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1347', '图形前端服务器（双活）2', 'X86服务器', '2102310YPY10J4000692', '华为', 'H22M-03 RH2288 V3', '1', 'A05', '29', '30', '2018-07-13', null, '1', '1', '晏良', null, '6.4.1.72', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1348', '生产X86虚拟化 ESX2', 'X86服务器', '06L2031', 'IBM', 'X3850 X5', '1', 'A06', '5', '8', '2012-07-30', null, '1', '1', '张杭/晏良', null, '192.168.230.32', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1349', '生产X86虚拟化 ESX9', 'X86服务器', '06BF158', 'IBM', 'X3850 X6', '1', 'A06', '10', '13', '2014-04-30', null, '1', '1', '张杭/晏良', null, '192.168.230.30', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1350', '生产X86虚拟化 ESX7', 'X86服务器', '06BF161', 'IBM', 'X3850 X6', '1', 'A06', '15', '18', '2014-05-08', null, '1', '1', '张杭/晏良', null, '192.168.230.28', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1351', 'OA X86虚拟化 ESX4', 'X86服务器', '06H8995', 'IBM', 'X3850 X5', '1', 'A06', '20', '23', '2012-08-25', null, '1', '1', '晏良/张杭', null, '192.168.230.62', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1352', '灾备X86虚拟化 ESXi2', 'X86服务器', '06H8996', 'IBM', 'X3850 X5', '1', 'A07', '4', '7', '2012-06-24', null, '3', '1', '张杭/晏良', null, '6.104.0.3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1353', '灾备X86虚拟化 ESXi1', 'X86服务器', '06L2032', 'IBM', 'X3850 X5', '1', 'A07', '8', '11', '2012-07-30', null, '3', '1', '张杭/晏良', null, '6.104.0.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1354', '灾备X86虚拟化 esxi3', 'X86服务器', '816451316', '浪潮', 'NF8460 M4', '1', 'A07', '13', '16', '2016-08-17', '2019-09-30', '3', '1', '张杭/晏良', null, '6.104.0.4', null, '192.168.1.102', null, null, null, '同城虚拟化', null);
INSERT INTO `machine_infos` VALUES ('1355', '灾备X86虚拟化 esxi4', 'X86服务器', '816451313', '浪潮', 'NF8460 M4', '1', 'A07', '19', '22', '2016-08-17', '2019-09-30', '3', '1', '张杭/晏良', '张杭', '6.104.0.5', null, '192.168.1.105', null, null, null, '同城灾备虚拟化', null);
INSERT INTO `machine_infos` VALUES ('1356', 'VMAX 存储-扩展柜', '磁盘阵列', 'CN498700317', 'EMC', 'VMAX 10K', '1', 'A08', '1', '42', '2014-01-01', null, '3', '1', '周中秋', null, '192.168.210.207', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1357', 'VMAX 存储-机头', '磁盘阵列', 'CN498700317', 'EMC', 'VMAX 10K', '1', 'A09', '1', '42', '2014-01-01', null, '3', '1', '周中秋', null, '192.168.210.207', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1358', '灾备国密新平台交易', '加密机', 'SJJ121416037', '江南信息', 'SJJ1214G', '1', 'A10', '5', '6', '2016-01-01', null, '3', '1', '王德明', null, '6.76.1.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1359', '灾备国密新平台交易', '加密机', 'SJJ121416075', '江南信息', 'SJJ1214G', '1', 'A10', '8', '9', '2016-01-01', null, '3', '1', '王德明', null, '6.76.1.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1360', '灾备国密新平台交易', '加密机', 'SJJ121416081', '江南信息', 'SJJ1214G', '1', 'A10', '11', '12', '2016-01-01', null, '3', '1', '王德明', null, '6.76.1.3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1361', '灾备国密发卡', '加密机', 'SJJ121416078', '江南信息', 'SJJ1214G', '1', 'A10', '14', '15', '2016-01-01', null, '3', '1', '王德明', null, '6.76.1.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1362', '灾备国密旧平台交易', '加密机', 'SHJ090212242', '江南信息', 'SHJ0902', '1', 'A10', '17', '18', '2012-01-01', null, '3', '1', '王德明', null, '6.76.1.5', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1363', '灾备国密旧平台交易', '加密机', 'SHJ090211258', '江南信息', 'SHJ0902', '1', 'A10', '20', '21', '2011-01-01', null, '3', '1', '王德明', null, '6.76.1.6', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1364', '灾备孤岛接入交换机', '交换机', '210231A1GCH161000039', 'H3C', 'S5560', '1', 'B01', '4', '4', '2016-01-01', null, '3', '1', '肖申波', null, '172.251.2.7', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1365', '业务接入交换机（电口）', '交换机', '210235A2C4H184000665', 'H3C', 'S6800', '1', 'B01', '6', '6', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1366', '开发测试区接入交换机', '交换机', '210235A0YQC159000230', 'H3C', 'S5120S', '1', 'B01', '12', '12', '2015-12-29', null, '4', '1', '肖申波', null, '6.96.239.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1367', '运管区接入交换机', '交换机', '210235A0YQC159000311', 'H3C', 'S5120S', '1', 'B01', '14', '14', '2015-12-29', null, '1', '1', '肖申波', null, '6.105.239.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1368', '灾备孤岛接入交换机', '交换机', '210231A1GCH161000040', 'H3C', 'S5560', '1', 'B02', '4', '4', '2015-01-01', null, '3', '1', '肖申波', null, '172.251.2.7', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1369', '业务接入交换机（电口）', '交换机', '210235A2C4H184001241', 'H3C', 'S6800', '1', 'B02', '6', '6', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1370', '开发测试区接入交换机', '交换机', '210235A0YQC159000274', 'H3C', 'S5120S', '1', 'B02', '12', '12', '2015-12-29', null, '4', '1', '肖申波', null, '6.96.239.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1371', '运管区接入交换机', '交换机', '210235A0YQC159000240', 'H3C', 'S5120S', '1', 'B02', '14', '14', '2015-12-29', null, '1', '1', '肖申波', null, '6.105.239.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1372', '灾备oracle RAC', 'X86服务器', '7241280987/3BR9S63', 'DELL', 'PowerEdgeR740', '1', 'B03', '4', '5', '2020-09-07', '2025-09-08', '3', '1', '晏良/王德明', null, '6.104.5.33', null, '192.168.0.13', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1373', '灾备oracle RAC', 'X86服务器', '7239881307/3BQFS63', 'DELL', 'PowerEdgeR740', '1', 'B03', '7', '8', '2020-09-07', '2025-09-08', '3', '1', '晏良/王德明', null, '6.104.5.34', null, '192.168.0.12', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1374', '灾备oracle RAC', 'X86服务器', '7241374299/3BRBS63', 'DELL', 'PowerEdgeR740', '1', 'B03', '10', '11', '2020-09-07', '2025-09-08', '3', '1', '晏良/王德明', null, '6.104.5.35', null, '192.168.0.11', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1375', '灾备oracle RAC', 'X86服务器', '7239694683/3BQBS63', 'DELL', 'PowerEdgeR740', '1', 'B03', '13', '14', '2020-09-07', '2025-09-08', '3', '1', '晏良/王德明', null, '6.104.5.36', null, '192.168.0.10', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1376', '灾备oracle RAC', 'X86服务器', '26698098207/C9JCWF3', 'DELL', 'PowerEdge R940xa', '1', 'B03', '18', '21', '2021-07-06', '2026-10-08', '3', '1', '晏良/王德明', null, null, null, '192.168.0.120', null, null, null, '', null);
INSERT INTO `machine_infos` VALUES ('1377', '灾备oracle RAC', 'X86服务器', '20167751199/99JCWF3', 'DELL', 'PowerEdge R940xa', '1', 'B03', '26', '29', '2021-07-06', '2026-10-08', '3', '1', '晏良/王德明', null, null, null, '192.168.0.120', null, null, null, '', null);
INSERT INTO `machine_infos` VALUES ('1378', '灾备CIF-RAC', '小型机', '10-78A4F', 'IBM', 'P570', '1', 'B04', '4', '19', '2011-12-06', null, '3', '1', '王德明', null, '6.104.5.17', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1379', '灾备图形前端&中间RAC', '小型机', '2130F8V', 'IBM', 'POWER 750', '1', 'B04', '23', '31', '2016-09-28', null, '3', '1', '王德明', null, '6.104.5.22', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1380', '磁带机', '磁带机', '94-02350', 'IBM', '7226-1U3', '1', 'B04', '32', '32', null, null, '3', '1', '周中秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1381', '灾备HMC控制台', 'X86服务器', '21D8CDC', 'IBM', 'X3550', '1', 'B04', '34', '34', '2014-06-30', null, '3', '1', '周中秋', null, '6.104.5.9', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1382', '磁带机', '磁带机', 'YL1520012488', 'IBM', '7214-1U2', '1', 'B04', '36', '36', null, null, '3', '1', '周中秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1383', '灾备CIF-RAC', '小型机', '10-E71D4', 'IBM', 'P570', '1', 'B05', '4', '19', '2011-12-06', null, '3', '1', '王德明', null, '6.104.5.16', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1384', '灾备图形前端&中间RAC', '小型机', '2130F7V', 'IBM', 'POWER 750', '1', 'B05', '23', '31', '2016-09-28', null, '3', '1', '王德明', null, '6.104.5.21', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1385', '磁带机', '磁带机', '94-02311', 'IBM', '7226-1U3', '1', 'B05', '32', '32', null, null, '3', '1', '周中秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1386', '磁带机', '磁带机', 'YL1520012021', 'IBM', '7214-1U2', '1', 'B05', '34', '34', null, null, '3', '1', '周中秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1387', '灾备核心生产主机（20）', '小型机', '06E9835', 'IBM', 'p570', '1', 'B06', '4', '19', '2011-12-06', null, '3', '1', '周中秋', '周中秋', '6.104.5.20', '192.168.1.20', null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1388', '磁带机', '磁带机', '23A3000', 'IBM', '7214-1U2', '1', 'B06', '20', '20', null, null, '3', '1', '周中秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1389', '灾备信贷内管RAC2', '小型机', '06-BD8F6', 'IBM', 'P550', '1', 'B06', '23', '26', '2011-07-25', null, '3', '1', '周中秋', null, '6.104.5.30', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1390', '灾备综合前置（25）', '小型机', '06E9845', 'IBM', 'p570', '1', 'B07', '4', '19', '2011-12-06', null, '3', '4', '周中秋', '周中秋', '6.104.5.25', '192.168.1.25', null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1391', '磁带机', '磁带机', '23A3016', 'IBM', '7214-1U2', '1', 'B07', '20', '20', null, null, '3', '4', '周中秋', null, null, null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1392', '灾备电子渠道rac', '小型机', '845D07V', 'IBM', 'POWER 750', '1', 'B07', '23', '31', '2015-05-18', null, '3', '1', '王德明', null, '6.104.5.26', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1393', '磁带机', '磁带机', '94-03554', 'IBM', '7226-1U3', '1', 'B07', '32', '32', null, null, '3', '1', '周中秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1394', '灾备创新平台', '小型机', '06-8F4A6', 'IBM', 'P550', '1', 'B07', '34', '37', '2011-07-25', null, '3', '4', '周中秋', null, '6.104.5.236', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1395', '容灾管理平台', 'X86服务器', '817220053', '浪潮', 'NF5270M4', '1', 'B08', '5', '6', '2017-03-04', '2020-04-30', '3', '1', '周中秋', null, '6.104.5.53', null, '192.168.1.101', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1396', '灾备核心测试用', '小型机', '06-8F4B6', 'IBM', 'P550', '1', 'B08', '8', '11', '2011-07-25', null, '3', '1', '周中秋', null, '6.104.5.221', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1397', '灾备核心备份机', '小型机', '06-BD8E6', 'IBM', 'P550', '1', 'B08', '13', '16', '2011-07-25', null, '3', '1', '周中秋', null, '6.104.5.23', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1398', '灾备电子渠道rac', '小型机', '845D0AV', 'IBM', 'POWER 750', '1', 'B08', '18', '26', '2015-11-30', null, '3', '1', '王德明', null, '6.104.5.27', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1399', '磁带机', '磁带机', '94-03488', 'IBM', '磁带机', '1', 'B08', '28', '28', null, null, '3', '1', '周中秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1400', '灾备创新平台', '小型机', '06-8F476', 'IBM', 'P550', '1', 'B08', '29', '32', '2011-12-06', null, '3', '4', '周中秋', null, '6.104.5.237', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1401', '灾备信贷内管RAC1', '小型机', '06-BD976', 'IBM', 'P550', '1', 'B08', '34', '37', '2011-12-06', null, '3', '1', '周中秋', null, '6.104.5.31', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1402', '外联区防火墙B', '防火墙', '02050055D193000013', '迪普', 'FW1000', '1', 'C01', '12', '12', '2014-04-28', null, '2', '1', '吴君华', null, '192.168.210.106', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1403', '外联区防火墙A', '防火墙', '02050056D138000432', '迪普', 'FW1000', '1', 'C01', '13', '13', '2014-04-28', null, '2', '1', '吴君华', null, '192.168.210.105', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1404', '开发外网', '安全设备', 'K1011042766', '天融信', 'NGFW4000', '1', 'C01', '19', '19', null, null, '4', '5', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1405', '人民银行开发测试VPN', '路由器', 'FGL155312Q5', 'CISCO', 'cisco2800', '1', 'C01', '21', '21', '2013-10-01', null, '4', '1', '吴君华', null, '192.168.120.12', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1406', '移动外联区防DOS设备B', '安全设备', '13-49-P-034', '绿盟', 'ADS 1200', '1', 'C01', '23', '24', '2013-10-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1407', '联通外联区防DOS设备B', '安全设备', '13-36-P-013', '绿盟', 'ADS 1200', '1', 'C01', '26', '27', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.101', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1408', '电信外联区防DOS设备A', '安全设备', '13-36-P-014', '绿盟', 'ADS 1200', '1', 'C01', '28', '29', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.100', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1409', '外联区链路负载B', '负载均衡', '31501189', 'Radware', 'LP2008', '1', 'C01', '31', '31', '2021-10-13', null, '2', '1', '吴君华', null, '192.168.210.102', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1410', '外联区链路负载A', '负载均衡', '31502181', 'Radware', 'LP2008', '1', 'C01', '32', '32', '2021-10-13', null, '2', '1', '吴君华', null, '192.168.210.103', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1411', '外联区交换机B', '交换机', '210235235610D6000288', '华为', 'S5700', '1', 'C01', '33', '33', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.104', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1412', '外联区交换机A', '交换机', '210235235610D6000272', '华为', 'S5700', '1', 'C01', '34', '34', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.104', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1413', '网银汇聚交换机B', '交换机', '210235317010D9000123', '华为', 'S5710', '1', 'C01', '35', '35', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.130', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1414', '网银汇聚交换机A', '交换机', '210235317010D9000122', '华为', 'S5710', '1', 'C01', '36', '36', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.130', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1415', '生产应用区RA服务器B', 'X86服务器', '06dppx4', 'IBM', 'X3650 M3', '1', 'C02', '7', '8', '2013-10-01', null, '2', '1', '晏良', null, '192.168.101.112', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1416', '生产应用区RA服务器A', 'X86服务器', '06DPPX2', 'IBM', 'X3650 M3', '1', 'C02', '10', '11', '2013-10-01', null, '2', '1', '晏良', null, '192.168.101.111', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1417', 'DMZ区WEB服务器B', 'X86服务器', '99V2590', 'IBM', 'X3650 M3', '1', 'C02', '13', '14', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.102.102', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1418', 'DMZ区WEB服务器A', 'X86服务器', '06BFKA6', 'IBM', 'X3650 M3', '1', 'C02', '16', '17', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.102.101', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1419', 'DMZ区入侵检测', '安全设备', '02050038d138000910', '迪普', 'IPS2000-ME', '1', 'C02', '19', '19', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.115', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1420', 'DMZ区WEB防火墙B', '防火墙', '02050648D209000001', '迪普', 'WAF 3000-TS', '1', 'C02', '21', '21', '2021-12-13', null, '2', '1', '吴君华', null, '131.10.6.58', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1421', 'DMZ区WEB防火墙A', '防火墙', '02051400D21C000003', '迪普', 'WAF 3000-TS', '1', 'C02', '23', '23', '2021-12-13', null, '2', '1', '吴君华', null, '131.10.6.57', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1422', '生产应用区签名服务器B', '安全设备', '1331G4099', '信安世纪', 'Netsign 3300', '1', 'C02', '25', '25', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.123', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1423', '生产应用区签名服务器A', '安全设备', '1331G4100', '信安世纪', 'Netsign 3300', '1', 'C02', '26', '26', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.122', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1424', 'DMZ区入侵防御B', '安全设备', '02050040d139000176', '迪普', 'IPS2000-GS', '1', 'C02', '28', '28', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.120', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1425', 'DMZ区入侵防御A', '安全设备', '02050040d139000175', '迪普', 'IPS2000-GS', '1', 'C02', '29', '29', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.119', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1426', '(DMZ区SSL网关B)主', '安全设备', 'I15060180', '信安世纪', 'NSAE 1500', '1', 'C02', '33', '33', '2013-10-01', null, '2', '1', '吴君华', null, '131.10.6.11', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1427', '(DMZ区SSL网关A)备', '安全设备', '1320G3689', '信安世纪', 'NSAE 1500', '1', 'C02', '34', '34', '2013-10-01', null, '2', '1', '吴君华', null, '131.10.6.11', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1428', 'DMZ区二层交换机B', '交换机', '210235235610D9000266', '华为', 'S5700', '1', 'C02', '35', '35', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.116', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1429', 'DMZ区二层交换机A', '交换机', '210235235610D6000063', '华为', 'S5700', '1', 'C02', '36', '36', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.116', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1430', 'DMZ区三层交换机B', '交换机', '210235235610DB000360', '华为', 'S5700', '1', 'C02', '37', '37', '2013-10-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1431', 'DMZ区三层交换机A', '交换机', '210235235610D9000283', '华为', 'S5700', '1', 'C02', '38', '38', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.112', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1432', '网银生产应用区虚拟化服务C', 'X86服务器', '06BF153', 'IBM', 'X3850 X6', '1', 'C03', '2', '5', '2013-10-01', null, '2', '1', '张杭/晏良', null, '192.168.230.69', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1433', '网银生产应用区虚拟化服务B', 'X86服务器', '06BF156', 'IBM', 'X3850 X6', '1', 'C03', '7', '10', '2013-10-01', null, '2', '1', '张杭/晏良', null, '192.168.230.68', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1434', '网银生产应用区虚拟化服务A', 'X86服务器', 'J33TLGB', 'IBM', 'X3850 X6', '1', 'C03', '12', '15', '2018-03-02', null, '2', '1', '张杭/晏良', null, '192.168.230.67', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1435', 'DP FW1000-SG-NC防火墙(未加电)', '防火墙', '02050022D136001052', '迪普', 'FW1000-SG-NC', '1', 'C03', '19', '19', '2013-10-01', null, '2', '5', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1436', 'netpass1000', '安全设备', 'I21681411', '信安世纪', 'Netpass1000', '1', 'C03', '22', '23', '2013-10-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1437', '生产应用区动态令牌服务器A', '安全设备', '840001-1311001', '信安世纪', 'Netpass', '1', 'C03', '24', '25', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.139', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1438', '生产应用区入侵检测', '防火墙', '02050038d138000911', '迪普', 'IPS2000-ME', '1', 'C03', '27', '27', '2014-04-28', null, '2', '1', '吴君华', null, '192.168.210.136', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1439', '生产应用区防火墙A', '防火墙', 'Q1407234736', '天融信', 'NGFW4000', '1', 'C03', '29', '29', '2014-04-28', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1440', '生产应用区防火墙B', '防火墙', 'Q1407234735', '天融信', 'NGFW4000', '1', 'C03', '30', '30', '2014-04-28', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1441', '生产应用区防火墙B', '防火墙', '1504946120009344', '山石', 'SG-6000-M6110', '1', 'C03', '33', '33', '2014-04-28', null, '2', '1', '吴君华', null, '192.168.210.134', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1442', '生产应用区防火墙A', '防火墙', '1504922130015033', '山石', 'SG-6000-M6110', '1', 'C03', '34', '34', '2014-04-28', null, '2', '1', '吴君华', null, '192.168.210.133', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1443', '生产应用区交换机B', '交换机', '210235234110D9000284', '华为', 'S5700', '1', 'C03', '35', '35', '2013-10-01', null, '2', '1', '吴君华', null, '131.10.6.34', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1444', '生产应用区交换机A', '交换机', '210235234110D9000338', '华为', 'S5700', '1', 'C03', '36', '36', '2013-10-01', null, '2', '1', '吴君华', null, '131.10.6.34', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1445', '接入交换机（机柜背面）', '交换机', 'FOC1612W1NX', 'CISCO', 'SW-C2960S', '1', 'C03', '38', '38', '2013-10-01', null, '2', '1', '吴君华', null, '192.168.210.3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1446', 'DMZ区WEB虚拟化服务器C', 'X86服务器', '06BF151', 'IBM', 'X3850 X6', '1', 'C04', '4', '7', '2013-10-01', null, '2', '1', '张杭/晏良', null, '192.168.230.72', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1447', 'DMZ区WEB虚拟化服务器B', 'X86服务器', '06BF159', 'IBM', 'X3850 X6', '1', 'C04', '9', '12', '2013-10-01', null, '2', '1', '张杭/晏良', null, '192.168.230.71', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1448', 'DMZ区WEB虚拟化服务器A', 'X86服务器', '06BF154', 'IBM', 'X3850 X6', '1', 'C04', '14', '17', '2013-10-01', null, '2', '1', '张杭/晏良', null, '192.168.230.70', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1449', '深信服-备', '安全设备', '5074000661', '深信服', 'VPN-H6300', '1', 'C04', '25', '26', '2016-01-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1450', '深信服-主-第三方外联', '安全设备', '5074000657', '深信服', 'VPN-H6300', '1', 'C04', '27', '28', '2016-01-01', null, '2', '1', '吴君华', null, '131.10.6.82', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1451', '深信服-备', '安全设备', '5074000570', '深信服', 'VPN-H6300', '1', 'C04', '30', '31', '2016-01-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1452', '深信服-办公', '安全设备', '5074000558', '深信服', 'VPN-H6300', '1', 'C04', '32', '33', '2016-01-01', null, '2', '1', '吴君华', null, '192.168.110.62/10.62', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1453', 'DMZ区负载均衡B', '负载均衡', 'f5-pdru-ycti', 'f5', 'BIG-IP2000series', '1', 'C04', '35', '35', '2022-01-20', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1454', 'DMZ区负载均衡A', '负载均衡', 'f5-zgpe-uqzf', 'f5', 'BIG-IP2000series', '1', 'C04', '36', '36', '2022-01-20', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1455', '生产应用区负载均衡B', '负载均衡', 'f5-hliq-wkut', 'f5', 'BIG-IP2000series', '1', 'C04', '38', '38', '2022-01-20', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1456', '生产应用区负载均衡A', '负载均衡', 'f5-rrno-epqo', 'f5', 'BIG-IP2000series', '1', 'C04', '39', '39', '2022-01-20', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1457', '网联接入交换机B', '交换机', '2102310JFA6TJC931911', '华为', 'S5720', '1', 'C05', '18', '18', '2013-10-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1458', '网联接入交换机A', '交换机', '2102310JFA6TJC931927', '华为', 'S5720', '1', 'C05', '19', '19', '2013-10-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1459', '绿盟IPS B', '防火墙', '1550J0748', '绿盟', 'NIPS NX3 SERIES', '1', 'C05', '25', '26', '2013-10-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1460', '绿盟IPS A', '防火墙', '1550J0749', '绿盟', 'NIPS NX3 SERIES', '1', 'C05', '27', '28', '2013-10-01', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1461', '天融信防火墙B', '防火墙', 'Q1411280849', '天融信', 'NGFW4000-UF(TG-51130)', '1', 'C05', '30', '31', '2016-03-18', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1462', '天融信防火墙A', '防火墙', 'Q1411280848', '天融信', 'NGFW4000-UF(TG-51130)', '1', 'C05', '32', '33', '2016-03-18', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1463', '山石网科防火墙B', '防火墙', '1107548140000637', '山石', 'sg-6000 M6860', '1', 'C05', '35', '36', '2016-03-18', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1464', '山石网科防火墙A', '防火墙', '1107548140001032', '山石', 'sg-6000 M6860', '1', 'C05', '37', '38', '2016-03-18', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1465', 'X86虚拟化（电渠区应用监控）', 'X86服务器', '210235A2CRH19A000267', 'H3C', 'R4900 G3', '1', 'C06', '4', '5', '2019-10-15', '2025-01-14', '2', '1', '张杭/晏良', null, '6.104.1.11', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1466', 'X86虚拟化（电渠区应用监控）', 'X86服务器', '210235A2CRH19A000280', 'H3C', 'R4900 G3', '1', 'C06', '7', '8', '2019-10-15', '2025-01-14', '2', '1', '张杭/晏良', null, '6.104.1.12', null, '192.168.1.21', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1467', 'X86虚拟化（电渠区应用监控）', 'X86服务器', '210235A2CRH19A000277', 'H3C', 'R4900 G3', '1', 'C06', '10', '11', '2019-10-15', '2025-01-14', '2', '1', '张杭/晏良', null, '6.104.1.13', null, '192.168.1.11', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1468', '暂未使用', 'X86服务器', '210235A2CT619BF00007', 'H3C', 'R4900 G3', '1', 'C06', '13', '14', '2019-11-13', null, null, '5', '晏良', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1469', '暂未使用', 'X86服务器', '210235A2CT619BF00006', 'H3C', 'R4900 G3', '1', 'C06', '18', '19', '2019-11-13', null, null, '5', '晏良', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1470', '双活PMTS 湘潭1', 'X86服务器', '201200A00QH189000999', 'H3C', 'R4900 G3', '1', 'C07', '26', '27', '2019-05-01', '2024-01-01', '1', '1', '李慧敏', null, '6.104.6.26', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1471', '服务器采集设备', '其它网络设备', '19011802FFF4020A', '智卓', 'SmartNCSP ZZ-CL42T8', '1', 'C08', '18', '20', '2019-01-01', null, '1', '1', '肖申波', null, '6.104.4.64\n外6.104.4.66/67', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1472', '智能网络综合服务平台（前置、图形前端）', '其它网络设备', '18C11802FFF2020A', '智卓', 'SmartNCSP ZZ-CL42T8', '1', 'C08', '26', '28', '2018-01-01', null, '1', '1', '肖申波', null, '6.104.4.49/65/68/69', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1473', '双活PMTS 湘潭2', 'X86服务器', '201200A00QH189000998', 'H3C', 'R4900 G3', '1', 'C09', '26', '27', '2019-05-01', '2024-01-01', '1', '1', '李慧敏', null, '6.104.6.27', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1474', '业务接入交换机（电口）', '交换机', '210235A2C4H184000588', 'H3C', 'S6800', '1', 'D01', '6', '6', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.6', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1475', '业务接入交换机（全光）', '交换机', '210235A1TXH18C000267', 'H3C', 'S6800', '1', 'D01', '8', '8', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.5', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1476', '电渠应用区接入交换机1', '交换机', '210235A0YQC159000261', 'H3C', 'S5120S', '1', 'D01', '10', '10', '2015-12-29', null, '2', '1', '吴君华', null, '192.168.10.12', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1477', '开发测试区接入交换机', '交换机', '210235A0YQC159000236', 'H3C', 'S5120S', '1', 'D01', '12', '12', '2015-12-29', null, '4', '1', '肖申波', null, '6.96.239.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1478', '运管区接入交换机', '交换机', '210235908110EC000213', '华为', 'CE5810', '1', 'D01', '14', '14', '2015-05-25', null, '1', '1', '肖申波', null, '6.105.239.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1479', '业务接入交换机（电口）', '交换机', '210235A2C4H184000944', 'H3C', 'S6800', '1', 'D02', '6', '6', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.6', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1480', '业务接入交换机（全光）', '交换机', '210235A1TXH18C000252', 'H3C', 'S6800', '1', 'D02', '8', '8', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.5', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1481', '电渠应用区接入交换机2', '交换机', '210235A0YQC159000244', 'H3C', 'S5120S', '1', 'D02', '10', '10', '2015-12-29', null, '2', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1482', '运管区接入交换机', '交换机', '210235908110EC000215', '华为', 'CE5810', '1', 'D02', '14', '14', '2015-05-25', null, '1', '1', '肖申波', null, '6.105.239.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1483', 'TAP', '交换机', '00017a925af8', 'MAIPU', 'my power t4320', '1', 'D02', '16', '16', '2019-03-15', null, '2', '1', '肖申波', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1484', 'isilon NAS节点1/2/3/4', '磁盘阵列', 'JVVXNM204800002/JVVXNM204800031/JVVXNM204800022/JVVXNM204800020', 'EMC', 'ISILON H400', '1', 'D03', '5', '8', '2021-04-20', '2026-04-20', '1', '4', '王德明', null, '6.68.1.102-108/6.64.0.123-125', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1485', 'isilon NAS节点5/6/7/8', '磁盘阵列', 'JVVXNM204800016/JVVXNM204800025/JVVXNM204800026/JVVXNM204800017', 'EMC', 'ISILON H400', '1', 'D03', '9', '12', '2021-04-20', '2026-04-20', '1', '4', '王德明', null, '6.68.1.102-108/6.64.0.123-125', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1486', 'isilon NAS交换机', '交换机', '1MZHPK2/3KZHPK2', 'EMC', 'S4112F', '1', 'D03', '21', '21', '2021-04-20', '2026-04-20', '1', '4', '王德明', null, '6.68.1.100-101', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1487', 'RPA3远程复制', '其它存储', 'CK2SY212100134', 'EMC', 'GEN 6', '1', 'D03', '37', '37', '2021-05-29', '2026-04-20', '1', '1', '周中秋', null, '6.104.4.12/192.168.99.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1488', 'RPA4远程复制', '其它存储', 'CK2SY212100132', 'EMC', 'GEN 6', '1', 'D03', '38', '38', '2021-05-29', '2026-04-20', '1', '1', '周中秋', null, '6.104.4.11/192.168.99.3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1489', 'NAS存储生产5300', '磁盘阵列', 'FCN00142900103', 'EMC', 'NAS5300', '1', 'D04', '2', '34', '2014-01-01', null, '1', '1', '王德明', null, '192.168.230.120', null, null, null, null, null, '192.168.230.120-123', null);
INSERT INTO `machine_infos` VALUES ('1490', 'RPA2远程复制', '其它存储', 'CK2SY182200125', 'EMC', 'GEN 6', '1', 'D04', '37', '37', '2017-01-01', null, '1', '1', '周中秋', null, '6.104.4.10/192.168.99.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1491', 'RPA1远程复制', '其它存储', 'CK2SY182200122', 'EMC', 'GEN 6', '1', 'D04', '38', '38', '2017-01-01', null, '1', '1', '周中秋', null, '6.104.4.9/192.168.99.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1492', 'EMC VPLEX 存储网关', '磁盘阵列', 'CKM00133803173', 'EMC', 'EMC VPLEX', '1', 'D05', '4', '28', '2014-01-01', null, '1', '1', '周中秋', null, '6.104.4.7', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1493', 'VMAX 存储', '磁盘阵列', 'CN498700149', 'EMC', 'VMAX 10K', '1', 'D06', '1', '42', '2014-01-01', null, '1', '1', '周中秋', null, '192.168.210.203', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1494', 'VMAX 存储', '磁盘阵列', 'CN498700149', 'EMC', 'VMAX 10K', '1', 'D07', '1', '42', '2014-01-01', null, '1', '1', '周中秋', null, '192.168.210.203', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1495', '光纤光纤交换机B', '安全设备', 'BRCANN1934J00E', 'brocade', 'DCX-4S-B', '1', 'D08', '2', '10', '2014-01-01', null, '1', '1', '周中秋', null, '6.104.4.1-3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1496', '光纤光纤交换机A', '存储光交', 'BRCANN1911J012', 'brocade', 'DCX-4S-B', '1', 'D08', '14', '22', '2014-01-01', null, '1', '1', '周中秋', null, '6.104.4.4-6', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1497', 'L2汇聚交换机', '交换机', '210235A1GFX18B00001P', 'H3C', 'S12504X', '2', 'A01', '6', '11', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1498', '开发测试区千兆防火墙1', '防火墙', '02050055D193000012', '迪普', 'FW1000-GC-N', '2', 'A01', '24', '24', '2019-05-01', null, '4', '1', '肖申波', null, '172.251.0.126', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1499', '开发测试区汇聚交换机1', '交换机', '210235A1TXH18C000229', 'H3C', 'S6800', '2', 'A01', '26', '26', '2019-05-01', null, '4', '1', '肖申波', null, '172.251.0.125', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1500', '业务2区汇聚交换机', '交换机', '210235A1GFX18B00000P', 'H3C', 'S12504X', '2', 'A02', '6', '11', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.15', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1501', '业务2区万兆防火墙1', '防火墙', '2809347162002549', '山石', 'sg-6000 E5560', '2', 'A02', '13', '14', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.17', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1502', '业务1区汇聚交换机', '交换机', '210235A1GFX18B00000T', 'H3C', 'S12504X', '2', 'A02', '16', '21', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.11', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1503', '业务1区万兆防火墙1', '防火墙', '2812334182004240', '山石', 'sg-6000 E5560', '2', 'A02', '23', '24', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.13', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1504', '运管区汇聚交换机1', '交换机', '210235A1TXH18C000285', 'H3C', 'S6800', '2', 'A02', '26', '26', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.254', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1505', '运管区千兆防火墙1', '防火墙', '02050218D193000002', '迪普', 'FW1000-GC-N', '2', 'A02', '37', '37', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.51', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1506', '业务2区汇聚交换机', '交换机', '210235A1GFX18B00000K', 'H3C', 'S12504X', '2', 'A03', '6', '11', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.15', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1507', '业务2区万兆防火墙2', '防火墙', '2809322162001339', '山石', 'sg-6000 E5560', '2', 'A03', '13', '14', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.17', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1508', '业务1区汇聚交换机', '交换机', '210235A1GFX18B00000F', 'H3C', 'S12504X', '2', 'A03', '16', '21', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.11', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1509', '业务1区万兆防火墙2', '防火墙', '2809347162004551', '山石', 'sg-6000 E5560', '2', 'A03', '23', '24', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.14', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1510', '骨干交换机1', '交换机', '210235A1GFX18B00000L', 'H3C', 'S12504X', '2', 'A04', '6', '11', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1511', '带外接入交换机1', '交换机', '210235A2C4H184001363', 'H3C', 'S6800', '2', 'A04', '13', '13', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.253', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1512', '管理DNS设备', 'DNS设备', '05-1708E-205', 'ZDNS', 'T7100', '2', 'A04', '14', '15', '2017-01-01', null, '1', '4', '肖申波', null, '6.127.253.5', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1513', '业务DNS设备', 'DNS设备', '05-1707E-1034', 'ZDNS', 'T5100', '2', 'A04', '16', '16', '2017-01-01', null, '1', '4', '肖申波', null, '6.127.253.8', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1514', 'DNS集群负载均衡B', '负载均衡', 'f5-mgea-mqjh', 'F5', 'BIG-IP 2000 SERIES', '2', 'A04', '26', '26', '2017-01-01', null, '1', '4', '肖申波', null, '6.127.253.7', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1515', '骨干交换机2', '交换机', '210235A1GFX18B00000M', 'H3C', 'S12504X', '2', 'A05', '6', '11', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1516', '带外接入交换机2', '交换机', '210235A0YQC159000297', 'H3C', 'S5120S', '2', 'A05', '16', '16', '2015-12-29', null, '1', '1', '肖申波', null, '172.251.0.252', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1517', 'TAP', '交换机', 'ccd81f103875', 'MAIPU', 'my power t5820', '2', 'A05', '18', '18', '2019-05-01', null, '1', '1', '肖申波', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1518', 'DNS集群负载均衡A', '负载均衡', 'f5-hjqs-lric', 'F5', 'BIG-IP 2000 SERIES', '2', 'A05', '26', '26', '2017-01-01', null, '1', '4', '肖申波', null, '6.127.253.6', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1519', 'L2汇聚交换机', '交换机', '210235A1GFX18B00001G', 'H3C', 'S12504X', '2', 'A06', '6', '11', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1520', 'VMAX 存储', '磁盘阵列', 'CN498700243', 'EMC', 'VMAX 10K', '2', 'A09', '1', '42', '2014-01-01', null, '1', '1', '周中秋', null, '192.168.210.205', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1521', 'VMAX 存储', '磁盘阵列', 'CN498700243', 'EMC', 'VMAX 10K', '2', 'A10', '1', '42', '2014-01-01', null, '1', '1', '周中秋', null, '192.168.210.205', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1522', '电信/中信波分', '其它网络设备', '2012120495N0H1000251/2012120495N0GA001558', '华为', 'OptiX OSN 8800 T32', '2', 'A11', '1', '42', '2017-05-01', null, '1', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1523', '生产外联前置DMZ万兆防火墙1', '防火墙', 'NT00277143', '启明星辰', 'USG-FW-12600', '2', 'B01', '17', '18', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.43', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1524', '生产外联前置DMZ汇聚交换机', '交换机', '2102350QAK6TJC000263', '华为', 'CE6855', '2', 'B01', '21', '21', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.41', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1525', '生产外联前置DMZ汇聚交换机', '交换机', '2102350QAKDMKB926427', '华为', 'CE6855', '2', 'B01', '22', '22', '2022-05-24', null, '1', '1', '肖申波', null, '172.251.0.41', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1526', 'C类第三方千兆防火墙1', '防火墙', 'Q1812999304', '天融信', 'TG51130', '2', 'B01', '24', '25', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.73', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1527', 'C类第三方接入交换机', '交换机', '2102359562DMJC002971', '华为', 'S5720', '2', 'B01', '28', '28', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.77', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1528', 'B类第三方千兆防火墙1', '防火墙', 'NT00277183', '启明星辰', 'USG-FW-3600EP', '2', 'B01', '30', '31', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.83', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1529', 'B类第三方入侵防御系统1', '安全设备', '0113211904089997', '启明星辰', 'NGIPS5000', '2', 'B01', '32', '33', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.85', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1530', 'B类第三方接入交换机', '交换机', '2102359562DMJC002712', '华为', 'S5720', '2', 'B01', '34', '34', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.87', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1531', 'A类第三方接入交换机', '交换机', '2102359562DMJC002995', '华为', 'S5720', '2', 'B01', '36', '36', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.57', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1532', 'A类第三方防火墙1', '防火墙', 'Q1812889045', '天融信', 'NGFW4000', '2', 'B01', '37', '37', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.93', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1533', '未接线', '防火墙', '02050055D193000017', '迪普', 'FW1000-GC-N', '2', 'B02', '5', '5', '2019-05-01', null, '1', '1', '肖申波', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1534', 'D类第三方接入交换机', '交换机', '2102359562DMJB003641', '华为', 'S5720', '2', 'B02', '16', '16', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.62', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1535', 'D类第三方千兆防火墙1', '防火墙', 'Q1812999303', '天融信', 'TG51130', '2', 'B02', '19', '20', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.63', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1536', 'D类第三方接入路由器', '路由器', '2102113374P0K1000018', '华为', 'AR3260', '2', 'B02', '22', '24', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.61', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1537', 'C类第三方接入路由器', '路由器', '2102113374P0K1000021', '华为', 'AR3260', '2', 'B02', '26', '28', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.79', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1538', 'B类第三方接入路由器', '路由器', '2102113374P0K1000020', '华为', 'AR3260', '2', 'B02', '30', '32', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.89', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1539', 'A类第三方接入路由器2', '路由器', '2102351HLE10K1000044', '华为', 'AR2200', '2', 'B02', '34', '34', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.60', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1540', 'A类第三方接入路由器1', '路由器', '2102351HLE10K1000042', '华为', 'AR2200', '2', 'B02', '35', '35', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.59', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1541', 'A类第三方接入交换机', '交换机', '2102359562DMJC002972', '华为', 'S5720', '2', 'B02', '36', '36', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.57', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1542', 'A类第三方防火墙2', '防火墙', 'Q1812889067', '天融信', 'NGFW4000', '2', 'B02', '37', '37', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.92', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1543', '环网区路由器2', '路由器', '2102355250P0EC000078', '华为', 'NE40', '2', 'B03', '4', '8', '2014-05-01', null, '1', '1', '肖申波', null, '172.251.0.28', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1544', '环网区路由器1', '路由器', '2102355250P0EC000047', '华为', 'NE40', '2', 'B03', '11', '15', '2014-05-01', null, '1', '1', '肖申波', null, '172.251.0.27', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1545', '广域网区万兆防火墙2', '防火墙', '0903342110004734', '山石', 'sg-6000 X5100', '2', 'B03', '17', '18', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.24', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1546', '广域网区万兆防火墙2', '防火墙', '2812349185003248', '山石', 'sg-6000 E5560', '2', 'B03', '19', '20', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.24', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1547', '广域网区万兆防火墙1', '防火墙', '0903330110003225', '山石', 'sg-6000 X5100', '2', 'B03', '23', '24', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.23', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1548', '广域网区万兆防火墙1', '防火墙', '2812349185001347', '山石', 'sg-6000 E5560', '2', 'B03', '25', '26', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.23', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1549', '广域网区下联分行接入路由器1', '路由器', '210235A0YVX18B00000P', 'H3C', 'SR8808-X', '2', 'B04', '4', '24', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.0.25', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1550', '广域网区汇聚交换机', '交换机', '2102113774P0EC000009', '华为', 'CE12804', '2', 'B04', '27', '37', '2014-12-01', null, '1', '1', '肖申波', null, '172.251.0.21', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1551', '广域网区下联分行接入路由器1', '路由器', '210235A0YVX18B00000X', 'H3C', 'SR8808-X', '2', 'B05', '4', '24', '2014-12-01', null, '1', '1', '肖申波', null, '172.251.0.26', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1552', '广域网区汇聚交换机', '交换机', '2102113774P0EC000004', '华为', 'CE12804', '2', 'B05', '27', '37', '2014-12-01', null, '1', '1', '肖申波', null, '172.251.0.21', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1553', '业务接入交换机（电口）', '交换机', '210235A2C4H184001147', 'H3C', 'S6800', '2', 'C01', '6', '6', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1554', '业务接入交换机（电口）', '交换机', '210235A2C4H184000581', 'H3C', 'S6800', '2', 'C01', '8', '8', '2019-05-01', null, '1', '1', '肖申波', null, '172.251.2.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1555', '运管区接入交换机', '交换机', '210235A0YQC159000309', 'H3C', 'S5120S', '2', 'C01', '14', '14', '2015-12-29', null, '1', '1', '肖申波', null, '6.105.239.3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1556', '运管区接入交换机', '交换机', '210235A0YQC159000235', 'H3C', 'S5120S', '2', 'C01', '16', '16', '2015-12-29', null, '1', '1', '肖申波', null, '6.105.239.3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1557', '新电话银行-呼叫中心SBC', 'X86服务器', '2102350FEB10J4000017', '华为', 'RH1288 V3', '2', 'C02', '9', '9', '2018-07-23', null, '1', '1', '谢小琪', null, '6.68.1.22', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1558', '新电话银行-排队机', '排队机', '2102120577N00J2000569', '华为', 'espace U1981', '2', 'C02', '11', '12', '2017-01-01', null, '1', '1', '谢小琪', null, '6.68.1.21  6.104.7.30', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1559', '老电话银行IVR192.168.110.27', 'X86服务器', '816534205', '浪潮', 'NF5270M4', '2', 'C02', '23', '24', '2016-12-26', null, '1', '1', '汪志', null, '192.168.110.27', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1560', '奇安信网神新一代安全感知系统', '安全设备', 'DF30001566', '奇安信', 'TSS10000-S56-WS', '2', 'C03', '15', '16', '2021-11-19', null, '1', '1', '王博文', null, '6.104.7.56', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1561', '生产HMC', 'X86服务器', '1085D7C', 'IBM', 'X3550', '2', 'C03', '23', '23', null, null, '1', '1', '胡运秋', null, '6.104.5.10', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1562', '生产HMC', 'X86服务器', '069696B', 'IBM', 'X3550', '2', 'C03', '24', '24', '2014-06-30', null, '1', '1', '胡运秋', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1563', '老财务系统服务器 +U key', 'X86服务器', 'CNG013S1J0', 'HP', 'DL380 G6', '2', 'C04', '18', '19', '2009-12-25', null, '1', '1', '游君子、颜麟权', null, '192.168.130.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1564', 'swift内部交换机', '交换机', '210235A0L69128N00397', 'H3C', '3600', '2', 'C04', '23', '23', null, null, '1', '1', '陈柏', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1565', 'swfit加密机', '加密机', 'B15-240', 'GEMALTO LUNAIS66', 'GEMALTO LUNAIS66', '2', 'C04', '35', '35', '2019-07-01', null, '1', '1', '陈柏', null, '192.168.0.70（内部地址）', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1566', 'SWFIT防火墙A', '防火墙', 'DS1319AF1259', 'Juniper', 'SRX345', '2', 'C04', '37', '37', '2021-05-31', null, '1', '1', '陈柏', null, '58.20.229.211', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1567', 'SWFIT防火墙B', '防火墙', 'DS1319AF0748', 'Juniper', 'SRX345', '2', 'C04', '38', '38', '2021-05-31', null, '1', '1', '陈柏', null, '220.170.8.154', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1568', '动环串口设备', '动环监控', null, '动环串口设备', '动环串口设备', '2', 'C05', '1', '1', '2019-05-01', null, '1', '1', '肖申波', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1569', 'XBROTHER INP-1430', '动环监控', null, 'XBROTHER', 'INP-1430', '2', 'C05', '4', '4', '2019-05-01', null, '1', '1', '肖申波', null, '192.168.1.140', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1570', 'XBROTHER', '动环监控', '191100120', 'XBROTHER', null, '2', 'C05', '5', '6', '2019-05-01', null, '1', '1', '肖申波', null, '192.168.1.150', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1571', '动环串口设备', '动环监控', '12381066', '康耐得', 'C2000 N380', '2', 'C05', '8', '8', '2019-05-01', null, '1', '1', '肖申波', null, '192.168.1.149', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1572', '动环监控服务器', 'X86服务器', 'CNGB43S3GJ', 'HP', 'DL380 G5', '2', 'C05', '10', '11', '2009-12-23', null, '1', '1', '肖申波', null, '192.168.1.7', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1573', '科来网络回溯分析系统', '其它网络设备', 'PHCS2306SX201905300004', '科来', 'CS2306SX-HR', '2', 'C05', '25', '26', '2019-05-01', null, '1', '1', '肖申波', null, '6.104.7.31', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1574', '基础数据平台ETL', '小型机', '06EADE5', 'IBM', '520', '2', 'C06', '5', '8', '2011-12-06', null, '1', '1', '兰明辉', null, '192.168.1.178', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1575', '基础数据平台存储', '磁盘阵列', '78K0RNB', 'IBM', '5020', '2', 'C06', '10', '12', null, null, '1', '1', '兰明辉', null, '192.168.128.101/102', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1576', '视频会议MCU', '其它网络设备', '2102120143P0B600031', '华为', 'ViewPoint 8650', '2', 'C06', '14', '18', '2015-01-01', null, '1', '1', '张伟', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1577', '办公网交换机', '交换机', '210235A0YQC159000237', 'H3C', 'S5120S', '3', 'A06', '6', '6', '2015-01-01', null, '1', '1', '肖申波', null, '10.8.8.251', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1578', '链路负载', '负载均衡', '31403128', 'Radware', 'ALTEON5224', '4', 'KF03', '10', '11', null, null, '4', '1', '吴君华', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1579', 'ODS服务器绩效考核', 'X86服务器', '99V5373', 'IBM', 'X3650 M3', '4', 'KF03', '25', '26', '2011-10-23', null, '4', '1', '兰明辉', null, '192.168.120.45', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1580', '吉大正元数字签名', '加密机', 'LZ15100939', '吉大正元', null, '4', 'KF03', '34', '36', '2016-01-01', null, '4', '1', '王德明/廖松嵘', null, '192.168.19.10', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1581', '同城灾备开发接入交换机', '交换机', '210235A0YPC15B001504', 'H3C', 'S5120S-28P-EI', '4', 'KF03', '37', '37', '2015-01-01', null, '4', '1', '肖申波', null, '192.168.19.247', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1582', '同城灾备管理接入交换机', '交换机', '210235A0YPC15B001475', 'H3C', 'S5120S-28P-EI', '4', 'KF03', '39', '39', '2015-01-01', null, '4', '1', '肖申波', null, '192.168.230.249', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1583', '网银签名验签服务器', '安全设备', 'Q2014011374', '信安世纪', 'Netsign \n3300', '4', 'KF05', '39', '39', '2016-01-01', null, '4', '1', '王尽如', null, '192.168.120.203', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1584', '开发接入迪普防火墙', '防火墙', '02050022D136001047', '迪普', 'FW1000-GC-N', '4', 'KF07', '20', '20', null, null, '4', '1', '肖申波', null, '192.168.120.128', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1585', '同城灾备开发接入交换机', '交换机', 'FOC1612W4QW', 'Cisco', 'WS-C2960S-48TS-L', '4', 'KF07', '29', '29', null, null, '4', '1', '肖申波', null, '192.168.19.248', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1586', '接入交换机', '交换机', '210235A0L69128N00325', 'H3C', 'S3600V2', '4', 'KF07', '31', '31', null, null, '4', '1', '肖申波', null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1587', '开发深信服VPN', '防火墙', '5031006948', '深信服', 'VPN-H4300', '4', 'KF07', '35', '35', null, null, '4', '1', '肖申波', null, '192.168.120.127', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1588', '支付密码验证机', 'X86服务器', '06FWWRW', '联想', 'X3650M5 新机', '4', 'KF08', '20', '21', '2015-06-13', null, '4', '4', '匡扬/游争光', null, '192.168.19.4', null, null, null, '2022-09-20', null, null, null);
INSERT INTO `machine_infos` VALUES ('1589', '灾备环网路由器R1', '路由器', '210235A0W8B159000138', 'H3C', 'MSR3640', '5', 'A01', '5', '6', '2016-01-20', null, '4', '1', '肖申波', null, '6.123.253.254', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1590', '灾备汇聚交换机SW1', '交换机', '210231A73SB149000017', 'H3C', 'S7502E', '5', 'A01', '8', '11', '2016-01-20', null, '4', '1', '肖申波', null, '6.123.253.253', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1591', '灾备管理接入交换机', '交换机', '210235A0YQC159000305', 'H3C', 'S5120', '5', 'A01', '13', '13', '2016-01-20', null, '4', '1', '肖申波', null, '6.123.253.250', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1592', '流量分析', '其它网络设备', null, '深信服', 'APM-4280', '5', 'A01', '15', '15', null, null, '4', '1', '肖申波', null, '6.123.253.200', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1593', '异地新存储光交A', '存储光交', '2102353VBN10LB000004', '华为', 'OceanStor SN3664', '5', 'A01', '23', '23', '2021-02-02', '2026-02-01', '4', '1', '胡运秋', null, '6.123.253.4', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1594', '灾备防火墙FW1', '防火墙', '1107500140030830', '山石', 'SG-6000-M6860', '5', 'A02', '5', '6', '2019-03-01', null, '4', '1', '肖申波', null, '6.123.253.252', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1595', '灾备业务接入交换机', '交换机', '210235A1GCH159000026', 'H3C', 'S5560', '5', 'A02', '8', '8', '2016-01-20', null, '4', '1', '肖申波', null, '6.123.253.251', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1596', '异地新存储光交B', '存储光交', '2102353VBN10LB000003', '华为', 'OceanStor SN3664', '5', 'A02', '23', '23', '2020-11-18', '2026-02-01', '4', '1', '胡运秋', null, '6.123.253.5', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1597', '灾备CIF、自助设备-VIOS2', '小型机', '06EAF95', 'IBM', 'P550', '5', 'A03', '5', '8', '2014-06-30', null, '4', '1', '胡运秋', null, '6.123.253.17', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1598', '灾备IC卡系统数据库-VIOS1', '小型机', '068F496', 'IBM', 'P550', '5', 'A03', '10', '13', '2014-06-30', null, '4', '1', '胡运秋', null, '6.123.253.16', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1599', '灾备恢复验证主机', '小型机', '06EAE15', 'IBM', 'P520', '5', 'A04', '5', '8', '2014-06-30', null, '4', '1', '胡运秋', null, '6.123.253.2', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1600', '灾备核心系统主机', '小型机', '068F486', 'IBM', 'P550', '5', 'A04', '10', '13', '2014-06-30', null, '4', '1', '胡运秋', null, '6.123.253.25', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1601', '灾备综合前置主机', '小型机', '06EAF25', 'IBM', 'P550', '5', 'A04', '15', '18', '2014-06-30', null, '4', '1', '胡运秋', null, '6.123.253.20', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1602', '异地灾备X86虚拟化2', 'X86服务器', '210235A2CRH19A000268', 'H3C', 'R4900 G3', '5', 'A05', '5', '6', '2019-12-27', '2025-01-14', '4', '1', '胡运秋', '晏良', '6.123.253.12', null, '6.123.253.14', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1603', '异地灾备X86虚拟化1', 'X86服务器', '210235A2CRH19A000264', 'H3C', 'R4900 G3', '5', 'A05', '8', '9', '2019-12-27', '2025-01-14', '4', '1', '胡运秋', '晏良', '6.123.253.11', null, '6.123.253.13', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1604', '异地灾备networker备份', 'X86服务器', '06ECNW6', 'IBM', 'X3650M3', '5', 'A05', '11', '12', '2012-09-26', null, '4', '1', '胡运秋', null, '6.123.253.1', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1605', 'HMC控制台', 'X86服务器', '06F7B9B', 'IBM', 'X3550', '5', 'A05', '14', '14', '2014-06-30', null, '4', '1', '胡运秋', null, '6.123.253.30', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1606', '异地灾备networker备份', 'X86服务器', '717203014', '浪潮', 'NF5270 M4', '5', 'A05', '16', '17', '2017-07-01', null, '4', '1', '胡运秋', null, '6.123.253.60', null, '6.191.253.63', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1607', '异地灾备加密机1', '加密机', 'SJJ121415342', '江南信息', 'SJJ1214', '5', 'A06', '5', '6', '2015-12-21', null, '4', '1', '胡运秋', null, '6.120.0.141', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1608', '异地灾备加密机2', '加密机', 'SJJ121415345', '江南信息', 'SJJ1214', '5', 'A06', '8', '9', '2015-12-21', null, '4', '1', '胡运秋', null, '6.120.0.73', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1609', '灾备虚拟带库', '虚拟带库', 'CKM00182400880', 'EMC', 'DD6300', '5', 'A07', '19', '24', '2018-09-27', null, '4', '1', '胡运秋', null, '6.120.0.3', null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('1610', '异地灾备华为6800V5存储', '磁盘阵列', '2102351NPT10LB000001', '华为', '6800 V5', '5', 'A08', '5', '22', '2020-11-18', '2026-02-01', '4', '1', '胡运秋', null, '6.123.253.61', null, null, null, null, null, '6.123.253.61/62两个管理地址', null);
INSERT INTO `machine_infos` VALUES ('1611', '开发HMC', 'X86服务器', '06-1894B', 'IBM', 'X3550', '4', 'KF09', '25', '25', '2000-01-01', '2000-01-01', '4', '4', '周中秋', '', '', '', '', '2000-01-01', '2022-09-20', '0', '', null);
INSERT INTO `machine_infos` VALUES ('1622', '硬盘录像机210', '视频监控', 'J06591718', '海康', 'DS-8832N-18/JM', '25', 'C04', '20', '21', '2000-01-01', '2000-01-01', '1', '1', '', '', '1.100.0.210', '', '', '2022-09-01', null, '1', '新中心新上线设备', null);
INSERT INTO `machine_infos` VALUES ('1623', '硬盘录像机215', '视频监控', 'J06591706', '海康', 'DS-8832N-18/JM', '25', 'C04', '23', '24', '2000-01-01', '2000-01-01', '1', '1', '', '', '1.100.0.215', '', '', '2022-09-01', null, '1', '', null);
INSERT INTO `machine_infos` VALUES ('1624', '硬盘录像机214', '视频监控', 'J06591700', '海康', 'DS-8832N-18/JM', '25', 'C04', '26', '27', '2000-01-01', '2000-01-01', '1', '1', '', '', '1.100.0.214', '', '', '2022-09-01', null, '1', '', null);
INSERT INTO `machine_infos` VALUES ('1625', '硬盘录像机213', '视频监控', 'J06591694', '海康', 'DS-8832N-18/JM', '25', 'C04', '29', '30', '2000-01-01', '2000-01-01', '1', '1', '', '', '1.100.0.213', '', '', '2022-09-01', null, '1', '', null);
INSERT INTO `machine_infos` VALUES ('1626', '硬盘录像机212', '视频监控', 'J06591668', '海康', 'DS-8832N-18/JM', '25', 'C04', '32', '33', '2000-01-01', '2000-01-01', '1', '1', '', '', '1.100.0.212', '', '', '2022-09-01', null, '1', '', null);
INSERT INTO `machine_infos` VALUES ('1627', '硬盘录像机211', '视频监控', 'J06591710', '海康', 'DS-8832N-18/JM', '25', 'C04', '35', '36', '2000-01-01', '2000-01-01', '1', '1', '胡运秋', '', '1.100.0.211', '', '', '2022-09-01', null, '1', '', '12');

-- ----------------------------
-- Table structure for machine_password
-- ----------------------------
DROP TABLE IF EXISTS `machine_password`;
CREATE TABLE `machine_password` (
  `pid` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `machine_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '设备名称',
  `ip` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'IP地址',
  `sn` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '序列号',
  `room` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '机房名称',
  `user` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户名',
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '密码',
  `machine_type` int NOT NULL DEFAULT '0' COMMENT '设备类型：0：物理设备，1：虚拟机',
  `machine_id` int DEFAULT NULL COMMENT '设备id',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of machine_password
-- ----------------------------
INSERT INTO `machine_password` VALUES ('12', '湘潭EBANK_WEB/OA vcenter', '192.168.230.13', null, 'ZB-1', 'vmadmin', 'P@ssw0rd', '1', null, '管理的物理机有192.168.230.70,71,72,61,62');
INSERT INTO `machine_password` VALUES ('13', '湘潭EBANK_APP vcenter', '192.168.230.16', null, 'ZB-1', 'vmadmin', 'P@ssw0rd', '1', null, '管理虚拟化物理机包括192.168.230.67,68,69');
INSERT INTO `machine_password` VALUES ('14', '湘潭生产虚拟化vcenter', '192.168.230.12', null, 'ZB-1', 'vmdmin', 'P@ssw0rd', '1', null, '管理的X86物理机192.168.230.28/30/32/34');
INSERT INTO `machine_password` VALUES ('15', '同城灾备虚拟化vcenter', '6.104.0.10', null, 'ZB-1', 'vmadmin', 'P@ssword', '1', null, '管理虚拟化物理机6.104.0.2/3');
INSERT INTO `machine_password` VALUES ('16', '同城灾备虚拟化vcenter2', '6.104.0.20', null, 'ZB-1', 'vmadmin', 'vmadmin/vmadmin@123', '1', null, '管理物理机6.104.0.4/5');
INSERT INTO `machine_password` VALUES ('17', '电渠新加VC', '6.104.1.10', null, 'ZB-1', 'xtcx@vsphere.local', 'xtcx@vsphere.local', '1', null, '管理物理机6.104.1.11/12/13');
INSERT INTO `machine_password` VALUES ('18', '灾备核心生产主机（20）', '6.104.5.20', '06E9835', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1387', 'root用户加入了堡垒机');
INSERT INTO `machine_password` VALUES ('19', '灾备综合前置（25）', '6.104.5.25', '06E9845', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1390', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('20', '灾备CIF-RAC', '6.104.5.16', '10-E71D4', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1383', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('21', '灾备CIF-RAC', '6.104.5.17', '10-78A4F', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1378', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('23', '灾备图形前端&中间RAC', '6.104.5.22', '2130F8V', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1379', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('24', '灾备电子渠道rac', '6.104.5.26', '845D07V', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1392', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('25', '灾备电子渠道rac', '6.104.5.27', '845D0AV', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1398', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('26', '灾备信贷内管RAC2', '6.104.5.30', '06-BD8F6', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1389', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('27', '灾备信贷内管RAC1', '6.104.5.31', '06-BD976', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1401', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('28', '灾备创新平台', '6.104.5.236', '06-8F4A6', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1394', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('29', '灾备创新平台', '6.104.5.237', '06-8F476', 'ZB-1', 'zbyw', 'zbyw1234', '0', '1400', 'root用户已加入堡垒机');
INSERT INTO `machine_password` VALUES ('30', '灾备核心测试用', '6.104.5.221', '06-8F4B6', 'ZB-1', 'root', 'tczb@WSX', '0', '1396', '');
INSERT INTO `machine_password` VALUES ('31', '灾备核心备份机', '6.104.5.23', '06-BD8E6', 'ZB-1', 'root', 'root_151', '0', '1397', '');
INSERT INTO `machine_password` VALUES ('32', 'VMAX 存储', '192.168.210.203', 'CN498700149', 'ZB-1', 'monitor', 'hrxj_123', '0', '1493', '');
INSERT INTO `machine_password` VALUES ('33', 'VMAX 存储', '192.168.210.205', 'CN498700243', 'ZB-2', 'monitor', 'hrxj_123', '0', '1520', '');
INSERT INTO `machine_password` VALUES ('34', 'VMAX 存储-机头', '192.168.210.207', 'CN498700317', 'ZB-1', 'monitor', 'hrxj_123', '0', '1357', '');
INSERT INTO `machine_password` VALUES ('35', '灾备HMC控制台', '6.104.5.9', '21D8CDC', 'ZB-1', 'root', 'abc123', '0', '1381', '');
INSERT INTO `machine_password` VALUES ('36', '生产HMC', '6.104.5.10', '1085D7C', 'ZB-2', 'root', 'abc1234', '0', '1561', '');
INSERT INTO `machine_password` VALUES ('37', '异地灾备X86虚拟化1', '6.123.253.11', '210235A2CRH19A000264', 'CZ-1', 'root', 'password', '0', '1603', 'exsi 用户信息');
INSERT INTO `machine_password` VALUES ('38', '异地灾备X86虚拟化2', '6.123.253.12', '210235A2CRH19A000268', 'CZ-1', 'root', 'password', '0', '1602', 'esxi用户信息');
INSERT INTO `machine_password` VALUES ('39', '异地灾备VC虚拟机', '6.123.253.15', null, '', 'administrator', 'password', '1', null, 'windows用户信息\nvc登录信息administrator@vsphere.local/1qaz@WSX');
INSERT INTO `machine_password` VALUES ('40', 'NAS存储生产5300', '192.168.230.120', 'FCN00142900103', 'ZB-1', 'sysadmin', 'hrxj@dxl1', '0', '1489', '');
INSERT INTO `machine_password` VALUES ('41', 'EMC VPLEX 存储网关', '6.104.4.7', 'CKM00133803173', 'ZB-1', 'service', 'p@ssw0rd', '0', '1492', '');
INSERT INTO `machine_password` VALUES ('42', 'X86虚拟化（电渠区应用监控）', '6.104.1.11', '210235A2CRH19A000267', 'ZB-1', 'root', '1qaz@WSX', '0', '1465', 'exsi用户信息');
INSERT INTO `machine_password` VALUES ('43', 'X86虚拟化（电渠区应用监控）', '6.104.1.12', '210235A2CRH19A000280', 'ZB-1', 'root', '1qaz@WSX', '0', '1466', 'exsi用户信息');
INSERT INTO `machine_password` VALUES ('44', 'X86虚拟化（电渠区应用监控）', '6.104.1.13', '210235A2CRH19A000277', 'ZB-1', 'root', '1qaz@WSX', '0', '1467', 'exsi用户信息');
INSERT INTO `machine_password` VALUES ('45', '灾备oracle RAC', '6.104.5.33', '7241280987/3BR9S63', 'ZB-1', 'root', 'abc123', '0', '1372', 'redhat 用户信息');
INSERT INTO `machine_password` VALUES ('46', '灾备oracle RAC', '192.168.0.13', '7241280987/3BR9S63', 'ZB-1', 'root', 'calvin', '0', '1372', 'IDRAC用户信息');
INSERT INTO `machine_password` VALUES ('47', '灾备oracle RAC', '6.104.5.34', '7239881307/3BQFS63', 'ZB-1', 'root', 'abc123', '0', '1373', 'redhat用户信息');
INSERT INTO `machine_password` VALUES ('48', '灾备oracle RAC', '192.168.0.12', '7239881307/3BQFS63', 'ZB-1', 'root', 'calvin', '0', '1373', 'idrac用户信息');
INSERT INTO `machine_password` VALUES ('49', '灾备oracle RAC', '6.104.5.35', '7241374299/3BRBS63', 'ZB-1', 'root', 'abc123', '0', '1374', 'redhat用户信息');
INSERT INTO `machine_password` VALUES ('50', '灾备oracle RAC', '192.168.0.11', '7241374299/3BRBS63', 'ZB-1', 'root', 'calvin', '0', '1374', 'idrac用户信息');
INSERT INTO `machine_password` VALUES ('51', '灾备oracle RAC', '6.104.5.36', '7239694683/3BQBS63', 'ZB-1', 'root', 'abc123', '0', '1375', 'redhat用户信息');
INSERT INTO `machine_password` VALUES ('52', '灾备oracle RAC', '192.168.0.10', '7239694683/3BQBS63', 'ZB-1', 'root', 'calvin', '0', '1375', 'idrac用户信息');
INSERT INTO `machine_password` VALUES ('53', '基础数据平台ETL', '192.168.1.178', '06EADE5', 'ZB-2', 'root', 'root_178', '0', '1574', 'AIX 用户信息。\n业务用户：xtbdpftp/xtbdpftp');
INSERT INTO `machine_password` VALUES ('54', '灾备虚拟带库', '6.120.0.3', 'CKM00182400880', 'CZ-1', 'sysadmin', 'abc123', '0', '1609', '');
INSERT INTO `machine_password` VALUES ('55', '灾备综合前置主机', '6.123.253.20', '06EAF25', 'CZ-1', 'root', 'hrxj_020', '0', '1601', '');
INSERT INTO `machine_password` VALUES ('56', '灾备综合前置主机', '6.123.253.20', '06EAF25', 'CZ-1', 'zbyw', 'zbyw123', '0', '1601', '');
INSERT INTO `machine_password` VALUES ('57', '灾备核心系统主机', '6.123.253.25', '068F486', 'CZ-1', 'root', 'root_25', '0', '1600', '');
INSERT INTO `machine_password` VALUES ('58', '灾备核心系统主机', '6.123.253.25', '068F486', 'CZ-1', 'zbyw', 'zbyw123', '0', '1600', '');
INSERT INTO `machine_password` VALUES ('59', '灾备恢复验证主机', '6.123.253.2', '06EAE15', 'CZ-1', 'root', 'root_007', '0', '1599', '');
INSERT INTO `machine_password` VALUES ('60', '灾备IC卡系统数据库-VIOS1', '6.123.253.16', '068F496', 'CZ-1', 'padmin', 'padmin', '0', '1598', '');
INSERT INTO `machine_password` VALUES ('61', '灾备CIF、自助设备-VIOS2', '6.123.253.17', '06EAF95', 'CZ-1', 'padmin', 'padmin', '0', '1597', 'VIOC');
INSERT INTO `machine_password` VALUES ('62', '异地灾备networker备份', '6.123.253.1', '06ECNW6', 'CZ-1', 'administrator', 'admin_258', '0', '1604', 'network服务器window2003用户信息');
INSERT INTO `machine_password` VALUES ('63', 'HMC控制台', '6.123.253.30', '06F7B9B', 'CZ-1', 'hscroot', 'abc123', '0', '1605', '');
INSERT INTO `machine_password` VALUES ('64', '异地新存储光交A', '6.123.253.4', '2102353VBN10LB000004', 'CZ-1', 'admin', 'Huawei12#$', '0', '1593', '华为SAN光交');
INSERT INTO `machine_password` VALUES ('65', '异地新存储光交B', '6.123.253.5', '2102353VBN10LB000003', 'CZ-1', 'admin', 'Huawei12#$', '0', '1596', '华为SAN光交');
INSERT INTO `machine_password` VALUES ('66', '异地灾备CXPT', '6.123.253.237', null, '', 'root', 'root_237', '1', null, '异地cxpt  root用户信息');
INSERT INTO `machine_password` VALUES ('67', '异地灾备CXPT', '6.123.253.237', null, 'CZ-1', 'oracle', 'ydzb@cxpt', '1', null, 'oracle用户信息');
INSERT INTO `machine_password` VALUES ('68', '异地cif', '6.123.253.52', null, 'CZ-1', 'root', 'root_52', '1', null, '异地灾备CIF root用户信息');
INSERT INTO `machine_password` VALUES ('69', '异地灾备cif', '6.123.253.52', null, 'CZ-1', 'oracle', 'ydzb@cifdb', '1', null, '异地cif oracle用户信息');
INSERT INTO `machine_password` VALUES ('70', '异地灾备图形前端', '6.123.253.116', null, 'CZ-1', 'root', 'root_116', '1', null, '异地图形前端 root用户信息');
INSERT INTO `machine_password` VALUES ('71', '异地灾备图形前端', '6.123.253.116', null, 'CZ-1', 'oracle', 'ydzb@txqd', '1', null, 'oracle用户信息');
INSERT INTO `machine_password` VALUES ('72', '异地灾备华为6800V5存储', '6.123.253.61', '2102351NPT10LB000001', 'CZ-1', 'admin', 'Admin@storage', '0', '1610', '通过web访问6.123.253.61:8088\n6.123.253.62:8088');
INSERT INTO `machine_password` VALUES ('73', '异地灾备华为6800V5存储', '6.123.253.61', '2102351NPT10LB000001', 'CZ-1', 'ywadmin', 'zbyw@123', '0', '1610', '通过web访问6.123.253.61:8088\n6.123.253.62:8088');
INSERT INTO `machine_password` VALUES ('74', '异地灾备networker备份', '6.123.253.60', '717203014', 'CZ-1', 'administrator', '1qaz@WSX', '0', '1606', 'os 的administrator用户信息');
INSERT INTO `machine_password` VALUES ('75', '灾备oracle RAC', '192.168.0.120', '26698098207/C9JCWF3', 'ZB-1', 'root', 'dell123', '0', '1376', 'idrac用户信息');
INSERT INTO `machine_password` VALUES ('76', '灾备oracle RAC', '192.168.0.120', '20167751199/99JCWF3', 'ZB-1', 'root', 'dell123', '0', '1377', 'idrac用户信息');

-- ----------------------------
-- Table structure for machine_room
-- ----------------------------
DROP TABLE IF EXISTS `machine_room`;
CREATE TABLE `machine_room` (
  `room_id` int(4) unsigned zerofill NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `room_name` varchar(45) NOT NULL COMMENT '机房名称',
  `room_alias` varchar(45) DEFAULT NULL COMMENT '别名',
  `comment` varchar(45) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`room_id`),
  UNIQUE KEY `room_id_UNIQUE` (`room_id`),
  UNIQUE KEY `room_name_UNIQUE` (`room_name`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3 AVG_ROW_LENGTH=1 COMMENT='机柜信息';

-- ----------------------------
-- Records of machine_room
-- ----------------------------
INSERT INTO `machine_room` VALUES ('0001', 'ZB-1', '主机房', '');
INSERT INTO `machine_room` VALUES ('0002', 'ZB-2', '网络机房', null);
INSERT INTO `machine_room` VALUES ('0003', 'ZB-3', '分行机房', null);
INSERT INTO `machine_room` VALUES ('0004', 'ZB-4', '开发机房', null);
INSERT INTO `machine_room` VALUES ('0005', 'CZ-1', '郴州机房', null);
INSERT INTO `machine_room` VALUES ('0025', '603', '603机房', null);

-- ----------------------------
-- Table structure for machine_sort
-- ----------------------------
DROP TABLE IF EXISTS `machine_sort`;
CREATE TABLE `machine_sort` (
  `sort_id` int NOT NULL COMMENT '分类ID',
  `sort_name` char(255) NOT NULL COMMENT '备设分类',
  `part_sort_id` int DEFAULT NULL COMMENT '上级分类ID',
  `part_sort_name` char(255) DEFAULT NULL COMMENT '上级分类名称',
  `conments` char(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`sort_id`),
  KEY `sort_id` (`sort_id`),
  KEY `sortid` (`part_sort_id`),
  KEY `sort_name` (`sort_name`),
  KEY `sortname` (`part_sort_name`),
  CONSTRAINT `sortid` FOREIGN KEY (`part_sort_id`) REFERENCES `machine_sort` (`sort_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of machine_sort
-- ----------------------------
INSERT INTO `machine_sort` VALUES ('1001', '主机', null, null, null);
INSERT INTO `machine_sort` VALUES ('1010', '存储', null, null, null);
INSERT INTO `machine_sort` VALUES ('1020', '网络', null, null, null);
INSERT INTO `machine_sort` VALUES ('1030', '机房环境', null, null, null);
INSERT INTO `machine_sort` VALUES ('1040', '安全加密', null, null, null);
INSERT INTO `machine_sort` VALUES ('1070', '其它', null, null, null);
INSERT INTO `machine_sort` VALUES ('10010001', 'X86服务器', '1001', '主机', null);
INSERT INTO `machine_sort` VALUES ('10010010', '小型机', '1001', '主机', null);
INSERT INTO `machine_sort` VALUES ('10100001', '磁盘阵列', '1010', '存储', null);
INSERT INTO `machine_sort` VALUES ('10100010', '存储光交', '1010', '存储', null);
INSERT INTO `machine_sort` VALUES ('10100020', '虚拟带库', '1010', '存储', null);
INSERT INTO `machine_sort` VALUES ('10100030', '存储网关', '1010', '存储', null);
INSERT INTO `machine_sort` VALUES ('10100040', '其它存储', '1010', '存储', null);
INSERT INTO `machine_sort` VALUES ('10100050', '磁带机', '1010', '存储', null);
INSERT INTO `machine_sort` VALUES ('10200001', '交换机', '1020', '网络', null);
INSERT INTO `machine_sort` VALUES ('10200010', '路由器', '1020', '网络', null);
INSERT INTO `machine_sort` VALUES ('10200020', '防火墙', '1020', '网络', null);
INSERT INTO `machine_sort` VALUES ('10200030', '安全设备', '1020', '网络', null);
INSERT INTO `machine_sort` VALUES ('10200040', '其它网络设备', '1020', '网络', null);
INSERT INTO `machine_sort` VALUES ('10200050', '负载均衡', '1020', '网络', null);
INSERT INTO `machine_sort` VALUES ('10200060', 'DNS设备', '1020', '网络', null);
INSERT INTO `machine_sort` VALUES ('10300001', '空调', '1030', '机房环境', null);
INSERT INTO `machine_sort` VALUES ('10300010', 'UPS', '1030', '机房环境', null);
INSERT INTO `machine_sort` VALUES ('10300020', '电池', '1030', '机房环境', null);
INSERT INTO `machine_sort` VALUES ('10300030', '动环监控', '1030', '机房环境', null);
INSERT INTO `machine_sort` VALUES ('10300040', '视频监控', '1030', '机房环境', null);
INSERT INTO `machine_sort` VALUES ('10400001', '加密机', '1040', '安全加密', null);
INSERT INTO `machine_sort` VALUES ('10400010', '数字签名', '1040', '安全加密', null);
INSERT INTO `machine_sort` VALUES ('10600020', '其它设备', '1070', '其它', null);
INSERT INTO `machine_sort` VALUES ('10600030', '排队机', '1070', '其它', null);
INSERT INTO `machine_sort` VALUES ('10600040', '运营商设备', '1070', '其它', null);

-- ----------------------------
-- Table structure for manufacturer
-- ----------------------------
DROP TABLE IF EXISTS `manufacturer`;
CREATE TABLE `manufacturer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `manufacturer_name` varchar(255) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of manufacturer
-- ----------------------------
INSERT INTO `manufacturer` VALUES ('1', 'IBM', null);
INSERT INTO `manufacturer` VALUES ('2', 'DELL', null);
INSERT INTO `manufacturer` VALUES ('3', 'H3C', null);
INSERT INTO `manufacturer` VALUES ('4', '浪潮', null);
INSERT INTO `manufacturer` VALUES ('5', '华为', null);
INSERT INTO `manufacturer` VALUES ('6', '联想', null);
INSERT INTO `manufacturer` VALUES ('7', 'HP', null);
INSERT INTO `manufacturer` VALUES ('8', 'EMC', null);
INSERT INTO `manufacturer` VALUES ('9', 'DELL EMC', null);
INSERT INTO `manufacturer` VALUES ('10', '吉大正元', null);
INSERT INTO `manufacturer` VALUES ('14', '江南信息', null);
INSERT INTO `manufacturer` VALUES ('15', '迪普', null);
INSERT INTO `manufacturer` VALUES ('16', '天融信', null);
INSERT INTO `manufacturer` VALUES ('17', '绿盟', null);
INSERT INTO `manufacturer` VALUES ('18', 'Radware', null);
INSERT INTO `manufacturer` VALUES ('19', '信安世纪', null);
INSERT INTO `manufacturer` VALUES ('20', '山石', null);
INSERT INTO `manufacturer` VALUES ('21', '深信服', null);
INSERT INTO `manufacturer` VALUES ('22', 'F5', null);
INSERT INTO `manufacturer` VALUES ('23', '智卓', null);
INSERT INTO `manufacturer` VALUES ('24', 'CISCO', null);
INSERT INTO `manufacturer` VALUES ('25', 'MAIPU', null);
INSERT INTO `manufacturer` VALUES ('26', '博科', null);
INSERT INTO `manufacturer` VALUES ('27', 'ZDNS', null);
INSERT INTO `manufacturer` VALUES ('28', '启明星辰', null);
INSERT INTO `manufacturer` VALUES ('29', '奇安信', null);
INSERT INTO `manufacturer` VALUES ('30', 'GEMALTO LUNAIS66', null);
INSERT INTO `manufacturer` VALUES ('31', 'Juniper', null);
INSERT INTO `manufacturer` VALUES ('32', '动环串口设备', null);
INSERT INTO `manufacturer` VALUES ('33', 'XBROTHER', null);
INSERT INTO `manufacturer` VALUES ('34', '康耐得', null);
INSERT INTO `manufacturer` VALUES ('35', '科来', null);
INSERT INTO `manufacturer` VALUES ('37', '海康', null);

-- ----------------------------
-- Table structure for shelf_manage
-- ----------------------------
DROP TABLE IF EXISTS `shelf_manage`;
CREATE TABLE `shelf_manage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `machine_id` int NOT NULL COMMENT '设备ID',
  `up_or_down` int NOT NULL COMMENT '上架或下架：1：上架，2：下架',
  `operator` char(255) DEFAULT NULL COMMENT '执行人',
  `date` date DEFAULT NULL COMMENT '上下架日期',
  `reason` char(255) DEFAULT NULL COMMENT '原因',
  `comments` char(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  KEY `shelf_manage_ibfk_machina_id` (`machine_id`),
  CONSTRAINT `shelf_manage_ibfk_machina_id` FOREIGN KEY (`machine_id`) REFERENCES `machine_infos` (`machine_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of shelf_manage
-- ----------------------------
INSERT INTO `shelf_manage` VALUES ('1', '1484', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('2', '1485', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('3', '1486', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('4', '1394', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('5', '1400', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('6', '1588', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('7', '1512', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('8', '1513', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('9', '1514', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('10', '1518', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('11', '1611', '2', '胡运秋', '2022-09-20', null, '下架搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('12', '1000', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('13', '1001', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('14', '1002', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('15', '1003', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('16', '1004', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('17', '1005', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('18', '1006', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('19', '1007', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('20', '1008', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('21', '1009', '2', '胡运秋', '2022-08-15', null, '由华讯搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('22', '1390', '2', '胡运秋', '2022-09-20', null, '搬迁至长沙新数据中心');
INSERT INTO `shelf_manage` VALUES ('23', '1391', '2', '胡运秋', '2022-09-20', null, '下架搬迁至长沙新数据中心');

-- ----------------------------
-- View structure for machine_list
-- ----------------------------
DROP VIEW IF EXISTS `machine_list`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `machine_list` AS select `machine_infos`.`machine_id` AS `machine_id`,`machine_room`.`room_id` AS `room_id`,`machine_room`.`room_name` AS `room_name`,`machine_infos`.`cabinet_name` AS `cab_name`,`machine_infos`.`start_position` AS `start_position`,((`machine_infos`.`end_position` - `machine_infos`.`start_position`) + 1) AS `postion_u`,`machine_infos`.`machine_sort_name` AS `machine_sort_name`,`machine_infos`.`machine_factory` AS `machine_factory`,`machine_infos`.`model` AS `model`,`machine_infos`.`machine_sn` AS `machine_sn`,`machine_infos`.`machine_name` AS `machine_name`,`machine_infos`.`mg_ip` AS `mg_ip`,`machine_infos`.`bmc_ip` AS `bmc_ip`,`machine_infos`.`machine_admin` AS `machine_admin` from (`machine_infos` join `machine_room` on((`machine_infos`.`machine_roomid` = `machine_room`.`room_id`))) where (`machine_infos`.`run_state` in (1,2,3,5)) order by `machine_room`.`room_id`,`machine_infos`.`cabinet_name`,`machine_infos`.`start_position` ;

-- ----------------------------
-- View structure for view_check_cmd
-- ----------------------------
DROP VIEW IF EXISTS `view_check_cmd`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `view_check_cmd` AS select `u`.`id` AS `id`,`mi`.`machine_name` AS `hostname`,`mi`.`mg_ip` AS `ip`,`u`.`user` AS `user`,`u`.`password` AS `password`,`c`.`cmd_id` AS `cmd_id`,`c`.`cmd` AS `cmd`,`c`.`cmd_name` AS `cmd_name`,`u`.`machine_id` AS `machine_id` from ((`machine_check_user` `u` join `cmd_file` `c` on((`u`.`cmd_id` = `c`.`cmd_id`))) join `machine_infos` `mi` on((`mi`.`machine_id` = `u`.`machine_id`))) ;

-- ----------------------------
-- View structure for view_downshelf
-- ----------------------------
DROP VIEW IF EXISTS `view_downshelf`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `view_downshelf` AS select `f`.`id` AS `id`,`t`.`machine_id` AS `machine_id`,`t`.`machine_name` AS `machine_name`,concat(`m`.`room_name`,'_',`t`.`cabinet_name`,'_',`t`.`start_position`,'U') AS `postion`,`t`.`machine_sort_name` AS `machine_sort_name`,`t`.`model` AS `model`,`t`.`machine_factory` AS `machine_factory`,`t`.`machine_sn` AS `machine_sn`,`t`.`mg_ip` AS `mg_ip`,`f`.`date` AS `date`,`f`.`operator` AS `operator`,`t`.`machine_admin` AS `machine_admin`,`f`.`comments` AS `comments` from ((`machine_infos` `t` join `machine_room` `m` on((`t`.`machine_roomid` = `m`.`room_id`))) join `shelf_manage` `f` on((`f`.`machine_id` = `t`.`machine_id`))) order by `f`.`id` ;

-- ----------------------------
-- View structure for view_upshelf
-- ----------------------------
DROP VIEW IF EXISTS `view_upshelf`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `view_upshelf` AS select `f`.`id` AS `id`,`t`.`machine_id` AS `machine_id`,`t`.`machine_name` AS `machine_name`,concat(`m`.`room_name`,'_',`t`.`cabinet_name`,'_',`t`.`start_position`,'U') AS `postion`,`t`.`machine_sort_name` AS `machine_sort_name`,`t`.`model` AS `model`,`t`.`machine_factory` AS `machine_factory`,`t`.`machine_sn` AS `machine_sn`,`t`.`mg_ip` AS `mg_ip`,`f`.`date` AS `date`,`f`.`operator` AS `operator`,`t`.`machine_admin` AS `machine_admin`,`f`.`comments` AS `comments` from ((`machine_infos` `t` join `machine_room` `m` on((`t`.`machine_roomid` = `m`.`room_id`))) join `shelf_manage` `f` on((`t`.`machine_id` = `f`.`machine_id`))) where (`f`.`up_or_down` = 1) order by `t`.`install_date` desc ;
