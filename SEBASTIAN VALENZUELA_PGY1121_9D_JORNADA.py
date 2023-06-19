import random

def grabar():
    print("responda")
    tipoau=input("ingrese le tipo de auto")
    patente=input("ingrese la patente")
    marca=input("ingerse la marca de su vehiculo")
    precio=input("ingrese el precio de su vehiculo")
    multa=input("ingrese el valor de la multa y fecha de cuando se la sacron")
    while True:
        opcion=input("tiene multa? si/no")
        if opcion.lower()=="no":
            break
        cuantocueta=int(input("de cuento es su multa"))
        fech=input("cuando fue ")
    fechareg=input("ingrese fecha de registro del vehiculo")
    dueño=input("ingrese el nombre del dueño del vehiculo")
    return{
        tipoau:tipoau,
        patente:patente,
        marca:marca,
        precio:precio,
        multa:multa,
        fechareg:fechareg,
        dueño:dueño
    }
def buscar():
    print("buscar auto")
    patente=input("ingrese la patente ")
    for vehiculo in vehiculo:
        if vehiculo in vehiculo:
            print("informacion del auto")
            print("tipo:",vehiculo())
            print("patente",)
            print("")
            print("")
            print("")
            #:(
           

    