#Desarrollar una aplicación en C# que funcione como un traductor básico entre los idiomas inglés y español,
#utilizando diccionarios como estructura principal para almacenar las palabras y sus equivalencias.
def main():
    # Diccionario inicial inglés → español
    diccionario = {
        "time": "tiempo",
        "person": "persona",
        "year": "año",
        "way": "camino",
        "day": "día",
        "thing": "cosa",
        "man": "hombre",
        "world": "mundo",
        "life": "vida",
        "hand": "mano",
        "part": "parte",
        "child": "niño",
        "eye": "ojo",
        "woman": "mujer",
        "place": "lugar",
        "work": "trabajo",
        "week": "semana",
        "case": "caso",
        "point": "punto",
        "government": "gobierno",
        "company": "empresa"
    }

    opcion = -1
    while opcion != 0:
        print("\n==================== MENÚ ====================")
        print("1. Traducir una frase")
        print("2. Agregar palabras al diccionario")
        print("0. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            frase = input("\nIngrese la frase a traducir: ")
            palabras = frase.split()  # separa por espacios

            traduccion = []
            for palabra in palabras:
                # Normalizamos la palabra en minúsculas quitando signos
                limpia = palabra.strip(",.;:!?").lower()
                if limpia in diccionario:
                    traduccion.append(diccionario[limpia])
                else:
                    traduccion.append(palabra)
            print("\nTraducción:", " ".join(traduccion))

        elif opcion == 2:
            ingles = input("Ingrese la palabra en inglés: ").lower()
            espanol = input("Ingrese la traducción al español: ").lower()

            if ingles not in diccionario:
                diccionario[ingles] = espanol
                print("Palabra agregada correctamente.")
            else:
                print("Esa palabra ya existe en el diccionario.")

        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    main()
