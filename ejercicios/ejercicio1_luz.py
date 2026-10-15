'''
PLANTEAMIENTO DEL PROBLEMA

Crear un programa en Python que calcule el importe del recibo
mensual de electricidad a partir del consumo en kWh.

La compañía maneja tres tarifas:
$1.00 por kWh hasta 150 kWh,
$1.50 por kWh de 151 a 280 kWh,
$3.00 por kWh arriba de 280 kWh.
'''

# PROBLEMA: calcular el importe del recibo de luz.

# ENTRADAS:
# consumo: cantidad de energía consumida en kWh.
# Tipo: número entero o decimal, mayor o igual a cero.

# SALIDAS:
# pago: importe del recibo en pesos mexicanos.
# Formato: mostrar dos decimales.

# ALGORITMO
# 1. Solicitar el consumo mensual en kWh.
# 2. Si consumo <= 150:
#       pago = consumo * 1.00
# 3. Si consumo > 150 y consumo <= 280:
#       pago = consumo * 1.50
# 4. Si consumo > 280:
#       pago = consumo * 3.00
# 5. Mostrar el consumo y el pago con dos decimales

# CONTRATO DE FUNCIONES

# leerConsumo()
# Entrada: ninguna.
# Salida: consumo.
# Responsabilidad: solicitar y devolver el consumo mensual.

# calcularPago(consumo)
# Entrada: consumo en kWh.
# Salida: pago en pesos.
# Responsabilidad: calcular y devolver el importe del recibo,
# sin imprimir resultados.

# mostrarRecibo(consumo, pago)
# Entrada: consumo y pago.
# Salida: ninguna.
# Responsabilidad: mostrar el consumo y el importe del recibo.

# CASOS DE PRUEBA
# Caso 1: consumo = 100
# Entrada: 100
# Salida esperada: $100.00

# Caso 2: consumo = 150
# Entrada: 150
# Salida esperada: $150.00

# Caso 3: consumo = 200
# Entrada: 200
# Salida esperada: $300.00

# Caso 4: consumo = 280
# Entrada: 280
# Salida esperada: $420.00

# Caso 5: consumo = 300
# Entrada: 300
# Salida esperada: $900.00


# RESTRICCIONES
# - No imprimir dentro de calcularPago().
# - Devolver el importe calculado desde calcularPago().
# - Utilizar únicamente las funciones del contrato.
# - No agregar funciones auxiliares ni clases.
# - No agregar bibliotecas ni validaciones no especificadas.
# - No llamar a las funciones desde este archivo.
# - No agregar un bloque principal de ejecución.
# - Mostrar el importe con dos decimales.
# - Si el consumo es menor o igual a 150 kWh, se cobran
#   $1.00 por cada kWh de todo el consumo.
# - Si el consumo es mayor a 150 y menor o igual a 280 kWh,
#   se cobran $1.50 por cada kWh de todo el consumo.
# - Si el consumo es mayor a 280 kWh, se cobran $3.00
#   por cada kWh de todo el consumo.
# - Las tarifas no se acumulan por bloques.
# - El consumo debe ser mayor o igual a cero.
# - El pago se muestra con dos decimales.

def leerConsumo():
    consumo = float(input("Ingrese el consumo mensual en kWh: "))
    return consumo

def calcularPago(consumo):
    if consumo <= 150:
        pago = consumo * 1.00
    elif consumo > 150 and consumo <= 280:
        pago = consumo * 1.50
    else:
        pago = consumo * 3.00
    return pago 

def mostrarRecibo(consumo, pago):
    print(f"Consumo: {consumo:.2f} kWh")
    print(f"Importe del recibo: ${pago:.2f}")