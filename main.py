import os
from builtins import float
import mysql.connector
import datetime
import threading
import time
from datetime import datetime, timedelta
from colorama import init
from colorama import Fore
from mysqlx.protobuf import _mysqlxpb_pure
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
    passwd="",
    database="aeropuerto"
)
mycursor = mydb.cursor()


# Clase cliente

class Pais():
    def __init__(self, id_pais, nombre_pais, region_pais):
        self.id_pais = id_pais
        self.nombre_pais = nombre_pais
        self.region_pais = region_pais

    def get_id_Pais(self):
        return self.id_pais

    def set_id_Pais(self, id_pais):
        self.id_pais = id_pais

    def get_nombre_pais(self):
        return self.nombre_pais

    def set_nombre_pais(self, nombre_pais):
        self.nombre_pais = nombre_pais

    def get_region_pais(self):
        return self.region_pais

    def set_region_pais(self, region_pais):
        self.region_pais = region_pais


class Aeropuerto():
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


class Cliente():
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


class Tipo_avion():
    def __init__(self, id_tipo, nombre):
        self.id_tipo = id_tipo
        self.nombre = nombre

    def get_id_tipo(self):
        return self.id_tipo

    def set_id_tipo(self, id_tipo):
        self.id_tipo = id_tipo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


class Marca():
    def __init__(self, id_marca, nombre):
        self.id_marca = id_marca
        self.nombre = nombre

    def get_id_marca(self):
        return self.id_marca

    def set_id_marca(self, id_marca):
        self.id_marca = id_marca

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


class Modelo():
    def __init__(self, id_modelo, nombre):
        self.id_modelo = id_modelo
        self.nombre = nombre

    def get_id_modelo(self):
        return self.id_modelo

    def set_id_modelo(self, id_modelo):
        self.id_modelo = id_modelo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


class Avion():
    def __init__(self, numero_de_serie, nombre, id_tipo, id_marca, id_modelo, capacidad, horas_vuelo):
        self.numero_de_serie = numero_de_serie
        self.nombre = nombre
        self.id_tipo = id_tipo
        self.id_marca = id_marca
        self.id_modelo = id_modelo
        self.capacidad = capacidad
        self.horas_vuelo = horas_vuelo

    def get_numero_de_serie(self):
        return self.numero_de_serie

    def set_numero_de_serie(self, numero_de_serie):
        self.numero_de_serie = numero_de_serie

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id_tipo(self):
        return self.id_tipo

    def set_id_tipo(self, id_tipo):
        self.id_tipo = id_tipo

    def get_id_marca(self):
        return self.id_marca

    def set_id_marca(self, id_marca):
        self.id_marca = id_marca

    def get_id_modelo(self):
        return self.id_modelo

    def set_id_modelo(self, id_modelo):
        self.id_modelo = id_modelo

    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def get_horas_vuelo(self):
        return self.horas_vuelo

    def set_horas_vuelo(self, horas_vuelo):
        self.horas_vuelo = horas_vuelo


class Silla():
    def __init__(self, id_silla, estado, n_silla, id_avion):
        self.id_silla = id_silla
        self.estado = estado
        self.n_silla = n_silla
        self.id_avion = id_avion

    def get_id_silla(self):
        return self.id_silla

    def set_id_silla(self, id_silla):
        self.id_silla = id_silla

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_n_silla(self):
        return self.n_silla

    def set_n_silla(self, n_silla):
        self.n_silla = n_silla

    def get_id_avion(self):
        return self.id_avion

    def set_id_avion(self, id_avion):
        self.id_avion = id_avion


class Estado():
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


class Vuelo():
    def __init__(self, fecha, horaSalida, horaLlegada, numero_Pista, comentarios, id_avion, id_aeropuerto_origen,
                 id_aeropuerto_destino, id_estado):
        self.fecha = fecha
        self.horaSalida = horaSalida
        self.horaLlegada = horaLlegada
        self.numero_Pista = numero_Pista
        self.comentarios = comentarios
        self.id_avion = id_avion
        self.id_aeropuerto_origen = id_aeropuerto_origen
        self.id_aeropuerto_destino = id_aeropuerto_destino
        self.id_estado = id_estado

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


