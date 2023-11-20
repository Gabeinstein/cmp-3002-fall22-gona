#Visualizacion calendario


import calendar

def display_calendar(year = None, month = None):
    if (year == None and month == None):
        year = int(input("Escriba el año: "))
        month = int(input("Escriba el mes: "))
        print("")

    calendario = calendar.TextCalendar(calendar.SUNDAY)
    display = calendario.formatmonth(year,month)
    print (display)

def menu(year = None,month = None):
    print("")
    print("APLICACION CALENDARIO")
    print("")
    
    opcion = ''
    while opcion != '5':
        print("------- Menu -------")
        print ("1. Ver todos eventos pendientes")
        print ("2. Agregar evento")
        print ("3. Eliminar evento")
        print ("4. Mostrar calendario")
        print ("5. Salir")
        print ("")
        opcion = input("Escoger opciones(1-5): ")

        if opcion == '1':
            print("-------Todos los eventos guardados-------")
            #traverse_all_events()
        elif opcion == '2':
            print("-------Anadir evento-------")
            #add_event()
        elif opcion == '3':
            print("-------Eliminar evento-------")
            #delete_event()
        elif opcion == '4':
            print("-------Calendario-------")
            display_calendar()
        elif opcion == '5':
            print("Gracias por usar el programa!")
        else:
            print("Opcion no valida")

menu()