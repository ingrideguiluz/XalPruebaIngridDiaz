/*1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?*/
select a.nombre_aeropuerto from  aeropuertos a, vuelos v 
where  a.id_aeropuerto = v.id_aeropuerto group by nombre_aeropuerto
having count(*) = (select max(contador) max_contador 
from (select id_aeropuerto, count(*) contador from vuelos group by id_aeropuerto) t); 

/*2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el
año?*/
select a.nombre_aerolinea from  aerolíneas a, vuelos v 
where  a.id_aerolinea = v.id_aerolinea group by nombre_aerolinea
having count(*) = (select max(contador) max_contador 
from (select id_aerolinea, count(*) contador from vuelos group by id_aerolinea) t); 

/*3. ¿En qué día se han tenido mayor número de vuelos?*/
select dia from vuelos group by dia
having count(*) = (select max(contador) max_contador 
from (select dia, count(*) contador from vuelos group by dia) t); 