class Tipo_tiquete():
    def __init__(self, id_tipo, nombre):
        self.id_tipo = id_tipo
        self.nombre = nombre

    def get_id_tipo(self):
        return self.id_tipo

    def set_id_tipo(self, id_tipo):
        self.id_tipo = id_tipo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


class Tiquete():
    def __init__(self, id_cliente, id_vuelo, tipo):
        self.id_cliente = id_cliente
        self.id_vuelo = id_vuelo
        self.tipo = tipo

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


class Estado():
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


def registrar_cliente(self):
    sql = "call registra_cliente(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
    self.cedula, self.nombre, self.apellido, self.fecha_nac, self.direccion, self.telefono, self.correo, self.id_pais)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN + "Inserción realizada.")
    print(Fore.GREEN + "Se ha registrado satisfactoriamente")


def registrar_avion(self):
    sql = "call registra_avion( %s, %s, %s, %s, %s, %s, %s)"
    val = (
    self.numero_de_serie, self.nombre, self.id_tipo, self.id_marca, self.id_modelo, self.capacidad, self.horas_vuelo)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN + "record inserted.")
    print(Fore.GREEN + "Se ha registrado el avion satisfactoriamente")


def registrarPersona():
    clear()
    cedula = input(Fore.LIGHTBLACK_EX + "Ingrese la cedula del cliente: ")
    existe = True
    while existe:
        mydb.close()
        mydb.connect()
        mycursor.execute("SELECT * FROM cliente")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == cedula:
                print(Fore.RED + "La cedula del cliente ya existe")
                cedula = input(Fore.LIGHTBLACK_EX + "Ingrese nuevamente la cedula del cliente: ")
            else:
                existe = False
    nombre = input(Fore.LIGHTBLACK_EX + "Ingrese el nombre del cliente: ")
    apellido = input(Fore.LIGHTBLACK_EX + "Ingrese el apellido del cliente: ")
    fecha = input(Fore.LIGHTBLACK_EX + "Ingrese la fecha de nacimiento del cliente: ")
    direccion = input(Fore.LIGHTBLACK_EX + "Ingrese la direccion del cliente: ")
    telefono = input(Fore.LIGHTBLACK_EX + "Ingrese el telefono del cliente: ")
    correo = input(Fore.LIGHTBLACK_EX + "Ingrese el correo del cliente: ")
    id_pais = input(Fore.LIGHTBLACK_EX + "Ingrese el id del pais del cliente: ")
    cliente = Cliente(cedula, nombre, apellido, fecha, direccion, telefono, correo, id_pais)

    registrar_cliente(cliente)


# Avion
def validar(id, nombre_tabla):
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT * FROM " + nombre_tabla)
    myresult = mycursor.fetchall()
    for x in myresult:
        if int(id) == int(x[0]):
            return True
            break
    return False


