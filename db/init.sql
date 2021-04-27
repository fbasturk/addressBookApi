create database IF NOT EXISTS dockerdb;

CREATE TABLE dockerdb.addressbook (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(45) NOT NULL, address VARCHAR(300) NOT NULL, 
 phone VARCHAR(13) NULL, mobilePhone VARCHAR(13) NULL, email VARCHAR(45) NULL, PRIMARY KEY (id, name));