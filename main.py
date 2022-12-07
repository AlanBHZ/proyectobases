import os
from builtins import float
import mysql.connector
import datetime
import threading
import time
from datetime import datetime, timedelta
from colorama import init
from colorama import Fore
from tabulate import tabulate 
 
init(autoreset=True)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="aeropuerto"
)

mycursor = mydb.cursor()


# Clase cliente

class Pais:
    def __init__(self, id_pais, nombre_pais, region_pais):
        self.id_pais = id_pais
        self.nombre_pais = nombre_pais
        self.region_pais = region_pais

    def get_id_pais(self):
        return self.id_pais
    def set_id_pais(self, id_pais):
        self.id_pais = id_pais
    def get_nombre_pais(self):
        return self.nombre_pais
    def set_nombre_pais(self, nombre_pais):
        self.nombre_pais = nombre_pais
    def get_region_pais(self):
        return self.region_pais
    def set_region_pais(self, region_pais):
        self.region_pais = region_pais

class Aeropuerto:
    def __init__(self, id_aeropuerto, nombre, id_pais):
        self.id_aeropuerto = id_aeropuerto
        self.nombre = nombre
        self.id_pais = id_pais

    def get_id_aeropuerto(self):
        return self.id_aeropuerto
    def set_id_aeropuerto(self, id_aeropuerto):
        self.id_aeropuerto = id_aeropuerto
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_id_pais(self):
        return self.id_pais
    def set_id_pais(self, id_pais):
        self.id_pais = id_pais

class Cliente:
    def __init__(self, cedula, nombre, apellido, fecha_nac, direccion, telefono, correo, id_pais):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.id_pais = id_pais
    def get_cedula(self):
        return self.cedula
    def set_cedula(self, cedula):
        self.cedula = cedula
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_apellido(self):
        return self.apellido
    def set_apellido(self, apellido):
        self.apellido = apellido
    def get_fecha_nac(self):
        return self.fecha_nac
    def set_fecha_nac(self, fecha_nac):
        self.fecha_nac = fecha_nac
    def get_direccion(self):
        return self.direccion
    def set_direccion(self, direccion):
        self.direccion = direccion
    def get_telefono(self):
        return self.telefono
    def set_telefono(self, telefono):
        self.telefono = telefono
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo
    def get_id_pais(self):
        return self.id_pais
    def set_id_pais(self, id_pais):
        self.id_pais = id_pais

class Avion:
    def __init__(self, id_avion, numero_de_serie, nombre, tipo, marca, modelo, capacidad, horas_vuelo):
        self.id_avion = id_avion
        self.numero_de_serie = numero_de_serie
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
        self.horas_vuelo = horas_vuelo

    def get_id_avion(self):
        return self.id_avion

    def set_id_avion(self, id_avion):
        self.id_avion = id_avion

    def get_numero_de_serie(self):
        return self.numero_de_serie

    def set_numero_de_serie(self, numero_de_serie):
        self.numero_de_serie = numero_de_serie

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def get_horas_vuelo(self):
        return self.horas_vuelo

    def set_horas_vuelo(self, horas_vuelo):
        self.horas_vuelo = horas_vuelo


class Silla:
    def __init__(self, id_silla, estado, id_avion):
        self.id_silla = id_silla
        self.estado = estado
        self.id_avion = id_avion

    def get_id_silla(self):
        return self.id_silla

    def set_id_silla(self, id_silla):
        self.id_silla = id_silla

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_id_avion(self):
        return self.id_avion

    def set_id_avion(self, id_avion):
        self.id_avion = id_avion


class Estado:
    def __init__(self, id_estado, estado):
        self.id_estado = id_estado
        self.estado = estado

    def get_id_estado(self):
        return self.id_estado

    def set_id_estado(self, id_estado):
        self.id_estado = id_estado

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado


