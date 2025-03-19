CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    link VARCHAR(100) NOT NULL
);

INSERT INTO companies (name, link) VALUES 
('Linkedin', 'https://www.linkedin.com/'),
('Glassdoor', 'https://www.glassdoor.com.br/index.htm'),
('Indeed', 'https://br.indeed.com/');


CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    description VARCHAR(1000) NOT NULL,
    type VARCHAR(100),
    datetime TIMESTAMP NOT NULL,
    company_id INTEGER
);


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    birthday_date DATE NOT NULL
);

INSERT INTO users (name, email, password, birthday_date) VALUES 
('Lucas Fernando Quinato de Camargo', 'lfqcamargo@gmail.com', '123', '1995-11-22');
