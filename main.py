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
        self.set_default_size(400, 300)

        self.simulador = None
        self.paso_actual = 0

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

        # Inicializar comunidad y simulador
        self.iniciar_simulacion()

    def iniciar_simulacion(self):
        num_ciudadanos = 1000
        promedio_conexion_fisica = 5
        enfermedad = Enfermedad(infeccion_probable=0.3, promedio_pasos=15, gamma=0.1)
        num_infectados = 10
        probabilidad_conexion_fisica = 0.5

        comunidad = Comunidad(num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica, [], 0.5)
        self.simulador = Simulador(comunidad, [], [], [])

    def on_avanzar_clicked(self, widget):
        self.simulador.inicio_simulacion(1)
        self.paso_actual += 1
        self.actualizar_ventana()

    def on_retroceder_clicked(self, widget):
        if self.paso_actual > 0:
            self.paso_actual -= 1
            self.actualizar_ventana()

    def actualizar_ventana(self):
        self.label.set_text(f"Día {self.paso_actual}")
        estado = self.simulador.obtener_estado(self.paso_actual)
        buffer = self.textview.get_buffer()
        buffer.set_text("")
        for ciudadano in estado:
            buffer.insert(buffer.get_end_iter(), f"{ciudadano['nombre']} {ciudadano['apellido']}: {ciudadano['estado']}\n")
            
        total_infectados = self.simulador.get_total_infectados_por_dia()[self.paso_actual]
        self.infectados_label.set_text(f"Total de Infectados: {total_infectados}")

def main(args):
    app = Gtk.Application(application_id="com.example.myapp")
    app.connect("activate", lambda app: VentanaGtk(application=app).present())
    return app.run(args)

if __name__ == "__main__":
    covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=15)
    talca = Comunidad(num_ciudadanos=1000, promedio_conexion_fisica=8, enfermedad=covid, num_infectados=10, probabilidad_conexion_fisica=0.8, ciudadanos=[], gamma=0.5)    
    sim = Simulador(talca, [], [], [])
    sim.set_comunidad(comunidad=talca)
    sim.inicio_simulacion(pasos=30)
    sys.exit(main(sys.argv))


