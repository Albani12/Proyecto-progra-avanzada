import pandas as pd
from comunidad import Comunidad

class Simulador:
    def __init__(self, comunidad, historial, ciudadanos, familias):
        self.__comunidad = comunidad
        self.__historial = []
        self.__total_infectados_por_dia = []
        print("Simulador inicializado.")  # Mensaje de depuracion

    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad
        print("Comunidad establecida.")  # Mensaje de depuracion

    def get_comunidad(self):
        return self.__comunidad
    
    def set_historial(self, historial):
        self.__historial = historial

    def get_historial(self):
        return self.__historial
    
    def set_total_infectados_por_dia(self, total_infectados_por_dia):
        self.__total_infectados_por_dia = total_infectados_por_dia
    
    def get_total_infectados_por_dia(self):
        return self.__total_infectados_por_dia

    def inicio_simulacion(self, pasos):
        if pasos > 0:
            print(f"Inicio de simulación con {pasos} pasos.")  # Mensaje de depuracion
            for paso in range(pasos):
                print(f"Paso {paso + 1} de la simulación.")  # Mensaje de depuracion
                self.__comunidad.simulacion_paso()
                self.guardar_estado(paso)  # Guardar el estado basado en el paso actual
            print("Simulación finalizada.")  # Mensaje de depuracion
        else:
            print("No se puede iniciar la simulación con un número negativo o cero de pasos.")
           
    def guardar_estado(self, paso):
        estado = []
        total_infectados = 0
        ciudadanos = self.__comunidad.get_ciudadanos()
        for i in range(len(ciudadanos)):
            ciudadano = ciudadanos[i]
            estado.append({
                'id': ciudadano.get_id(),
                'nombre': ciudadano.get_nombre(),
                'apellido': ciudadano.get_apellido(),
                'estado': ciudadano.get_estado(),
                'contador': ciudadano.get_contador()
            })
            if ciudadano.get_estado() == 'I':
                total_infectados += 1

        if paso < len(self.__historial):
            self.__historial[paso] = estado
        else:
            self.__historial.append(estado)
        self.__total_infectados_por_dia[paso] = total_infectados if paso < len(self.__total_infectados_por_dia) else total_infectados

        print(f"Estado guardado para el paso {paso}: {total_infectados} infectados.")  # Mensaje de depuración
        self.guardar_csv(paso, estado)

    def guardar_csv(self, paso, estado):
        df = pd.DataFrame(estado)
        filename = f'estado_paso_{paso}.csv'
        df.to_csv(filename, index=False)
        print(f"CSV guardado: {filename}")  #Mensaje de depuracion

    def obtener_estado(self, paso):
        if 0 <= paso < len(self.__historial):
            print(f"Obteniendo estado para el paso {paso}.")  #Mensaje de depuracion
            return self.__historial[paso]
        else:
            print(f"Paso {paso} fuera de rango.")  #Mensaje de depuracion
            return []
        