def registrarAvion():
    clear()
    # Se valida que el numero de serie de avion no exista
    numero_serie = input(Fore.LIGHTBLACK_EX + "Ingrese el numero de serie de avion: ")
    nombre = input(Fore.LIGHTBLACK_EX + "Ingrese el nombre de avion: ")
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT * FROM tipo_avion")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["ID TIPO", "TIPO DE AVIÓN"], tablefmt="fancy_grid"))
    tipo = input(Fore.LIGHTBLACK_EX + "Ingrese el id tipo de avion: ")
    exite = validar(tipo, "tipo_avion")
    while not exite:
        tipo = input(Fore.LIGHTBLACK_EX + "Ingrese el id tipo de avion: ")
        exite = validar(tipo, "tipo_avion")

    mycursor.execute("SELECT * FROM marca")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["ID MARCA", "MARCA DE AVIÓN"], tablefmt="fancy_grid"))
    marca = input(Fore.LIGHTBLACK_EX + "Ingrese la marca del avion: ")
    exite = validar(marca, "marca")
    while not exite:
        marca = input(Fore.LIGHTBLACK_EX + "Ingrese la marca del avion: ")
        exite = validar(marca, "marca")

    mycursor.execute("SELECT * FROM modelo")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["ID MODELO", "MODELO DE AVIÓN"], tablefmt="fancy_grid"))
    modelo = input(Fore.LIGHTBLACK_EX + "Ingrese el modelo del avion: ")
    exite = validar(modelo, "modelo")
    while not exite:
        modelo = input(Fore.LIGHTBLACK_EX + "Ingrese el modelo del avion: ")
        exite = validar(modelo, "modelo")

    capacidad = input(Fore.LIGHTBLACK_EX + "Ingrese la capacidad del avion: ")
    horas = input(Fore.LIGHTBLACK_EX + "Ingrese la horas de vuelo del avion: ")
    avion = Avion(numero_serie, nombre, tipo, marca, modelo, capacidad, horas)
    registrar_avion(avion)


# Vuelo

def registrar_vuelo(self):
    sql = "call registra_vuelo (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (
        self.fecha, self.horaSalida, self.horaLlegada, self.numero_Pista, self.comentarios,
        self.id_avion, self.id_aeropuerto_origen, self.id_aeropuerto_destino, self.id_estado)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN + "Vuelo creado exitosamente")


######################### PONER ÉSTE MÉTODO COMO UN TRIGGER #########################
def validarNumeroVuelo(numero_de_vuelo):
    existe = True
    while existe:
        mydb.close()
        mydb.connect()
        mycursor.execute("SELECT id_vuelo FROM vuelo")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == numero_de_vuelo:
                print(Fore.RED + "El numero de vuelo ya existe")
                numero_de_vuelo = input(Fore.LIGHTBLACK_EX + "Ingrese nuevamente el numero de vuelo: ")
            else:
                existe = False


def validarNumeroAvion(numero_de_avion):
    existe = True
    while existe:
        mydb.close()
        mydb.connect()
        mycursor.execute("SELECT * FROM avion")
        myresult = mycursor.fetchall()
        for x in myresult:
            if str(x[0]) == str(numero_de_avion):
                return numero_de_avion
            else:
                numero_de_avion = input(Fore.LIGHTBLACK_EX + "Ingrese nuevamente el numero de avion: ")
    return numero_de_avion


def registrarVuelo():
    clear()
    fecha = input(Fore.LIGHTBLACK_EX + "Ingrese el fecha: ")
    horaS = input(Fore.LIGHTBLACK_EX + "Ingrese la hora de salida: ")
    numero_p = input(Fore.LIGHTBLACK_EX + "Ingrese el numero de pista: ")
    comentarios = input(Fore.LIGHTBLACK_EX + "Ingrese los comentarios del vuelo: ")
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT id_avion,nombre FROM avion")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["ID AVION", "NOMBRE AVIÓN"], tablefmt="fancy_grid"))
    id_avion = input(Fore.LIGHTBLACK_EX + "Ingrese el id del avion: ")
    exite = validar(id_avion, "avion")
    while not exite:
        id_avion = input(Fore.LIGHTBLACK_EX + "Ingrese el id del avion: ")
        exite = validar(id_avion, "avion")
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT id_aeropuerto,nombre FROM aeropuerto")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["ID AEROPUERTO", "NOMBRE AEROPUERTO"], tablefmt="fancy_grid"))
    id_ao = input(Fore.LIGHTBLACK_EX + "Ingrese el id del aeropuerto de origen: ")
    exite = validar(id_ao, "aeropuerto")
    while not exite:
        id_ao = input(Fore.LIGHTBLACK_EX + "Ingrese el id del aeropuerto de origen: ")
        exite = validar(id_ao, "aeropuerto")
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT id_aeropuerto,nombre FROM aeropuerto")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["ID AEROPUERTO", "NOMBRE AEROPUERTO"], tablefmt="fancy_grid"))
    id_ad = input(Fore.LIGHTBLACK_EX + "Ingrese el id del aeropuerto del destino: ")
    exite = validar(id_ad, "aeropuerto")
    while not exite:
        id_ad = input(Fore.LIGHTBLACK_EX + "Ingrese el id del aeropuerto del destino: ")
        exite = validar(id_ad, "aeropuerto")

    vuelo = Vuelo(fecha, horaS, '00:00:00', numero_p, comentarios,
                  id_avion, id_ao, id_ad, 1)
    registrar_vuelo(vuelo)

