import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ============================================================
# CLASE HERRAMIENTA ALQUILER
# ============================================================

class HerramientaAlquiler:
    """
    Clase que representa una herramienta que puede ser alquilada.

    Atributos privados:
        _id_herramienta: Identificador de la herramienta.
        _hora_salida: Hora en la que se entrega la herramienta.
        _tarifa_hora: Valor que se cobra por cada hora de alquiler.
    """

    def __init__(self, id_herramienta, hora_salida, tarifa_hora):
        # Atributos privados de la clase
        self._id_herramienta = id_herramienta
        self._hora_salida = hora_salida
        self._tarifa_hora = tarifa_hora
        self._hora_retorno = None
        self._costo = None

    # --------------------------------------------------------
    # Método para registrar la hora de salida
    # --------------------------------------------------------

    def registrar_salida(self, hora):
        """
        Registra la hora en que sale la herramienta.
        """
        self._hora_salida = hora

    # --------------------------------------------------------
    # Método para registrar la hora de retorno
    # --------------------------------------------------------

    def registrar_retorno(self, hora):
        """
        Registra la hora en que retorna la herramienta.
        """
        self._hora_retorno = hora

    # --------------------------------------------------------
    # Método para calcular el costo
    # --------------------------------------------------------

    def calcular_costo(self, hora_retorno):
        """
        Calcula automáticamente el costo del alquiler
        según las horas utilizadas.
        """

        # Convertimos las horas a objetos datetime
        salida = datetime.strptime(self._hora_salida, "%H:%M")
        retorno = datetime.strptime(hora_retorno, "%H:%M")

        # Validamos que el retorno sea posterior a la salida
        if retorno <= salida:
            raise ValueError(
                "La hora de retorno debe ser posterior a la hora de salida."
            )

        # Calculamos la diferencia entre las horas
        diferencia = retorno - salida

        # Convertimos la diferencia a horas
        horas = diferencia.total_seconds() / 3600

        # Se cobra proporcionalmente según las horas utilizadas
        self._costo = horas * self._tarifa_hora

        # Registramos la hora de retorno
        self.registrar_retorno(hora_retorno)

        return self._costo

    # --------------------------------------------------------
    # Método para obtener el ID
    # --------------------------------------------------------

    def obtener_id(self):
        """
        Retorna el identificador de la herramienta.
        """
        return self._id_herramienta
    # --------------------------------------------------------
    # Método para obtener la hora de salida
    # --------------------------------------------------------

    def obtener_hora_salida(self):
        """
        Retorna la hora de salida de la herramienta.
        """
        return self._hora_salida

    # --------------------------------------------------------
    # Método para obtener la hora de retorno
    # --------------------------------------------------------

    def obtener_hora_retorno(self):
        """
        Retorna la hora de retorno de la herramienta.
        """
        return self._hora_retorno

    # --------------------------------------------------------
    # Método para obtener el costo
    # --------------------------------------------------------

    def obtener_costo(self):
        """
        Retorna el costo total del alquiler.
        """
        return self._costo

    # --------------------------------------------------------
    # Método para obtener la tarifa
    # --------------------------------------------------------

    def obtener_tarifa_hora(self):
        """
        Retorna la tarifa por hora de la herramienta.
        """
        return self._tarifa_hora
    
# ============================================================
# CLASE SISTEMA DE ALQUILER
# ============================================================

class SistemaAlquiler:
    """
    Clase encargada de administrar la lista interna
    de herramientas.
    """

    def __init__(self):
        # Lista interna donde se almacenan las herramientas
        self._herramientas = []

    # --------------------------------------------------------
    # Registrar una herramienta
    # --------------------------------------------------------

    def registrar_herramienta(self, herramienta):
        """
        Agrega una herramienta a la lista interna.
        """

        # Verificamos que el ID no esté repetido
        for herramienta_registrada in self._herramientas:
            if herramienta_registrada.obtener_id() == herramienta.obtener_id():
                return False

        self._herramientas.append(herramienta)
        return True

    # --------------------------------------------------------
    # Buscar una herramienta
    # --------------------------------------------------------

    def buscar_herramienta(self, id_herramienta):
        """
        Busca una herramienta por su identificador.
        """

        for herramienta in self._herramientas:
            if herramienta.obtener_id() == id_herramienta:
                return herramienta

        return None

    # --------------------------------------------------------
    # Obtener todas las herramientas
    # --------------------------------------------------------

    def obtener_herramientas(self):
        """
        Retorna la lista de herramientas registradas.
        """
        return self._herramientas