class Vuelo:
    def __init__(self, id_vuelo, fecha, horaSalida, horaLlegada, numero_Pista, comentarios, id_avion,
                 id_aeropuerto_origen, id_aeropuerto_destino, id_estado):
        self.id_vuelo = id_vuelo
        self.fecha = fecha
        self.horaSalida = horaSalida
        self.horaLlegada = horaLlegada
        self.numero_Pista = numero_Pista
        self.comentarios = comentarios
        self.id_avion = id_avion
        self.id_aeropuerto_origen = id_aeropuerto_origen
        self.id_aeropuerto_destino = id_aeropuerto_destino
        self.id_estado = id_estado

    def get_id_vuelo(self):
        return self.id_vuelo

    def set_id_vuelo(self, id_vuelo):
        self.id_vuelo = id_vuelo

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_horaSalida(self):
        return self.horaSalida

    def set_horaSalida(self, horaSalida):
        self.horaSalida = horaSalida

    def get_horaLlegada(self):
        return self.horaLlegada

    def set_horaLlegada(self, horaLlegada):
        self.horaLlegada = horaLlegada

    def get_numero_Pista(self):
        return self.numero_Pista

    def set_numero_Pista(self, numero_Pista):
        self.numero_Pista = numero_Pista

    def get_comentarios(self):
        return self.comentarios

    def set_comentarios(self, comentarios):
        self.comentarios = comentarios

    def get_id_avion(self):
        return self.id_avion

    def set_id_avion(self, id_avion):
        self.id_avion = id_avion

    def get_id_aeropuerto_origen(self):
        return self.id_aeropuerto_origen

    def set_id_aeropuerto_origen(self, id_aeropuerto_origen):
        self.id_aeropuerto_origen = id_aeropuerto_origen

    def get_id_aeropuerto_destino(self):
        return self.id_aeropuerto_destino

    def set_id_aeropuerto_destino(self, id_aeropuerto_destino):
        self.id_aeropuerto_destino = id_aeropuerto_destino

    def get_id_estado(self):
        return self.id_estado

    def set_id_estado(self, id_estado):
        self.id_estado = id_estado


class Horario_dia:
    def __init__(self, id_horariodia, dias_disponibles, id_vuelo):
        self.id_horariodia = id_horariodia
        self.dias_disponibles = dias_disponibles
        self.id_vuelo = id_vuelo

    def get_id_horariodia(self):
        return self.id_horariodia

    def set_id_horariodia(self, id_horariodia):
        self.id_horariodia = id_horariodia

    def get_dias_disponibles(self):
        return self.dias_disponibles

    def set_dias_disponibles(self, dias_disponibles):
        self.dias_disponibles = dias_disponibles

    def get_id_vuelo(self):
        return self.id_vuelo

    def set_id_vuelo(self, id_vuelo):
        self.id_vuelo = id_vuelo


class Horario_hora:
    def __init__(self, id_horariohora, hora_disponibles, id_dia):
        self.id_horariohora = id_horariohora
        self.hora_disponibles = hora_disponibles
        self.id_dia = id_dia

    def get_id_horariohora(self):
        return self.id_horariohora

    def set_id_horariohora(self, id_horariohora):
        self.id_horariohora = id_horariohora

    def get_hora_disponibles(self):
        return self.hora_disponibles

    def set_hora_disponibles(self, hora_disponibles):
        self.hora_disponibles = hora_disponibles

    def get_id_dia(self):
        return self.id_dia

    def set_id_dia(self, id_dia):
        self.id_dia = id_dia


class Tiquete:
    def __init__(self, id_tiquete, id_cliente, id_vuelo, tipo):
        self.id_tiquete = id_tiquete
        self.id_cliente = id_cliente
        self.id_vuelo = id_vuelo
        self.tipo = tipo

    def get_id_tiquete(self):
        return self.id_tiquete

    def set_id_tiquete(self, id_tiquete):
        self.id_tiquete = id_tiquete

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def get_id_vuelo(self):
        return self.id_vuelo

    def set_id_vuelo(self, id_vuelo):
        self.id_vuelo = id_vuelo

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo


def registrar_cliente(self):
    sql = "call registra_cliente(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (self.cedula, self.nombre, self.apellido,self.fecha_nac, self.direccion, self.telefono,self.correo,self.id_pais)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN+"Inserción realizada.")
    print(Fore.GREEN+"Se ha registrado satisfactoriamente")