# Ticket

def registrar_tiquete(self):
    # print("Se registrara el tiquete con la siguiente informacion:", self.numero_de_tiquete_id, self.cedula, self.numero_de_vuelo_id, self.numero_de_asiento)
    sql = "INSERT INTO tiquete (id_cliente,id_vuelo,tipo) values (%s,%s,%s);"
    val = (self.id_cliente, self.id_vuelo, self.tipo)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN + "Tiquete creado exitosamente")

def validarCedula(cedula):
    existe = True
    while existe:
        mydb.close()
        mydb.connect()
        mycursor.execute("SELECT * FROM cliente")
        myresult = mycursor.fetchall()
        for x in myresult:
            if str(x[0]) == str(cedula):
                return cedula
        cedula = input(Fore.LIGHTBLACK_EX + "Ingrese nuevamente la cedula: ")
    return cedula

def validar_asiento(n_asiento,id_avion):
    mydb.close()
    mydb.connect()
    existe = True
    sql="select n_silla, estado from silla where id_avion = %s"
    val = [id_avion]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    # Se recorre asientos para verificar si existe el numero de asiento
    for x in myresult:
        if int(x[0]) == int(n_asiento):
            if(str(x[1]) == 'Disponible'):
                sql = "update silla set estado = 'Ocupado' where n_silla = %s and id_avion = %s"
                val = (n_asiento,id_avion)
                mydb.close()
                mydb.connect()
                mycursor.execute(sql,val)
                mydb.commit()
                existe = False
    if existe:
        print(Fore.RED + "El numero de asiento ya esta ocupado")
        numero_de_asiento = input(Fore.LIGHTBLACK_EX + "Ingrese nuevamente el asiento: ")
        validar_asiento(numero_de_asiento,id_avion)

def validarEstadoVuelo(numero_de_vuelo_id):
    mydb.close()
    mydb.connect()
    mycursor.execute(
        "SELECT e.estado FROM vuelo v join estado e on e.id_estado = v.id_estado WHERE v.id_vuelo = " + numero_de_vuelo_id)
    myresult = mycursor.fetchall()
    estado = ""
    for x in myresult:
        estado = x[0]
    return estado

def asientos_o(id_vuelo,estado):
    sql = "call asientos(%s,%s)"
    val = (id_vuelo,estado)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql,val)
    myresult =mycursor.fetchall()
    mydb.close()
    return myresult[0][0]
def asientos_d(id_vuelo,estado):
    mydb.connect()
    sql = "call asientos(%s,%s)"
    val = (id_vuelo,estado)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql,val)
    myresult =mycursor.fetchall()
    return myresult[0][0]
