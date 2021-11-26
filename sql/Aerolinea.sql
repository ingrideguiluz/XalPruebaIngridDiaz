create database aerolinea;
use aerolinea

CREATE TABLE aerolineas
(id_aerolinea int, 
nombre_aerolinea varchar(30), 
primary key (id_aerolinea));

CREATE TABLE aeropuertos
(id_aeropuerto int, 
nombre_aeropuerto varchar(30), 
primary key (id_aeropuerto));

CREATE TABLE movimientos
(id_movimiento int, 
descripcion varchar(30), 
primary key (id_movimiento));

CREATE TABLE vuelos
(id_aerolinea int, id_aeropuerto int, id_movimiento int, dia date,
FOREIGN KEY(id_aerolinea) REFERENCES aerolíneas (id_aerolinea),
FOREIGN KEY(id_aeropuerto) REFERENCES aeropuertos (id_aeropuerto),
FOREIGN KEY(id_movimiento) REFERENCES movimientos (id_movimiento));

INSERT INTO aerolíneas VALUES (1,'Volaris');
INSERT INTO aerolíneas VALUES (2,'Aeromar');
INSERT INTO aerolíneas VALUES (3,'Interjet');
INSERT INTO aerolíneas VALUES (4,'Aeromexico');

INSERT INTO aeropuertos VALUES (1,'Benito Juarez');
INSERT INTO aeropuertos VALUES (2,'Guanajuato');
INSERT INTO aeropuertos VALUES (3,'La Paz');
INSERT INTO aeropuertos VALUES (4,'Oaxaca');

INSERT INTO movimientos VALUES (1,'Salida');
INSERT INTO movimientos VALUES (2,'Llegada');

INSERT INTO vuelos VALUES (1,1,1,'2021-05-02');
INSERT INTO vuelos VALUES (2,1,1,'2021-05-02');
INSERT INTO vuelos VALUES (3,2,2,'2021-05-02');
INSERT INTO vuelos VALUES (4,3,2,'2021-05-02');
INSERT INTO vuelos VALUES (1,3,2,'2021-05-02');
INSERT INTO vuelos VALUES (2,1,1,'2021-05-02');
INSERT INTO vuelos VALUES (2,3,1,'2021-05-04');
INSERT INTO vuelos VALUES (3,4,1,'2021-05-04');
INSERT INTO vuelos VALUES (3,4,1,'2021-05-04');


