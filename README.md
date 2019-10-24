# Concesionaria---Practica


Una concesionaria de autos necesita saber cuál es el monto total que deberá pagar a sus
vendedores en concepto de comisión, por las unidades vendidas durante el mes. El porcentaje
de comisión varía si el auto es nuevo o usado. Además, si el valor de venta del auto es superior
a 1 millón de pesos, el porcentaje de comisión se aplica sobre 1 millón de pesos, y no sobre el
valor de venta. Se cuenta con las siguientes funciones:
AutosVendidos() : Retorna una lista que contiene los números de chasis (VIN) de los autos
vendidos.
ValorVenta(VIN) : Recibe un número de chasis y retorna el valor de venta del auto.
EsCeroKm(VIN) : Recibe un número de chasis y devuelve True si el auto es 0km, y False si es
usado.
PorcenComisionOkm() : Retorna el porcentaje de comisión sobre el valor de venta de un
auto Okm.
PorcenComisionUsado() : Retorna el porcentaje de comisión sobre el valor de venta de un
auto usado.
Armar un programa que calcule e imprima el monto total a pagar por la concesionaria en
concepto de comisión. Las funciones dadas retornan el valor del porcentaje ya dividido por 100
(es decir, un 2% de comisión se retorna como 0,02).
