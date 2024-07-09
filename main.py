import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from comunidad import Comunidad
from simulador import Simulador
from enfermedad import Enfermedad

class VentanaGtk(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title("Expansion de Enfermedad Altamente contagiosa")
        self.set_default_size(600, 400)

        self.paso_actual = 0
        self.simulador = None

        # Crea un contenedor vertical
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(vbox)

        # Componentes de la ventana
        self.label = Gtk.Label(label="Día 0")
        vbox.append(self.label)

        self.avanzar_btn = Gtk.Button(label="Avanzar")
        self.avanzar_btn.connect("clicked", self.on_avanzar_clicked)
        vbox.append(self.avanzar_btn)

        self.retroceder_btn = Gtk.Button(label="Retroceder")
        self.retroceder_btn.connect("clicked", self.on_retroceder_clicked)
        vbox.append(self.retroceder_btn)

        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)
        vbox.append(self.textview)

        self.infectados_label = Gtk.Label(label="Total de Infectados: 0")
        vbox.append(self.infectados_label)

        self.about_btn = Gtk.Button(label="Acerca de")
        self.about_btn.connect("clicked", self.show_about_dialog)
        vbox.append(self.about_btn)

        self.iniciar_simulacion()  #Inicializar la simulacion

        
    def show_about_dialog(self, action):
        about = Gtk.AboutDialog()
        about.set_transient_for(self)
        about.set_modal(self)
        about.set_program_name("Simulacion de Enfermedad")
        about.set_authors(["Ing. Albani Medina"])  #Créditos con nombre
        about.set_version("1.0")
        about.set_copyright("Ing. Albani Medina 2024")
        about.set_comments("Simulación de expansión de enfermedad altamente contagiosa")
        about.set_visible(True)


    # Inicializar comunidad y simulador

    def iniciar_simulacion(self):
        num_ciudadanos = 1000
        promedio_conexion_fisica = 0.5
        covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=15, probabilidad_recuperacion=0.1, probabilidad_muerte=0.05)
        num_infectados = 10
        probabilidad_conexion_fisica = 0.5

        talca = Comunidad(num_ciudadanos, promedio_conexion_fisica, covid, num_infectados, probabilidad_conexion_fisica, [], 0.5)
        talca.crear_ciudadanos()  # Crear ciudadanos y asignar a la comunidad
        talca.asignar_familias()  # Asignar familias
        talca.inicializar_infectados()  # Inicializar infectados
        self.simulador = Simulador(talca, [])
        print("Simulación inicializada.")  # Mensaje de depuracion

    def on_avanzar_clicked(self, widget):
        print("Botón Avanzar presionado.")  # Mensaje de depuración
        if self.simulador:
            self.paso_actual += 1
            self.simulador.inicio_simulacion(1)  # Avanzar un paso en la simulación
            self.actualizar_ventana()

    def on_retroceder_clicked(self, widget):
        if self.paso_actual > 0:
            print("Botón Retroceder presionado.")  #Mensaje de depuración
            self.paso_actual -= 1
            self.actualizar_ventana()

    def actualizar_ventana(self):
        self.label.set_text(f"Día {self.paso_actual}")

        total_infectados_list = self.simulador.get_total_infectados_por_dia()
        if self.paso_actual < len(total_infectados_list):
            total_infectados = total_infectados_list[self.paso_actual]
            self.infectados_label.set_text(f"Total de Infectados: {total_infectados}")
        else:
            self.infectados_label.set_text(f"Total de Infectados: 0")

        # Actualizar el estado de los ciudadanos en el TextView
        estado = self.simulador.obtener_estado(self.paso_actual)
        buffer = self.textview.get_buffer()
        buffer.set_text("")
        for ciudadano in estado:
            buffer.insert(buffer.get_end_iter(), f"{ciudadano['nombre']} {ciudadano['apellido']}: {ciudadano['estado']}\n")

def main(args):
    app = Gtk.Application(application_id="com.example.myapp")
    app.connect("activate", lambda app: VentanaGtk(application=app).present())
    return app.run(args)

if __name__ == "__main__":
    sys.exit(main(sys.argv))









# import sys
# import gi
# gi.require_version('Gtk', '4.0')
# from gi.repository import Gtk
# from comunidad import Comunidad
# from simulador import Simulador
# from enfermedad import Enfermedad

# class VentanaGtk(Gtk.ApplicationWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.set_title("Expansion de Enfermedad Altamente contagiosa")
#         self.set_default_size(600, 400)