def registrar_avion(self):
    sql = "call registra_avion(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (self.id_avion,self.numero_de_serie,self.nombre, self.tipo, self.marca, self.modelo, self.capacidad,self.horas_vuelo)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN+"record inserted.")
    print(Fore.GREEN+"Se ha registrado el avion satisfactoriamente")

def registrarPersona():
    clear()
    cedula = input(Fore.LIGHTBLACK_EX+"Ingrese la cedula del cliente: ")
    existe = True
    while existe:
        mycursor.execute("SELECT * FROM cliente")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == cedula:
                print(Fore.RED+"La cedula del cliente ya existe")
                cedula = input(Fore.LIGHTBLACK_EX+"Ingrese nuevamente la cedula del cliente: ")
            else:
                existe = False
    nombre = input(Fore.LIGHTBLACK_EX+"Ingrese el nombre del cliente: ")
    apellido = input(Fore.LIGHTBLACK_EX+"Ingrese el apellido del cliente: ")
    fecha = input(Fore.LIGHTBLACK_EX+"Ingrese la fecha de nacimiento del cliente: ")
    direccion = input(Fore.LIGHTBLACK_EX+"Ingrese la direccion del cliente: ")
    telefono = input(Fore.LIGHTBLACK_EX+"Ingrese el telefono del cliente: ")
    correo = input(Fore.LIGHTBLACK_EX+"Ingrese el correo del cliente: ")
    id_pais = input(Fore.LIGHTBLACK_EX+"Ingrese el id del pais del cliente: ")
    print(cedula, nombre, apellido, fecha, direccion, telefono, correo, id_pais)
    cliente = Cliente(cedula, nombre, apellido, fecha, direccion, telefono, correo, id_pais)

    registrar_cliente(cliente)


# Avion

def registrarAvion():
    clear()
    # Se valida que el numero de serie de avion no exista
    id_avion = input(Fore.LIGHTBLACK_EX+"Ingrese el id del avion: ")
    existe = True
    while existe:
        mycursor.execute("SELECT id_avion FROM avion")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == id_avion:
                print(Fore.RED+"El id_avion del avion ya existe")
                id_avion = input(Fore.LIGHTBLACK_EX+"Ingrese nuevamente el numero de serie del avion: ")
            else:
                existe = False
    numero_serie = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de serie de avion: ")
    nombre = input(Fore.LIGHTBLACK_EX+"Ingrese el nombre de avion: ")
    tipo = input(Fore.LIGHTBLACK_EX+"Ingrese el tipo de avion: ")
    marca = input(Fore.LIGHTBLACK_EX+"Ingrese la marca del avion: ")
    modelo = input(Fore.LIGHTBLACK_EX+"Ingrese el modelo del avion: ")
    capacidad = input(Fore.LIGHTBLACK_EX+"Ingrese la capacidad del avion: ")
    horas = input(Fore.LIGHTBLACK_EX+"Ingrese la horas de vuelo del avion: ")
    avion = Avion(id_avion, numero_serie, nombre, tipo, marca, modelo, capacidad, horas)
    registrar_avion(avion)


# Vuelo


def registrar_vuelo(self):

    sql = "call registra_vuelo (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    val = (
    self.id_vuelo, self.fecha, self.horaSalida, self.horaLlegada, self.numero_Pista, self.comentarios,
    self.id_avion, self.id_aeropuerto_origen, self.id_aeropuerto_destino, self.id_estado)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN+"Vuelo creado exitosamente")

######################### PONER ÉSTE MÉTODO COMO UN TRIGGER #########################
def validarNumeroVuelo(numero_de_vuelo):
    existe = True
    while existe:
        mycursor.execute("SELECT id_vuelo FROM vuelo")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == numero_de_vuelo:
                print(Fore.RED+"El numero de vuelo ya existe")
                numero_de_vuelo = input(Fore.LIGHTBLACK_EX+"Ingrese nuevamente el numero de vuelo: ")
            else:
                existe = False
    return numero_de_vuelo


