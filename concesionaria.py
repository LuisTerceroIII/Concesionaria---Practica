

#Ejercicio 4
def comisionesMontoTotal(nroVendedor):
    autosVendidos = autosVendidos()#autosVendidos(nroVendedor)
    tope = 1000000
    comisionTotal = 0
    for auto in autosVendidos():
        if(esCeroKm(auto)):
            if(valorVenta(auto) > tope):
                comisionTotal = comisionTotal + tope*porcenComision0km()
            else:
                comisionTotal = comisionTotal + valorVenta(auto)*porcenComision0km()
        else:
            if(valorVenta(auto) > tope):
                comisionTotal = comisionTotal + tope*porcenComisionUsado()
            else:
                comisionTotal = comisionTotal + valorVenta(auto)*porcenComisionUsado()
    return comisionTotal

print(comisionesMontoTotal(00001))