#         self.paso_actual = 0
#         self.simulador = None  # Inicialmente no hay simulador

#         # Crea un contenedor vertical
#         vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
#         self.set_child(vbox)

#         # Componentes de la ventana
#         self.label = Gtk.Label(label="Día 0")
#         vbox.append(self.label)

#         self.avanzar_btn = Gtk.Button(label="Avanzar")
#         self.avanzar_btn.connect("clicked", self.on_avanzar_clicked)
#         vbox.append(self.avanzar_btn)

#         self.retroceder_btn = Gtk.Button(label="Retroceder")
#         self.retroceder_btn.connect("clicked", self.on_retroceder_clicked)
#         vbox.append(self.retroceder_btn)

#         self.textview = Gtk.TextView()
#         self.textview.set_editable(False)
#         self.textview.set_cursor_visible(False)
#         vbox.append(self.textview)

#         self.infectados_label = Gtk.Label(label="Total de Infectados: 0")
#         vbox.append(self.infectados_label)

#         self.about_btn = Gtk.Button(label="Acerca de")
#         self.about_btn.connect("clicked", self.show_about_dialog)
#         vbox.append(self.about_btn)

#         self.iniciar_simulacion()  # Inicializar la simulacion

#     def show_about_dialog(self, action):
#         about = Gtk.AboutDialog()
#         about.set_transient_for(self)
#         about.set_modal(self)
#         about.set_program_name("Simulacion de Enfermedad")
#         about.set_authors(["Ing. Albani Medina"])  # Créditos con nombre
#         about.set_version("1.0")
#         about.set_copyright("Ing. Albani Medina 2024")
#         about.set_comments("Simulación de expansión de enfermedad altamente contagiosa")
#         about.set_visible(True)

#     def iniciar_simulacion(self):
#         num_ciudadanos = 1000
#         promedio_conexion_fisica = 0.5
#         covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=15, probabilidad_recuperacion=0.1, probabilidad_muerte=0.05)
#         num_infectados = 10
#         probabilidad_conexion_fisica = 0.5

#        # if num_infectados > num_ciudadanos:
#         #    raise ValueError("El número de infectados iniciales no puede ser mayor que el número total de ciudadanos.")


#         talca = Comunidad(num_ciudadanos, promedio_conexion_fisica, covid, num_infectados, probabilidad_conexion_fisica, [], 0.5)
#         talca.crear_ciudadanos()  # Crear ciudadanos y asignar a la comunidad
#         talca.asignar_familias()  # Asignar familias
#         talca.inicializar_infectados()  # Inicializar infectados
#         self.simulador = Simulador(talca, [])
#         print("Simulación inicializada.")  # Mensaje de depuracion

#     def on_avanzar_clicked(self, widget):
#         print("Botón Avanzar presionado.")  # Mensaje de depuración
#         if self.simulador:
#             self.paso_actual += 1
#             self.simulador.inicio_simulacion(1)  # Avanzar un paso en la simulación
#             self.actualizar_ventana()

#     def on_retroceder_clicked(self, widget):
#         print("Botón Retroceder presionado.")  # Mensaje de depuración
#         if self.paso_actual > 0:
#             self.paso_actual -= 1
#             self.actualizar_ventana()

#     def actualizar_ventana(self):
#         self.label.set_text(f"Día {self.paso_actual}")

#         total_infectados_list = self.simulador.get_total_infectados_por_dia()
#         if self.paso_actual < len(total_infectados_list):
#             total_infectados = total_infectados_list[self.paso_actual]
#             self.infectados_label.set_text(f"Total de Infectados: {total_infectados}")
#         else:
#             self.infectados_label.set_text(f"Total de Infectados: 0")

#         # Actualizar el estado de los ciudadanos en el TextView
#         estado = self.simulador.obtener_estado(self.paso_actual)
#         buffer = self.textview.get_buffer()
#         buffer.set_text("")
#         for ciudadano in estado:
#             buffer.insert(buffer.get_end_iter(), f"{ciudadano['nombre']} {ciudadano['apellido']}: {ciudadano['estado']}\n")

# def main(args):
#     app = Gtk.Application(application_id="com.example.myapp")
#     app.connect("activate", lambda app: VentanaGtk(application=app).present())
#     return app.run(args)

# if __name__ == "__main__":
#     sys.exit(main(sys.argv))
