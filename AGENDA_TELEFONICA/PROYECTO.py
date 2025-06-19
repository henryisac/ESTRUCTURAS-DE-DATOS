#Crear una agenda Telefónica con aplicación sencilla que permite registrar, visualizar y buscar contactos personales o profesionales.
# Cada contacto contiene información básica como nombre, número de teléfono y correo electrónico.
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}\n")


class AgendaTelefonica:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("✅ Contacto agregado con éxito.\n")

    def mostrar_contactos(self):
        if not self.contactos:
            print("⚠️ No hay contactos en la agenda.\n")
            return
        print("📋 Lista de Contactos:")
        for contacto in self.contactos:
            contacto.mostrar()

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if nombre.lower() in c.nombre.lower()]
        if encontrados:
            print("🔍 Contactos encontrados:")
            for c in encontrados:
                c.mostrar()
        else:
            print("❌ Contacto no encontrado.\n")


def menu():
    agenda = AgendaTelefonica()
    while True:
        print("====== AGENDA TELEFÓNICA ======")
        print("1. Agregar Contacto")
        print("2. Ver Todos los Contactos")
        print("3. Buscar Contacto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo: ")
            nuevo = Contacto(nombre, telefono, correo)
            agenda.agregar_contacto(nuevo)

        elif opcion == "2":
            agenda.mostrar_contactos()

        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            agenda.buscar_contacto(nombre)

        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠️ Opción no válida.\n")


# Ejecutar el menú principal
if __name__ == "__main__":
    menu()

