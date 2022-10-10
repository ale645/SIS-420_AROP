def selec():
    menu = """

Bienvenido a este sector informativo,podra visualisar los campos 
que prefiera ver seleccionando del 1 al 3: 

[1] Biografia
[2] Datos Importantes
[3] Salir

"""
    print(menu)

    opcion = input('digita una opcion del 1 al 3: ')

    while opcion != '3':
        if opcion == '1':
            print("""
      BIOGRAFIA
      Alejandra Reyes Ortiz Pérez
      Nació el 5 de febrero de 1998 en el departamento de Tarija, creció en los departamentos 
      Chuquisaca, Santa Cruz, Potosídurante su etapa escolar, estudiando en diferentes unidades
      educativas, durante su etapa secundaria e universitaria permaneció en la ciudad de 
      Sucre – Chuquisaca, Saliendo Graduada del colegio Don Bosco B, estudiando actualmente en 
      la facultad Mecánica para la carrera de Ing. Electrónica y Tecnológica para la carrera de 
      Ing. en Diseño y animacion digital que brinda la universidad San Francisco Xavier de Chuquisaca.
      """)
            print('=-=' * 20, '\n')

        elif opcion == '2':
            # print(""" DATOS IMPORTANTES
            #      Alejandra Reyes Ortiz Pérez
            #     Altura : 1.50 metros
            #      """)
            print('DATOS IMPORTANTES \n Alejandra Reyes Ortiz Pérez \n',
                  'Altura : 1.50 metros \n Fecha de nacimiento : 05/02/1998  \n Nacionalidad : Tarijeña \n',
                  'Enfermedad de base : si \n tipo de sangre : O+ \n Edad: 24 años')
            print('=-=' * 20, '\n')

        else:
            print('Debes digitar un numero entre el 1 y el 3')
            print('=-=' * 20, '\n')

        opcion = input('digita una opcion del 1 al 3: ')


selec()