def registrarTiquete():
    id_cliente = input(Fore.LIGHTBLACK_EX + "Ingrese la cedula: ")
    validarCedula(id_cliente)
    # Se valida que el numero de vuelo exista
    id_vuelo = input(Fore.LIGHTBLACK_EX + "Ingrese el numero de vuelo: ")
    validarNumeroVuelo(id_vuelo)
    salida_vuelo = validarEstadoVuelo(id_vuelo)
    if (salida_vuelo != "Activo"):
        print(Fore.RED + "El vuelo se encuentra disponible, no es posible registrar tiquetes")
        return
    # Se valida que el asiento no este ocupado

    print(Fore.BLUE + "Asientos Ocupados: ",asientos_o(id_vuelo,"Ocupado"))
    print(Fore.BLUE + "Asientos disponibles: ",asientos_d(id_vuelo,"Disponible"))
    mydb.close()
    mydb.connect()
    mycursor.execute(
        "SELECT id_avion FROM vuelo WHERE id_vuelo = " + id_vuelo)
    myresult = mycursor.fetchall()
    id_avion = myresult[0][0]
    mydb.close()
    mydb.connect()
    sql = "SELECT n_silla,estado FROM silla where estado = 'Disponible' AND id_avion = %s"
    val = [id_avion]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["N SILLA", "ESTADO"], tablefmt="fancy_grid"))
    n_asiento=input(Fore.LIGHTBLACK_EX + "Ingrese el numero de asiento: ")

    validar_asiento(n_asiento, id_avion)
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT * FROM tipo_tiquete")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["ID TIPO_TIQUETE", "TIPO TIQUETE"], tablefmt="fancy_grid"))
    tipo = input(Fore.LIGHTBLACK_EX + "Ingrese el tipo de tiquete: ")

    exite = validar(tipo, "tipo_tiquete")
    while not exite:
        tipo = input(Fore.LIGHTBLACK_EX + "Ingrese el tipo de tiquete: ")
        exite = validar(tipo, "tipo_tiquete")
    tiquete = Tiquete(id_cliente, id_vuelo, tipo)
    registrar_tiquete(tiquete)


###SALIDA VUELOS

def salidaVuelos():
    horaActual = datetime.now().time()

    horaActual = horaActual.strftime('%H:%M:%S')
    print(horaActual)
    mydb.close()
    mydb.connect()
    mycursor.execute(
        "SELECT id_vuelo,id_estado FROM vuelo where id_estado = 1 or id_estado = 6 or id_estado =7 or id_estado = 8 and id_estado = 10")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])
        if (len(myresult) != 0):
            mydb.close()
            mydb.connect()
            mycursor.execute(
                "UPDATE vuelo SET id_estado = 11,horaSalida = NOW(), comentarios='El vuelo en vuelo' WHERE id_vuelo =" + str(
                    x[0]))
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print(Fore.YELLOW + "EL vuelo identificado " + str(x[0]) + " esta en vuelo y salio a las: ", horaActual)
        else:
            print(Fore.RED + "El no hay vuelos listos")
        print(mycursor.rowcount, Fore.GREEN + "record(s) affected")


def cambioEstadoVuelo(numero_de_vuelo_id, comentrario):
    sql = "UPDATE vuelo SET id_estado = 3,comentarios = %s WHERE id_vuelo = %s"
    val = (comentrario, numero_de_vuelo_id)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN + "record(s) affected")


def RetrasoArreglado(numero_de_vuelo_id):
    # Pedirle al usuario que ingrese el numero de vuelo
    estadoSiguiente = input(
        Fore.LIGHTBLACK_EX + "Digite el nuevo estado del vuelo: 1. En espera 2. En vuelo 3. Retraso")
    estadovuelo = "Retraso"
    if (estadoSiguiente == str(1)):
        estadovuelo = "En espera"
    if (estadoSiguiente == str(2)):
        estadovuelo = "En vuelo"
    comentrario = "Retraso arreglado"
    sql = "UPDATE vuelo SET estado = %s WHERE numero_de_vuelo = %s"
    val = (estadovuelo, numero_de_vuelo_id)
    mydb.close()
    mydb.connect()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, Fore.GREEN + "record(s) affected")
    # cambio comentario
    mydb.close()
    mydb.connect()
    sqll = "UPDATE vuelo SET comentarios = %s WHERE numero_de_vuelo = %s"
    vall = (comentrario, numero_de_vuelo_id)

    mycursor.execute(sqll, vall)
    mydb.commit()


