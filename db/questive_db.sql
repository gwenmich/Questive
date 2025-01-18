DROP DATABASE IF exists questive;

CREATE DATABASE IF NOT EXISTS questive;
USE questive;

CREATE TABLE suspects (
    suspect_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    age INT NOT NULL,
    hair_colour VARCHAR(20) NOT NULL,
    eye_colour VARCHAR(10) NOT NULL,
    wears_glasses BOOL NOT NULL,
    shirt_colour VARCHAR(20) NOT NULL,
    trouser_colour VARCHAR(20) NOT NULL,
    shoe_colour VARCHAR(20) NOT NULL,
    earring BOOL NOT NULL,
    wears_a_hat BOOL NOT NULL
);


CREATE TABLE high_scores (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    score INT NOT NULL
);


-- list of suspect details
INSERT INTO suspects (name, age, hair_colour, eye_colour, wears_glasses, shirt_colour, trouser_colour, shoe_colour, earring, wears_a_hat)
VALUES
('Al Ibi', 42, 'Red', 'Brown', FALSE, 'Blue', 'White', 'Red', TRUE, TRUE),
('Tom Foolery', 19, 'Brown', 'Brown', TRUE, 'Red', 'White', 'Blue', TRUE, TRUE),
('Mo Tives', 38, 'Blonde', 'Brown', FALSE, 'Blue', 'Black', 'Blue', FALSE, FALSE),
('Bend Da-Rules', 24, 'Brown', 'Brown', TRUE, 'Yellow', 'Brown', 'Red', FALSE, TRUE),
('De Cissed', 29, 'Blonde', 'Blue', TRUE, 'Red', 'Black', 'Blue', FALSE, FALSE),
('Cole Blooded', 31, 'Brown', 'Blue', FALSE, 'Red', 'Black', 'Orange', TRUE, TRUE),
('Ima Goner', 37, 'Red', 'Blue', FALSE, 'Yellow', 'Brown', 'Orange', FALSE, FALSE),
('Barry De-Hatchett', 51, 'Blonde', 'Blue', TRUE, 'Yellow', 'Brown', 'Orange', FALSE, FALSE),
('Faye Tality', 51, 'Red', 'Blue', TRUE, 'Blue', 'White', 'White', FALSE, TRUE),
('Hugh Dunnit', 59, 'Brown', 'Brown', FALSE, 'Yellow', 'Black', 'Red', TRUE, TRUE)
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