def validarNumeroAvion(numero_de_avion):
    existe = True
    while existe:
        mycursor.execute("SELECT * FROM avion")
        myresult = mycursor.fetchall()
        for x in myresult:
            if str(x[0]) == str(numero_de_avion):
                return numero_de_avion
            else:
                numero_de_avion = input(Fore.LIGHTBLACK_EX+"Ingrese nuevamente el numero de avion: ")
    return numero_de_avion


def registrarVuelo():
    clear()
    # Se valida que el numero de vuelo no exista
    id_vuelo = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de vuelo: ")
    numero_de_vuelo = validarNumeroVuelo(id_vuelo)
    # Se valida que el numero de avion exista
    fecha = input(Fore.LIGHTBLACK_EX+"Ingrese el fecha: ")
    #numero_de_avion = validarNumeroAvion(numero_de_avion)
    horaS = input(Fore.LIGHTBLACK_EX+"Ingrese la hora de salida: ")
    numero_p = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de pista: ")
    comentarios = input(Fore.LIGHTBLACK_EX+"Ingrese los comentarios del vuelo: ")
    id_avion = input(Fore.LIGHTBLACK_EX+"Ingrese el id del avion: ")
    id_ao = input(Fore.LIGHTBLACK_EX+"Ingrese el id del aeropuerto de origen: ")
    id_ad = input(Fore.LIGHTBLACK_EX+"Ingrese el id del aeropuerto del destino: ")
    vuelo = Vuelo(id_vuelo, fecha, horaS,'00:00:00', numero_p, comentarios,
                  id_avion, id_ao, id_ad,1)
    registrar_vuelo(vuelo)


# Ticket

def registrar_tiquete(self):
    # print("Se registrara el tiquete con la siguiente informacion:", self.numero_de_tiquete_id, self.cedula, self.numero_de_vuelo_id, self.numero_de_asiento)
    sql = "INSERT INTO tiquete (id_tiquete,id_cliente,id_vuelo,tipo) values (%s,%s,%s,%s);"
    val = (self.id_tiquete, self.id_cliente, self.id_vuelo, self.tipo)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN+"Tiquete creado exitosamente")


def validarNumeroTiquete(numero_de_tiquete_id):
    existe = True
    while existe:
        mycursor.execute("SELECT * FROM tiquete")
        myresult = mycursor.fetchall()
        for x in myresult:
            if str(x[0]) == str(numero_de_tiquete_id):
                print(Fore.RED+"El numero de tiquete ya existe")
                numero_de_tiquete_id = input(Fore.LIGHTBLACK_EX+"Ingrese nuevamente el numero de tiquete: ")
            else:
                existe = False
    return numero_de_tiquete_id


def validarCedula(cedula):
    existe = True
    while existe:
        mycursor.execute("SELECT * FROM cliente")
        myresult = mycursor.fetchall()
        for x in myresult:
            if str(x[0]) == str(cedula):
                return cedula
        cedula = input(Fore.LIGHTBLACK_EX+"Ingrese nuevamente la cedula: ")
    return cedula


def mostrarAsientosOcupados(numero_de_vuelo_id):
    mycursor.execute("SELECT s.id_silla FROM vuelo v join avion a on a.id_avion = v.id_avion join silla s on s.id_avion = a.id_avion WHERE v.id_vuelo  = " + numero_de_vuelo_id + " and  s.estado = 'Disponible'")
    myresult = mycursor.fetchall()
    asientos = []
    for x in myresult:
        x[0]
        asientos.append(x[0])
    return asientos


def validar_asiento(numero_de_asiento, asientos):
    existe = True
    # Se recorre asientos para verificar si existe el numero de asiento
    while existe:
        for x in asientos:
            if x == int(numero_de_asiento):
                sql = "update silla set estado = 'Ocupado' where id_silla ="+numero_de_asiento
                mycursor.execute(sql)
                mydb.commit()
                existe = False
        if existe:
            print(Fore.RED+"El numero de asiento ya esta ocupado")
            numero_de_asiento = input(Fore.LIGHTBLACK_EX+"Ingrese nuevamente el asiento: ")
    return numero_de_asiento


