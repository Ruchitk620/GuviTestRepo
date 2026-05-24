CREATE DATABASE IMDB;
USE IMDB;


#created Movie table 
CREATE TABLE movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    release_year INT
);

#created Media table 
CREATE TABLE media (
    media_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    media_type VARCHAR(50), -- Image / Video
    url VARCHAR(255),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

#created genres table 
CREATE TABLE genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50)
);

#created Movie_genre table 
CREATE TABLE movie_genre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

#created Users table 
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50)
);

#created Reviews table 
CREATE TABLE reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

#created Artist table
CREATE TABLE artists (
    artist_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

#created Skills table 
CREATE TABLE skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(50)
);
 
 #created artist_skill table 
CREATE TABLE artist_skill (
    artist_id INT,
    skill_id INT,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

#created artist_movie_role table 
CREATE TABLE artist_movie_role (
    artist_id INT,
    movie_id INT,
    role VARCHAR(50),
    PRIMARY KEY (artist_id, movie_id, role),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

INSERT INTO movies (title, release_year) VALUES ('Inception', 2010);

INSERT INTO genres (genre_name) VALUES ('Sci-Fi'), ('Action');

INSERT INTO movie_genre VALUES (1,1), (1,2);

INSERT INTO users (username) VALUES ('Ruchit');

INSERT INTO reviews (movie_id, user_id, rating, comment)
VALUES (1,1,5,'Great Movie');

INSERT INTO artists (name) VALUES ('Leonardo');

INSERT INTO skills (skill_name) VALUES ('Acting');

INSERT INTO artist_skill VALUES (1,1);

INSERT INTO artist_movie_role VALUES (1,1,'Hero');


#To get the one movie_title with multiple genre_name 
SELECT m.title, g.genre_name
FROM movies m
JOIN movie_genre mg ON m.movie_id = mg.movie_id
JOIN genres g ON mg.genre_id = g.genre_id;
