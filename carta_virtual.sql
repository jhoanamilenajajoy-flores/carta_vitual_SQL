/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 8.0.24 : Database - carta_virtual
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`carta_virtual` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `carta_virtual`;

/*Table structure for table `clientes` */

DROP TABLE IF EXISTS `clientes`;

CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `contrasena` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;

/*Data for the table `clientes` */

insert  into `clientes`(`id`,`nombre`,`email`,`contrasena`) values 
(11,'juan','juanhelypz@hotmail.com','ed08c290d7e22f7bb324b15cbadce35b0b348564fd2d5f95752388d86d71bcca'),
(12,'juan','juanhelypz@hotmail.com','ba83f79d43537a525eb5a38096b56f2fbee05fffdacb6ec9271b0c24b08dce24'),
(13,'juan','juanhelypz@hotmail.com','40e1e27242ceacfea2ed108016bdd95870184000d6142a9afe3be2e909e6c15b'),
(14,'juan','juanhelypz@hotmail.com','090b235e9eb8f197f2dd927937222c570396d971222d9009a9189e2b6cc0a2c1'),
(15,'juan','juanhelypz@hotmail.com','a73bda04b7f95193a2faaf910d1bd8bc5345cd8e9ecbe341800f4bd1fa47d3df'),
(16,'jjose ','juanhelypz@hotmail.com','8cbe71fa51a4fbd329a331117d19b2ff3924ab0ba7e12ec27bee070591e8008f'),
(17,'jose ','juanhelypz@hotmail.com','5cd38f85f66bc64702320d8cb9cb702914e210fc4756e158660976cc9df664c0');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
