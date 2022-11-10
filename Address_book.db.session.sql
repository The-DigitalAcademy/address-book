-- Active: 1667747711399@@127.0.0.1@5430@address_book
CREATE TABLE details(
    id INT PRIMARY KEY NOT NULL,
    names VARCHAR(50) NOT NULL,
    email VARCHAR(25) NOT NULL,
    contact VARCHAR(10) NOT NULL,
    
);

CREATE TABLE location(
    street_name INT PRIMARY KEY NOT NULL,
    house_number VARCHAR (10) NOT NULL,
    city VARCHAR(45) NOT NULL,
    postcode VARCHAR NOT NULL,
    province VARCHAR(30) NOT NULL,
    search_count INT NOT NULL,
    CONSTRAINT fk_id
        FOREIGN KEY(id) 
        REFERENCES details(id)
);


INSERT INTO details(id,names, email,contact)
VALUES
(9420,"linah Joseph","linahjoseph@gmail.com", "0713042320"),
(9421, "queen latifa", "quuenl@gmail.com", "0813456091")
;
INSERT INTO location(street_name, house_number, city, postcode, provide,)
VALUES
("hellen_joseph", "234", "Cape town","0157" "western cape"),
("church_street", "123" , "polokwane", "0737", "limpopo")
;