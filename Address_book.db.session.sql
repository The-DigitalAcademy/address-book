-- Active: 1667640099306@@127.0.0.1@5430@mafia_casino_db@public
DROP TABLE IF EXISTS details,locations;

CREATE TABLE details(
id INT PRIMARY KEY NOT NULL,
names VARCHAR(50) NOT NULL,
email VARCHAR(25) NOT NULL,
contact VARCHAR(10) NOT NULL    
);

CREATE TABLE locations(
id INT,
street_name VARCHAR(50) NOT NULL,
house_number VARCHAR (10) NOT NULL,
city VARCHAR(45) NOT NULL,
postcode VARCHAR NOT NULL,
province VARCHAR(30) NOT NULL,
search_count INT NOT NULL,
CONSTRAINT fk_id
    FOREIGN KEY(id)
    REFERENCES details(id)
    ON DELETE CASCADE
);


INSERT INTO details(id,names, email,contact)
VALUES
    (9420,'linah Joseph','linahjoseph@gmail.com', '0713042320'),
    (9421, 'queen latifa', 'queenl@gmail.com', '0813456091');
INSERT INTO locations(id,street_name, house_number, city, postcode, province,search_count)
VALUES
    (9420,'hellen_joseph', '234', 'Cape town','0157', 'western cape',0),
    (9421,'church_street', '123' , 'polokwane', '0737', 'limpopo',0);