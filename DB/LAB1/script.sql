CREATE TYPE DERECTION AS ENUM ('up', 'down', 'other', 'not fall');
CREATE TYPE TERRAIN AS ENUM ('plain', 'mountains', 'river', 'desert', 'wasteland', 'other');
CREATE TYPE ENVORONMENT AS ENUM ('well', 'normal', 'aggressive', 'dangerous', 'other');

CREATE TABLE Human (
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL,
 profession TEXT NOT NULL,
 age INT NOT NULL,
);
CREATE TABLE Sensation (
 id SERIAL PRIMARY KEY,
 fall_derection DERECTION NOT NULL,
 emotion TEXT NOT NULL,
 now_time TIME NOT NULL,
 now_date DATE NOT NULL,
 location_id INT REFERENCES Location (id) ON DELETE SET NULL,
 visible_light_id INT REFERENCES Light (id) ON DELETE SET NULL
);
CREATE TABLE Light (
 id SERIAL PRIMARY KEY,
 distance_to_light FLOAT,
 brightness INT NOT NULL
);
CREATE TABLE World (
 id SERIAL PRIMARY KEY,
 name TEXT,
 known BOOLEAN NOT NULL
);
CREATE TABLE Location (
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL,
 terrain TERRAIN NOT NULL,
 environment ENVORONMENT NOT NULL,
 world_id INT REFERENCES World (id) ON DELETE CASCADE,
);
CREATE TABLE Portal (
 id SERIAL PRIMARY KEY,
 width FLOAT NOT NULL,
 arrival_world_id INT REFERENCES World (id) ON DELETE CASCADE,
 departure_world_id INT REFERENCES World (id) ON DELETE CASCADE,
 location_id INT REFERENCES Location (id) ON DELETE SET NULL
);
CREATE TABLE Sensation_to_Human (
 id SERIAL PRIMARY KEY,
 sensation_id INT REFERENCES Sensation (id) ON DELETE CASCADE,
 human_id INT REFERENCES Human (id) ON DELETE CASCADE
);
INSERT INTO World (name, known) VALUES
 ('Japet', TRUE),
 (NULL, FALSE),
 ('Earth', TRUE);
 INSERT INTO Location (name, terrain, environment, world_id) VALUES
 ('Tunnel', 'other', 'normal', 1),
 ('House', 'other', 'good', 3);
 ('unknown plain', 'plain', 'mormal', 2);
INSERT INTO Human (name, profession, age) VALUES
 ('Boymen', 'world traveler', 30),
 ('Roman', 'programmer', 19);
INSERT INTO Light (distance_to_light, brightness) VALUES
 (NULL, 1500),
 (, 369000000),
 (1, 1500),
 (0.5, 1500),
 (0.01, 1500);
INSERT INTO Sensation (fall_derection, emotion, now_time, now_date location_id, visible_light_id) VALUES
 ('not fall', 'unhappy', 7:00:00, 2025-03-11, 2, 2),
 ('down', 'scared', 12:35:00, 1989-01-23, 1, 1),
 ('down', 'scared', 12:35:05, 1989-01-23, 1, 3),
 ('up', 'scared', 12:35:10, 1989-01-23, 1, 4),
 ('up', 'scared', 12:35:15, 1989-01-23, 1, 5),
 ('not fall', 'scared', 12:35:20, 1989-01-23, 3, NULL);
INSERT INTO Portal (width, arrival_world_id, departure_world_id, location_id) VALUES
 (3.5, 2, 1, 1);
INSERT INTO Sensation_to_Human (sensation_id, human_id) VALUES
 (1, 2),
 (2, 1),
 (3, 1),
 (4, 1),
 (5, 1),
 (6, 1);
