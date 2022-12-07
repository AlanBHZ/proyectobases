create database aeropuerto;
use aeropuerto;
create table Pais(
id_pais int primary key,
nombre_pais varchar(45) not null,
Region_pais varchar(45) not null
);
create table Aeropuerto(
id_aeropuerto int primary key,
nombre varchar(45) not null,
id_pais int not null,
foreign key (id_pais) references Pais(id_pais)
);
#Se crea la tabla cliente
create table cliente(
    cedula int primary key,
    nombre varchar(45) not null,
    apellido varchar(45) not null,
    fecha_nac date not null,
    direccion varchar(100)  not null,
    telefono varchar(10)  not null,
    correo varchar(45) not null,
    id_pais int not null,
    foreign key (id_pais) references pais(id_pais)
);

#Se crea la tabla avion
create table avion(
	id_avion int primary key,
    numero_de_serie int not null,
    nombre varchar(50)  not null,
    tipo varchar(50)  not null,
    marca varchar(50)  not null,
    modelo varchar(50)  not null,
    capacidad int not null,
    horas_vuelo int not null
);
create table silla(
	id_silla int primary key,
    estado varchar(45),
    id_avion int not null,
    foreign key (id_avion) references avion(id_avion)
);
select * from avion;
create table estado(
	id_estado int primary key,
    estado varchar(45)
);
#Se crea la tabla vuelo
create table vuelo(
    id_vuelo int primary key,
    fecha date not null,
    horaSalida time not null,
    horaLlegada time,
    numero_Pista varchar(50) not null,
    comentarios varchar(100) not null,#Esta en retraso por una lluvia, por u
    id_avion int not null,
    id_aeropuerto_origen int not null,
    id_aeropuerto_destino int not null,
    id_estado int not null,
    foreign key (id_avion) references avion(id_avion),
    foreign key (id_aeropuerto_origen) references aeropuerto(id_aeropuerto),
    foreign key (id_aeropuerto_destino) references aeropuerto(id_aeropuerto),
    foreign key (id_estado) references estado(id_estado)
);
create table horario_dia(
id_horariodia int primary key,
dias_disponibles varchar(45) not null,
id_vuelo int not null,
foreign key (id_vuelo) references vuelo (id_vuelo)
);
create table horario_hora(
	id_horariohora int primary key,
    hora_disponibles varchar(45) not null,
    id_dia int not null,
    foreign key (id_dia) references horario_dia(id_horariodia)
);

#Se crea la tabla tiquete
create table tiquete(
    id_tiquete int primary key ,
    id_cliente int  not null,
    id_vuelo int not null,
    tipo varchar(45) not null,
    foreign key (id_cliente) references cliente(cedula),
    foreign key (id_vuelo) references vuelo(id_vuelo)
);

INSERT INTO Pais (id_pais, nombre_pais, Region_pais) 
VALUES (1, 'Mexico', 'Centroamerica'), 
(2, 'El Salvador', 'Centroamerica'), 
(3, 'Honduras', 'Centroamerica'), 
(4, 'Guatemala', 'Centroamerica'), 
(5, 'Belice', 'Centroamerica'), 
(6, 'Nicaragua', 'Centroamerica'), 
(7, 'Costa Rica', 'Centroamerica'), 
(8, 'Panama', 'Centroamerica'), 
(9, 'Argentina', 'Suramerica'), 
(10, 'Brasil', 'Suramerica');

INSERT INTO Aeropuerto (id_aeropuerto, nombre, id_pais) 
VALUES (1, 'Aeropuerto Internacional de Mexico', 1), 
(2, 'Aeropuerto Internacional de El Salvador', 2), 
(3, 'Aeropuerto Internacional de Honduras', 3), 
(4, 'Aeropuerto Internacional de Guatemala', 4), 
(5, 'Aeropuerto Internacional de Belice', 5), 
(6, 'Aeropuerto Internacional de Nicaragua', 6), 
(7, 'Aeropuerto Internacional de Costa Rica', 7), 
(8, 'Aeropuerto Internacional de Panama', 8), 
(9, 'Aeropuerto Internacional de Argentina', 9), 
(10, 'Aeropuerto Internacional de Brasil', 10);

