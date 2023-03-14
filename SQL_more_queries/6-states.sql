-- A script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT DEFAULT 1 NOT NULL UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL);
