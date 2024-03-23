lista_de_compras = []

while True:
    producto = input("agrege un producto:")
    if producto.lower()== "terminar":
        break
    lista_de_compras.append(producto)

    print("as comprado")
    for producto in lista_de_compras:
          
          print(producto)
