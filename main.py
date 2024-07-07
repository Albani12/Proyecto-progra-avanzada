import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from comunidad import Comunidad
from simulador import Simulador
from enfermedad import Enfermedad

class VentanaGtk(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Expansion de Enfermedad Altamente contagiosa")
        self.set_default_size(400, 300)

        self.simulador = None
        self.paso_actual = 0

        # Componentes de la ventana
        self.label = Gtk.Label(label="Día 0")
        self.add(self.label)

        self.avanzar_btn = Gtk.Button(label="Avanzar")
        self.avanzar_btn.connect("clicked", self.on_avanzar_clicked)
        self.add(self.avanzar_btn)

        self.retroceder_btn = Gtk.Button(label="Retroceder")
        self.retroceder_btn.connect("clicked", self.on_retroceder_clicked)
        self.add(self.retroceder_btn)

        self.textview = Gtk.TextView() #muestra el estado de los ciudadanos durante la simulacion
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)
        self.add(self.textview)

        # Inicializar comunidad y simulador
        self.iniciar_simulacion()

    def iniciar_simulacion(self):
        num_ciudadanos = 1000
        promedio_conexion_fisica = 5
        enfermedad = {'beta': 0.3, 'gamma': 0.1} #β es la tasa de transmision
        num_infectados = 10
        probabilidad_conexion_fisica = 0.5

        comunidad = Comunidad(num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica)
        self.simulador = Simulador(comunidad, [])

    def on_avanzar_clicked(self, widget):
        self.simulador.inicio_simulacion(1)
        self.paso_actual += 1
        self.actualizar_ventana()

    def on_retroceder_clicked(self, widget):
        if self.paso_actual > 0:
            self.paso_actual -= 1
            self.actualizar_ventana()

    def actualizar_ventana(self): #Actualiza el dia del Gtk.Label
        self.label.set_text(f"Día {self.paso_actual}")
        estado = self.simulador.obtener_estado(self.paso_actual) #Se obtiene el estado actual de los ciudadanos
        buffer = self.textview.get_buffer()
        buffer.set_text("")   #Limpia el contenido actual del Gtk.TextView
        for ciudadano in estado:
            buffer.insert(buffer.get_end_iter(), f"{ciudadano['nombre']} {ciudadano['apellido']}: {ciudadano['estado']}\n")

app = VentanaGtk()
app.connect("destroy", Gtk.main_quit)
app.show_all()
Gtk.main()

if __name__ == "__main__":
    covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=15)
    talca = Comunidad(num_ciudadanos=1000, promedio_conexion_fisica=8, enfermedad=covid, num_infectados=10, probabilidad_conexion_fisica=0.8)
    sim = Simulador()
    sim.set_comunidad(comunidad=talca)
    sim.run(pasos=45)

    app = VentanaGtk(comunidad=talca, sim=sim)
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()