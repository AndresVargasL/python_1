#Conversor 1 de COP a USD
def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('¿Cuántos pesos ' + tipo_pesos + ' tienes?: '))
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares.')


menu = """
Bienvenido al conversor de moneda

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:  """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3950)
elif opcion == '2':
    conversor('argentinos', 65)
elif opcion =='3':
    conversor('mexicanos', 24)
else:
    print('Ingresa una opción correcta, por favor.')


