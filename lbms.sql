-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.48 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             9.5.0.5222
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for signup
CREATE DATABASE IF NOT EXISTS `signup` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `signup`;

-- Dumping structure for table signup.admin_table
CREATE TABLE IF NOT EXISTS `admin_table` (
  `user_name` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `roleid` int(11) NOT NULL,
  PRIMARY KEY (`email`),
  KEY `FK_admin_table_superadmin` (`password`),
  CONSTRAINT `FK_admin_table_superadmin` FOREIGN KEY (`password`) REFERENCES `superadmin` (`password`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table signup.admin_table: ~0 rows (approximately)
/*!40000 ALTER TABLE `admin_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_table` ENABLE KEYS */;

-- Dumping structure for table signup.bookss
CREATE TABLE IF NOT EXISTS `bookss` (
  `book_id` int(100) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(100) NOT NULL,
  `book_author` varchar(100) NOT NULL,
  `book_quantity` int(200) NOT NULL,
  `is_active` tinyint(4) NOT NULL DEFAULT '1',
  `book_image` varchar(50) NOT NULL,
  PRIMARY KEY (`book_id`),
  UNIQUE KEY `book_name` (`book_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table signup.bookss: ~0 rows (approximately)
/*!40000 ALTER TABLE `bookss` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookss` ENABLE KEYS */;

-- Dumping structure for table signup.signup
CREATE TABLE IF NOT EXISTS `signup` (
  `email` varchar(50) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table signup.signup: ~5 rows (approximately)
/*!40000 ALTER TABLE `signup` DISABLE KEYS */;
INSERT INTO `signup` (`email`, `password`, `name`, `city`) VALUES
	('ASC', 'AAA', 'DS', 'SD'),
	('kartikayy000@gmail.com', '123', 'kartikay', 'shimla'),
	('kartikayy00@gmail.com', '123', 'kartikay', 'shimla'),
	('sa', 'sa', 'sdds', 'd'),
	('X', 'Y', 'S', 'E');
/*!40000 ALTER TABLE `signup` ENABLE KEYS */;

-- Dumping structure for table signup.superadmin
CREATE TABLE IF NOT EXISTS `superadmin` (
  `name` varchar(50) NOT NULL,
  `email` varchar(500) NOT NULL,
  `role_id` int(100) NOT NULL,
  `password` varchar(500) NOT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `password` (`password`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table signup.superadmin: ~0 rows (approximately)
/*!40000 ALTER TABLE `superadmin` DISABLE KEYS */;
/*!40000 ALTER TABLE `superadmin` ENABLE KEYS */;

-- Dumping structure for table signup.user_role
CREATE TABLE IF NOT EXISTS `user_role` (
  `Role_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Role_id`),
  UNIQUE KEY `role_name` (`role_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table signup.user_role: ~3 rows (approximately)
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` (`Role_id`, `role_name`) VALUES
	(2, 'admin'),
	(3, 'student'),
	(1, 'superadmin\r\n\r\n');
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;

-- Dumping structure for table signup.user_table
CREATE TABLE IF NOT EXISTS `user_table` (
  `password` varchar(300) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_address` varchar(500) NOT NULL,
  `university_rollno` varchar(30) NOT NULL,
  `mobile_number` bigint(20) NOT NULL,
  `is_active` tinyint(4) NOT NULL,
  `email` varchar(50) NOT NULL,
  `roll_id` int(11) NOT NULL,
  `branch` varchar(50) NOT NULL,
  `is_fine` tinyint(4) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `is_issued` tinyint(4) NOT NULL DEFAULT '0',
  `registered_date` varchar(100) NOT NULL,
  `last_issued` varchar(100) NOT NULL DEFAULT '0',
  `last_login` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `mobile_number` (`mobile_number`),
  UNIQUE KEY `university_rollno` (`university_rollno`),
  KEY `FK_user_table_user_role` (`roll_id`),
  CONSTRAINT `FK_user_table_user_role` FOREIGN KEY (`roll_id`) REFERENCES `user_role` (`Role_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table signup.user_table: ~1 rows (approximately)
/*!40000 ALTER TABLE `user_table` DISABLE KEYS */;
INSERT INTO `user_table` (`password`, `user_name`, `user_address`, `university_rollno`, `mobile_number`, `is_active`, `email`, `roll_id`, `branch`, `is_fine`, `dob`, `is_issued`, `registered_date`, `last_issued`, `last_login`) VALUES
	('123', 'Kseran', 'chandigarh sec 22b  house no. 1804', '650**', 9886895432, 1, 'abc', 1, 'CSE', 100, '30/03/1999', 0, '28-01-2019', '0', '0');
/*!40000 ALTER TABLE `user_table` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
signupadmin_table