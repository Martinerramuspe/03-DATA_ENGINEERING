CREATE DATABASE BINANCE;
USE BINANCE;
DROP DATABASE BINANCE;
-- CREACION TABLAS SIN FOREIGN KEY_____________________________________________________________________________________________________________________________________________ 
CREATE TABLE `tabla` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `time` BIGINT NOT NULL,
  `open` INT NOT NULL,
  `high` INT NOT NULL,
  `low` INT NOT NULL,
  `close` INT NOT NULL,
  `volumen` INT NOT NULL,
  PRIMARY KEY (`Id`));
  
SELECT * FROM tabla;

