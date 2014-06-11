from funciones import *

resp = 's'
while resp == 's':
    numero1=raw_input('ingrese el primer numero: ')
    numero2=raw_input('ingrese el segundo numero: ')


    print '1 - para sumar: '
    print '2 - para restar: '
    print '3 - para multiplicar: '
    print '4 - para dividir: '
    print '5 - para potencia: '
    print '6 - para raiz: '
    opcion = raw_input('ingrese opcion: ')

    if opcion == '1':
        print suma(numero1, numero2)
    elif opcion == '2':
        print resta (numero1, numero2)
    elif opcion == '3':
        print multiplicar(numero1, numero2)
    elif opcion == '4':
        print division(numero1, numero2)
    elif opcion == '5':
        print potencia(numero1, numero2)
    elif opcion == '6':
        print raiz(numero1)
    else:
        print 'Debe seleccionar una opcion valida.'



    resp = raw_input('desea volver a usar?:')

