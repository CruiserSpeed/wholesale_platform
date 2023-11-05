CREATE DATABASE whosale_platform;

CREATE TABLE admins (\
    id SERIAL PRIMARY KEY, \
    email VARCHAR(128) NOT NULL, \
    password VARCHAR(128) NOT NULL \
);