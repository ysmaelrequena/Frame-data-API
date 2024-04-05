-- Create Dtabase for use

CREATE DATABASE fighting_game_api;
USE fighting_game_api;

-- Dropping database for updates if needed
DROP DATABASE fighting_game_api;

	-- Select list for all the tables
    
    SELECT * from characters;
    SELECT * from normals;
    SELECT * from command_normals;
    SELECT * from target_combos;
    SELECT * from throws;
    SELECT * from drive_system;
    SELECT * from special_moves;
    SELECT * from super_arts;
    SELECT * from taunts;
    SELECT * from serenity_stance;
    
    SELECT * from super_arts
	WHERE character_id = 19;

-- Recreate the character table which is the matrix of all

DROP TABLE characters;
    
CREATE TABLE IF NOT EXISTS characters (
id INT AUTO_INCREMENT PRIMARY KEY,
character_name VARCHAR (50)
);

INSERT INTO characters (character_name)
VALUES
('A.K.I'),
('BLANKA'),
('CAMMY'),
('CHUN-LI'),
('DEE-JAY'),
('DHALSIM'),
('ED'),
('E. HONDA'),
('GUILE'),
('J.P'),
('JAMIE'),
('JURI'),
('KEN'),
('KIMBERLY'),
('LILY'),
('LUKE'),
('MANON'),
('MARISA'),
('RASHID'),
('RYU'),
('ZANGIEF');

-- Queries for security and authentication

CREATE TABLE users (
user_id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255),
email VARCHAR(255)
);

DROP TABLE users;

CREATE TABLE user_pass (

FOREIGN KEY (user_id) REFERENCES users(user_id)
)