print("Hola mundo")
frutas=["manzana","coco","galleta"]

def imprimir_fruta(lista):
    for fruta in lista:
        print(fruta)

imprimir_fruta(frutas)

vehiculo={
    "marca":"carro",
    "modelo":2007,
    "kilometraje":"2015"
}

print (vehiculo["marca"])
print (vehiculo.get("modelo"))