# Menu
def retrasoVuelo():
    numero_de_vuelo_id = input(Fore.LIGHTBLACK_EX + "Ingrese el numero de vuelo: ")
    existe = False
    while not existe:
        mydb.close()
        mydb.connect()
        mycursor.execute("SELECT id_estado FROM vuelo where id_vuelo=" + numero_de_vuelo_id)

        myresult = mycursor.fetchall()
        if (len(myresult) != 0):
            existe = True
        for x in myresult:
            print(x[0])
            if (int(x[0]) != 1 and x[0] != 7 and x[0] != 8):
                print(Fore.RED + "No se le puede cambiar el estado al vuelo :", numero_de_vuelo_id)
                menu()
                break
        if existe == False:
            print(Fore.RED + "El numero de vuelo no existe")
            menu()
        comentarios = input(Fore.LIGHTBLACK_EX + "Ingrese los comentarios del vuelo: ")
        cambioEstadoVuelo(numero_de_vuelo_id, comentarios)
        break


def llegadaVuelo(id_vuelo):
    horaActual = datetime.now().time()
    horaActual = horaActual.strftime('%H:%M:%S')
    print(horaActual)
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT id_estado FROM vuelo where id_vuelo=" + id_vuelo)
    myresult = mycursor.fetchall()
    print(myresult[0][0])
    if (len(myresult) != 0):
        if (myresult[0][0] == 11):
            mydb.close()
            mydb.connect()
            mycursor.execute(
                "UPDATE vuelo SET id_estado = 5,horaLlegada = NOW(), comentarios='El vuelo finalizado' WHERE id_vuelo =" + id_vuelo)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print(Fore.YELLOW + "EL vuelo ha finalizado a las: ", horaActual)
        else:
            print(Fore.RED + "El vuelo no esta en vuelo")
    else:
        print(Fore.RED + "El vuelo no existe")


def listarClientesVuelo():
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT * FROM clientes_vuelo")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult,
                                 headers=["CÉDULA", "CLIENTE", "N° VUELO", "FECHA", "HORA DE SALIDA", "HORA DE LLEGADA",
                                          "COMENTARIO"], tablefmt="fancy_grid"))


def listarAvionesListosPartir():
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT * FROM aviones_listos")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult, headers=["N° AVIÓN", "NOMBRE DEL AVIÓN", "N° VUELO", "FECHA", "ESTADO"],
                                 tablefmt="fancy_grid"))


def listarAvionesLlegaronDestino():
    mydb.close()
    mydb.connect()
    mycursor.execute("select * from vuelos_finalizados")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult,
                                 headers=["N° AVIÓN", "NOMBRE DEL AVIÓN", "N° VUELO", "HORA DE VUELO", "ESTADO"],
                                 tablefmt="fancy_grid"))


def listarAvionesRetrasados():
    mydb.close()
    mydb.connect()
    mycursor.execute("select * from vuelos_retrasados")
    myresult = mycursor.fetchall()
    print(Fore.YELLOW + tabulate(myresult,
                                 headers=["N° AVIÓN", "NOMBRE DEL AVIÓN", "N° VUELO", "FECHA DE VUELO", "COMENTARIO"],
                                 tablefmt="fancy_grid"))


def menuInformes():
    clear()
    print(Fore.CYAN + "\tMENU INFORMES")
    print(Fore.CYAN + "1." + Fore.BLUE + " Listado de clientes por vuelo.")
    print(
        Fore.CYAN + "2." + Fore.BLUE + " Listado de aviones que se encuentran listos para partir asi como la cantidad de clientes que trasportan.")
    print(
        Fore.CYAN + "3." + Fore.BLUE + " Listado de aviones que han llegado a su destino y el tiempo que tardaron en llegar.")
    print(
        Fore.CYAN + "4." + Fore.BLUE + " Listado de aviones que se han retrasado y el motivo del retraso de su partida.")
    print(Fore.CYAN + "5." + Fore.BLUE + " Volver a menu principal.")
    opcionMenu = int(input(Fore.CYAN + "Ingrese una opcion del menu: "))
    if opcionMenu == 5:
        menu()
    while opcionMenu != 5:
        if opcionMenu == 1:
            listarClientesVuelo()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menuInformes()
            break
        elif opcionMenu == 2:
            listarAvionesListosPartir()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menuInformes()
            break
        elif opcionMenu == 3:
            listarAvionesLlegaronDestino()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menuInformes()
            break
        elif opcionMenu == 4:
            listarAvionesRetrasados()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menuInformes()
            break


