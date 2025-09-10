#Desarrollar una aplicación que permita gestionar un catálogo de revistas y realizar búsquedas
# de títulos utilizando una técnica de búsqueda recursiva o iterativa.

def buscar_revista_recursiva(catalogo, titulo, indice=0):
    """Búsqueda recursiva en el catálogo"""
    if indice >= len(catalogo):
        return False
    if catalogo[indice].lower() == titulo.lower():
        return True
    return buscar_revista_recursiva(catalogo, titulo, indice + 1)


def buscar_revista_iterativa(catalogo, titulo):
    """Búsqueda iterativa en el catálogo"""
    for revista in catalogo:
        if revista.lower() == titulo.lower():
            return True
    return False


def mostrar_catalogo(catalogo):
    print("\nCatálogo de Revistas:")
    for revista in catalogo:
        print(f"- {revista}")
    print()


def menu():
    catalogo = [
        "National Geographic",
        "Time",
        "Forbes",
        "Scientific American",
        "Nature",
        "The Economist",
        "Reader's Digest",
        "Harvard Business Review",
        "Popular Science",
        "Sports Illustrated"
    ]

    while True:
        print("===== Catálogo de Revistas =====")
        print("1. Buscar revista (recursivo)")
        print("2. Buscar revista (iterativo)")
        print("3. Mostrar catálogo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("\nIngrese el título de la revista a buscar: ")
            if buscar_revista_recursiva(catalogo, titulo):
                print("\n Resultado: Encontrado\n")
            else:
                print("\n Resultado: No encontrado\n")

        elif opcion == "2":
            titulo = input("\nIngrese el título de la revista a buscar: ")
            if buscar_revista_iterativa(catalogo, titulo):
                print("\n Resultado: Encontrado\n")
            else:
                print("\n Resultado: No encontrado\n")

        elif opcion == "3":
            mostrar_catalogo(catalogo)

        elif opcion == "4":
            print("\nSaliendo del programa...")
            break

        else:
            print("\nOpción no válida. Intente de nuevo.\n")


if __name__ == "__main__":
    menu()
