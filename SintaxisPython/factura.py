"""
Realizar un programa que me permita facturar la compra de
de 2 productos, añadir el valor del iva al 12%.
utilice funciones para calcular el total de la factura
"""
print("facturacion de 2 productos")
print("ingrese los productos")

def ingresoProductos():
    producto1=input("Nombre del producto 1: ")
    cant1=int(input("Cantidad: "))
    precio1=float(input("Precio: "))
    producto2=input("Nombre del producto 2: ")
    cant2=int(input("cantidad: "))
    precio2=float(input("Precio: "))
    return producto1,cant1,precio1,producto2,cant2,precio2

def facturar(cant1,precio1,cant2,precio2):
    subtotal=((cant1*precio1)+(cant2*precio2))
    iva=subtotal*0.12
    total=subtotal+iva
    return total

nombreP1,cantidadP1,precioP1,nombreP2,cantidadP2,precioP2=ingresoProductos()
totalPagar=facturar(cantidadP1,precioP1,cantidadP2,precioP2)
print("El total por sus ",nombreP1," y sus ",nombreP2," es de: ",totalPagar)
