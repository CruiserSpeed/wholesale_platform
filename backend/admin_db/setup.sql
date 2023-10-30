CREATE DATABASE whosale_platform;

CREATE TABLE user (\
    id SERIAL PRIMARY KEY, \
    email VARCHAR(128) NOT NULL, \
    password VARCHAR(128) NOT NULL \
);