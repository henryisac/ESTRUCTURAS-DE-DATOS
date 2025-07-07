#Crear un programa que maneje el Crear un programa que maneje el registro de los est registro de los estudiantes de la unidad curricular udiantes de la unidad curricular de Redes III utilizando listas enlazadas. Los estudiantes aprobados deben insertarse por el
#inicio y los reprobados por el inicio y los reprobados por el final de la lista
"""
Registro de estudiantes de Redes III con lista enlazada.
• Aprobados se insertan al inicio.
• Reprobados se insertan al final.
Operaciones: agregar, buscar, eliminar, totales.
"""

NOTA_APROBATORIA = 6  # ⇦ Modifica aquí si tu reglamento usa otro valor

class Estudiante:
    def __init__(self, cedula, nombre, apellido, correo, nota):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nota = nota

    def __str__(self):
        estado = "Aprobado" if self.nota >= NOTA_APROBATORIA else "Reprobado"
        return f"{self.cedula} | {self.nombre} {self.apellido} | {self.correo} | {self.nota:.1f} | {estado}"


class Nodo:
    def __init__(self, estudiante: Estudiante):
        self.dato = estudiante
        self.sig = None


class ListaEstudiantes:
    def __init__(self):
        self.head = None
        self.tail = None
        self.aprobados = 0
        self.reprobados = 0

    # --------- Operación A: Agregar estudiante ----------
    def agregar(self, estudiante: Estudiante):
        nuevo = Nodo(estudiante)
        if estudiante.nota >= NOTA_APROBATORIA:
            # insertar al inicio
            nuevo.sig = self.head
            self.head = nuevo
            if self.tail is None:  # lista estaba vacía
                self.tail = nuevo
            self.aprobados += 1
        else:
            # insertar al final
            if self.tail:
                self.tail.sig = nuevo
                self.tail = nuevo
            else:  # lista vacía
                self.head = self.tail = nuevo
            self.reprobados += 1

    # --------- Operación B: Buscar por cédula ----------
    def buscar(self, cedula):
        actual = self.head
        while actual:
            if actual.dato.cedula == cedula:
                return actual.dato
            actual = actual.sig
        return None

    # --------- Operación C: Eliminar estudiante ----------
    def eliminar(self, cedula):
        ant = None
        actual = self.head
        while actual:
            if actual.dato.cedula == cedula:
                # actualizar head/tail si aplica
                if ant:
                    ant.sig = actual.sig
                else:
                    self.head = actual.sig
                if actual == self.tail:
                    self.tail = ant
                # actualizar contadores
                if actual.dato.nota >= NOTA_APROBATORIA:
                    self.aprobados -= 1
                else:
                    self.reprobados -= 1
                return True
            ant = actual
            actual = actual.sig
        return False  # no encontrado

    # --------- Operaciones D & E: totales ----------
    def total_aprobados(self):
        return self.aprobados

    def total_reprobados(self):
        return self.reprobados

    # (utilidad) Mostrar la lista completa
    def mostrar(self):
        if not self.head:
            print("Lista vacía.")
            return
        print("Cédula | Nombre Apellido | Correo | Nota | Estado")
        print("-"*60)
        actual = self.head
        while actual:
            print(actual.dato)
            actual = actual.sig


# --------------- Ejemplo de uso ---------------
def menu():
    lista = ListaEstudiantes()
    opciones = {
        "1": "Agregar estudiante",
        "2": "Buscar estudiante por cédula",
        "3": "Eliminar estudiante por cédula",
        "4": "Mostrar lista completa",
        "5": "Totales aprobados / reprobados",
        "0": "Salir"
    }

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        for k, v in opciones.items():
            print(f"{k}. {v}")
        eleccion = input("Seleccione una opción: ").strip()

        match eleccion:
            case "1":
                try:
                    ced = input("Cédula: ").strip()
                    nom = input("Nombre: ").strip()
                    ape = input("Apellido: ").strip()
                    cor = input("Correo: ").strip()
                    nota = float(input("Nota definitiva (1‑10): ").strip())
                    lista.agregar(Estudiante(ced, nom, ape, cor, nota))
                    print("✓ Estudiante agregado correctamente.")
                except ValueError:
                    print("✗ Nota inválida. Intente de nuevo.")
            case "2":
                ced = input("Cédula a buscar: ").strip()
                est = lista.buscar(ced)
                print(est if est else "No se encontró el estudiante.")
            case "3":
                ced = input("Cédula a eliminar: ").strip()
                print("✓ Eliminado" if lista.eliminar(ced) else "✗ No se encontró la cédula.")
            case "4":
                lista.mostrar()
            case "5":
                print(f"Aprobados: {lista.total_aprobados()}")
                print(f"Reprobados: {lista.total_reprobados()}")
            case "0":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
