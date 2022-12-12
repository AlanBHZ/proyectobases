use aeropuerto;
select * from tiquete where id_tiquete = 18;
select * from historial;
select * from cliente;
call registra_cliente(141234,"sjahd","!4ewsd",'2002-12-12',"asdasds",867832,"asdvvcsx",4);
select CURRENT_USER();
delimiter //
CREATE TRIGGER log_cliente  
	AFTER INSERT ON cliente
    FOR EACH ROW
BEGIN
    INSERT INTO historial (usuario, accion, fecha) 
    VALUES (CURRENT_USER(), 'INSERT', NOW());
END;
// delimiter ;
select * from vuelo;