def modificarEstadoRetraso():
    id_vuelo = input(Fore.LIGHTBLACK_EX + "Ingrese el numero de vuelo: ")
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT id_estado FROM vuelo where id_vuelo=" + id_vuelo)
    myresult = mycursor.fetchall()
    print(myresult[0][0])
    if (len(myresult) != 0):
        if (myresult[0][0] == 3):
            mydb.close()
            mydb.connect()
            mycursor.execute(
                "UPDATE vuelo SET id_estado = 1, comentarios='Se reactivo el vuelo' WHERE id_vuelo =" + id_vuelo)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print(Fore.GREEN + "EL vuelo se ha reactivado")
        else:
            print(Fore.RED + "El vuelo no esta en retraso")
    else:
        print(Fore.RED + "El vuelo no existe")
def modificarEstadoEnVuelo():
    id_vuelo = input(Fore.LIGHTBLACK_EX + "Ingrese el numero de vuelo: ")
    mydb.close()
    mydb.connect()
    mycursor.execute("SELECT id_estado FROM vuelo where id_vuelo=" + id_vuelo)
    myresult = mycursor.fetchall()
    print(myresult[0][0])
    if (len(myresult) != 0):
        if (myresult[0][0] == 1):
            mydb.close()
            mydb.connect()
            mycursor.execute(
                "UPDATE vuelo SET id_estado = 11, comentarios='El vuelo se puso en En Vuelo' WHERE id_vuelo =" + id_vuelo)
            print(Fore.GREEN + "EL vuelo se ha puesto en estado: En Vuelo")
        else:
            print(Fore.RED + "El vuelo no esta en estado activo")
    else:
        print(Fore.RED + "El vuelo no existe")
def menu_cliente():
    print(Fore.CYAN + "\tMENU CLIENTE")
    print(Fore.CYAN + "1." + Fore.BLUE + " Registrarse como Cliente")
    print(Fore.CYAN + "2." + Fore.BLUE + " Comprar nuevo Tiquete")
    print(Fore.CYAN + "3." + Fore.BLUE + " Ver destinos disponibles")
    print(Fore.CYAN + "4." + Fore.BLUE + " Ver vuelos disponibles")
    print(Fore.CYAN + "5." + Fore.BLUE + " Ver mis tiquetes")
    print(Fore.CYAN + "6." + Fore.BLUE + " Volver al login")
    opcionMenu = int(input(Fore.CYAN + "Digite una opcion: "))
    while opcionMenu != 6:
        if(opcionMenu == 1 ):
            registrarPersona()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu_cliente()
            break
        elif(opcionMenu == 2):
            registrarTiquete()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu_cliente()
            break
        elif (opcionMenu == 3):
            mydb.close()
            mydb.connect()
            mycursor.execute("Select * from destinos_disponibles")
            myresult = mycursor.fetchall()
            print(Fore.YELLOW + tabulate(myresult,
                                         headers=["ID PAIS", "NOMBRE DEL PAIS", "REGIÓN DEL PAIS"],tablefmt="fancy_grid"))
            menu_cliente()
            break
        elif (opcionMenu == 4):
            mydb.close()
            mydb.connect()
            mycursor.execute("Select * from vuelos_disponibles")
            myresult = mycursor.fetchall()
            print(Fore.YELLOW + tabulate(myresult,
                                         headers=["ID AVIÓN", "NOMBRE DEL AVIÓN", "ID VUELO","FECHA DEL VUELO","ESTADO","COMENTARIOS"],
                                         tablefmt="fancy_grid"))
            menu_cliente()
            break
        elif (opcionMenu == 5):
            cedula = input(Fore.LIGHTBLUE_EX + "Digite su cédula: ")
            cedula = int(validarCedula(cedula))
            mydb.close()
            mydb.connect()
            sql = "call ver_mis_tiquetes(%s)"
            val = [cedula]
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            if(len(myresult) == 0):
                print(Fore.RED + "El cliente no tiene vuelos")
            else:
                print(Fore.YELLOW + tabulate(myresult,
                                             headers=["ID TIQUETE", "ID CLIENTE", "CLIENTE", "TIPO TIQUETE"],
                                             tablefmt="fancy_grid"))
            menu_cliente()
            break
    menu_inicio()
