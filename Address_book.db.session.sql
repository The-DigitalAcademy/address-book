-- Active: 1667747711399@@127.0.0.1@5430@address_book
CREATE TABLE details(
    id SERIAL PRIMARY KEY NOT NULL,
    names VARCHAR(50) NOT NULL,
    email VARCHAR(25) NOT NULL,
    address VARCHAR(45) NOT NULL,
    postcode INT NOT NULL,
    province VARCHAR NOT NULL,
    contact VARCHAR(10) NOT NULL,
    search_count INT NOT NULL
);

INSERT INTO details(names, email, address,postcode,province,contact,search_count)
VALUES
('John Diale','john@gmail.com','22Top',0152,'Gauteng','0684214968',0),
('Mbedzi Gudani','mbedzigudani@gmail.com', '111 kerk',2001,'Gauteng', '0718345255',0);