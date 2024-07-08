
import pandas as pd

class Simulador:
    def __init__(self, comunidad, historial, ciudadanos, familias):
        self.__comunidad = comunidad
        self.__historial = []
        self.__total_infectados_por_dia = []

    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad

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
        for paso in range(pasos):
            self.__comunidad.simulacion_paso()
            self.guardar_estado(paso)
            #print("Simulación finalizada.") #Para verficar que pasa pero todo sigue igual :(
            
    def guardar_estado(self, paso):
        estado = []
        total_infectados = 0
        for ciudadano in self.__comunidad.get_ciudadanos():
            estado.append({
                'id': ciudadano.get_id(),
                'nombre': ciudadano.get_nombre(),
                'apellido': ciudadano.get_apellido(),
                'estado': ciudadano.get_estado(),
                'contador': ciudadano.get_contador()
            })
            if ciudadano.get_estado() == 'I':
                total_infectados += 1
        
        self.__historial.append(estado)
        self.__total_infectados_por_dia.append(total_infectados)
        self.guardar_csv(paso, estado)

    def guardar_csv(self, paso, estado):
        df = pd.DataFrame(estado)
        df.to_csv(f'estado_paso_{paso}.csv', index=False)

    def obtener_estado(self, paso):
        if 0 <= paso < len(self.__historial):
            return self.__historial[paso]
        else:
            return []
        
    def get_total_infectados_por_dia(self): 
       return self.__total_infectados_por_dia 

