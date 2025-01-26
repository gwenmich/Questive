DROP DATABASE IF exists questive;

CREATE DATABASE IF NOT EXISTS questive;
USE questive;

CREATE TABLE suspects (
    suspect_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    hair_colour VARCHAR(20) NOT NULL,
    eye_colour VARCHAR(10) NOT NULL,
    wears_glasses BOOL NOT NULL,
    shirt_colour VARCHAR(20) NOT NULL,
    trouser_colour VARCHAR(20) NOT NULL,
    shoe_colour VARCHAR(20) NOT NULL,
    wears_a_hat BOOL NOT NULL
);


CREATE TABLE high_scores (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    score INT NOT NULL
);


-- list of suspect details
INSERT INTO suspects (name, hair_colour, eye_colour, wears_glasses, shirt_colour, trouser_colour, shoe_colour, wears_a_hat)
VALUES
('Al Ibi', 'Red', 'Brown', FALSE, 'Blue', 'White', 'Red', TRUE),
('Barry De-Hatchett', 'Blonde', 'Blue', TRUE, 'Yellow', 'Brown', 'Orange', FALSE),
('Bend Da-Rules', 'Brown', 'Brown', TRUE, 'Yellow', 'Brown', 'Red', TRUE),
('Cole Blooded', 'Brown', 'Blue', FALSE, 'Red', 'Black', 'Orange', TRUE),
('De Cissed', 'Blonde', 'Blue', TRUE, 'Red', 'Black', 'Blue', FALSE),
('Faye Tality', 'Red', 'Blue', TRUE, 'Blue', 'White', 'White', TRUE),
('Hugh Dunnit', 'Brown', 'Brown', FALSE, 'Yellow', 'Black', 'Red', TRUE),
('Ima Goner', 'Red', 'Blue', FALSE, 'Yellow', 'Brown', 'Orange', FALSE),
('Mo Tives', 'Blonde', 'Brown', FALSE, 'Blue', 'Black', 'Blue', FALSE),
('Tom Foolery', 'Brown', 'Brown', TRUE, 'Red', 'White', 'Blue', TRUE)
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
