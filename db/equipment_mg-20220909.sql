/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80025
Source Host           : localhost:3306
Source Database       : equipment_mg

Target Server Type    : MYSQL
Target Server Version : 80025
File Encoding         : 65001

Date: 2022-09-09 16:54:34
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
) ENGINE=InnoDB AUTO_INCREMENT=158 DEFAULT CHARSET=utf8mb3 COMMENT='机柜信息';

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
  PRIMARY KEY (`machine_id`),
  KEY `room_id` (`machine_roomid`),
  KEY `sort_name` (`machine_sort_name`),
  KEY `s_position` (`start_position`),
  KEY `e_position` (`end_position`),
  KEY `fr_cabinet_name` (`cabinet_name`),
  CONSTRAINT `cabinet_name` FOREIGN KEY (`cabinet_name`) REFERENCES `cabinet` (`cab_num`),
  CONSTRAINT `e_position` FOREIGN KEY (`end_position`) REFERENCES `cab_position` (`num`),
  CONSTRAINT `machine_infos_ibfk_1` FOREIGN KEY (`machine_sort_name`) REFERENCES `machine_sort` (`sort_name`) ON UPDATE CASCADE,
  CONSTRAINT `room_id` FOREIGN KEY (`machine_roomid`) REFERENCES `machine_room` (`room_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `s_position` FOREIGN KEY (`start_position`) REFERENCES `cab_position` (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of machine_infos
-- ----------------------------

-- ----------------------------
-- Table structure for machine_password
-- ----------------------------
DROP TABLE IF EXISTS `machine_password`;
CREATE TABLE `machine_password` (
  `pid` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `machine_name` varchar(32) DEFAULT NULL COMMENT '设备名称',
  `ip` varchar(32) NOT NULL COMMENT 'IP地址',
  `sn` varchar(20) DEFAULT NULL COMMENT '序列号',
  `room` varchar(10) DEFAULT NULL COMMENT '机房名称',
  `user` varchar(20) NOT NULL COMMENT '用户名',
  `password` varchar(32) NOT NULL COMMENT '密码',
  `machine_type` int NOT NULL DEFAULT '0' COMMENT '设备类型：0：物理设备，1：虚拟机',
  `machine_id` int DEFAULT NULL COMMENT '设备id',
  `remark` varchar(32) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of machine_password
-- ----------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3 AVG_ROW_LENGTH=1 COMMENT='机柜信息';

-- ----------------------------
-- Records of machine_room
-- ----------------------------
INSERT INTO `machine_room` VALUES ('0001', 'ZB-1', '主机房', '');
INSERT INTO `machine_room` VALUES ('0002', 'ZB-2', '网络机房', null);
INSERT INTO `machine_room` VALUES ('0003', 'ZB-3', '分行机房', null);
INSERT INTO `machine_room` VALUES ('0004', 'ZB-4', '开发机房', null);
INSERT INTO `machine_room` VALUES ('0005', 'CZ-1', '郴州机房', null);

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
INSERT INTO `manufacturer` VALUES ('13', '测试', null);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of shelf_manage
-- ----------------------------

-- ----------------------------
-- View structure for machine_list
-- ----------------------------
DROP VIEW IF EXISTS `machine_list`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `machine_list` AS select `machine_infos`.`machine_id` AS `machine_id`,`machine_room`.`room_name` AS `room_name`,`machine_infos`.`cabinet_name` AS `cab_name`,`machine_infos`.`start_position` AS `start_position`,((`machine_infos`.`end_position` - `machine_infos`.`start_position`) + 1) AS `postion_u`,`machine_infos`.`machine_sort_name` AS `machine_sort_name`,`machine_infos`.`machine_factory` AS `machine_factory`,`machine_infos`.`model` AS `model`,`machine_infos`.`machine_sn` AS `machine_sn`,`machine_infos`.`machine_name` AS `machine_name`,`machine_infos`.`mg_ip` AS `mg_ip`,`machine_infos`.`bmc_ip` AS `bmc_ip`,`machine_infos`.`machine_admin` AS `machine_admin` from (`machine_infos` join `machine_room` on((`machine_infos`.`machine_roomid` = `machine_room`.`room_id`))) where (`machine_infos`.`run_state` in (1,2,3,5)) order by `machine_room`.`room_name`,`machine_infos`.`cabinet_name`,`machine_infos`.`start_position` ;

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