def cantidad_asientos_vuelo_actual(numero_de_vuelo_id):
    mycursor.execute("select capacidad from avion a join vuelo v on a.id_avion = v.id_avion where v.id_vuelo = " + numero_de_vuelo_id)
    myresult = mycursor.fetchall()
    asientos = 0
    for x in myresult:
        asientos = x[0]
    return asientos


def validarEstadoVuelo(numero_de_vuelo_id):
    mycursor.execute("SELECT e.estado FROM vuelo v join estado e on e.id_estado = v.id_estado WHERE v.id_vuelo = " + numero_de_vuelo_id)
    myresult = mycursor.fetchall()
    estado = ""
    for x in myresult:
        estado = x[0]
    return estado

def registrarTiquete():
    # Se valida que el numero de vuelo exista
    id_tiquete = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de tiquete: ")
    numero_de_tiquete_id = validarNumeroTiquete(id_tiquete)
    # Se valida que la cedula exista
    id_cliente = input(Fore.LIGHTBLACK_EX+"Ingrese la cedula: ")
    cedula = validarCedula(id_cliente)
    # Se valida que el numero de vuelo exista
    id_vuelo = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de vuelo: ")
    numero_de_vuelo_id = validarNumeroVuelo(id_vuelo)
    salida_vuelo = validarEstadoVuelo(numero_de_vuelo_id)
    if (salida_vuelo != "Activo" ):
        print(Fore.RED+"El vuelo se encuentra disponible, no es posible registrar tiquetes")
        return
    # Se valida que el asiento no este ocupado
    print(Fore.BLUE+"Asientos Ocupados: ")
    asientos = mostrarAsientosOcupados(id_vuelo)
    cantidad_asientos = len(asientos)

    print(cantidad_asientos)
    asientos_vuelo = cantidad_asientos_vuelo_actual(numero_de_vuelo_id)

    print(Fore.BLUE+"Asientos disponibles: ", (int(asientos_vuelo) - int(cantidad_asientos)))
    if ((int(asientos_vuelo) - int(cantidad_asientos))) >= int(0):
        numero_de_asiento = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de asiento: ")
        validar_asiento(numero_de_asiento, asientos)
        tipo = input(Fore.LIGHTBLACK_EX+"Ingrese el tipo de tiquete: ")
        tiquete = Tiquete(id_tiquete, id_cliente, id_vuelo, tipo)
        registrar_tiquete(tiquete)
    else:
        print(Fore.RED+"No hay asientos disponibles")

###SALIDA VUELOS

def salidaVuelos():
    horaActual = datetime.now().time()

    horaActual = horaActual.strftime('%H:%M:%S')
    print(horaActual)
    mycursor.execute("SELECT id_vuelo,id_estado FROM vuelo where id_estado = 1 or id_estado = 6 or id_estado =7 or id_estado = 8 and id_estado = 10")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])
        if (len(myresult) != 0):
            mycursor.execute(
                "UPDATE vuelo SET id_estado = 11,horaSalida = NOW(), comentarios='El vuelo en vuelo' WHERE id_vuelo ="+ str(x[0]))
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print(Fore.YELLOW+"EL vuelo identificado "+ str(x[0]) +" esta en vuelo y salio a las: ", horaActual)
        else:
            print(Fore.RED+"El no hay vuelos listos")
        print(mycursor.rowcount, Fore.GREEN+"record(s) affected")

def cambioEstadoVuelo(numero_de_vuelo_id, comentrario):
    sql = "UPDATE vuelo SET id_estado = 3,comentarios = %s WHERE id_vuelo = %s"
    val = (comentrario, numero_de_vuelo_id)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN+"record(s) affected")

