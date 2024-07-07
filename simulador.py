import pandas as pd

class Simulador:
    def __init__(self, comunidad, historial, ciudadanos, familias):
        self.__comunidad = None
        self.__historial = []

    def set_comunidad(self, comunidad):
        self.comunidad = comunidad

    def get_comunidad(self):
        return self.__comunidad
    
    def set_historial(self, historial):
        self.historial = historial

    def get_historial(self):
        return self.__historial

    def inicio_simulacion(self, pasos):
        for paso in range(pasos):
            self.comunidad.simular_paso()
            self.guardar_estado(paso)
           #Paso, indica en que paso de la simulacion se encuentre 
            
    def guardar_estado(self, paso):
        estado = []
        for ciudadano in self.comunidad.ciudadanos:
            estado.append({
                'id': ciudadano.get_id(),
                'nombre': ciudadano.get_nombre(),
                'apellido': ciudadano.get_apellido(),
                'estado': 'Sano' if ciudadano.get_estado else 'Enfermo',
                'contador': ciudadano.get_contador()
            })
        self.historial.append(estado)
        self.guardar_csv(paso, estado)

    def guardar_csv(self, paso, estado):
        df = pd.DataFrame(estado)
        df.to_csv(f'estado_paso_{paso}.csv', index=False)

    def obtener_estado(self, paso):
        if 0 <= paso < len(self.historial):
            return self.historial[paso]
        return []
    
    