#Cliente
INSERT INTO cliente VALUES (123456789, 'Juan', 'García', '2000-03-03', 'Calle Falsa 123', '55555555', 'juan.garcia@example.com', 1);
INSERT INTO cliente VALUES (987654321, 'Maria', 'Perez', '1995-04-10', 'Calle Falsa 456', '66666666', 'maria.perez@example.com', 2);
INSERT INTO cliente VALUES (147258369, 'Jorge', 'Rodriguez', '1999-01-01', 'Calle Falsa 789', '77777777', 'jorge.rodriguez@example.com', 3);
INSERT INTO cliente VALUES (123456799, 'Carlos', 'Gonzalez', '1997-06-20', 'Calle Falsa 101', '88888888', 'carlos.gonzalez@example.com', 4);
INSERT INTO cliente VALUES (987654921, 'Andrea', 'Lopez', '1998-11-15', 'Calle Falsa 112', '99999999', 'andrea.lopez@example.com', 5);
INSERT INTO cliente VALUES (147258169, 'Sofia', 'Sanchez', '1996-09-07', 'Calle Falsa 113', '00000000', 'sofia.sanchez@example.com', 6);
INSERT INTO cliente VALUES (123456123, 'Camila', 'Gomez', '1994-05-25', 'Calle Falsa 114', '11111111', 'camila.gomez@example.com', 7);
INSERT INTO cliente VALUES (927654521, 'Mateo', 'Diaz', '1991-12-30', 'Calle Falsa 115', '22222222', 'mateo.diaz@example.com', 8);
INSERT INTO cliente VALUES (137258169, 'Valentina', 'Martinez', '1992-08-16', 'Calle Falsa 116', '33333333', 'valentina.martinez@example.com', 9);
INSERT INTO cliente VALUES (123436719, 'Nicolas', 'Gutierrez', '1993-07-04', 'Calle Falsa 117', '44444444', 'nicolas.gutierrez@example.com', 10);

#Avion
INSERT INTO avion VALUES (1, 39805, 'Boeing 737-800', 'Avión comercial', 'Boeing', '737-800', 162, 0);
INSERT INTO avion VALUES (2, 39837, 'Airbus A320', 'Avión comercial', 'Airbus', 'A320', 150, 0);
INSERT INTO avion VALUES (3, 39839, 'Airbus A321', 'Avión comercial', 'Airbus', 'A321', 200, 0);
INSERT INTO avion VALUES (4, 39841, 'Boeing 767-300', 'Avión comercial', 'Boeing', '767-300', 230, 0);
INSERT INTO avion VALUES (5, 39843, 'Boeing 777-200', 'Avión comercial', 'Boeing', '777-200', 250, 0);
INSERT INTO avion VALUES (6, 39845, 'Airbus A330-200', 'Avión comercial', 'Airbus', 'A330-200', 300, 0);
INSERT INTO avion VALUES (7, 39847, 'Boeing 747-400', 'Avión comercial', 'Boeing', '747-400', 400, 0);
INSERT INTO avion VALUES (8, 39849, 'Boeing 787-9', 'Avión comercial', 'Boeing', '787-9', 350, 0);
INSERT INTO avion VALUES (9, 39851, 'Airbus A350-900', 'Avión comercial', 'Airbus', 'A350-900', 330, 0);
INSERT INTO avion VALUES (10, 39853, 'Boeing 787-10', 'Avión comercial', 'Boeing', '787-10', 380, 0);

#Silla
INSERT INTO silla VALUES (1, 'Disponible', 1);
INSERT INTO silla VALUES (2, 'Disponible', 2);
INSERT INTO silla VALUES (3, 'Disponible', 3);
INSERT INTO silla VALUES (4, 'Disponible', 4);
INSERT INTO silla VALUES (5, 'Disponible', 5);
INSERT INTO silla VALUES (6, 'Disponible', 6);
INSERT INTO silla VALUES (7, 'Disponible', 7);
INSERT INTO silla VALUES (8, 'Disponible', 8);
INSERT INTO silla VALUES (9, 'Disponible', 9);
INSERT INTO silla VALUES (10, 'Disponible', 10);

#Estado
INSERT INTO estado VALUES (1, 'Activo');
INSERT INTO estado VALUES (2, 'Cancelado');
INSERT INTO estado VALUES (3, 'Retrasado');
INSERT INTO estado VALUES (4, 'Suspendido');
INSERT INTO estado VALUES (5, 'Finalizado');
INSERT INTO estado VALUES (6, 'Programado');
INSERT INTO estado VALUES (7, 'En espera');
INSERT INTO estado VALUES (8, 'Preparando');
INSERT INTO estado VALUES (9, 'Aterrizando');
INSERT INTO estado VALUES (10, 'Despegando');
INSERT INTO estado VALUES (11, 'En vuelo');