def RetrasoArreglado(numero_de_vuelo_id):
    # Pedirle al usuario que ingrese el numero de vuelo
    estadoSiguiente = input(Fore.LIGHTBLACK_EX+"Digite el nuevo estado del vuelo: 1. En espera 2. En vuelo 3. Retraso")
    estadovuelo = "Retraso"
    if (estadoSiguiente == str(1)):
        estadovuelo = "En espera"
    if (estadoSiguiente == str(2)):
        estadovuelo = "En vuelo"
    comentrario = "Retraso arreglado"
    sql = "UPDATE vuelo SET estado = %s WHERE numero_de_vuelo = %s"
    val = (estadovuelo, numero_de_vuelo_id)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN+"record(s) affected")
    # cambio comentario
    sqll = "UPDATE vuelo SET comentarios = %s WHERE numero_de_vuelo = %s"
    vall = (comentrario, numero_de_vuelo_id)

    mycursor.execute(sqll, vall)
    mydb.commit()

# Menu
def retrasoVuelo():
    numero_de_vuelo_id = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de vuelo: ")
    existe = False
    while not existe:
        mycursor.execute("SELECT id_estado FROM vuelo where id_vuelo="+numero_de_vuelo_id)

        myresult = mycursor.fetchall()
        if(len(myresult)!=0):
            existe=True
        for x in myresult:
            print(x[0])
            if(int(x[0]) != 1 and x[0] != 7 and x[0] != 8):
                print(Fore.RED+"No se le puede cambiar el estado al vuelo :",numero_de_vuelo_id)
                menu()
                break
        if existe == False:
            print(Fore.RED+"El numero de vuelo no existe")
            menu()
        comentarios = input(Fore.LIGHTBLACK_EX+"Ingrese los comentarios del vuelo: ")
        cambioEstadoVuelo(numero_de_vuelo_id, comentarios)
        break


def llegadaVuelo(id_vuelo):
    horaActual = datetime.now().time()
    horaActual = horaActual.strftime('%H:%M:%S')
    print(horaActual)
    mycursor.execute("SELECT id_estado FROM vuelo where id_vuelo="+id_vuelo)
    myresult = mycursor.fetchall()
    print(myresult[0][0])
    if(len(myresult) != 0):
        if(myresult[0][0] == 11):

            mycursor.execute("UPDATE vuelo SET id_estado = 5,horaLlegada = NOW(), comentarios='El vuelo finalizado' WHERE id_vuelo ="+id_vuelo)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print(Fore.YELLOW+"EL vuelo ha finalizado a las: ",horaActual)
        else:
            print(Fore.RED+"El vuelo no esta en vuelo")
    else:
        print(Fore.RED+"El vuelo no existe")


def listarClientesVuelo():
    mycursor.execute("SELECT * FROM clientes_vuelo")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW+tabulate(myresult, headers = ["CÉDULA", "CLIENTE", "N° VUELO", "FECHA", "HORA DE SALIDA", "HORA DE LLEGADA", "COMENTARIO"], tablefmt = "fancy_grid"))


def listarAvionesListosPartir():
    mycursor.execute("SELECT * FROM aviones_listos")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW+tabulate(myresult, headers = ["N° AVIÓN", "NOMBRE DEL AVIÓN", "N° VUELO", "FECHA", "ESTADO"], tablefmt = "fancy_grid"))
    

def listarAvionesLlegaronDestino():
    mycursor.execute("select * from vuelos_finalizados")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW+tabulate(myresult, headers = ["N° AVIÓN", "NOMBRE DEL AVIÓN", "N° VUELO", "HORA DE VUELO", "ESTADO"], tablefmt = "fancy_grid"))

def listarAvionesRetrasados():
    mycursor.execute("select * from vuelos_retrasados")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW+tabulate(myresult, headers = ["N° AVIÓN", "NOMBRE DEL AVIÓN", "N° VUELO", "FECHA DE VUELO", "COMENTARIO"], tablefmt = "fancy_grid"))