def menu_inicio():
    print(Fore.CYAN + "\tLOGIN")
    usuario =input(Fore.BLUE + "USUARIO: ")
    contra = str(input(Fore.BLUE + "CONTRASEÑA: "))
    mydb.close()
    mydb.connect()
    sql = "call validar_usuario(%s,%s)"
    val = (usuario, contra)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if(myresult[0][0] == 'cliente'):
        menu_cliente()
    elif(myresult[0][0] == 'empleado'):
        menu()
    else:
        menu_inicio()
def menu_estados():
    clear()
    print(Fore.CYAN + "\tMENU CAMBIO DE ESTADOS")
    print(Fore.CYAN + "1." + Fore.BLUE + " Cambiar estado de vuelo de Activo a Retraso")
    print(Fore.CYAN + "2." + Fore.BLUE + " Cambiar estado de vuelo de En vuelo a Finalizado")
    print(Fore.CYAN + "3." + Fore.BLUE + " Cambiar estado de vuelo de Retrasado a Activo")
    print(Fore.CYAN + "4." + Fore.BLUE + " Cambiar estado de vuelo de Activo a En Vuelo")
    print(Fore.CYAN + "5." + Fore.BLUE + " Volver al menu empleado")
    opcionMenu = int(input(Fore.CYAN + "Digite una opcion: "))
    while opcionMenu != 5:
        if opcionMenu == 1:
            # Se valida que el numero de vuelo exista en la base de datos
            retrasoVuelo()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu_estados()
        elif opcionMenu == 2:
            id_vuelo = input("Digite el id del vuelo: ")
            llegadaVuelo(id_vuelo)
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu_estados()
        elif opcionMenu == 3:
            modificarEstadoRetraso()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu_estados()
        elif opcionMenu == 4:
            modificarEstadoEnVuelo()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu_estados()
    menu()
def menu():
    clear()
    print(Fore.CYAN + "\tMENU EMPLEADO")
    print(Fore.CYAN + "1." + Fore.BLUE + " Registrar un nuevo Cliente")
    print(Fore.CYAN + "2." + Fore.BLUE + " Registrar un nuevo Avion")
    print(Fore.CYAN + "3." + Fore.BLUE + " Registrar un nuevo Vuelo")
    print(Fore.CYAN + "4." + Fore.BLUE + " Registrar un nuevo Tiquete")
    print(Fore.CYAN + "5." + Fore.BLUE + " Informes del Aeropuerto")
    print(Fore.CYAN + "6." + Fore.BLUE + " Ir a menu cambio de estados")
    print(Fore.CYAN + "7." + Fore.BLUE + " Volver al login")
    opcionMenu = int(input(Fore.CYAN + "Digite una opcion: "))
    while opcionMenu != 7:
        if opcionMenu == 1:
            registrarPersona()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu()
        elif opcionMenu == 2:
            registrarAvion()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu()
        elif opcionMenu == 3:
            registrarVuelo()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu()
        elif opcionMenu == 4:
            registrarTiquete()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu()
        elif opcionMenu == 6:
            menu_estados()
            input(Fore.CYAN + "presione cualquier tecla para continuar")
            menu()
        elif opcionMenu == 5:
            menuInformes()
        else:
            print(Fore.CYAN + "No existe esa opcion")
            menu()
        opcionMenu = int(input(Fore.CYAN + "Digite una opcion: "))
    menu_inicio()
menu_inicio()