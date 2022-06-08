-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: xurpas
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users_customuser`
--

DROP TABLE IF EXISTS `users_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(100) NOT NULL,
  `post_code` varchar(10) NOT NULL,
  `contact_phone_number` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser`
--

LOCK TABLES `users_customuser` WRITE;
/*!40000 ALTER TABLE `users_customuser` DISABLE KEYS */;
INSERT INTO `users_customuser` VALUES (1,'dmiles','Dawn','Hoffman','evansnatasha@example.com','045 Harrington Valley\nDavidview, WV 72624','Perform.','It deal.'),(2,'yochoa','Ethan','Frazier','davisemily@example.org','31112 House Alley Apt. 012\nChandlerport, SC 63393','Believe.','Indeed.'),(3,'fjordan','Scott','Conner','gregorybean@example.com','9192 Harris Light Suite 612\nChasefort, PA 01436','Like.','Time and.'),(4,'adam86','Sarah','Price','bryanethan@example.org','19456 Thompson Villages\nEast Deborah, NM 07968','Base.','Then.'),(5,'angelabrennan','Jordan','Walker','walkermary@example.com','138 Timothy Throughway\nPagefort, WY 60562','Pull.','Three.'),(6,'ortizgregory','Tonya','Williams','austin95@example.com','3488 Marvin Motorway\nJamestown, KY 91283','Some.','Small.'),(7,'willie94','Tony','Cowan','lburke@example.com','130 Misty Road Suite 207\nNorth Julia, MS 61372','Senior.','Plan find.'),(8,'susan17','Travis','Park','gkent@example.net','26595 Alexandra Manors\nKarenstad, ME 24031','Team.','Subject.'),(9,'hunterbrandon','Perry','Lee','christopher78@example.org','4179 Timothy Shoal\nLake Matthewmouth, AL 31866','Treat if.','Account.'),(10,'matthew18','Zachary','Knight','jamie11@example.net','Unit 2233 Box 6410\nDPO AA 32360','In.','Cut.'),(11,'nwilliams','Martin','Lawson','dunnmichaela@example.org','690 Paul Cliff Apt. 914\nZamoraland, CT 67488','Attorney.','Partner.'),(12,'snyderjuan','Wesley','Smith','russellemily@example.org','14095 Swanson Spurs\nLake Curtisland, MN 67112','Station.','Agency.'),(13,'nolananne','Kenneth','Taylor','sweeneynatasha@example.org','76169 Greg Meadow Suite 989\nBrownland, WV 10360','Position.','Take upon.'),(14,'jameswilliams','Jacob','Perez','davidhall@example.net','PSC 8202, Box 6418\nAPO AP 89518','Could.','High.'),(15,'xpugh','Jennifer','Campbell','christopher36@example.org','82224 Herring Bypass\nBaileyland, OK 21194','Age serve.','Strategy.'),(16,'johnnystevenson','Mark','Jones','jpetersen@example.org','601 Padilla Center Apt. 079\nPort Victoria, MS 14451','Me go.','Yourself.'),(17,'keithcarroll','Brian','Lucas','meredithrivera@example.org','PSC 9028, Box 7919\nAPO AP 13740','Develop.','Matter.'),(18,'moraleselizabeth','Kristin','Howard','john24@example.net','2845 Antonio Parkway\nFitzgeraldstad, OH 67782','Thank.','Already.'),(19,'cathyelliott','Katie','Allen','allenrebecca@example.com','8686 Meyers Squares Apt. 057\nEast Jamesberg, NM 25933','On.','Draw.'),(20,'christina87','Beth','Davis','joeldelgado@example.org','862 Ortega Burg Suite 107\nNorth Morgan, NY 77775','Kid.','Amount.');
/*!40000 ALTER TABLE `users_customuser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-08 13:02:39
