#Crear un programa que Crear un programa que permita llevar el registro de permita llevar el registro de los vehículos del est los vehículos del estacionamiento del acionamiento del
# Área de Ingeniería de Sistemas de la Área de Ingeniería de Sistemas de la Universidad ut Universidad utilizando como estructura de ilizando como estructura de
# almacenamiento listas enlazadas.
"""
Registro de vehículos del estacionamiento – Ingeniería de Sistemas
Estructura: lista enlazada simple
Operaciones:
  a) Agregar vehículo
  b) Buscar vehículo por placa
  c) Ver vehículos por año
  d) Ver todos los vehículos
  e) Eliminar vehículo por placa
"""

class Vehiculo:
    """Estructura que representa un vehículo."""
    def __init__(self, placa, marca, modelo, anio, precio):
        self.placa = placa.upper()
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def __str__(self):
        return f"{self.placa:>8} | {self.marca:<12} | {self.modelo:<15} | {self.anio:<4} | ${self.precio:,.2f}"


class Nodo:
    """Nodo de la lista enlazada."""
    def __init__(self, vehiculo: Vehiculo):
        self.dato = vehiculo
        self.sig = None


class ListaVehiculos:
    """Lista enlazada para almacenar los vehículos."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamano = 0

    # ---------- a) Agregar vehículo ----------
    def agregar(self, vehiculo: Vehiculo):
        nuevo = Nodo(vehiculo)
        # Inserción al final (mantiene orden de entrada)
        if self.tail:
            self.tail.sig = nuevo
            self.tail = nuevo
        else:                # lista vacía
            self.head = self.tail = nuevo
        self.tamano += 1

    # ---------- b) Buscar vehículo por placa ----------
    def buscar(self, placa: str):
        placa = placa.upper()
        actual = self.head
        while actual:
            if actual.dato.placa == placa:
                return actual.dato
            actual = actual.sig
        return None

    # ---------- c) Ver vehículos por año ----------
    def filtrar_por_anio(self, anio: int):
        actual = self.head
        filtrados = []
        while actual:
            if actual.dato.anio == anio:
                filtrados.append(actual.dato)
            actual = actual.sig
        return filtrados

    # ---------- d) Ver todos los vehículos ----------
    def todos(self):
        actual = self.head
        if not actual:
            return []
        lista = []
        while actual:
            lista.append(actual.dato)
            actual = actual.sig
        return lista

    # ---------- e) Eliminar vehículo por placa ----------
    def eliminar(self, placa: str):
        placa = placa.upper()
        ant = None
        actual = self.head
        while actual:
            if actual.dato.placa == placa:
                # Re‑enlazar
                if ant:
                    ant.sig = actual.sig
                else:
                    self.head = actual.sig
                if actual == self.tail:
                    self.tail = ant
                self.tamano -= 1
                return True
            ant = actual
            actual = actual.sig
        return False

    # ---------- Utilidad: imprimir una lista de vehículos ----------
    @staticmethod
    def imprimir(lista):
        if not lista:
            print("No hay registros.")
            return
        print("   PLACA | MARCA        | MODELO          | AÑO  | PRECIO")
        print("-"*60)
        for v in lista:
            print(v)


# ---------------- Menú interactivo ----------------
def menu():
    lista = ListaVehiculos()

    opciones = {
        "1": "Agregar vehículo",
        "2": "Buscar vehículo por placa",
        "3": "Ver vehículos por año",
        "4": "Ver todos los vehículos",
        "5": "Eliminar vehículo por placa",
        "0": "Salir"
    }

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        for k, v in opciones.items():
            print(f"{k}. {v}")
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":   # Agregar
                try:
                    placa = input("Placa: ").strip()
                    marca = input("Marca: ").strip()
                    modelo = input("Modelo: ").strip()
                    anio = int(input("Año: ").strip())
                    precio = float(input("Precio: ").strip())
                    lista.agregar(Vehiculo(placa, marca, modelo, anio, precio))
                    print("✓ Vehículo agregado.")
                except ValueError:
                    print("✗ Datos numéricos incorrectos. Intente de nuevo.")

            case "2":   # Buscar
                placa = input("Placa a buscar: ").strip()
                v = lista.buscar(placa)
                print(v if v else "No se encontró la placa.")

            case "3":   # Filtrar por año
                try:
                    anio = int(input("Año a consultar: ").strip())
                    vehs = lista.filtrar_por_anio(anio)
                    print(f"\nVehículos del año {anio}:")
                    ListaVehiculos.imprimir(vehs)
                except ValueError:
                    print("✗ Año inválido.")

            case "4":   # Ver todos
                print("\nVehículos registrados:")
                ListaVehiculos.imprimir(lista.todos())

            case "5":   # Eliminar
                placa = input("Placa a eliminar: ").strip()
                print("✓ Eliminado" if lista.eliminar(placa) else "✗ Placa no encontrada.")

            case "0":
                print("¡Hasta luego!")
                break

            case _:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
