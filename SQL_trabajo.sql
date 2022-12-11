create database aeropuerto;

use aeropuerto;
create table Pais(
	id_pais int primary key auto_increment,
	nombre_pais varchar(45) not null,
	Region_pais varchar(45) not null
);
create table Aeropuerto(
	id_aeropuerto int primary key auto_increment,
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
create table usuarios(
	id_usuario int primary key,
    contra varchar(45) not null,
    usuario varchar(45) not null
);
create table tipo_avion(
 id_tipo int primary key auto_increment,
 nombre varchar(45)
);
create table marca(
 id_marca int primary key auto_increment,
 nombre varchar(45)
);
create table modelo(
 id_modelo int primary key auto_increment,
 nombre varchar(45)
);
#Se crea la tabla avion
create table avion(
	id_avion int primary key auto_increment,
    numero_de_serie int not null,
    nombre varchar(50)  not null,
    id_tipo int  not null,
    id_marca int  not null,
    id_modelo int not null,
    capacidad int not null,
    horas_vuelo int not null,
    foreign key (id_tipo) references tipo_avion(id_tipo),
    foreign key (id_marca) references marca(id_marca),
    foreign key (id_modelo) references modelo(id_modelo)
);

create table silla(
	id_silla int primary key auto_increment,
    estado varchar(45),
    n_silla int not null,
    id_avion int not null,
    foreign key (id_avion) references avion(id_avion)
);

create table estado(
	id_estado int primary key,
    estado varchar(45)
);

#Se crea la tabla vuelo
create table vuelo(
    id_vuelo int primary key auto_increment,
    fecha date not null,
    horaSalida time not null,
    horaLlegada time,
    numero_Pista varchar(50) not null,
    comentarios varchar(100) not null,
    id_avion int not null,
    id_aeropuerto_origen int not null,
    id_aeropuerto_destino int not null,
    id_estado int not null,
    foreign key (id_avion) references avion(id_avion),
    foreign key (id_aeropuerto_origen) references aeropuerto(id_aeropuerto),
    foreign key (id_aeropuerto_destino) references aeropuerto(id_aeropuerto),
    foreign key (id_estado) references estado(id_estado)
);
create table tipo_tiquete(
 id_tipo int primary key auto_increment,
 nombre varchar(45)
);
#Se crea la tabla tiquete
create table tiquete(
    id_tiquete int primary key auto_increment,
    id_cliente int  not null,
    id_vuelo int not null,
    tipo int not null,
    foreign key (id_cliente) references cliente(cedula),
    foreign key (id_vuelo) references vuelo(id_vuelo),
    foreign key (tipo) references tipo_tiquete(id_tipo)
);

delimiter //
CREATE TRIGGER sillas_avion
AFTER INSERT ON avion
FOR EACH ROW
BEGIN
	DECLARE i INT DEFAULT 1;
	WHILE i <= NEW.capacidad DO
		INSERT INTO silla (estado, n_silla, id_avion) 
		VALUES ('Disponible', i, NEW.id_avion);
		SET i = i + 1;
	END WHILE;
END;
// delimiter ;
INSERT INTO Pais (nombre_pais, Region_pais) 
VALUES ('Mexico', 'Centroamerica'), 
('El Salvador', 'Centroamerica'), 
('Honduras', 'Centroamerica'), 
('Guatemala', 'Centroamerica'), 
('Belice', 'Centroamerica'), 
('Nicaragua', 'Centroamerica'), 
('Costa Rica', 'Centroamerica'), 
('Panama', 'Centroamerica'), 
('Argentina', 'Suramerica'), 
('Brasil', 'Suramerica'),
('Colombia','Suramerica'),
('Peru','Suramerica'),
('Uruguay','Suramerica');
INSERT INTO Aeropuerto (nombre, id_pais) 
VALUES ('Aeropuerto Internacional de Mexico', 1), 
('Aeropuerto Internacional de El Salvador', 2), 
('Aeropuerto Internacional de Honduras', 3), 
('Aeropuerto Internacional de Guatemala', 4), 
('Aeropuerto Internacional de Belice', 5), 
('Aeropuerto Internacional de Nicaragua', 6), 
('Aeropuerto Internacional de Costa Rica', 7), 
('Aeropuerto Internacional de Panama', 8), 
('Aeropuerto Internacional de Argentina', 9), 
('Aeropuerto Internacional de Brasil', 10),
('Aeropuerto Internacional El Dorado',1),
('Aeropuerto Internacional Ezeiza',2),
('Aeropuerto Internacional Guarulhos',3),
('Aeropuerto Internacional Jorge Chavez',4),
('Aeropuerto Internacional Carrasco',5);
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
INSERT INTO cliente VALUES(12345678, 'Juan', 'Perez', '1995-05-20', 'Calle 123', '12345678', 'juanperez@gmail.com',1);
INSERT INTO cliente VALUES(12345679, 'Maria', 'Gomez', '1990-04-15', 'Calle 456', '12345679', 'mariagomez@gmail.com',2);
INSERT INTO cliente VALUES(12345680, 'Jorge', 'Lopez', '1992-08-30', 'Calle 789', '12345680', 'jorgelopez@gmail.com',3);
INSERT INTO cliente VALUES(12345681, 'Ana', 'Sanchez', '1996-11-10', 'Calle 987', '12345681', 'anasanchez@gmail.com',4);
INSERT INTO cliente VALUES(12345682, 'Pedro', 'Gonzalez', '1998-07-20', 'Calle 654', '12345682', 'pedrogonzalez@gmail.com',5);

insert into usuarios values (1,'123456',"cliente"),(2,'4567',"empleado");

#Insertar datos en la tabla tipo
INSERT INTO tipo_avion(nombre) VALUES('Avion de pasajeros'),
('Avion de carga'),
('Avion de guerra'),
('Avion de entrenamiento'),
('Avion Comercial');

insert into modelo (nombre) values ('DC-9');
insert into modelo (nombre) values ('DC-10');
insert into modelo (nombre) values ('Fokker F-27');
insert into modelo (nombre) values ('A320');
insert into modelo (nombre) values ('B767');
insert into modelo (nombre) values ('A340');
insert into modelo (nombre) values ('B777');
insert into modelo (nombre) values ('A380');
insert into modelo (nombre) values ('MD-11');
insert into modelo (nombre) values ('CRJ-700');

insert into marca (nombre) values ('McDonnell Douglas');
insert into marca (nombre) values ('Fokker');
insert into marca (nombre) values ('Airbus');
insert into marca (nombre) values ('Boeing');
insert into marca (nombre) values ('Boeing');
insert into marca (nombre) values ('Airbus');
insert into marca (nombre) values ('Boeing');
insert into marca (nombre) values ('Airbus');
insert into marca (nombre) values ('McDonnell Douglas');
insert into marca (nombre) values ('Bombardier');
#Insertar datos en la tabla avion
INSERT INTO avion(numero_de_serie, nombre, id_tipo, id_marca, id_modelo, capacidad, horas_vuelo) VALUES(12345, 'Avion 1', 1, 1, 1, 200, 500),
(12346, 'Avion 2', 2, 2, 2, 200, 500),
(12347, 'Avion 3', 3, 3, 3, 200, 500),
(12348, 'Avion 4', 4, 4, 4, 200, 500),
(12349, 'Avion 5', 5, 5, 5, 200, 500);
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
INSERT INTO vuelo (fecha,horaSalida,horaLlegada,numero_Pista,comentarios,id_avion,id_aeropuerto_origen,id_aeropuerto_destino,id_estado) VALUES 
('2020-02-01', '14:00:00', '18:00:00', 'Pista 23', 'Vuelo sin incidentes', 1, 1, 2, 1),
('2020-02-02', '12:00:00', '15:00:00', 'Pista 24', 'Vuelo sin incidentes', 2, 2, 3, 1),
('2020-02-03', '14:00:00', '17:00:00', 'Pista 25', 'Vuelo sin incidentes', 3, 3, 4, 1),
('2020-02-04', '16:00:00', '20:00:00', 'Pista 26', 'Vuelo sin incidentes', 4, 4, 5, 1),
('2020-02-05', '18:00:00', '22:00:00', 'Pista 27', 'Vuelo sin incidentes', 5, 5, 6, 1),
('2020-05-20', '19:00:00', '22:00:00', 'A1', 'A tiempo', 1, 1, 5, 5),
('2020-05-20', '19:00:00', '23:00:00', 'A2', 'Retrasado por lluvia', 2, 2, 7, 2),
('2020-05-20', '19:00:00', '22:00:00', 'A3', 'A tiempo', 3, 3, 4, 5),
('2020-05-20', '19:00:00', '23:00:00', 'A4', 'Retrasado por mantenimiento', 4, 4, 8, 2),
('2020-05-20', '19:00:00', '22:00:00', 'A5', 'A tiempo', 5, 5, 10, 5);

#Tipos de tiquetes
INSERT INTO tipo_tiquete (nombre) values('Economica'), ('Primera Clase'), ('Clase Ejecutiva');
#Tiquete
INSERT INTO tiquete (id_cliente,id_vuelo,tipo) VALUES 
(123456789, 1, 1),
(987654321, 2, 1),
(147258369, 3, 2),
(123456789, 4, 3),
(987654321, 5, 1),
(147258369, 6, 2),
(123456789, 7, 3),
(987654321, 8, 1),
(147258369, 9, 2),
(123456789, 10, 3),
(12345678, 1, 1),
(12345679, 2, 2),
(12345680, 3, 3),
(12345681, 4, 1),
(12345682, 5, 2);
#Silla
select * from silla;
########## USUARIOS ##########

########## VISTAS ##########
#Listado de clientes por vuelo.
create view clientes_vuelo as 
SELECT c.cedula, concat(c.nombre,' ',c.apellido) as cliente, v.id_vuelo, v.fecha, v.horaSalida, v.horaLlegada, v.comentarios 
FROM vuelo v join tiquete t on t.id_vuelo = v.id_vuelo 
			join cliente c on c.cedula = t.id_cliente;
select * from clientes_vuelo;

#Listado de aviones que se encuentran listos para partir asi como la cantidad de clientes que trasportan.
create view aviones_listos as 
select a.id_avion, a.nombre, v.id_vuelo, v.fecha, e.estado 
from vuelo v join estado e on e.id_estado = v.id_estado 
			join avion a on a.id_avion = v.id_avion 
where e.id_estado = 1 or e.id_estado = 6 or e.id_estado =7 or e.id_estado = 8 and e.id_estado = 10;
select * from aviones_listos;

#Listado de aviones que han llegado a su destino y el tiempo que tardaron en llegar.
create view vuelos_finalizados as
select a.id_avion, a.nombre,v.id_vuelo, hour(timediff(v.horaLlegada, v.horaSalida)), e.estado 
from vuelo v join estado e on e.id_estado = v.id_estado 
				join avion a on a.id_avion = v.id_avion 
where e.id_estado = 5;
select * from vuelos_finalizados;

#Listado de aviones que se han retrasado y el motivo del retraso de su partida.   
create view vuelos_retrasados as
select a.id_avion, a.nombre, v.id_vuelo, v.fecha, e.estado, v.comentarios 
from vuelo v join estado e on e.id_estado = v.id_estado 
			join avion a on a.id_avion = v.id_avion 
where e.id_estado = 3;
select * from vuelos_retrasados;

create view vuelos_disponibles as
select  a.id_avion, a.nombre, v.id_vuelo, v.fecha, e.estado, v.comentarios 
from vuelo v join estado e on e.id_estado = v.id_estado 
			join avion a on a.id_avion = v.id_avion 
where e.id_estado = 1 or e.id_estado = 6 or e.id_estado = 7 or e.id_estado = 8;
select * from vuelos_disponibles;


########## PROCEDIMIENTOS ##########

#Registrar clientes
delimiter //
create procedure registra_cliente (in cedula int, in nombre varchar(50), in apellido varchar(50), in fecha_nac date, in direccion varchar(45), in telefono varchar(10),in correo varchar(45), in id_pais int)
begin
	INSERT INTO cliente (cedula, nombre, apellido, fecha_nac, direccion, telefono, correo, id_pais)
           VALUES (cedula, nombre, apellido, fecha_nac,direccion, telefono, correo, id_pais);
end
// delimiter 

#Registrar aviones
delimiter //
create procedure registra_avion (in numero_de_serie int, in nombre varchar(50), in tipo int, in marca int, in modelo int, in capacidad int, in horas_vuel int)
begin
    INSERT INTO avion (numero_de_serie, nombre, id_tipo, id_marca, id_modelo, capacidad, horas_vuelo) 
    VALUES (numero_de_serie, nombre, tipo, marca, modelo, capacidad, horas_vuel);
end
// delimiter 
drop procedure registra_avion;

#Registrar Vuelo
delimiter //
create procedure registra_vuelo (in fecha date, in hora_salida time,in hora_llegada time, in pista varchar(45), in comentarios varchar(100), in id_avion int, in id_aeropuertoO int, in id_aeropuertoD int, in estado int)
begin
    INSERT INTO vuelo (fecha,horaSalida,horaLlegada, numero_Pista,comentarios,id_avion,id_aeropuerto_origen,id_aeropuerto_destino,id_estado) 
    VALUES (fecha,hora_salida,hora_llegada, pista,comentarios,id_avion,id_aeropuertoO,id_aeropuertoD,estado);
end
// delimiter 

#Registrar Tiquete
delimiter //
create procedure registra_tiquete (in cliente int, in vuelo int, in tipo int )
begin
    INSERT INTO tiquete (id_cliente,id_vuelo,tipo) 
    VALUES (cliente, vuelo, tipo);
end
// delimiter 
delimiter //
create procedure asientos(in vuelo int, in estado varchar(45))
begin
	SELECT count(s.id_silla) 
	FROM vuelo v join avion a on a.id_avion = v.id_avion 
				 join silla s on s.id_avion = a.id_avion 
	WHERE v.id_vuelo  = vuelo  and  s.estado = estado;
end
// delimiter 
call asientos(3,'Disponible');






#Registrar Retraso
delimiter //
create procedure validar_usuario (in id int, in contras varchar(10))
begin
	select usuario from usuarios where id_usuario = id and contra = contras;
end
// delimiter 



drop procedure registra_vuelo;
#Registrar Llegada
delimiter //
create procedure registra_vuelo (in id_avion int, in numero_de_serie int, in nombre varchar(50), in tipo varchar(45), in marca varchar(45), in modelo varchar(45), in capacidad int, in horas_vuelo int)
begin
    INSERT INTO avion (id_avion,numero_de_serie, nombre, tipo, marca, modelo, capacidad, horas_vuelo) 
    VALUES (id_avion,numero_de_serie, nombre, tipo, marca, modelo, capacidad, horas_vuelo);
end
// delimiter 
drop procedure registra_vuelo;
#Modificar Estado de Retraso
delimiter //
create procedure registra_vuelo (in id_avion int, in numero_de_serie int, in nombre varchar(50), in tipo varchar(45), in marca varchar(45), in modelo varchar(45), in capacidad int, in horas_vuelo int)
begin
    INSERT INTO avion (id_avion,numero_de_serie, nombre, tipo, marca, modelo, capacidad, horas_vuelo) 
    VALUES (id_avion,numero_de_serie, nombre, tipo, marca, modelo, capacidad, horas_vuelo);
end
// delimiter 
drop procedure registra_vuelo;
########## TRIGGERS ##########

