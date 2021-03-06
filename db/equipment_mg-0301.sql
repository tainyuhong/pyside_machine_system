/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80025
Source Host           : localhost:3306
Source Database       : equipment_mg

Target Server Type    : MYSQL
Target Server Version : 80025
File Encoding         : 65001

Date: 2022-03-03 17:27:58
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
  CONSTRAINT `roomid` FOREIGN KEY (`room_id`) REFERENCES `machine_room` (`room_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=140 DEFAULT CHARSET=utf8mb3 COMMENT='机柜信息';

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
INSERT INTO `cabinet` VALUES ('39', 'D08', 'D08', '1', '0', null, '42', null, null);
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
INSERT INTO `cabinet` VALUES ('139', 'A11', '波分机柜-（电信、中信）', '2', '1', null, '42', null, '波分机柜');

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
  PRIMARY KEY (`id`,`num`),
  KEY `position_num` (`position_name`),
  KEY `id` (`id`),
  KEY `id_2` (`id`),
  KEY `num` (`num`),
  KEY `num_2` (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3 COMMENT='U位表';

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
  `cmd_id` int NOT NULL COMMENT 'id',
  `cmd_name` varchar(255)  DEFAULT NULL COMMENT '命令集名称',
  `cmd` varchar(255) DEFAULT NULL COMMENT '命令内容',
  PRIMARY KEY (`cmd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_general_ci;

-- ----------------------------
-- Records of cmd_file
-- ----------------------------
INSERT INTO `cmd_file` VALUES ('1', '日期', 'date\r\nhostname\r\nuname');
INSERT INTO `cmd_file` VALUES ('2', '主机名', 'hostname');

-- ----------------------------
-- Table structure for machine_check_user
-- ----------------------------
DROP TABLE IF EXISTS `machine_check_user`;
CREATE TABLE `machine_check_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) DEFAULT NULL COMMENT '主机名称',
  `ip` varchar(255) NOT NULL COMMENT 'ip',
  `user` varchar(255) DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `cmd_id` int DEFAULT NULL COMMENT '命令集合id',
  `comment` varchar(255) DEFAULT NULL COMMENT '备注',
  `machine_id` int DEFAULT NULL COMMENT '主机id',
  PRIMARY KEY (`id`),
  KEY `machine_check_user_idfk_machine_id` (`machine_id`),
  CONSTRAINT `machine_check_user_idfk_machine_id` FOREIGN KEY (`machine_id`) REFERENCES `machine_infos` (`machine_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_general_ci COMMENT='设备巡检用户信息';

-- ----------------------------
-- Records of machine_check_user
-- ----------------------------
INSERT INTO `machine_check_user` VALUES ('1', 'k8s-master', '192.168.1.70', 'root', '123456', '1', '', '5741');
INSERT INTO `machine_check_user` VALUES ('2', 'k8s-node1', '192.168.1.61', 'root', '123456', '2', '', '5742');
INSERT INTO `machine_check_user` VALUES ('3', 'K8S-node2', '192.168.1.62', 'root', '123456', '1', '', '5743');
INSERT INTO `machine_check_user` VALUES ('4', 'K8S-NODE3', '192.168.1.63', 'root', '123456', '1', '', '5744');
INSERT INTO `machine_check_user` VALUES ('5', 'mysql-node1', '192.168.1.51', 'root', '123456', '1', '', '5748');
INSERT INTO `machine_check_user` VALUES ('6', 'mysql-node2', '192.168.1.52', 'root', '123456', '1', '', '5749');
INSERT INTO `machine_check_user` VALUES ('7', 'k8s-master', '192.168.1.70', 'root', '123456', '2', null, '5741');

-- ----------------------------
-- Table structure for machine_infos
-- ----------------------------
DROP TABLE IF EXISTS `machine_infos`;
CREATE TABLE `machine_infos` (
  `machine_id` int NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `machine_name` char(255) DEFAULT NULL COMMENT '设备名称',
  `machine_sort_id` int DEFAULT NULL COMMENT '分类id',
  `machine_sort_name` char(255) DEFAULT NULL COMMENT '分类名称',
  `machine_sn` char(255) DEFAULT NULL COMMENT '序列号',
  `machine_factory` char(255) DEFAULT NULL COMMENT '设备厂商',
  `model` char(255) DEFAULT NULL COMMENT '型号',
  `machine_roomid` int unsigned DEFAULT NULL COMMENT '机房ID',
  `cabinet_id` int DEFAULT NULL COMMENT '机柜ID',
  `cabinet_name` varchar(255) DEFAULT NULL COMMENT '机房编号',
  `start_position` int DEFAULT NULL COMMENT '开始U位',
  `end_position` int DEFAULT NULL COMMENT '结束U位',
  `factory_date` date DEFAULT '9999-12-31' COMMENT '生产日期',
  `end_ma_date` date DEFAULT '9999-12-31' COMMENT '到保日期',
  `work_are` char(255) DEFAULT NULL COMMENT '业务类型：1生产，2电渠，3灾备，4开发',
  `run_state` int DEFAULT '1' COMMENT '运行状态:1运行，2下线，3关机，4下架，5未加电',
  `redundancy_mode` int DEFAULT NULL COMMENT '冗余方式',
  `machine_admin` char(255) DEFAULT NULL COMMENT '管理员',
  `app_admin` char(255) DEFAULT NULL COMMENT '应用管理员',
  `mg_ip` char(255) DEFAULT NULL COMMENT '业务管理IP地址',
  `app_ip1` char(255) DEFAULT NULL COMMENT '业务IP1',
  `app_ip2` char(255) DEFAULT NULL,
  `app_ip3` char(255) DEFAULT NULL,
  `app_ip4` char(255) DEFAULT NULL,
  `bmc_ip` char(255) DEFAULT NULL COMMENT 'bmc IP',
  `machine_use` char(255) DEFAULT NULL COMMENT '用途',
  `issinglepower` int DEFAULT NULL COMMENT '是否单电源：1：是，2：否',
  `install_date` date DEFAULT NULL COMMENT '上架安装时间',
  `uninstatll_date` date DEFAULT NULL COMMENT '下架时间',
  `comments` char(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`machine_id`),
  KEY `cabinet_id` (`cabinet_id`),
  KEY `room_id` (`machine_roomid`),
  KEY `sort_id` (`machine_sort_id`),
  KEY `sort_name` (`machine_sort_name`),
  KEY `s_position` (`start_position`),
  KEY `e_position` (`end_position`),
  KEY `fr_cabinet_name` (`cabinet_name`),
  KEY `idx_room_cabinet_sposition` (`machine_roomid`,`cabinet_id`,`start_position`) USING BTREE,
  CONSTRAINT `cabinet_id` FOREIGN KEY (`cabinet_id`) REFERENCES `cabinet` (`cab_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `cabinet_name` FOREIGN KEY (`cabinet_name`) REFERENCES `cabinet` (`cab_num`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `e_position` FOREIGN KEY (`end_position`) REFERENCES `cab_position` (`num`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `room_id` FOREIGN KEY (`machine_roomid`) REFERENCES `machine_room` (`room_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `s_position` FOREIGN KEY (`start_position`) REFERENCES `cab_position` (`num`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sort_name` FOREIGN KEY (`machine_sort_name`) REFERENCES `machine_sort` (`sort_name`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5750 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of machine_infos
-- ----------------------------
INSERT INTO `machine_infos` VALUES ('5373', '开发测试环境存储-两个阵列柜', '10100001', '磁盘阵列', '78N25ZV/78RETFZ', 'IBM', 'V7000', '1', '1', 'A01', '1', '4', null, null, '4', '1', null, '周琦', null, '10.0.0.70/192.168.210.30', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5374', 'POWER虚拟化主机1', '10010010', '小型机', '06DBDCR', 'IBM', 'POWER 750', '1', '1', 'A01', '6', '13', null, null, '4', '1', null, '周琦', null, '192.168.231.12(hmc)', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5375', '开发HMC', '10010001', 'X86服务器', '1085D7C', 'IBM', 'IBM X3550 M3 7042', '1', '1', 'A01', '14', '14', null, null, '4', '1', null, '周琦', null, '192.168.121.10/10.0.0.10/192.168.231.10', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5376', '显示套件', '10600020', '其它设备', null, 'IBM', '显示套件', '1', '1', 'A01', '17', '17', null, null, '4', '1', null, '周琦', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5377', '开发X86虚拟化', '10010001', 'X86服务器', '816451315', '浪潮', 'NF8460 M4', '1', '1', 'A01', '18', '21', '2016-08-17', '2019-09-30', '4', '1', null, '周琦', null, '192.168.230.109', null, null, null, null, '192.168.1.104', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5378', 'POWER虚拟化主机2', '10010010', '小型机', '06DBDER', 'IBM', 'POWER 750', '1', '1', 'A01', '24', '31', null, null, '4', '1', null, '周琦', null, '192.168.231.11(hmc)', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5379', '开发测试用存储', '10100001', '磁盘阵列', 'FCN00122100176', 'EMC', 'VNX 5100', '1', '3', 'A02', '30', '33', '2012-09-01', null, '4', '1', null, '晏良', null, '192.168.230.81/82', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5380', '准生产测试用存储', '10100001', '磁盘阵列', 'FCN00112900210', 'EMC', 'VNX 5100', '1', '4', 'A03', '1', '4', '2012-09-01', null, '4', '1', null, '晏良', null, '192.168.230.83/84', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5381', '开发、验证准生产X86虚拟化5', '10010001', 'X86服务器', '06BF148', 'IBM', 'X3850 X6', '1', '4', 'A03', '6', '9', '2014-05-06', '2017-07-06', '4', '1', null, '周琦', null, '192.168.230.37', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5382', '开发、验证准生产X86虚拟化4', '10010001', 'X86服务器', '06BF152', 'IBM', 'X3850 X6', '1', '4', 'A03', '11', '14', '2014-05-06', '2017-07-06', '4', '1', null, '周琦', null, '192.168.230.38', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5383', '开发、验证准生产X86虚拟化3', '10010001', 'X86服务器', '06BF155', 'IBM', 'X3850 X6', '1', '4', 'A03', '17', '20', '2014-05-06', '2017-07-06', '4', '1', null, '周琦', null, '192.168.230.41', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5384', '模拟银行', '10010001', 'X86服务器', '06BKEV1', 'IBM', 'X3650 M4', '1', '4', 'A03', '32', '33', '2012-04-30', '2015-06-13', '4', '1', null, '周琦', null, '192.168.16.230', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5385', '测试存储虚拟网关', '10100030', '存储网关', '2102350AWH10FA000008', '华为', 'oceanstor Vis6600T', '1', '4', 'A03', '34', '37', '2016-02-06', '2021-02-05', '4', '1', null, '周琦', null, '192.168.230.52', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5386', '开发X86虚拟化', '10010001', 'X86服务器', '816451310', '浪潮', 'NF8460 M4', '1', '5', 'A04', '2', '5', '2016-08-17', '2019-09-30', '4', '1', null, '周琦', null, '192.168.230.110', null, null, null, null, '192.168.1.105', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5387', '测试powervm虚拟化', '10010010', '小型机', '8492F9W', 'IBM', 'POWER S824', '1', '5', 'A04', '10', '13', null, null, '4', '1', null, '周琦', null, '192.168.231.41（hmc）', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5388', '磁带机', '10100050', '磁带机', '97-A0715', 'IBM', '7226-1U3', '1', '5', 'A04', '14', '14', null, null, '4', '1', null, '周琦', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5389', '开发X86虚拟化', '10010001', 'X86服务器', '816451312', '浪潮', 'NF8460 M4', '1', '5', 'A04', '21', '24', '2016-08-18', '2019-09-30', '4', '1', null, '周琦', null, '192.168.230.106', null, null, null, null, '192.168.1.101', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5390', '磁带机', '10100050', '磁带机', '97-A0392', 'IBM', '7226-1U3', '1', '5', 'A04', '27', '27', null, null, '4', '1', null, '周琦', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5391', '测试powervm虚拟化', '10010010', '小型机', '8492FAW', 'IBM', 'POWER S824', '1', '5', 'A04', '28', '31', null, null, '4', '1', null, '周琦', null, '192.168.231.40（hmc）', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5392', '云平台', '10010001', 'X86服务器', '816534205', '浪潮', 'NF5270M4', '1', '5', 'A04', '33', '34', '2016-12-26', '2020-01-31', '4', '3', null, '周琦', null, '192.168.230.242', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5393', 'OA X86虚拟化 ESX6', '10010001', 'X86服务器', '06L2028', 'IBM', 'X3850 X5', '1', '6', 'A05', '5', '8', '2012-07-30', '2015-09-12', '1', '1', null, '周琦', null, '192.168.230.61', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5394', 'SC X86虚拟化 ESX5', '10010001', 'X86服务器', '06L2033', 'IBM', 'X3850 X5', '1', '6', 'A05', '9', '12', '2012-07-31', '2015-09-13', '1', '1', null, '周琦', null, '192.168.230.34', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5395', '图形前端服务器（双活）1', '10010001', 'X86服务器', '2102310YPY10J4000697', '华为', 'H22M-03 RH2288 V3', '1', '6', 'A05', '26', '27', '2018-07-13', '2021-07-12', '1', '1', null, '周琦', null, '6.4.1.71', null, null, null, null, '2018.5.24安装', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5396', '图形前端服务器（双活）2', '10010001', 'X86服务器', '2102310YPY10J4000692', '华为', 'NF8460 M4', '1', '6', 'A05', '29', '30', '2018-07-13', '2021-07-12', '1', '1', null, '周琦', null, '6.4.1.72', null, null, null, null, '2018.5.24安装', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5397', '生产X86虚拟化 ESX2', '10010001', 'X86服务器', '06L2031', 'IBM', 'X3850 X5', '1', '7', 'A06', '5', '8', '2012-07-30', '2015-09-12', '1', '1', null, '周琦', null, '192.168.230.32', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5398', '生产X86虚拟化 ESX9', '10010001', 'X86服务器', '06BF158', 'IBM', 'X3850 X6', '1', '7', 'A06', '10', '13', '2014-04-30', '2017-06-30', '1', '1', null, '周琦', null, '192.168.230.30', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5399', '生产X86虚拟化 ESX7', '10010001', 'X86服务器', '06BF161', 'IBM', 'X3850 X6', '1', '7', 'A06', '15', '18', '2014-05-08', '2017-07-08', '1', '1', null, '周琦', null, '192.168.230.28', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5400', '生产X86虚拟化 ESX4', '10010001', 'X86服务器', '06H8995', 'IBM', 'X3850 X5', '1', '7', 'A06', '20', '23', '2012-08-25', '2016-10-31', '1', '1', null, '周琦', null, '192.168.230.62', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5401', '灾备X86虚拟化 ESXi2', '10010001', 'X86服务器', '06H8996', 'IBM', 'X3850 X5', '1', '8', 'A07', '4', '7', '2012-06-24', '2015-08-07', '3', '1', null, '周琦', null, '6.104.0.3', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5402', '灾备X86虚拟化 ESXi1', '10010001', 'X86服务器', '06L2032', 'IBM', 'X3850 X5', '1', '8', 'A07', '8', '11', '2012-07-30', '2015-09-12', '3', '1', null, '周琦', null, '6.104.0.2', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5403', '灾备X86虚拟化 esxi3', '10010001', 'X86服务器', '816451316', '浪潮', 'NF8460 M4', '1', '8', 'A07', '13', '16', '2016-08-17', '2019-09-30', '3', '1', null, '周琦', null, '6.104.0.4', null, null, null, null, '192.168.1.102', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5404', '灾备X86虚拟化 esxi4', '10010001', 'X86服务器', '816451313', '浪潮', 'NF8460 M4', '1', '8', 'A07', '19', '22', '2016-08-17', '2019-09-30', '3', '1', null, '周琦', null, '6.104.0.5', null, null, null, null, '192.168.1.103', null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5405', 'VMAX 存储-扩展柜', '10100001', '磁盘阵列', 'CN498700317', 'EMC', 'VMAX 10K', '1', '9', 'A08', '1', '42', '2014-01-01', null, '3', '1', null, '周中秋', null, '192.168.210.207', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5406', 'VMAX 存储-机头', '10100001', '磁盘阵列', 'CN498700317', 'EMC', 'VMAX 10K', '1', '10', 'A09', '1', '42', '2014-01-01', null, '3', '1', null, '周中秋', null, '192.168.210.207', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5407', '灾备国密新平台交易', '10400001', '加密机', 'SJJ121416037', '江南信息', 'SJJ1214G', '1', '11', 'A10', '5', '6', '2016-01-01', null, '3', '1', null, '王德明', null, '6.76.1.1', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5408', '灾备国密新平台交易', '10400001', '加密机', 'SJJ121416075', '江南信息', 'SJJ1214G', '1', '11', 'A10', '8', '9', '2016-01-01', null, '3', '1', null, '王德明', null, '6.76.1.2', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5409', '灾备国密新平台交易', '10400001', '加密机', 'SJJ121416081', '江南信息', 'SJJ1214G', '1', '11', 'A10', '11', '12', '2016-01-01', null, '3', '1', null, '王德明', null, '6.76.1.3', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5410', '灾备国密发卡', '10400001', '加密机', 'SJJ121416078', '江南信息', 'SJJ1214G', '1', '11', 'A10', '14', '15', '2016-01-01', null, '3', '1', null, '王德明', null, '6.76.1.4', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5411', '灾备国密旧平台交易', '10400001', '加密机', 'SHJ090212242', '江南信息', 'SHJ0902', '1', '11', 'A10', '17', '18', '2012-01-01', null, '3', '1', null, '王德明', null, '6.76.1.5', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5412', '灾备国密旧平台交易', '10400001', '加密机', 'SHJ090211258', '江南信息', 'SHJ0902', '1', '11', 'A10', '20', '21', '2011-01-01', null, '3', '1', null, '王德明', null, '6.76.1.6', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5413', '灾备孤岛接入交换机', '10200001', '交换机', null, 'H3C', 'S5560', '1', '12', 'B01', '4', '4', '2016-01-01', null, null, '1', null, '肖申波', null, '172.251.2.7', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5414', '业务接入交换机（电口）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '12', 'B01', '6', '6', null, null, null, '1', null, '肖申波', null, '172.251.2.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5415', '业务接入交换机（全光）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '12', 'B01', '8', '8', null, null, null, '1', null, '肖申波', null, '172.251.2.3', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5416', '开发测试区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '1', '12', 'B01', '12', '12', '2015-01-01', null, null, '1', null, '肖申波', null, '6.96.239.1', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5417', '运管区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '1', '12', 'B01', '14', '14', '2015-01-01', null, null, '1', null, '肖申波', null, '6.105.239.1', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5418', '灾备孤岛接入交换机', '10200001', '交换机', null, 'H3C', 'S5560', '1', '13', 'B02', '4', '4', '2015-01-01', null, null, '1', null, '肖申波', null, '172.251.2.7', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5419', '业务接入交换机（电口）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '13', 'B02', '6', '6', '2015-01-01', null, null, '1', null, '肖申波', null, '172.251.2.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5420', '业务接入交换机（全光）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '13', 'B02', '8', '8', '2015-01-01', null, null, '1', null, '肖申波', null, '172.251.2.3', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5421', '开发测试区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '1', '13', 'B02', '12', '12', '2015-01-01', null, null, '1', null, '肖申波', null, '6.96.239.1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5422', '运管区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '1', '13', 'B02', '14', '14', '2015-01-01', null, null, '1', null, '肖申波', null, '6.105.239.1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5423', '灾备CIF-RAC', '10010010', '小型机', '10-78A4F', 'IBM', 'P570', '1', '15', 'B04', '4', '19', null, null, '3', '1', null, '周中秋', null, '6.104.5.17', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5424', '灾备图形前端&中间RAC', '10010010', '小型机', '2130F8V', 'IBM', 'POWER 750', '1', '15', 'B04', '23', '31', null, null, '3', '1', null, null, null, '6.104.5.22', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5425', '磁带机', '10100050', '磁带机', '94-02350', 'IBM', '7226-1U3', '1', '15', 'B04', '32', '32', null, null, '3', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5426', '灾备HMC控制台', '10010001', 'X86服务器', '21D8CDC', 'IBM', 'X3550', '1', '15', 'B04', '34', '34', null, null, '3', '1', null, null, null, '6.104.5.9', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5427', '磁带机', '10100050', '磁带机', 'YL1520012488', 'IBM', '7214-1U2', '1', '15', 'B04', '36', '36', null, null, '3', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5428', '灾备CIF-RAC', '10010010', '小型机', '10-E71D4', 'IBM', 'P570', '1', '16', 'B05', '4', '19', null, null, '3', '1', null, '周中秋', null, '6.104.5.16', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5429', '灾备图形前端&中间RAC', '10010010', '小型机', '2130F7V', 'IBM', 'POWER 750', '1', '16', 'B05', '23', '31', null, null, '3', '1', null, null, null, '6.104.5.21', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5430', '磁带机', '10100050', '磁带机', '94-02311', 'IBM', '7226-1U3', '1', '16', 'B05', '32', '32', null, null, '3', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5431', '磁带机', '10100050', '磁带机', 'YL1520012021', 'IBM', '7214-1U2', '1', '16', 'B05', '34', '34', null, null, '3', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5432', '灾备核心生产主机（20）', '10010010', '小型机', '06E9835', 'IBM', 'p570', '1', '17', 'B06', '4', '19', null, null, '3', '1', null, '周中秋', null, '6.104.5.20/192.168.1.20', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5433', '磁带机', '10100050', '磁带机', '23A3000', 'IBM', '7214-1U2', '1', '17', 'B06', '20', '20', null, null, '3', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5434', '灾备信贷内管RAC2', '10010010', '小型机', '06-BD8F6', 'IBM', 'P550', '1', '17', 'B06', '23', '26', null, null, '3', '1', null, '周中秋', null, '6.104.5.30', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5435', '灾备服务器', '10010010', '小型机', '06-22F8H', 'IBM', 'P550', '1', '17', 'B06', '28', '31', null, null, '3', '1', null, null, null, '6.104.5.32', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5436', '灾备综合前置（25）', '10010010', '小型机', '06E9845', 'IBM', 'p570', '1', '18', 'B07', '4', '19', null, null, '3', '1', null, '周中秋', null, '6.104.5.25/192.168.1.25', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5437', '磁带机', '10100050', '磁带机', '23A3016', 'IBM', '7214-1U2', '1', '18', 'B07', '20', '20', null, null, '3', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5438', '灾备电子渠道rac', '10010010', '小型机', '845D07V', 'IBM', 'POWER 750', '1', '18', 'B07', '23', '31', null, null, '3', '1', null, '王德明', null, '6.104.5.26', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5439', '磁带机', '10100050', '磁带机', '94-03554', 'IBM', '7226-1U3', '1', '18', 'B07', '32', '32', null, null, '3', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5440', '灾备创新平台', '10010010', '小型机', '06-8F4A6', 'IBM', 'P550', '1', '18', 'B07', '34', '37', null, null, '3', '1', null, '周中秋', null, '6.104.5.236', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5441', '容灾管理平台', '10010001', 'X86服务器', '817220053', '浪潮', 'NF5270M4', '1', '19', 'B08', '5', '6', '2017-03-04', '2020-04-30', '3', '1', null, '周中秋', null, '6.104.5.53', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5442', '灾备二代支付PMTS-改为核心测试用', '10010010', '小型机', '06-8F4B6', 'IBM', 'P550', '1', '19', 'B08', '8', '11', null, null, '3', '1', null, '周中秋', null, '6.104.5.221', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5443', '灾备核心备份机', '10010010', '小型机', '06-BD8E6', 'IBM', 'P550', '1', '19', 'B08', '13', '16', null, null, '3', '1', null, '周中秋', null, '6.104.5.23', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5444', '灾备电子渠道rac', '10010010', '小型机', '845D0AV', 'IBM', 'POWER 750', '1', '19', 'B08', '18', '26', null, null, '3', '1', null, '王德明', null, '6.104.5.27', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5445', '磁带机', '10100050', '磁带机', '94-03488', 'IBM', '磁带机', '1', '19', 'B08', '28', '28', null, null, '3', '1', null, '王德明', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5446', '灾备创新平台', '10010010', '小型机', '06-8F476', 'IBM', 'P550', '1', '19', 'B08', '29', '32', null, null, '3', '1', null, '周中秋', null, '6.104.5.237', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5447', '灾备信贷内管RAC1', '10010010', '小型机', '06-BD976', 'IBM', 'P550', '1', '19', 'B08', '34', '37', null, null, '3', '1', null, '周中秋', null, '6.104.5.31', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5448', '外联区防火墙B', '10200020', '防火墙', null, '迪普', 'FW1000', '1', '22', 'C01', '12', '12', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.106', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5449', '外联区防火墙A', '10200020', '防火墙', null, '迪普', 'FW1000', '1', '22', 'C01', '13', '13', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.105', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5450', '人民银行开发测试VPN', '10200010', '路由器', null, 'CISCO', 'cisco2800', '1', '22', 'C01', '21', '21', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.120.12', null, null, null, null, null, '人民银行开发测试VPN', null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5451', '移动外联区防DOS设备B', '10200030', '安全设备', '13-49-P-034', '绿盟', 'ADS 1200', '1', '22', 'C01', '23', '24', '2013-10-01', null, null, '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5452', '联通外联区防DOS设备B', '10200030', '安全设备', '13-36-P-013', '绿盟', 'ADS 1200', '1', '22', 'C01', '26', '27', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.100', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5453', '电信外联区防DOS设备A', '10200030', '安全设备', '13-36-P-014', '绿盟', 'ADS 1200', '1', '22', 'C01', '28', '29', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.101', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5454', '外联区链路负载B', '10200050', '负载均衡', null, 'Radware', 'LP2008', '1', '22', 'C01', '31', '31', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.102', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5455', '外联区链路负载A', '10200050', '负载均衡', null, 'Radware', 'LP2008', '1', '22', 'C01', '32', '32', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.103', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5456', '外联区交换机B', '10200001', '交换机', null, '华为', 'S5700', '1', '22', 'C01', '33', '33', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.104', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5457', '外联区交换机A', '10200001', '交换机', null, '华为', 'S5700', '1', '22', 'C01', '34', '34', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.104', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5458', '网银汇聚交换机B', '10200001', '交换机', null, '华为', 'S5710', '1', '22', 'C01', '35', '35', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.130', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5459', '网银汇聚交换机A', '10200001', '交换机', null, '华为', 'S5710', '1', '22', 'C01', '36', '36', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.130', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5460', '生产应用区RA服务器B', '10010001', 'X86服务器', '06dppx4', 'IBM', 'X3650 M3', '1', '23', 'C02', '7', '8', '2013-10-01', '2015-09-08', '1', '1', null, '吴君华', null, '192.168.101.112', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5461', '生产应用区RA服务器A', '10010001', 'X86服务器', '06DPPX2', 'IBM', 'X3650 M3', '1', '23', 'C02', '10', '11', '2013-10-01', '2015-09-08', '1', '1', null, '吴君华', null, '192.168.101.111', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5462', 'DMZ区WEB服务器B', '10010001', 'X86服务器', '99V2590', 'IBM', 'X3650 M3', '1', '23', 'C02', '13', '14', '2013-10-01', '2014-11-12', '1', '1', null, '吴君华', null, '192.168.102.102', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5463', 'DMZ区WEB服务器A', '10010001', 'X86服务器', '06BFKA6', 'IBM', 'X3650 M3', '1', '23', 'C02', '16', '17', '2013-10-01', '2015-06-10', '1', '1', null, '吴君华', null, '192.168.102.101', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5464', 'DMZ区入侵检测', '10200030', '安全设备', null, '迪普', 'IPS2000-ME', '1', '23', 'C02', '19', '19', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.115', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5465', 'DMZ区WEB防火墙B', '10200030', '安全设备', null, '迪普', 'WAF 3000', '1', '23', 'C02', '20', '21', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.114', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5466', 'DMZ区WEB防火墙A', '10200030', '安全设备', null, '迪普', 'WAF 3000', '1', '23', 'C02', '22', '23', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.113', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5467', '生产应用区签名服务器B', '10200030', '安全设备', null, '信安世纪', 'Netsign 3300', '1', '23', 'C02', '25', '25', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.123', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5468', '生产应用区签名服务器A', '10200030', '安全设备', null, '信安世纪', 'Netsign 3300', '1', '23', 'C02', '26', '26', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.122', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5469', 'DMZ区入侵防御B', '10200030', '安全设备', null, '迪普', 'IPS2000-GS', '1', '23', 'C02', '28', '28', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.120', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5470', 'DMZ区入侵防御A', '10200030', '安全设备', null, '迪普', 'IPS2000-GS', '1', '23', 'C02', '29', '29', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.119', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5471', 'F5 LTM 3600(DMZ区负载均衡B)', '10200050', '负载均衡', null, 'F5', 'LTM 3600', '1', '23', 'C02', '31', '31', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.111', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5472', 'F5 LTM 3600(DMZ区负载均衡A)', '10200050', '负载均衡', null, 'F5', 'LTM 3600', '1', '23', 'C02', '32', '32', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.110', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5473', '(DMZ区SSL网关B)主', '10200030', '安全设备', null, '信安世纪', 'NSAE 1500', '1', '23', 'C02', '33', '33', '2013-10-01', null, null, '1', null, '吴君华', null, '131.10.6.11', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5474', '(DMZ区SSL网关A)备', '10200030', '安全设备', null, '信安世纪', 'NSAE 1500', '1', '23', 'C02', '34', '34', '2013-10-01', null, null, '1', null, '吴君华', null, '131.10.6.11', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5475', '华为S5700(DMZ区二层交换机B)', '10200001', '交换机', null, '华为', 'S5700', '1', '23', 'C02', '35', '35', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.116', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5476', '华为S5700(DMZ区二层交换机A)', '10200001', '交换机', null, '华为', 'S5700', '1', '23', 'C02', '36', '36', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.116', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5477', '华为S5700(DMZ区三层交换机B)', '10200001', '交换机', null, '华为', 'S5700', '1', '23', 'C02', '37', '37', '2013-10-01', null, null, '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5478', '(DMZ区三层交换机A)', '10200001', '交换机', null, '华为', 'S5700', '1', '23', 'C02', '38', '38', '2013-10-01', null, null, '1', null, '吴君华', null, '192.168.210.112', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5479', '网银生产应用区虚拟化服务C', '10010001', 'X86服务器', '06BF153', 'IBM', 'X3850 X6', '1', '24', 'C03', '2', '5', '2013-10-01', '2017-06-30', '1', '1', null, '周琦', null, ' 192.168.230.69', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5480', '网银生产应用区虚拟化服务B', '10010001', 'X86服务器', '06BF156', 'IBM', 'X3850 X6', '1', '24', 'C03', '7', '10', '2013-10-01', '2017-06-30', '1', '1', null, '周琦', null, ' 192.168.230.68', null, null, null, null, null, null, null, null, null, '0620更换主230.29');
INSERT INTO `machine_infos` VALUES ('5481', '网银生产应用区虚拟化服务A', '10010001', 'X86服务器', 'J33TLGB', 'IBM', 'X3850 X6', '1', '24', 'C03', '12', '15', '2013-10-01', '2021-03-02', '1', '1', null, '周琦', null, ' 192.168.230.67', null, null, null, null, null, null, null, null, null, '0620换新机器');
INSERT INTO `machine_infos` VALUES ('5482', 'DP FW1000-SG-NC防火墙(未加电)', '10200020', '防火墙', null, '迪普', 'FW1000-SG-NC', '1', '24', 'C03', '19', '19', '2013-10-01', null, '1', '5', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5483', 'netpass1000', '10200030', '安全设备', null, '信安世纪', 'Netpass', '1', '24', 'C03', '22', '23', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5484', '生产应用区动态令牌服务器A', '10200030', '安全设备', null, '信安世纪', 'Netpass', '1', '24', 'C03', '24', '25', '2013-10-01', null, '1', '1', null, '吴君华', null, '192.168.210.139', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5485', '生产应用区入侵检测', '10200020', '防火墙', null, '迪普', 'IPS2000-ME', '1', '24', 'C03', '27', '27', '2013-10-01', null, '1', '1', null, '吴君华', null, '192.168.210.136', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5486', '生产应用区防火墙A', '10200020', '防火墙', 'Q1407234736', '天融信', 'NGFW4000', '1', '24', 'C03', '29', '29', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5487', '生产应用区防火墙B', '10200020', '防火墙', 'Q1407234735', '天融信', 'NGFW4000', '1', '24', 'C03', '30', '30', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5488', '生产应用区负载均衡B', '10200050', '负载均衡', null, 'F5', 'LTM 3600', '1', '24', 'C03', '31', '31', '2013-10-01', null, '1', '1', null, '吴君华', null, '192.168.210.131', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5489', '生产应用区负载均衡A', '10200050', '负载均衡', null, 'F5', 'LTM 3600', '1', '24', 'C03', '32', '32', '2013-10-01', null, '1', '1', null, '吴君华', null, '192.168.210.132', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5490', '生产应用区防火墙B', '10200020', '防火墙', '1504946120009340', '山石', 'SG-6000-M6110', '1', '24', 'C03', '33', '33', '2013-10-01', null, '1', '1', null, '吴君华', null, '192.168.210.134', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5491', '生产应用区防火墙A', '10200020', '防火墙', '1504922130015030', '山石', 'SG-6000-M6110', '1', '24', 'C03', '34', '34', '2013-10-01', null, '1', '1', null, '吴君华', null, '192.168.210.133', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5492', '生产应用区交换机B', '10200001', '交换机', null, '华为', 'S5700', '1', '24', 'C03', '35', '35', '2013-10-01', null, '1', '1', null, '吴君华', null, '131.10.6.34', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5493', '生产应用区交换机A', '10200001', '交换机', null, '华为', 'S5700', '1', '24', 'C03', '36', '36', '2013-10-01', null, '1', '1', null, '吴君华', null, '131.10.6.34', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5494', '接入交换机（机柜背面）', '10200001', '交换机', null, 'CISCO', 'SW-C2960S', '1', '24', 'C03', '38', '38', '2013-10-01', null, '1', '1', null, '吴君华', null, '192.168.210.3', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5495', 'DMZ区WEB虚拟化服务器C', '10010001', 'X86服务器', '06BF151', 'IBM', 'X3850 X6', '1', '25', 'C04', '4', '7', '2013-10-01', '2017-06-30', '1', '1', null, '周琦', null, '192.168.230.72', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5496', 'DMZ区WEB虚拟化服务器B', '10010001', 'X86服务器', '06BF159', 'IBM', 'X3850 X6', '1', '25', 'C04', '9', '12', '2013-10-01', '2017-06-30', '1', '1', null, '周琦', null, '192.168.230.71', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5497', 'DMZ区WEB虚拟化服务器A', '10010001', 'X86服务器', '06BF154', 'IBM', 'X3850 X6', '1', '25', 'C04', '14', '17', '2013-10-01', '2017-06-30', '1', '1', null, '周琦', null, '192.168.230.70', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5498', '深信服-备', '10200030', '安全设备', '5074000661', '深信服', 'VPN-H6300', '1', '25', 'C04', '25', '26', null, null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5499', '深信服-主-第三方外联', '10200030', '安全设备', '5074000657', '深信服', 'VPN-H6300', '1', '25', 'C04', '27', '28', null, null, '1', '1', null, '吴君华', null, '131.10.6.82', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5500', '深信服-备', '10200030', '安全设备', '5074000570', '深信服', 'VPN-H6300', '1', '25', 'C04', '30', '31', null, null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5501', '深信服-办公', '10200030', '安全设备', '5074000558', '深信服', 'VPN-H6300', '1', '25', 'C04', '32', '33', null, null, '1', '1', null, '吴君华', null, '192.168.110.62/10.62', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5502', '短信平台服务器', '10010001', 'X86服务器', '06BFHZ5', 'IBM', 'X3650 M3', '1', '26', 'C05', '7', '8', '2013-10-01', '2015-06-10', '1', '1', null, '晏良', null, '192.168.104.31', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5503', '短信平台服务器', '10010001', 'X86服务器', '06BFKA2', 'IBM', 'X3650 M3', '1', '26', 'C05', '10', '11', '2013-10-01', '2015-06-10', '1', '1', null, '晏良', null, '192.168.104.32', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5504', '安全防护短信加密机2', '10010001', 'X86服务器', '91Y40K2', 'DELL', 'POWERedgeR430', '1', '26', 'C05', '13', '13', '2013-10-01', '2020-04-18', '1', '1', null, '张超', null, '192.168.10.110', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5505', '安全防护短信加密机1', '10010001', 'X86服务器', '92050K2', 'DELL', 'POWERedgeR430', '1', '26', 'C05', '15', '15', '2013-10-01', '2020-04-18', '1', '1', null, '张超', null, '192.168.10.109', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5506', '网联接入交换机B', '10200001', '交换机', null, '华为', 'S5720', '1', '26', 'C05', '18', '18', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5507', '网联接入交换机A', '10200001', '交换机', null, '华为', 'S5720', '1', '26', 'C05', '19', '19', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5508', null, '10400001', '加密机', 'B15-240', 'GEMALTO LUNAIS66', 'GEMALTO LUNAIS66', '1', '26', 'C05', '21', '21', '2019-07-01', null, '1', '5', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5509', '绿盟IPS B', '10200020', '防火墙', '1550J0748', '绿盟', 'NIPS NX3 SERIES', '1', '26', 'C05', '25', '26', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5510', '绿盟IPS A', '10200020', '防火墙', '1550J0749', '绿盟', 'NIPS NX3 SERIES', '1', '26', 'C05', '27', '28', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5511', '天融信防火墙B', '10200020', '防火墙', 'Q1411280849', '天融信', 'NGFW4000-UF(TG-51130)', '1', '26', 'C05', '30', '31', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5512', '天融信防火墙A', '10200020', '防火墙', 'Q1411280848', '天融信', 'NGFW4000-UF(TG-51130)', '1', '26', 'C05', '32', '33', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5513', '山石网科防火墙B', '10200020', '防火墙', '1107548140000630', '山石', 'sg-6000 M6860', '1', '26', 'C05', '35', '36', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5514', '山石网科防火墙A', '10200020', '防火墙', '1107548140001030', '山石', 'sg-6000 M6860', '1', '26', 'C05', '37', '38', '2013-10-01', null, '1', '1', null, '吴君华', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5515', 'X86虚拟化（电渠区应用监控）', '10010001', 'X86服务器', '210235A2CRH19A000267', 'H3C', 'R4900 G3', '1', '27', 'C06', '5', '6', '2019-10-15', '2025-01-14', '1', '1', null, null, null, '6.104.1.11', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5516', 'X86虚拟化（电渠区应用监控）', '10010001', 'X86服务器', '210235A2CT619BF00007', 'H3C', 'R4900 G3', '1', '27', 'C06', '8', '9', '2019-11-13', '2025-02-12', '1', '1', null, null, null, '6.104.1.12', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5517', 'X86虚拟化（电渠区应用监控）', '10010001', 'X86服务器', '210235A2CT619BF00006', 'H3C', 'R4900 G3', '1', '27', 'C06', '11', '12', '2019-11-13', '2025-02-12', '1', '1', null, null, null, '6.104.1.13', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5518', '双活PMTS 湘潭1', '10010001', 'X86服务器', '201200A00QH189000999', 'H3C', 'R4900 G3', '1', '28', 'C07', '26', '27', '2019-05-01', '2024-01-01', '1', '1', null, null, null, '6.104.6.28', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5519', '中新创时间同步服务器B', '10010001', 'X86服务器', null, '中新创', 'NTP', '1', '28', 'C07', '36', '36', null, null, '1', '2', null, '肖申波', null, '192.168.1.217', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5520', '中新创时间同步服务器A', '10010001', 'X86服务器', null, '中新创', 'NTP', '1', '28', 'C07', '37', '37', null, null, '1', '2', null, '肖申波', null, '192.168.1.216', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5521', '电渠服务器采集设备', '10200040', '其它网络设备', '19011802FFF4020A', '智卓', 'SmartNCSP ZZ-CL42T8', '1', '29', 'C08', '18', '20', null, null, '1', '1', null, '肖申波', null, '6.104.4.64\n外6.104.4.66/67', null, null, null, null, null, null, null, null, null, 'admin/8888');
INSERT INTO `machine_infos` VALUES ('5522', '智能网络综合服务平台（前置、图形前端）', '10200040', '其它网络设备', null, '智卓', 'SmartNCSP ZZ-CL42T8', '1', '29', 'C08', '26', '28', null, null, '1', '1', null, '肖申波', null, '6.104.4.49/65/68/69', null, null, null, null, null, null, null, null, null, 'admin/8888');
INSERT INTO `machine_infos` VALUES ('5523', '双活PMTS 湘潭2', '10010001', 'X86服务器', '201200A00QH189000998', 'H3C', 'R4900 G3', '1', '30', 'C09', '26', '27', '2019-05-01', '2024-01-01', '1', '1', null, null, null, '6.104.6.29', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5524', '业务接入交换机（电口）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '32', 'D01', '6', '6', null, null, null, '1', null, '肖申波', null, '172.251.2.6', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5525', '业务接入交换机（全光）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '32', 'D01', '8', '8', null, null, null, '1', null, '肖申波', null, '172.251.2.5', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5526', '开发测试区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '1', '32', 'D01', '12', '12', '2015-01-01', null, null, '1', null, '肖申波', null, '6.96.239.2', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5527', '运管区接入交换机', '10200001', '交换机', null, '华为', 'CE5810', '1', '32', 'D01', '14', '14', '2014-12-01', null, null, '1', null, '肖申波', null, '6.105.239.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5528', '业务接入交换机（电口）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '33', 'D02', '6', '6', null, null, null, '1', null, '肖申波', null, '172.251.2.6', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5529', '业务接入交换机（全光）', '10200001', '交换机', null, 'H3C', 'S6800', '1', '33', 'D02', '8', '8', null, null, null, '1', null, '肖申波', null, '172.251.2.5', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5530', '开发测试区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '1', '33', 'D02', '12', '12', '2015-01-01', null, null, '1', null, '肖申波', null, '6.96.239.2', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5531', '运管区接入交换机', '10200001', '交换机', null, '华为', 'CE5810', '1', '33', 'D02', '14', '14', '2014-12-01', null, null, '1', null, '肖申波', null, '6.105.239.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5532', 'NAS存储生产5300', '10100001', '磁盘阵列', 'FCN00142900103', 'EMC', 'NAS5300', '1', '35', 'D04', '2', '34', '2014-01-01', null, null, '1', null, '王德明', null, '192.168.230.120-123', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5533', 'RPA2远程复制', '10100040', '其它存储', 'CK2SY182200125', 'EMC', 'RPA', '1', '35', 'D04', '37', '37', null, null, '3', '1', null, '周中秋', null, '6.104.4.10/192.168.99.2', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5534', 'RPA1远程复制', '10100040', '其它存储', 'CK2SY182200122', 'EMC', 'RPA', '1', '35', 'D04', '38', '38', null, null, '3', '1', null, '周中秋', null, '6.104.4.9/192.168.99.1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5535', 'EMC VPLEX 存储网关', '10100030', '存储网关', 'CKM00133803173', 'EMC', 'EMC VPLEX', '1', '36', 'D05', '4', '28', '2014-01-01', null, null, '1', null, '周中秋', null, '6.104.4.7', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5536', 'VMAX 存储', '10100001', '磁盘阵列', 'CN498700149', 'EMC', 'VMAX 10K', '1', '37', 'D06', '1', '42', '2014-01-01', null, null, '1', null, '周中秋', null, '192.168.210.203', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5537', 'VMAX 存储', '10100001', '磁盘阵列', 'CN498700149', 'EMC', 'VMAX 10K', '1', '38', 'D07', '1', '42', '2014-01-01', null, null, '1', null, '周中秋', null, '192.168.210.203', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5538', '光纤光纤交换机B', '10100010', '存储光交', 'BRCANN1934J00E', 'brocade', 'DCX-4S-B', '1', '39', 'D08', '2', '10', '2014-01-01', null, null, '1', null, '周中秋', null, '6.104.4.1-3', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5539', '光纤光纤交换机A', '10100010', '存储光交', 'BRCANN1911J012', 'brocade', 'DCX-4S-B', '1', '39', 'D08', '14', '22', '2014-01-01', null, null, '1', null, '周中秋', null, '6.104.4.4-6', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5540', 'power虚拟化环境光交A', '10100010', '存储光交', 'BRW2521L07T', '华为', '2248', '1', '39', 'D08', '24', '24', null, null, null, '1', null, '晏良', null, '192.168.210.32', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5541', 'power虚拟化环境光交B', '10100010', '存储光交', 'BRW2525L0CA', '华为', '2248', '1', '39', 'D08', '25', '25', null, null, null, '1', null, '晏良', null, '192.168.210.33', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5542', 'L2汇聚交换机', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '1', 'A01', '6', '11', null, null, null, '1', null, '肖申波', null, '172.251.0.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5543', '开发测试区千兆防火墙1', '10200020', '防火墙', null, '迪普', 'FW1000-GC-N', '2', '1', 'A01', '24', '24', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.126', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5544', '开发测试区汇聚交换机1', '10200001', '交换机', null, 'H3C', 'S6800', '2', '1', 'A01', '26', '26', null, null, null, '1', null, '肖申波', null, '172.251.0.125', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5545', '业务2区汇聚交换机', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '3', 'A02', '6', '11', null, null, null, '1', null, '肖申波', null, '172.251.0.15', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5546', '业务2区万兆防火墙1', '10200020', '防火墙', null, '山石', 'sg-6000 E5560', '2', '3', 'A02', '13', '14', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.17', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5547', '业务1区汇聚交换机', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '3', 'A02', '16', '21', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.11', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5548', '业务1区万兆防火墙1', '10200020', '防火墙', null, '山石', 'sg-6000 E5560', '2', '3', 'A02', '23', '24', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.13', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5549', '运管区汇聚交换机1', '10200001', '交换机', null, 'H3C', 'S6800', '2', '3', 'A02', '26', '26', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.254', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5550', '运管区千兆防火墙1', '10200020', '防火墙', null, '迪普', 'FW1000-GC-N', '2', '3', 'A02', '37', '37', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.51', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5551', '业务2区汇聚交换机', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '4', 'A03', '6', '11', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.15', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5552', '业务2区万兆防火墙1', '10200020', '防火墙', null, '山石', 'sg-6000 E5560', '2', '4', 'A03', '13', '14', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.17', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5553', '业务1区汇聚交换机', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '4', 'A03', '16', '21', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.11', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5554', '业务1区万兆防火墙1', '10200020', '防火墙', null, '山石', 'sg-6000 E5560', '2', '4', 'A03', '23', '24', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.13', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5555', '骨干交换机1', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '5', 'A04', '6', '11', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5556', '管理DNS设备', '10200040', '其它网络设备', '05-1708E-205', 'ZDNS', 'T7100', '2', '5', 'A04', '14', '15', null, null, '1', '1', null, '肖申波', null, '6.127.253.5', null, null, null, null, null, null, null, null, '2020-08-25', '2020/8/25上架');
INSERT INTO `machine_infos` VALUES ('5557', '业务DNS设备', '10200040', '其它网络设备', '05-1707E-1024', 'ZDNS', 'T5100', '2', '5', 'A04', '16', '16', null, null, '1', '1', null, '肖申波', null, '6.127.253.8', null, null, null, null, null, null, null, null, '2020-08-25', '2020/8/25上架');
INSERT INTO `machine_infos` VALUES ('5558', 'DNS集群负载均衡B', '10200050', '负载均衡', 'f5-mgea-mgjh', 'F5', 'BIG-IP 2000 SERIES', '2', '5', 'A04', '26', '26', null, null, '1', '1', null, '肖申波', null, '6.127.253.7', null, null, null, null, null, null, null, null, '2020-08-27', '2020/8/27上架');
INSERT INTO `machine_infos` VALUES ('5559', '带外接入交换机1', '10200001', '交换机', null, 'H3C', 'S6800', '2', '5', 'A04', '13', '13', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.253', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5560', '骨干交换机2', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '6', 'A05', '6', '11', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.2', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5561', '骨干交换区入侵检测系统1', '10200030', '安全设备', null, '绿盟', 'NIDS NX3 N2010A', '2', '6', 'A05', '13', '14', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.3', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5562', '带外接入交换机2', '10200001', '交换机', null, 'H3C', 'S5120S', '2', '6', 'A05', '16', '16', '2019-05-01', null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5563', 'TAP', '10200001', '交换机', null, 'MAIPU', 'my power t5820', '2', '6', 'A05', '18', '18', '2019-05-01', null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5564', 'DNS集群负载均衡A', '10200050', '负载均衡', 'f5-hjqs-lric', 'F5', 'BIG-IP 2000 SERIES', '2', '6', 'A05', '26', '26', null, null, '1', '1', null, '肖申波', null, '6.127.253.6', null, null, null, null, null, null, null, null, '2020-08-27', '2020/8/27上架');
INSERT INTO `machine_infos` VALUES ('5565', 'L2汇聚交换机', '10200001', '交换机', null, 'H3C', 'S12504X', '2', '7', 'A06', '6', '11', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5566', 'VMAX 存储', '10100001', '磁盘阵列', 'CN498700243', 'EMC', 'VMAX 10K', '2', '10', 'A09', '1', '42', '2014-01-01', null, null, '1', null, '肖申波', null, '192.168.210.205', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5567', 'VMAX 存储', '10100001', '磁盘阵列', 'CN498700243', 'EMC', 'VMAX 10K', '2', '11', 'A10', '1', '42', '2014-01-01', null, null, '1', null, '肖申波', null, '192.168.210.205', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5568', '电信/联通波分', '10200040', '其它网络设备', null, '华为', null, '2', '139', 'A11', '1', '42', '2019-05-01', null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5569', '生产外联前置DMZ万兆防火墙1', '10200020', '防火墙', null, '启明星辰', 'USG-FW-12600', '2', '12', 'B01', '17', '18', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.43', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5570', '生产外联前置入侵检测系统1', '10200030', '安全设备', null, '绿盟', 'NIDS NX3 N2010A', '2', '12', 'B01', '19', '20', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.44', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5571', '生产外联前置DMZ汇聚交换机', '10200001', '交换机', null, '华为', 'CE6855', '2', '12', 'B01', '21', '21', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.41', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5572', '生产外联前置DMZ汇聚交换机', '10200001', '交换机', null, '华为', 'CE6855', '2', '12', 'B01', '22', '22', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.41', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5573', 'C类第三方千兆防火墙1', '10200020', '防火墙', null, '天融信', 'TG51130', '2', '12', 'B01', '24', '25', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.73', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5574', 'C类第三方入侵检测系统1', '10200030', '安全设备', null, '绿盟', 'NIDS NX3 N2010A', '2', '12', 'B01', '26', '27', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.75', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5575', 'C类第三方接入交换机', '10200001', '交换机', null, '华为', 'S5720', '2', '12', 'B01', '28', '28', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.77', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5576', 'B类第三方千兆防火墙1', '10200020', '防火墙', null, '启明星辰', 'USG-FW-12600', '2', '12', 'B01', '30', '31', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.83', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5577', 'B类第三方入侵防御系统1', '10200030', '安全设备', null, '启明星辰', 'NGIPS5000', '2', '12', 'B01', '32', '33', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.85', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5578', 'B类第三方接入交换机', '10200001', '交换机', null, '华为', 'S5720', '2', '12', 'B01', '34', '34', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.87', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5579', 'A类第三方接入交换机', '10200001', '交换机', null, '华为', 'S5720', '2', '12', 'B01', '36', '36', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.57', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5580', 'A类第三方防火墙1', '10200020', '防火墙', null, '天融信', 'NGFW4000', '2', '12', 'B01', '37', '37', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.93', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5581', 'A类第三方入侵防御系统1', '10200030', '安全设备', null, '迪普', 'IPS2000-GS', '2', '12', 'B01', '38', '38', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.94', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5582', '未接线', '10200020', '防火墙', null, '迪普', 'FW1000-GC-N', '2', '13', 'B02', '5', '5', '2019-05-01', null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5583', 'D类第三方接入交换机', '10200001', '交换机', null, '华为', 'S5720', '2', '13', 'B02', '16', '16', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.62', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5584', 'D类第三方入侵检测系统1', '10200030', '安全设备', null, '绿盟', 'NIPS NX3 N1600A', '2', '13', 'B02', '17', '18', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.64', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5585', 'D类第三方千兆防火墙1', '10200030', '安全设备', null, '天融信', 'TG51130', '2', '13', 'B02', '19', '20', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.63', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5586', 'D类第三方接入路由器', '10200010', '路由器', null, '华为', 'AR3260', '2', '13', 'B02', '22', '24', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.61', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5587', 'C类第三方接入路由器', '10200010', '路由器', null, '华为', 'AR3260', '2', '13', 'B02', '26', '28', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.79', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5588', 'B类第三方接入路由器', '10200010', '路由器', null, '华为', 'AR3260', '2', '13', 'B02', '30', '32', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.89', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5589', 'A类第三方接入路由器2', '10200010', '路由器', null, '华为', 'AR2200', '2', '13', 'B02', '34', '34', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.60', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5590', 'A类第三方接入路由器1', '10200010', '路由器', null, '华为', 'AR2200', '2', '13', 'B02', '35', '35', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.59', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5591', 'A类第三方接入交换机', '10200001', '交换机', null, '华为', 'S5720', '2', '13', 'B02', '36', '36', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.57', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5592', 'A类第三方防火墙2', '10200020', '防火墙', null, '天融信', 'NGFW4000', '2', '13', 'B02', '37', '37', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.92', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5593', 'A类第三方入侵防御系统2', '10200030', '安全设备', null, '迪普', 'IPS2000-GS', '2', '13', 'B02', '38', '38', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.95', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5594', '环网区路由器2', '10200010', '路由器', null, '华为', 'NE40', '2', '14', 'B03', '4', '8', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.28', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5595', '环网区路由器2', '10200010', '路由器', null, '华为', 'NE40', '2', '14', 'B03', '11', '15', '2019-05-01', null, null, '1', null, '肖申波', null, '172.251.0.27', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5596', '广域网区万兆防火墙2', '10200020', '防火墙', '0903342110004734', '山石', 'sg-6000 X5100', '2', '14', 'B03', '17', '18', null, null, null, '1', null, '肖申波', null, '172.251.0.24', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5597', '广域网区万兆防火墙1', '10200020', '防火墙', '0903330110003225', '山石', 'sg-6000 X5100', '2', '14', 'B03', '23', '24', null, null, null, '1', null, '肖申波', null, '172.251.0.23', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5598', '广域网区下联分行接入路由器1', '10200010', '路由器', null, 'H3C', 'SR8808-X', '2', '15', 'B04', '4', '24', null, null, null, '1', null, '肖申波', null, '172.251.0.25', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5599', '广域网区汇聚交换机', '10200001', '交换机', null, '华为', 'CE12804', '2', '15', 'B04', '27', '37', '2014-12-01', null, null, '1', null, '肖申波', null, '172.251.0.21', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5600', '广域网区下联分行接入路由器1', '10200010', '路由器', null, 'H3C', 'SR8808-X', '2', '16', 'B05', '4', '24', '2014-12-01', null, null, '1', null, '肖申波', null, '172.251.0.26', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5601', '广域网区汇聚交换机', '10200001', '交换机', null, '华为', 'CE12804', '2', '16', 'B05', '27', '37', '2014-12-01', null, null, '1', null, '肖申波', null, '172.251.0.21', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5602', '业务接入交换机（电口）', '10200001', '交换机', null, 'H3C', 'S6800', '2', '22', 'C01', '6', '6', null, null, null, '1', null, '肖申波', null, '172.251.2.2', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5603', '业务接入交换机（电口）', '10200001', '交换机', null, 'H3C', 'S6800', '2', '22', 'C01', '8', '8', null, null, null, '1', null, '肖申波', null, '172.251.2.2', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5604', '业务接入交换机（全光）', '10200001', '交换机', null, 'H3C', 'S6800', '2', '22', 'C01', '10', '10', null, null, null, '1', null, '肖申波', null, '172.251.2.1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5605', '业务接入交换机（全光）', '10200001', '交换机', null, 'H3C', 'S6800', '2', '22', 'C01', '12', '12', null, null, null, '1', null, '肖申波', null, '172.251.2.1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5606', '运管区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '2', '22', 'C01', '14', '14', null, null, null, '1', null, '肖申波', null, '6.105.239.3', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5607', '运管区接入交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '2', '22', 'C01', '16', '16', null, null, null, '1', null, '肖申波', null, '6.105.239.3', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5608', '新电话银行-呼叫中心SBC', '10010001', 'X86服务器', '2102350FEB10J4000017', '华为', 'RH1288 V3', '2', '23', 'C02', '9', '9', '2018-07-23', '2021-07-22', '1', '1', null, '倪智', null, '6.68.1.22', null, null, null, null, null, null, null, null, '2018-05-24', '2018.5.24安装');
INSERT INTO `machine_infos` VALUES ('5609', '新电话银行-排队机', '10600030', '排队机', '2102120577N00J2000569', '华为', 'espace U1981', '2', '23', 'C02', '11', '12', null, null, '1', '1', null, '倪智', null, '6.68.1.21  6.104.7.30', null, null, null, null, null, null, null, null, '2018-05-24', '2018.5.24安装');
INSERT INTO `machine_infos` VALUES ('5610', 'IVR语音自动应答（27）电话银行', '10010001', 'X86服务器', 'CNG913S2JN', 'HP', 'DL380 G5', '2', '23', 'C02', '17', '18', '2009-01-25', '2012-12-23', '1', '1', null, '周琦', null, '192.168.110.27', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5611', 'IBM 储存', '10100001', '磁盘阵列', 'SX21101330', 'IBM', 'DS3512', '2', '23', 'C02', '20', '21', null, null, null, '1', null, '晏良', null, 'IVR语音用110.27', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5612', '湘潭特色前置', '10010010', '小型机', '06750D4', 'IBM', 'P550', '2', '24', 'C03', '18', '21', null, null, '1', '1', null, '周中秋', null, '192.168.1.101', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5613', '生产HMC', '10010001', 'X86服务器', '069696B', 'IBM', 'X3550', '2', '24', 'C03', '23', '23', null, null, '1', '1', null, null, null, '6.104.5.10', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5614', '分行网点前置B', '10010010', '小型机', '06-EAFC5', 'IBM', 'P550', '2', '25', 'C04', '4', '7', null, null, '1', '1', null, '周中秋', null, '192.168.1.29', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5615', '分行网点前置A', '10010010', '小型机', '06-EAF75', 'IBM', 'P550', '2', '25', 'C04', '9', '12', null, null, '1', '1', null, '周中秋', null, '192.168.1.28', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5616', '湘潭网点前置', '10010010', '小型机', '06-75084', 'IBM', '550', '2', '25', 'C04', '14', '17', null, null, '1', '1', null, '周中秋', null, '192.168.1.115', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5617', '新财务系统服务器 +U key', '10010001', 'X86服务器', 'CNG013S1J0', 'HP', 'DL380 G6', '2', '25', 'C04', '21', '22', '2009-12-25', '2013-01-23', '1', '1', null, '周琦', null, '192.168.130.1', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5618', 'swift内部交换机', '10200001', '交换机', null, 'H3C', '3600', '2', '25', 'C04', '23', '23', null, null, '1', '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5619', 'Juniper SSG5 VPN A', '10200020', '防火墙', null, 'Juniper', 'SSG5', '2', '25', 'C04', '25', '25', '2019-05-01', null, '1', '1', null, '肖申波', null, null, null, null, null, null, null, 'swift防火墙', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5620', 'Juniper SSG5 VPN B', '10200020', '防火墙', null, 'Juniper', 'SSG5', '2', '25', 'C04', '26', '26', '2019-05-01', null, '1', '1', null, '肖申波', null, null, null, null, null, null, null, 'swift防火墙', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5621', 'swift服务器（备）+U key 防火墙', '10010001', 'X86服务器', '06BFKA0', 'IBM', 'X3650 M3', '2', '25', 'C04', '30', '31', '2019-05-01', '2015-06-10', '1', '3', null, '周琦', null, '192.168.1.69', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5622', 'swift服务器（主）+U key', '10010001', 'X86服务器', '06ECNZ7', 'IBM', 'X3650 M3', '2', '25', 'C04', '33', '34', '2019-05-01', '2015-09-09', '1', '3', null, '周琦', null, '192.168.1.70', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5623', '动环串口设备', '10300030', '动环监控', null, '动环串口设备', '动环串口设备', '2', '26', 'C05', '1', '1', '2019-05-01', null, '1', '1', null, '肖申波', null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5624', 'XBROTHER INP-1430', '10300030', '动环监控', null, 'XBROTHER', 'INP-1430', '2', '26', 'C05', '4', '4', '2019-05-01', null, '1', '1', null, '肖申波', null, '192.168.1.140', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5625', 'XBROTHER', '10300030', '动环监控', null, 'XBROTHER', null, '2', '26', 'C05', '5', '6', '2019-05-01', null, '1', '1', null, '肖申波', null, '192.168.1.150', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5626', '动环串口设备', '10300030', '动环监控', null, '康耐得', 'C2000 N380', '2', '26', 'C05', '8', '8', '2019-05-01', null, '1', '1', null, '肖申波', null, '192.168.1.149', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5627', '动环监控服务器', '10010001', 'X86服务器', 'CNGB43S3GJ', 'HP', 'DL380 G5', '2', '26', 'C05', '10', '11', '2019-05-01', '2012-12-23', '1', '1', null, '肖申波', null, '192.168.1.7', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5628', '老IT监控服务器', '10010001', 'X86服务器', '99V2589', 'IBM', 'X3650 M3', '2', '26', 'C05', '15', '16', '2019-05-01', '2014-11-13', '1', '1', null, '周琦', '杨武灯', '192.168.210.220', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5629', '老IT监控服务器', '10010001', 'X86服务器', '99A9339', 'IBM', 'X3650 M3', '2', '26', 'C05', '18', '19', '2019-05-01', '2013-07-14', '1', '1', null, '周琦', '杨武灯', '192.168.210.219', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5630', '老IT监控服务器', '10010001', 'X86服务器', '06DPPV7', 'IBM', 'X3650 M3', '2', '26', 'C05', '21', '22', '2019-05-01', '2015-09-08', '1', '1', null, '周琦', '杨武灯', '192.168.210.218', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5631', '科来网络回溯分析系统', '10200030', '安全设备', 'PHCS2306SX201905300004', '科来', 'CS2306SX-HR', '2', '26', 'C05', '25', '26', '2019-05-01', null, '1', '1', null, '肖申波', null, '6.104.7.31', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5632', '基础数据平台ETL', '10010010', '小型机', '06EADE5', 'IBM', '520', '2', '27', 'C06', '5', '8', null, null, '1', '1', null, '周中秋', '兰明辉', '192.168.1.178\n172.28.4.110', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5633', '基础数据平台存储', '10100001', '磁盘阵列', '78K0RNB', 'IBM', '5020', '2', '27', 'C06', '10', '12', null, null, '1', '1', null, '晏良', null, '192.168.128.101/102', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5634', '视频会议MCU', '10200040', '其它网络设备', '2102120143P0B600031', '华为', 'ViewPoint 8650', '2', '27', 'C06', '14', '18', '2019-05-01', null, '1', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5635', '北京外汇管理局防火墙', '10200020', '防火墙', null, '天融信', 'NGFW4000', '2', '27', 'C06', '19', '19', '2019-05-01', null, '1', '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5636', '网御网闸', '10200030', '安全设备', null, '网御', '网御3000', '2', '27', 'C06', '21', '22', '2019-05-01', null, '1', '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5637', '外网防火墙', '10200020', '防火墙', null, '深信服', 'M5100-AC', '3', '7', 'A06', '4', '4', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, '外网防火墙', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5638', '外网DMZ交换机', '10200001', '交换机', null, 'H3C', 'S5120S', '3', '7', 'A06', '6', '6', '2015-01-01', null, null, '1', null, '肖申波', null, '10.8.8.251', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5639', '外网接入交换机', '10200001', '交换机', null, 'cisco', 'SW-C2960S', '3', '7', 'A06', '8', '8', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5640', '堡垒机', '10200030', '安全设备', null, '奇治', 'SH200', '3', '7', 'A06', '12', '12', null, null, null, '2', null, '肖申波', null, '192.168.1.146', null, null, null, null, null, '堡垒机备', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5641', '堡垒机', '10200030', '安全设备', null, '奇治', 'SH200', '3', '7', 'A06', '14', '14', null, null, null, '2', null, '肖申波', null, '192.168.1.145', null, null, null, null, null, '堡垒机主', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5642', '移动PTN1900电源中兴ZXDU58', '10600040', '运营商设备', null, '中兴', 'ZXDU58', '3', '7', 'A06', '16', '18', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5643', '移动PTN1900运营商设备', '10600040', '运营商设备', null, '中兴', 'PTN1900', '3', '7', 'A06', '21', '25', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5644', null, '10200010', '路由器', null, 'Cisco', 'CISCO2911/K9', '3', '7', 'A06', '35', '36', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, '无线3G', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5645', '安全网关', '10200030', '安全设备', null, 'JN', 'JN-SJW08S', '3', '7', 'A06', '38', '39', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, '安全网关', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5646', '安全网关', '10200030', '安全设备', null, 'JN', 'JN-SJW08S', '3', '7', 'A06', '40', '41', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, '安全网关', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5647', '联通传输设备', '10600040', '运营商设备', null, '华为', 'OPT3500', '3', '8', 'A07', '18', '33', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5648', '联通外网HUB+光猫', '10200040', '其它网络设备', null, '运营商设备', '联通外网HUB', '3', '9', 'A08', '1', '1', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5649', '电信传输设备', '10600040', '运营商设备', null, '华为', 'OPT2500', '3', '9', 'A08', '25', '37', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5650', 'GP验证2/sdw2.test', '10010001', 'X86服务器', '06BKEM4', 'IBM', 'X3650 M4', '4', '128', 'KF01', '10', '11', '2012-04-29', '2015-06-12', '4', '1', null, null, '兰明辉', '192.168.120.113', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5651', 'GP验证1/sdw3.test', '10010001', 'X86服务器', '06BKEM6', 'IBM', 'X3650 M4', '4', '128', 'KF01', '13', '14', '2012-04-29', '2015-06-12', '4', '1', null, null, '兰明辉', '192.168.120.112', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5652', '虚拟化桌面VDI8', '10010001', 'X86服务器', '817274244', '浪潮', 'NF5270M4', '4', '128', 'KF01', '16', '17', '2017-05-24', '2020-06-30', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5653', '金融监测', '10010001', 'X86服务器', 'CNG536S2YH', 'HP', 'DL380', '4', '128', 'KF01', '20', '21', '2005-09-16', '2008-10-15', '4', '3', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5654', '虚拟化桌面VDIMG02', '10010001', 'X86服务器', '815127616', '浪潮', 'NF5270M4', '4', '128', 'KF01', '23', '24', '2015-09-25', '2018-10-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5655', '虚拟化桌面VDIMG01', '10010001', 'X86服务器', '815127615', '浪潮', 'NF5270M4', '4', '128', 'KF01', '26', '27', '2015-09-28', '2018-10-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5656', '开发虚拟化桌面存储', '10100001', '磁盘阵列', 'CKM00144900988', 'EMC', 'EMC xtremid', '4', '128', 'KF01', '29', '35', null, null, null, '1', null, '向宇', '向宇', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5657', '云平台虚拟桌面使用', '10200001', '交换机', '210235A1LTH158000016', 'H3C', 'S5130S', '4', '128', 'KF01', '38', '38', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, '云平台虚拟桌面使用', null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5658', '云平台虚拟桌面使用', '10200001', '交换机', '210235A1LTH158000068', 'H3C', 'S5130S', '4', '128', 'KF01', '40', '40', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, '云平台虚拟桌面使用', null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5659', '中间业务编译环境', '10600020', '其它设备', null, 'lenovo', null, '4', '129', 'KF02', '1', '5', null, null, '4', '1', null, null, null, '192.168.120.53', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5660', '云平台测试240', '10010001', 'X86服务器', '816370384', '浪潮', 'NF5280M4', '4', '129', 'KF02', '7', '8', '2016-03-11', '2019-04-30', '4', '3', null, null, null, '192.168.230.240', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5661', '云平台测试245', '10010001', 'X86服务器', '816370381', '浪潮', 'NF5280M4', '4', '129', 'KF02', '10', '11', '2016-03-11', '2019-04-30', '4', '3', null, null, null, '192.168.230.245', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5662', '云平台测试244', '10010001', 'X86服务器', '816370385', '浪潮', 'NF5280M4', '4', '129', 'KF02', '13', '14', '2016-03-11', '2019-04-30', '4', '1', null, null, null, '192.168.230.244', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5663', '云平台测试243', '10010001', 'X86服务器', '816370386', '浪潮', 'NF5280M4', '4', '129', 'KF02', '16', '17', '2016-03-11', '2019-04-30', '4', '1', null, null, null, '192.168.230.243', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5664', '云平台测试242', '10010001', 'X86服务器', '816370383', '浪潮', 'NF5280M4', '4', '129', 'KF02', '19', '20', '2016-03-11', '2019-04-30', '4', '1', null, null, null, '192.168.230.242', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5665', '云平台测试241', '10010001', 'X86服务器', '816370382', '浪潮', 'NF5280M4', '4', '129', 'KF02', '22', '23', '2016-03-11', '2019-04-30', '4', '1', null, null, null, '192.168.230.241', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5666', '虚拟化桌面VDI11', '10010001', 'X86服务器', '817274245', '浪潮', 'NF5270M4', '4', '129', 'KF02', '25', '26', '2017-05-24', '2020-06-30', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5667', '虚拟化桌面VDI10', '10010001', 'X86服务器', '817274243', '浪潮', 'NF5270M4', '4', '129', 'KF02', '30', '31', '2017-05-24', '2020-06-30', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5668', '虚拟化桌面VDI9', '10010001', 'X86服务器', '817274246', '浪潮', 'NF5270M4', '4', '129', 'KF02', '33', '34', '2017-05-24', '2020-06-30', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5669', '开发测试华为存储', '10100001', '磁盘阵列', '2102350BSJ10FA000032', '华为', 'OceanStor 5500v3', '4', '130', 'KF03', '1', '6', '2016-02-06', '2021-02-05', '4', '1', null, '晏良', null, '192.168.230.91', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5670', '存储光纤交换机', '10100010', '存储光交', null, 'EMC', 'DS-300B', '4', '130', 'KF03', '8', '8', null, null, '4', '3', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5671', '链路负载', '10200050', '负载均衡', '31403128', 'Radware', 'ALTEON5224', '4', '130', 'KF03', '10', '11', null, null, '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5672', '中金国信', '10400010', '数字签名', 'E5GGPE02003012', '中金国信', null, '4', '130', 'KF03', '12', '13', null, null, '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5673', 'SJJ121416082', '10400001', '加密机', 'SJJ121416082', '江南信息', 'SJJ1214', '4', '130', 'KF03', '15', '16', '2016-01-01', null, '4', '1', null, null, null, '192.168.19.8', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5674', 'SJJ121416083', '10400001', '加密机', 'SJJ121416083', '江南信息', 'SJJ1214', '4', '130', 'KF03', '18', '19', '2016-01-01', null, '4', '1', null, null, null, '192.168.19.7', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5675', 'SJJ121416142', '10400001', '加密机', 'SJJ121416142', '江南信息', 'SJJ1214', '4', '130', 'KF03', '20', '21', '2016-01-01', null, '4', '1', null, null, null, '192.168.19.9', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5676', 'ODS服务器绩效考核', '10010001', 'X86服务器', '99V5373', 'IBM', 'X3650 M3', '4', '130', 'KF03', '25', '26', '2011-10-23', '2014-12-06', '4', '1', null, null, null, '192.168.120.45', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5677', '文档服务器', '10010001', 'X86服务器', '99A2727', 'IBM', 'X3250M2', '4', '130', 'KF03', '27', '27', null, null, null, '3', null, null, null, '192.168.110.41', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5678', '吉大正元数字签名', '10400001', '加密机', null, '吉大正元', null, '4', '130', 'KF03', '34', '36', null, null, null, '1', null, null, null, '192.168.19.10', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5679', 'XTZH-8FKFJF-KFJR-S5120-SW03-02', '10200001', '交换机', null, 'H3C', 'S5120S-28P-EI', '4', '130', 'KF03', '37', '37', '2015-01-01', null, null, '1', null, '肖申波', null, '192.168.19.247', null, null, null, null, null, '同城灾备开发接入交换机', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5680', 'XTZH-8FKFJF-GLJR-S5120-SW03-01', '10200001', '交换机', null, 'H3C', 'S5120S-28P-EI', '4', '130', 'KF03', '39', '39', '2015-01-01', null, null, '1', null, '肖申波', null, '192.168.230.249', null, null, null, null, null, '同城灾备管理接入交换机', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5681', '湘潭分行趋势备机', '10600020', '其它设备', null, 'PC机', null, '4', '131', 'KF04', '1', '9', null, null, '4', '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5682', '湘潭分行开发PC', '10600020', '其它设备', null, 'HP', 'PC机', '4', '131', 'KF04', '10', '16', null, null, '4', '1', null, null, null, '192.168.1.131', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5683', '湘潭分行内网安全服务器', '10010001', 'X86服务器', 'CNG002S16C', 'Hp', 'DL380 G6', '4', '131', 'KF04', '17', '18', '2009-12-25', '2013-01-23', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5684', '分行开发中转机', '10010001', 'X86服务器', 'CNG606S11W', 'HP', 'DL380 G4', '4', '131', 'KF04', '33', '34', '2006-02-13', '2009-03-14', '4', '1', null, null, null, '192.168.120.99', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5685', '趋势杀毒内网', '10600020', '其它设备', 'CNG9500J8G', 'HP', 'PC机', '4', '132', 'KF05', '1', '9', null, null, '4', '1', null, null, null, '169.20.208.106', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5686', '湘潭分行TIPS备机', '10600020', '其它设备', 'CNG9220585', 'HP', 'PC机', '4', '132', 'KF05', '1', '9', null, null, '4', '1', null, null, null, '192.168.110.4/192.168.1.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5687', '分行影像缓存服务器', '10010001', 'X86服务器', '06DKNF9', 'IBM', 'X3650 M3', '4', '132', 'KF05', '25', '26', '2012-09-03', '2015-09-02', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5688', 'SSL安全网关', '10200030', '安全设备', null, '信安世纪', 'NSAE 1500', '4', '132', 'KF05', '37', '38', null, null, null, '1', null, null, null, '192.168.120.200', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5689', '网银签名验签服务器', '10200030', '安全设备', null, '信安世纪', 'NSAE 1500', '4', '132', 'KF05', '40', '40', null, null, null, '1', null, null, null, '192.168.120.203', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5690', '开发虚拟化桌面存储', '10100001', '磁盘阵列', 'CKM00153700966', 'EMC', 'EMC xtremid', '4', '133', 'KF06', '2', '9', null, null, null, '1', null, '向宇', '向宇', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5691', '虚拟桌面光纤交换机', '10100010', '存储光交', 'BRCALJ1908L078', 'EMC', 'DS-300B', '4', '133', 'KF06', '11', '11', null, null, null, '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5692', '虚拟桌面光纤交换机', '10100010', '存储光交', 'BRCALJ1908L08W', 'EMC', 'DS-300B', '4', '133', 'KF06', '13', '13', null, null, null, '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5693', '虚拟化桌面VDI1', '10010001', 'X86服务器', '815127619', '浪潮', 'NF5270M4', '4', '133', 'KF06', '15', '16', '2015-09-25', '2018-10-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5694', '虚拟化桌面VDI2', '10010001', 'X86服务器', '815127617', '浪潮', 'NF5270M4', '4', '133', 'KF06', '20', '21', '2015-09-28', '2018-10-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5695', '虚拟化桌面VDI3', '10010001', 'X86服务器', '815127618', '浪潮', 'NF5270M4', '4', '133', 'KF06', '23', '24', '2015-09-26', '2018-10-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5696', '虚拟化桌面VDI4', '10010001', 'X86服务器', '815155438', '浪潮', 'NF5270M4', '4', '133', 'KF06', '26', '27', '2015-11-25', '2018-12-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5697', '虚拟化桌面VDI5', '10010001', 'X86服务器', '815155436', '浪潮', 'NF5270M4', '4', '133', 'KF06', '29', '30', '2015-11-25', '2018-12-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5698', '虚拟化桌面VDI6', '10010001', 'X86服务器', '815155437', '浪潮', 'NF5270M4', '4', '133', 'KF06', '34', '35', '2015-11-25', '2018-12-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5699', '虚拟化桌面VDI7', '10010001', 'X86服务器', '815155439', '浪潮', 'NF5270M4', '4', '133', 'KF06', '37', '38', '2015-11-25', '2018-12-31', '4', '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5700', '开发迪普WAF防火墙', '10200020', '防火墙', null, '迪普', null, '4', '134', 'KF07', '22', '22', null, null, '4', '4', null, '肖申波', null, null, null, null, null, null, null, null, '1', null, '2020-08-31', '2020年8、31日下架厂商拿走');
INSERT INTO `machine_infos` VALUES ('5701', 'XTZH-8FKFJF-KFJR-C2960-SW7-03', '10200001', '交换机', 'FOC1612W4QW', 'Cisco', 'WS-C2960S-48TS-L', '4', '134', 'KF07', '29', '29', null, null, null, '1', null, '肖申波', null, '192.168.19.248', null, null, null, null, null, '同城灾备开发接入交换机', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5702', 'HNXTZH-8FKFJF-SCJR-C2960-SW7-02', '10200001', '交换机', 'FOC1612W4PM', 'Cisco', 'WS-C2960S-48TS-L', '4', '134', 'KF07', '33', '33', null, null, null, '1', null, '肖申波', null, '192.168.10.14', null, null, null, null, null, '同城灾备生产接入交换机', '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5703', '列头柜接入', '10200001', '交换机', null, 'Cisco', 'WS-C2960S-48TS-L', '4', '134', 'KF07', '37', '37', null, null, null, '1', null, '肖申波', null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5704', '支付系统汇票密押机测试', '10400001', '加密机', null, '信雅达', null, '4', '135', 'KF08', '7', '8', null, null, '4', '1', null, '周琦', null, '192.168.120.239', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5705', '开发生产脱敏机', '10010010', '小型机', '06EAE05', 'IBM', '520', '4', '135', 'KF08', '10', '13', null, null, '4', '1', null, '兰明辉', null, '192.168.120.0/24', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5706', '多媒体信息发布系统', '10010001', 'X86服务器', 'O6DPPW0', 'IBM', 'X3650 M3', '4', '135', 'KF08', '16', '17', '2010-07-26', '2013-07-25', '1', '1', null, null, null, '192.168.110.40', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5707', '支付密码验证机', '10010001', 'X86服务器', '06FWWRW', 'IBM', 'X3650M5 新机', '4', '135', 'KF08', '20', '21', '2015-06-13', '2019-03-13', '4', '1', null, null, null, '192.168.19.4', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5708', '开发SVN服务器', '10010001', 'X86服务器', 'CNG952S396', 'HP', 'DL380 G6', '4', '135', 'KF08', '23', '24', '2009-12-25', '2013-01-23', '4', '1', null, null, null, '192.168.120.199', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5709', '稽核用', '10010001', 'X86服务器', '06ECNZ8', 'IBM', 'X3650 M3', '4', '135', 'KF08', '26', '27', '2012-07-27', '2015-09-09', '1', '1', null, null, null, '192.168.110.214', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5710', '开发江南科友加密机', '10400001', '加密机', 'SHJ090210107', '江南信息', 'SHJ0902', '4', '135', 'KF08', '30', '31', '2010-01-01', null, '4', '1', null, null, null, '192.168.120.150', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5711', '开发江南科友加密机', '10400001', '加密机', 'SHJ090212066', '江南信息', 'SHJ0902', '4', '135', 'KF08', '33', '34', '2012-01-01', null, '4', '1', null, null, null, '192.168.120.16', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5712', '供118、120、121与5020存储用', '10100010', '存储光交', null, 'emc', 'ds-300', '4', '135', 'KF08', '38', '38', null, null, null, '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5713', '供118、120、121与5020存储用', '10100010', '存储光交', null, 'brocade', '300B', '4', '135', 'KF08', '39', '39', null, null, null, '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5714', '扩展柜', '10100001', '磁盘阵列', '131928Z', 'IBM', 'DS4800', '4', '136', 'KF09', '1', '3', null, null, null, '3', null, '晏良', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5715', '机头', '10100001', '磁盘阵列', '13A0910', 'IBM', '1815-B2A', '4', '136', 'KF09', '5', '8', null, null, null, '3', null, '晏良', null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5716', '版本机', '10010010', '小型机', '06-922OH', 'IBM', 'SYSTEM P5', '4', '136', 'KF09', '10', '13', null, null, '4', '1', null, null, null, '192.168.120.121', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5717', '3', '10100001', '磁盘阵列', '78K0RNA', 'IBM', 'DS5020', '4', '136', 'KF09', '15', '17', null, null, '4', '3', null, '晏良', null, '无网线，光纤', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5718', '开发主机', '10010010', '小型机', '06-09CBH', 'IBM', 'SYSTEM P5', '4', '136', 'KF09', '20', '23', null, null, '4', '1', null, null, null, '192.168.120.120', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5719', 'HMC控制台', '10010001', 'X86服务器', '06-1894B', 'IBM', 'SYSTEM X3550', '4', '136', 'KF09', '25', '25', null, null, '4', '1', null, null, null, null, null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5720', null, '10010001', 'X86服务器', 'CNG526S004', 'HP', 'DL380', '4', '136', 'KF09', '30', '31', '2005-12-25', '2009-01-23', null, '3', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5721', '不能登录', '10010001', 'X86服务器', 'CNG528S00L', 'HP', 'DL380', '4', '136', 'KF09', '32', '33', '2005-12-25', '2009-01-23', null, '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5722', '供118、120、121用', '10100001', '磁盘阵列', '78K1870', 'IBM', 'DS5020', '4', '136', 'KF09', '34', '36', null, null, null, '1', null, '晏良', null, '1:192.168.230.93/94/\n2:192.168.129.101/102', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5723', '开发主机', '10010010', '小型机', '06-EAFB5', 'IBM', 'P550', '4', '136', 'KF09', '38', '41', null, null, '4', '1', null, null, null, '192.168.120.118', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5724', '电话银行开发机', '10010001', 'X86服务器', 'XTSC0001', 'IBM', 'xSeries235', '4', '137', 'KF10', '1', '5', null, null, '4', '3', null, null, null, null, null, null, null, null, null, null, null, null, null, '接显示器无显示');
INSERT INTO `machine_infos` VALUES ('5725', '验证', '10010010', '小型机', '06EADF5', 'IBM', 'P520', '4', '137', 'KF10', '10', '13', null, null, '4', '1', null, null, null, '192.168.120.10', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5726', '验证环境GP', '10010001', 'X86服务器', '99V5370', 'IBM', 'X3650 M3', '4', '137', 'KF10', '15', '16', '2011-10-23', '2014-12-06', '4', '1', null, null, null, '192.168.120.13', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5727', '验证环境', '10010001', 'X86服务器', 'CNG717S1DV', 'HP', 'DL580 G4', '4', '137', 'KF10', '25', '28', '2007-04-30', '2010-05-29', '4', '1', null, null, null, '192.168.120.14', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5728', '验证环境', '10010001', 'X86服务器', 'CNG921S2B2', 'hp', 'DL380 G5', '4', '137', 'KF10', '30', '31', '2009-01-25', '2012-12-23', '4', '2', null, null, null, '192.168.120.6', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5729', null, '10010001', 'X86服务器', 'CNG111TGS0', 'HP', 'DL385 G7', '4', '137', 'KF10', '33', '36', null, null, null, '2', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5730', '湘潭分行', '10010010', '小型机', null, 'HP', 'RP4440', '4', '138', 'KF11', '1', '4', null, null, '4', '3', null, null, null, '停机', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5731', '湘潭分行', '10010010', '小型机', null, 'HP', 'RP4440', '4', '138', 'KF11', '4', '8', null, null, '4', '3', null, null, null, '停机', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5732', '湘潭分行用', '10100001', '磁盘阵列', 'SG44110001', 'HP', '2405', '4', '138', 'KF11', '9', '10', null, null, null, '3', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5733', '3个阵列柜湘潭分行用', '10100001', '磁盘阵列', '130166B', 'IBM', 'DS3200', '4', '138', 'KF11', '12', '17', null, null, null, '1', null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5734', '分行事监识别服务器', '10010001', 'X86服务器', '99M9427', 'IBM', 'X3650 M3', '4', '138', 'KF11', '21', '22', '2010-02-10', '2013-03-26', '4', '1', null, null, null, '192.168.110.78', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5735', '分行事监主服务器', '10010001', 'X86服务器', '99M8269', 'IBM', 'X3650 M3', '4', '138', 'KF11', '24', '25', '2011-02-16', '2014-02-25', '4', '1', null, null, null, '192.168.110.79', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5736', '分行事监识别服务器', '10010001', 'X86服务器', '99M7962', 'IBM', 'X3650 M3', '4', '138', 'KF11', '27', '28', '2011-02-17', '2014-02-26', '4', '1', null, null, null, '192.168.110.80', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5737', '分行事监数据库服务器', '10010001', 'X86服务器', '99M8410', 'IBM', 'X3650 M3', '4', '138', 'KF11', '30', '31', '2011-02-16', '2014-02-25', '4', '1', null, null, null, '192.168.110.81', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5738', '分行OA数据库服务器', '10010001', 'X86服务器', '99X8310', 'IBM', 'X3650 M3', '4', '138', 'KF11', '33', '34', null, null, '4', '1', null, null, null, '192.168.110.88', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5739', '分行OA邮件服务器', '10010001', 'X86服务器', '99X8308', 'IBM', 'X3650 M3', '4', '138', 'KF11', '35', '36', null, null, '4', '1', null, null, null, '192.168.110.89', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5740', '分行OAWEB', '10010001', 'X86服务器', 'XTSC0017', 'DELL', '2950', '4', '138', 'KF11', '38', '39', null, null, '4', '1', null, null, null, '192.168.110.88', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `machine_infos` VALUES ('5741', 'k8s-master', '10200030', '安全设备', 'vmware', 'vm', 'linux', '1', '1', 'A01', '5', '5', '2022-02-28', '2022-02-25', null, '1', null, null, null, '192.168.1.70', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5742', 'k8s-node1', '10200030', '安全设备', 'vmware', 'vm', 'linux', '1', '1', 'A01', '6', '6', '2022-02-25', '2022-02-25', null, '1', null, null, null, '192.168.1.61', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5743', 'K8S-node2', '10200030', '安全设备', 'vmware', 'vn', 'linux', '1', '1', 'A01', '7', '7', '2022-02-25', '2022-02-25', null, '1', null, null, null, '192.168.1.62', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5744', 'K8S-NODE3', '10200030', '安全设备', 'vmware', 'vm', 'linux', '1', '1', 'A01', '8', '8', '2022-02-25', '2022-02-25', null, '1', null, null, null, '192.168.1.63', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5748', 'mysql-node1', '10200030', '安全设备', 'vmware', 'vm', 'mysql', '1', '3', 'A02', '5', '5', '2022-02-25', '2022-02-25', null, '1', null, null, null, '192.168.1.51', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `machine_infos` VALUES ('5749', 'mysql-node2', '10200030', '安全设备', 'vmware', 'vm', 'mysql', '1', '3', 'A02', '7', '7', '2022-02-25', '2022-02-25', null, '1', null, null, null, '192.168.1.52', null, null, null, null, null, null, null, null, null, null);

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 AVG_ROW_LENGTH=1 COMMENT='机柜信息';

-- ----------------------------
-- Records of machine_room
-- ----------------------------
INSERT INTO `machine_room` VALUES ('0001', 'ZB-1', '主机房', '');
INSERT INTO `machine_room` VALUES ('0002', 'ZB-2', '网络机房', null);
INSERT INTO `machine_room` VALUES ('0003', 'ZB-3', '分行机房', null);
INSERT INTO `machine_room` VALUES ('0004', 'ZB-4', '开发机房', null);

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
  PRIMARY KEY (`sort_id`,`sort_name`),
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_general_ci;

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

-- ----------------------------
-- Table structure for shelf_manage
-- ----------------------------
DROP TABLE IF EXISTS `shelf_manage`;
CREATE TABLE `shelf_manage` (
  `machine_id` int NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `machine_name` char(255) DEFAULT NULL COMMENT '设备名称',
  `machine_sort_name` char(255) DEFAULT NULL COMMENT '分类名称',
  `machine_sn` char(255) DEFAULT NULL COMMENT '序列号',
  `machine_factory` char(255) DEFAULT NULL COMMENT '设备厂商',
  `model` char(255) DEFAULT NULL COMMENT '型号',
  `machine_roomid` int unsigned NOT NULL COMMENT '机房ID',
  `cabinet_id` int DEFAULT NULL COMMENT '机柜ID',
  `cabinet_name` varchar(255) DEFAULT NULL COMMENT '机房编号',
  `start_position` int DEFAULT NULL COMMENT '开始U位',
  `end_position` int DEFAULT NULL COMMENT '结束U位',
  `machine_admin` char(255) DEFAULT NULL COMMENT '管理员',
  `state` int DEFAULT NULL COMMENT '状态：1上架，2下架',
  `app_admin` char(255) DEFAULT NULL COMMENT '应用管理员',
  `mg_ip` char(255) DEFAULT NULL COMMENT '业务管理IP地址',
  `app_ip1` char(255) DEFAULT NULL COMMENT '业务IP1',
  `machine_use` char(255) DEFAULT NULL COMMENT '用途',
  `operator` char(255) DEFAULT NULL COMMENT '执行人',
  `date` date DEFAULT NULL COMMENT '上下架日期',
  `reason` char(255) DEFAULT NULL COMMENT '原因',
  `comments` char(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`machine_id`),
  KEY `idx_room_cabinet_start_position` (`machine_roomid`,`cabinet_name`,`start_position`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of shelf_manage
-- ----------------------------

-- ----------------------------
-- View structure for machine_list
-- ----------------------------
DROP VIEW IF EXISTS `machine_list`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `machine_list` AS select `machine_infos`.`machine_id` AS `machine_id`,`machine_room`.`room_name` AS `room_name`,`machine_infos`.`cabinet_name` AS `cab_name`,`machine_infos`.`start_position` AS `start_position`,((`machine_infos`.`end_position` - `machine_infos`.`start_position`) + 1) AS `postion_u`,`machine_infos`.`machine_sort_name` AS `machine_sort_name`,`machine_infos`.`machine_factory` AS `machine_factory`,`machine_infos`.`model` AS `model`,`machine_infos`.`machine_sn` AS `machine_sn`,`machine_infos`.`machine_name` AS `machine_name`,`machine_infos`.`mg_ip` AS `mg_ip`,`machine_infos`.`machine_admin` AS `machine_admin` from (`machine_infos` join `machine_room` on((`machine_infos`.`machine_roomid` = `machine_room`.`room_id`))) where (`machine_infos`.`run_state` in (1,2,3,5)) order by `machine_room`.`room_name`,`machine_infos`.`cabinet_name`,`machine_infos`.`start_position` ;

-- ----------------------------
-- View structure for view_check_cmd
-- ----------------------------
DROP VIEW IF EXISTS `view_check_cmd`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `view_check_cmd` AS select `u`.`id` AS `id`,`u`.`hostname` AS `hostname`,`u`.`ip` AS `ip`,`u`.`user` AS `user`,`u`.`password` AS `password`,`c`.`cmd_id` AS `cmd_id`,`c`.`cmd` AS `cmd`,`c`.`cmd_name` AS `cmd_name`,`u`.`machine_id` AS `machine_id` from (`machine_check_user` `u` join `cmd_file` `c` on((`u`.`cmd_id` = `c`.`cmd_id`))) ;

-- ----------------------------
-- View structure for view_downshelf
-- ----------------------------
DROP VIEW IF EXISTS `view_downshelf`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `view_downshelf` AS select `t`.`machine_id` AS `machine_id`,`t`.`machine_name` AS `machine_name`,`m`.`room_name` AS `room_name`,concat(`t`.`cabinet_name`,'_',`t`.`start_position`,'U') AS `postion`,`t`.`machine_sort_name` AS `machine_sort_name`,`t`.`model` AS `model`,`t`.`machine_factory` AS `machine_factory`,`t`.`machine_sn` AS `machine_sn`,`t`.`mg_ip` AS `mg_ip`,`t`.`uninstatll_date` AS `date`,`t`.`comments` AS `comments` from (`machine_infos` `t` join `machine_room` `m` on((`t`.`machine_roomid` = `m`.`room_id`))) where (`t`.`run_state` = 4) order by `t`.`uninstatll_date` desc ;

-- ----------------------------
-- View structure for view_upshelf
-- ----------------------------
DROP VIEW IF EXISTS `view_upshelf`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `view_upshelf` AS select `t`.`machine_name` AS `machine_name`,concat(`m`.`room_name`,'_',`t`.`cabinet_name`,'_',`t`.`start_position`,'U') AS `postion`,`t`.`machine_sort_name` AS `machine_sort_name`,`t`.`model` AS `model`,`t`.`machine_factory` AS `machine_factory`,`t`.`machine_sn` AS `machine_sn`,`t`.`mg_ip` AS `mg_ip`,`t`.`date` AS `date`,`t`.`operator` AS `operator`,`t`.`machine_admin` AS `machine_admin`,`t`.`comments` AS `comments` from (`shelf_manage` `t` join `machine_room` `m` on((`t`.`machine_roomid` = `m`.`room_id`))) where (`t`.`state` = 1) order by `t`.`date` desc ;

-- ----------------------------
-- Event structure for Evnt_addSortid
-- ----------------------------
DROP EVENT IF EXISTS `Evnt_addSortid`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` EVENT `Evnt_addSortid` ON SCHEDULE EVERY 1 MINUTE STARTS '2020-09-15 10:54:35' ON COMPLETION NOT PRESERVE ENABLE COMMENT '补全设备信息表中分类ID及机房编号' DO BEGIN

# 更新并补全设备信息表中分类ID信息
UPDATE machine_infos
 INNER JOIN machine_sort ON machine_infos.machine_sort_name = machine_sort.sort_name
SET machine_infos.machine_sort_id = machine_sort.sort_id;


UPDATE machine_infos
 INNER JOIN cabinet ON machine_infos.cabinet_name = cabinet.cab_num
SET machine_infos.cabinet_id = cabinet.cab_id;

# 更新并补全设备上下架表中分类ID信息

UPDATE shelf_manage
 INNER JOIN cabinet ON shelf_manage.cabinet_name = cabinet.cab_num
SET shelf_manage.cabinet_id = cabinet.cab_id;

END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_update_machineinfo_u`;
DELIMITER ;;
CREATE TRIGGER `Tgr_update_machineinfo_u` AFTER UPDATE ON `machine_infos` FOR EACH ROW update shelf_manage 
	set 
		machine_name=new.machine_name,
		machine_sort_name=new.machine_sort_name,
		machine_sn=new.machine_sn,
		machine_factory=new.machine_factory,
		model=new.model,
		machine_roomid=new.machine_roomid,
		cabinet_name=new.cabinet_name,
		start_position=new.start_position,
		end_position=new.end_position,
		machine_admin=new.machine_admin,
		app_admin=new.app_admin,
		mg_ip=new.mg_ip,
		app_ip1=new.app_ip1,
		machine_use=new.machine_use
	where shelf_manage .machine_id=new.machine_id
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_add_machineinfo_i`;
DELIMITER ;;
CREATE TRIGGER `Tgr_add_machineinfo_i` AFTER INSERT ON `shelf_manage` FOR EACH ROW INSERT INTO machine_infos (
	machine_id,
	machine_name,
	machine_sort_name,
	machine_sn,
	machine_factory,
	model,
	machine_roomid,
	cabinet_name,
	start_position,
	end_position,
	machine_admin,
	app_admin,
	mg_ip,
	app_ip1,
	machine_use,
	install_date
)
VALUES
	(
		new.machine_id,
		new.machine_name,
		new.machine_sort_name,
		new.machine_sn,
		new.machine_factory,
		new.model,
		new.machine_roomid,
		new.cabinet_name,
		new.start_position,
		new.end_position,
		new.machine_admin,
		new.app_admin,
		new.mg_ip,
		new.app_ip1,
		new.machine_use,
		new.date
	)
;;
DELIMITER ;