#Vuelo
INSERT INTO vuelo VALUES (1, '2020-02-01', '14:00:00', '18:00:00', 'Pista 23', 'Vuelo sin incidentes', 1, 1, 2, 1);
INSERT INTO vuelo VALUES (2, '2020-02-02', '12:00:00', '15:00:00', 'Pista 24', 'Vuelo sin incidentes', 2, 2, 3, 1);
INSERT INTO vuelo VALUES (3, '2020-02-03', '14:00:00', '17:00:00', 'Pista 25', 'Vuelo sin incidentes', 3, 3, 4, 1);
INSERT INTO vuelo VALUES (4, '2020-02-04', '16:00:00', '20:00:00', 'Pista 26', 'Vuelo sin incidentes', 4, 4, 5, 1);
INSERT INTO vuelo VALUES (5, '2020-02-05', '18:00:00', '22:00:00', 'Pista 27', 'Vuelo sin incidentes', 5, 5, 6, 1);
INSERT INTO vuelo VALUES (6, '2020-02-06', '20:00:00', '23:00:00', 'Pista 28', 'Vuelo sin incidentes', 6, 6, 7, 1);
INSERT INTO vuelo VALUES (7, '2020-02-07', '22:00:00', '02:00:00', 'Pista 29', 'Vuelo sin incidentes', 7, 7, 8, 1);
INSERT INTO vuelo VALUES (8, '2020-02-08', '00:00:00', '04:00:00', 'Pista 30', 'Vuelo sin incidentes', 8, 8, 9, 1);
INSERT INTO vuelo VALUES (9, '2020-02-09', '02:00:00', '06:00:00', 'Pista 31', 'Vuelo sin incidentes', 9, 9, 10, 1);
INSERT INTO vuelo VALUES (10, '2020-02-10', '04:00:00', '08:00:00', 'Pista 32', 'Vuelo sin incidentes', 10, 10, 1, 1);
#Horario dia
INSERT INTO horario_dia VALUES (1, 'Lunes', 1);
INSERT INTO horario_dia VALUES (2, 'Martes', 2);
INSERT INTO horario_dia VALUES (3, 'Miércoles', 3);
INSERT INTO horario_dia VALUES (4, 'Jueves', 4);
INSERT INTO horario_dia VALUES (5, 'Viernes', 5);
INSERT INTO horario_dia VALUES (6, 'Sábado', 6);
INSERT INTO horario_dia VALUES (7, 'Domingo', 7);
INSERT INTO horario_dia VALUES (8, 'Lunes', 8);
INSERT INTO horario_dia VALUES (9, 'Martes', 9);
INSERT INTO horario_dia VALUES (10, 'Miércoles', 10);

#Horario hora
INSERT INTO horario_hora VALUES (1, '09:00:00', 1);
INSERT INTO horario_hora VALUES (2, '11:00:00', 2);
INSERT INTO horario_hora VALUES (3, '13:00:00', 3);
INSERT INTO horario_hora VALUES (4, '15:00:00', 4);
INSERT INTO horario_hora VALUES (5, '17:00:00', 5);
INSERT INTO horario_hora VALUES (6, '19:00:00', 6);
INSERT INTO horario_hora VALUES (7, '21:00:00', 7);
INSERT INTO horario_hora VALUES (8, '23:00:00', 8);
INSERT INTO horario_hora VALUES (9, '01:00:00', 9);
INSERT INTO horario_hora VALUES (10, '03:00:00', 10);
#Tiquete
INSERT INTO tiquete VALUES (1, 123456789, 1, 'Economica');
INSERT INTO tiquete VALUES (2, 987654321, 2, 'Economica');
INSERT INTO tiquete VALUES (3, 147258369, 3, 'Economica');
INSERT INTO tiquete VALUES (4, 123456789, 4, 'Economica');
INSERT INTO tiquete VALUES (5, 987654321, 5, 'Economica');
INSERT INTO tiquete VALUES (6, 147258369, 6, 'Economica');
INSERT INTO tiquete VALUES (7, 123456789, 7, 'Economica');
INSERT INTO tiquete VALUES (8, 987654321, 8, 'Economica');
INSERT INTO tiquete VALUES (9, 147258369, 9, 'Economica');
INSERT INTO tiquete VALUES (10, 123456789, 10, 'Economica');

select * from vuelo;
select id_vuelo, id_estado from vuelo;
SELECT id_vuelo,id_estado FROM vuelo where id_vuelo=4;
UPDATE vuelo SET id_estado = 11,comentarios = "En vuelo" WHERE id_vuelo=10;
select * from cliente;

select a.id_avion, a.nombre,v.id_vuelo, hour(timediff(v.horaLlegada, v.horaSalida)), e.estado 
from vuelo v join estado e on e.id_estado = v.id_estado
			 join avion a on a.id_avion = v.id_avion
where e.id_estado = 5;
select a.id_avion, a.nombre, v.id_vuelo, v.fecha, e.estado 
from vuelo v join estado e on e.id_estado = v.id_estado 
join avion a on a.id_avion = v.id_avion
where e.id_estado = 1 or e.id_estado = 6 or e.id_estado =7 or e.id_estado = 8 and e.id_estado = 10;
SELECT * FROM silla;
##Cuando se cree el avion se cree la disponibilidad de las ssillas para el avion

##Cantidad
select a.id_avion, a.nombre, v.id_vuelo, v.fecha, e.estado , a.capacidad
from vuelo v join estado e on e.id_estado = v.id_estado 
join avion a on a.id_avion = v.id_avion 
where e.id_estado = 1 or e.id_estado = 6 or e.id_estado =7 or e.id_estado = 8 and e.id_estado = 10