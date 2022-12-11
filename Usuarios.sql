use aeropuerto;

create user 'Cliente'@'localhost' identified by '456';
create user 'Empleado'@'localhost' identified by '789';

GRANT ALL PRIVILEGES ON * . * TO 'Empleado'@'localhost';

GRANT SELECT,INSERT ON aeropuerto.cliente TO 'Cliente'@'localhost';
GRANT SELECT,INSERT ON aeropuerto.tiquete TO 'Cliente'@'localhost';
GRANT SELECT ON aeropuerto.pais TO 'Cliente'@'localhost';
GRANT SELECT ON aeropuerto.vuelos_disponibles TO 'Cliente'@'localhost';