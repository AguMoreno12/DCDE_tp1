#!/bin/bash
PASS="admin"
USER="root"
mysql -u$USER -p$PASS <<MYSQL_SCRIPT
CREATE SCHEMA bdPruebaTp;
USE bdPruebaTp;
CREATE TABLE beacons (  DistanceA DOUBLE NULL,  DistanceB DOUBLE NULL,  DistanceC DOUBLE NULL,  PositionX INT NULL,  PositionY INT NULL,  DateTime DATETIME NOT NULL,  PRIMARY KEY (DateTime));
MYSQL_SCRIPT