def menuInformes():
    clear()
    print(Fore.CYAN+"\tMENU INFORMES")
    print(Fore.CYAN+"1."+Fore.BLUE+" Listado de clientes por vuelo.")
    print(Fore.CYAN+"2."+Fore.BLUE+" Listado de aviones que se encuentran listos para partir asi como la cantidad de clientes que trasportan.")
    print(Fore.CYAN+"3."+Fore.BLUE+" Listado de aviones que han llegado a su destino y el tiempo que tardaron en llegar.")
    print(Fore.CYAN+"4."+Fore.BLUE+" Listado de aviones que se han retrasado y el motivo del retraso de su partida.")
    print(Fore.CYAN+"5."+Fore.BLUE+" Volver a menu principal.")
    opcionMenu = int(input(Fore.CYAN+"Ingrese una opcion del menu: "))
    if opcionMenu == 5:
        menu()
    while opcionMenu != 5:
        if opcionMenu == 1:
            listarClientesVuelo()
            input(Fore.CYAN+"presione cualquier tecla para continuar")
            menuInformes()
            break
        elif opcionMenu == 2:
            listarAvionesListosPartir()
            input(Fore.CYAN+"presione cualquier tecla para continuar")
            menuInformes()
            break
        elif opcionMenu == 3:
            listarAvionesLlegaronDestino()
            input(Fore.CYAN+"presione cualquier tecla para continuar")
            menuInformes()
            break
        elif opcionMenu == 4:
            listarAvionesRetrasados()
            input(Fore.CYAN+"presione cualquier tecla para continuar")
            menuInformes()
            break



def modificarEstadoRetraso():
    id_vuelo = input(Fore.LIGHTBLACK_EX+"Ingrese el numero de vuelo: ")
    mycursor.execute("SELECT id_estado FROM vuelo where id_vuelo=" + id_vuelo)
    myresult = mycursor.fetchall()
    print(myresult[0][0])
    if (len(myresult) != 0):
        if (myresult[0][0] == 3):
            mycursor.execute(
                "UPDATE vuelo SET id_estado = 1, comentarios='Se reactivo el vuelo' WHERE id_vuelo =" + id_vuelo)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print(Fore.GREEN+"EL vuelo se ha reactivado")
        else:
            print(Fore.RED+"El vuelo no esta en retraso")
    else:
        print(Fore.RED+"El vuelo no existe")




def menu():
    clear()
    print(Fore.CYAN+"\tMENU")
    print(Fore.CYAN+"1."+Fore.BLUE+" Registrar Cliente")
    print(Fore.CYAN+"2."+Fore.BLUE+" Registrar Avion")
    print(Fore.CYAN+"3."+Fore.BLUE+" Registrar Vuelo")
    print(Fore.CYAN+"4."+Fore.BLUE+" Registrar Tiquete")
    print(Fore.CYAN+"5."+Fore.BLUE+" Registrar Retraso")
    print(Fore.CYAN+"6."+Fore.BLUE+" Registrar Llegada")
    print(Fore.CYAN+"7."+Fore.BLUE+" Modificar Estado de Retraso")
    print(Fore.CYAN+"8."+Fore.BLUE+" Informes")
    print(Fore.CYAN+"9."+Fore.BLUE+" Salida vuelos")
    print(Fore.CYAN+"10."+Fore.BLUE+" Salir")
menu()

opcionMenu = int(input(Fore.CYAN+"Digite una opcion: "))

while opcionMenu != 10:
    if opcionMenu == 1:
        registrarPersona()
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    elif opcionMenu == 2:
        registrarAvion()
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    elif opcionMenu == 3:
        registrarVuelo()
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    elif opcionMenu == 4:
        registrarTiquete()
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    elif opcionMenu == 5:
        # Se valida que el numero de vuelo exista en la base de datos
        retrasoVuelo()
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    elif opcionMenu == 6:
        id_vuelo = input("Digite el id del vuelo: ")
        llegadaVuelo(id_vuelo)
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    elif opcionMenu == 7:
        modificarEstadoRetraso()
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    elif opcionMenu == 8:
        menuInformes()
    elif opcionMenu == 9:
        print(Fore.CYAN+"Saliendo los vuelos")
        salidaVuelos()
        input(Fore.CYAN+"presione cualquier tecla para continuar")
        menu()
    else:
        print(Fore.CYAN+"No existe esa opcion")
        menu()
    opcionMenu = int(input(Fore.CYAN+"Digite una opcion: "))
print(Fore.MAGENTA+"Ha salido del programa")