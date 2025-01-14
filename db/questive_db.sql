DROP DATABASE IF exists questive;

CREATE DATABASE IF NOT EXISTS questive;
USE questive;

CREATE TABLE suspects (
    suspect_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    age INT NOT NULL,
    hair_colour VARCHAR(20) NOT NULL,
    eye_colour VARCHAR(10) NOT NULL,
    height INT NOT NULL,
    piercing BOOL NOT NULL,
    tattoo BOOL NOT NULL,
    wears_a_hat BOOL NOT NULL,
    occupation VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL
);


CREATE TABLE high_scores (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    score INT NOT NULL
);


-- list of suspect details
INSERT INTO suspects (name, age, hair_colour, eye_colour, height, piercing, tattoo, wears_a_hat, occupation, country)
VALUES
('Aisha', 19, 'Brown', 'Brown', 160, TRUE, TRUE, TRUE, 'Student', 'England'),
('Arianne', 38, 'Blonde', 'Brown', 164, TRUE, TRUE, FALSE, 'Teacher', 'England'),
('Bob', 24, 'Brown', 'Brown', 190, TRUE, FALSE, TRUE, 'Software developer', 'Wales'),
('Carlos', 29, 'Blonde', 'Blue', 165, FALSE, FALSE, FALSE, 'Life Guard', 'Greece'),
('Dave', 31, 'Brown', 'Blue', 178, FALSE, TRUE, TRUE, 'Cyber security', 'Scotland'),
('Emily', 37, 'Black', 'Blue', 166, FALSE, TRUE, FALSE, 'Cyber security', 'France'),
('Fathiah', 42, 'Black', 'Hazel', 183, TRUE, FALSE, TRUE, 'Teacher', 'Scotland'),
('Giovanni', 51, 'Grey', 'Blue', 172, TRUE, FALSE, FALSE, 'Actor', 'Greece'),
('Gwen', 51, 'Black', 'Blue', 172, TRUE, TRUE, TRUE, 'Software developer', 'Greece'),
('Hamed', 59, 'Brown', 'Brown', 180, FALSE, TRUE, FALSE, 'Teacher', 'Wales'),
('Helen', 60, 'Blonde', 'Blue', 175, FALSE, FALSE, TRUE, 'Teacher', 'Greece'),
('Luke', 64, 'Bald', 'Brown', 171, FALSE, FALSE, FALSE, 'Teacher', 'England'),
('Mel', 75, 'Blonde', 'Brown', 182, TRUE, TRUE, TRUE, 'Actor', 'England'),
('Miguel', 80, 'Grey', 'Hazel', 170, TRUE, TRUE, FALSE, 'Student', 'Wales')
;


-- sample of high scores for starting game
INSERT INTO high_scores (score)
VALUES
(8),
(7),
(6),
(5),
(5),
(4),
(3),
(2),
(1),
(0)
;