# ============================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================

def validar_hora(hora):
    """
    Valida que la hora tenga el formato HH:MM.
    """

    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False


# ============================================================
# VENTANA PRINCIPAL DEL SISTEMA
# ============================================================

class Aplicacion:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Sistema de Alquiler de Herramientas")
        self.ventana.geometry("650x900")
        self.ventana.resizable(False, False)

        # Creamos el sistema que almacenará las herramientas

        self.sistema = SistemaAlquiler()

        # Tool catalog with hourly rental rates.
        # Catálogo de herramientas con sus tarifas por hora.

        self.catalogo_herramientas = {
            "H001 - Taladro": 10000,
            "H002 - Serrucho": 7000,
            "H003 - Martillo": 5000,
            "H004 - Flexómetro": 4000
        }
        # Mostramos primero la ventana de inicio de sesión
        self.mostrar_login()

    # ========================================================
    # LOGIN
    # ========================================================

    def mostrar_login(self):

        # Limpiar la ventana
        for widget in self.ventana.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.ventana,
            text="SISTEMA DE ALQUILER DE HERRAMIENTAS",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=40)

        subtitulo = tk.Label(
            self.ventana,
            text="Inicio de sesión",
            font=("Arial", 14)
        )
        subtitulo.pack(pady=10)

        # Campo usuario
        tk.Label(
            self.ventana,
            text="Usuario:",
            font=("Arial", 11)
        ).pack(pady=5)

        self.usuario_entry = tk.Entry(
            self.ventana,
            width=30
        )
        self.usuario_entry.pack()

        # Campo contraseña
        tk.Label(
            self.ventana,
            text="Contraseña:",
            font=("Arial", 11)
        ).pack(pady=5)

        self.password_entry = tk.Entry(
            self.ventana,
            width=30,
            show="*"
        )
        self.password_entry.pack()

        # Botón ingresar
        tk.Button(
            self.ventana,
            text="INGRESAR",
            width=20,
            command=self.verificar_login
        ).pack(pady=25)

        tk.Label(
            self.ventana,
            text="Usuario: admin   |   Contraseña: 1234",
            font=("Arial", 9)
        ).pack(pady=10)

        # ========================================================
    # VERIFICAR LOGIN
    # ========================================================

    def verificar_login(self):

        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        # Datos de acceso del sistema
        if usuario == "admin" and password == "1234":
            self.mostrar_sistema()
        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )

    # ========================================================
    # VENTANA DEL SISTEMA
    # ========================================================

    def mostrar_sistema(self):

        # Limpiar ventana
        for widget in self.ventana.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.ventana,
            text="SISTEMA DE ALQUILER DE HERRAMIENTAS",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        # ----------------------------------------------------
        # SECCIÓN REGISTRAR HERRAMIENTA
        # ----------------------------------------------------

        marco_registro = tk.LabelFrame(
            self.ventana,
            text="Registrar herramienta",
            padx=15,
            pady=15
        )
        marco_registro.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        tk.Label(
            marco_registro,
            text="Herramienta:"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.id_entry = tk.StringVar()

        self.herramienta_menu = tk.OptionMenu(
            marco_registro,
            self.id_entry,
            "H001 - Taladro",
            "H002 - Serrucho",
            "H003 - Martillo",
            "H004 - Flexómetro"
        )

        self.herramienta_menu.config(width=25)

        self.herramienta_menu.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )   

        self.id_entry.trace_add(
            "write",
            self.actualizar_tarifa
        )
        tk.Label(
            marco_registro,
            text="Hora salida (HH:MM):"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.salida_entry = tk.Entry(
            marco_registro,
            width=20
        )
        self.salida_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(
            marco_registro,
            text="Tarifa por hora:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.tarifa_label = tk.Label(
            marco_registro,
            text="$0"
        )
        self.tarifa_label.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        tk.Button(
            marco_registro,
            text="Registrar herramienta",
            command=self.registrar_herramienta
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

        # ----------------------------------------------------
        # SECCIÓN RETORNO
        # ----------------------------------------------------

        marco_retorno = tk.LabelFrame(
            self.ventana,
            text="Registrar retorno",
            padx=15,
            pady=15
        )
        marco_retorno.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        tk.Label(
            marco_retorno,
            text="Herramienta:"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.id_retorno_entry = tk.StringVar()

        self.herramienta_retorno_menu = tk.OptionMenu(
            marco_retorno,
            self.id_retorno_entry,
            "H001 - Taladro",
            "H002 - Serrucho",
            "H003 - Martillo",
            "H004 - Flexómetro"
        )

        self.herramienta_retorno_menu.config(width=25)

        self.herramienta_retorno_menu.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            marco_retorno,
            text="Hora retorno (HH:MM):"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.retorno_entry = tk.Entry(
            marco_retorno,
            width=20
        )
        self.retorno_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        tk.Button(
            marco_retorno,
            text="Registrar retorno y calcular costo",
            command=self.registrar_retorno
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10
        )
        # ----------------------------------------------------
        # BOTÓN PARA MOSTRAR HERRAMIENTAS
        # ----------------------------------------------------

        tk.Button(
            self.ventana,
            text="Mostrar herramientas registradas",
            command=self.mostrar_herramientas
        ).pack(pady=10)

        # ----------------------------------------------------
        # BOTÓN CERRAR SESIÓN
        # ----------------------------------------------------

        tk.Button(
            self.ventana,
            text="Cerrar sesión",
            command=self.mostrar_login
        ).pack(pady=5)
        

    # ========================================================
# ACTUALIZAR TARIFA
# ========================================================

    def actualizar_tarifa(self, *args):
        """
        Updates the hourly rate according to the selected tool.
        Actualiza la tarifa por hora según la herramienta seleccionada.
        """

        herramienta = self.id_entry.get()

        if herramienta in self.catalogo_herramientas:
            tarifa = self.catalogo_herramientas[herramienta]

            self.tarifa_label.config(
                text=f"${tarifa:,.0f}"
            )
        else:
            self.tarifa_label.config(
                text="$0"
            )

            # ========================================================
# REGISTRAR HERRAMIENTA
# ========================================================

    def registrar_herramienta(self):

        id_seleccionado = self.id_entry.get()

        # Obtain only the tool code.
        # Obtener únicamente el código de la herramienta.
        id_herramienta = id_seleccionado.split(" - ")[0]

        # Obtain the rental start time.
        # Obtener la hora de inicio del alquiler.
        hora_salida = self.salida_entry.get().strip()

        # Obtain the hourly rate from the catalog.
        # Obtener la tarifa por hora desde el catálogo.
        tarifa = self.catalogo_herramientas.get(
            id_seleccionado
        )

        # Validate empty fields.
        # Validar campos vacíos.
        if not id_seleccionado or not hora_salida or tarifa is None:
            messagebox.showwarning(
                "Incomplete fields",
                "Please complete all required fields."
            )
            return

        # Validate time format.
        # Validar formato de hora.
        if not validar_hora(hora_salida):
            messagebox.showerror(
                "Incorrect time",
                "The time must have the format HH:MM.\n"
                "Example: 08:30"
            )
            return

        # Create the tool object.
        # Crear el objeto herramienta.
        herramienta = HerramientaAlquiler(
            id_herramienta,
            hora_salida,
            tarifa
        )

        # Register the tool in the internal list.
        # Registrar la herramienta en la lista interna.
        if self.sistema.registrar_herramienta(herramienta):

            messagebox.showinfo(
                "Successful registration",
                "The tool was registered successfully."
            )

            # Clear the fields.
            # Limpiar los campos.
            self.id_entry.set("")
            self.salida_entry.delete(0, tk.END)
            self.tarifa_label.config(
                text="$0"
            )

        else:

            messagebox.showerror(
                "Error",
                "A tool with that ID already exists."
            )

    # ========================================================
    # REGISTRAR RETORNO
    # ========================================================

    def registrar_retorno(self):

        id_seleccionado = self.id_retorno_entry.get().strip()
        id_herramienta = id_seleccionado.split(" - ")[0]
       
        hora_retorno = self.retorno_entry.get().strip()

        # Validar campos
        if not id_seleccionado or not hora_retorno:
            messagebox.showwarning(
                "Campos incompletos",
                "Debe ingresar el ID y la hora de retorno."
            )
            return

        # Validar hora
        if not validar_hora(hora_retorno):
            messagebox.showerror(
                "Hora incorrecta",
                "La hora debe tener el formato HH:MM.\n"
                "Ejemplo: 16:30"
            )
            return

        # Buscar la herramienta
        herramienta = self.sistema.buscar_herramienta(
            id_herramienta
        )

        if herramienta is None:
            messagebox.showerror(
                "Herramienta no encontrada",
                "No existe una herramienta registrada con ese ID."
            )
            return

        # Calcular el costo
        try:

            costo = herramienta.calcular_costo(
                hora_retorno
            )

            messagebox.showinfo(
                "Retorno registrado",
                f"Herramienta: {id_herramienta}\n"
                f"Hora de retorno: {hora_retorno}\n"
                f"Costo total: ${costo:,.2f}"
            )

            # Limpiar campos
            self.id_retorno_entry.set("")
            self.retorno_entry.delete(0, tk.END)

        except ValueError as error:

            messagebox.showerror(
                "Error de hora",
                str(error)
            )

        # ========================================================
    # MOSTRAR HERRAMIENTAS
    # ========================================================

    def mostrar_herramientas(self):

        herramientas = self.sistema.obtener_herramientas()

        ventana_lista = tk.Toplevel(self.ventana)
        ventana_lista.title("Herramientas registradas")
        ventana_lista.geometry("650x450")
        ventana_lista.resizable(False, False)

        texto = tk.Text(
            ventana_lista,
            width=75,
            height=22
        )
        texto.pack(
            padx=10,
            pady=10
        )

        texto.insert(
            tk.END,
            "=== HERRAMIENTAS REGISTRADAS ===\n\n"
        )

        if not herramientas:

            texto.insert(
                tk.END,
                "No hay herramientas registradas."
            )

        else:

            for herramienta in herramientas:

                texto.insert(
                    tk.END,
                    f"ID: {herramienta.obtener_id()}\n"
                )

                texto.insert(
                    tk.END,
                    f"Hora de salida: {herramienta.obtener_hora_salida()}\n"
                )

                hora_retorno = herramienta.obtener_hora_retorno()

                if hora_retorno:

                    texto.insert(
                        tk.END,
                        f"Hora de retorno: {hora_retorno}\n"
                    )

                    texto.insert(
                        tk.END,
                        f"Tarifa por hora: ${herramienta.obtener_tarifa_hora():,.0f}\n"
                    )

                    texto.insert(
                        tk.END,
                        f"Costo total: ${herramienta.obtener_costo():,.0f}\n"
                    )

                    texto.insert(
                        tk.END,
                        "Estado: Retornada\n"
                    )

                else:

                    texto.insert(
                        tk.END,
                        "Hora de retorno: Pendiente\n"
                    )

                    texto.insert(
                        tk.END,
                        f"Tarifa por hora: ${herramienta.obtener_tarifa_hora():,.0f}\n"
                    )

                    texto.insert(
                        tk.END,
                        "Costo total: Pendiente\n"
                    )

                    texto.insert(
                        tk.END,
                        "Estado: Alquilada\n"
                    )

                texto.insert(
                    tk.END,
                    "-" * 55 + "\n"
                )

        texto.config(
            state="disabled"
        )
# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":

    # Crear la ventana principal
    ventana_principal = tk.Tk()

    # Crear la aplicación
    aplicacion = Aplicacion(
        ventana_principal
    )

    # Mantener abierta la interfaz
    ventana_principal.mainloop()