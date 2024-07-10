import pandas as pd
from comunidad import Comunidad

class Simulador:
    def __init__(self, comunidad, historial):
        self.__comunidad = comunidad
        self.__historial = []
        self.__total_infectados_por_dia = []
        print("Simulador inicializado.")  # Mensaje de depuracion

    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad
        print("Comunidad establecida.")  # Mensaje de depuracion

    def get_comunidad(self):
        return self.__comunidad
    
    # def set_historial(self, historial):
    #     self.__historial = historial

    def get_historial(self):
        return self.__historial
    
    def set_total_infectados_por_dia(self, total_infectados_por_dia):
        self.__total_infectados_por_dia = total_infectados_por_dia
    
    def get_total_infectados_por_dia(self):
        return self.__total_infectados_por_dia

    def inicio_simulacion(self, pasos):
        for _ in range(pasos):
            self.__comunidad.simulacion_paso()
            estado_actual = self.obtener_estado_actual()
            self.__historial.append(estado_actual)
            total_infectados = sum(1 for ciudadano in self.__comunidad.get_ciudadanos() if ciudadano.get_estado() == 'I')
            self.__total_infectados_por_dia.append(total_infectados)
            self.guardar_estado(len(self.__historial) - 1)
            print(f"Estado guardado para el paso {len(self.__historial) - 1}: {total_infectados} infectados.")
        
        print("Simulación finalizada.")

    def guardar_estado(self, paso):
        estado = []
        total_infectados = 0
        ciudadanos = self.__comunidad.get_ciudadanos()

        for ciudadano in ciudadanos:
            estado_ciudadano = {
                'id': ciudadano.get_id(),
                'nombre': ciudadano.get_nombre(),
                'apellido': ciudadano.get_apellido(),
                'estado': ciudadano.get_estado(),
                'contador': 0  # Valor por defecto si el ciudadano no tiene enfermedad asignada
            }
            enfermedad = ciudadano.get_enfermedad()
        if enfermedad is not None:
            estado_ciudadano['contador'] = enfermedad.get_contador()

        estado.append(estado_ciudadano)

        if ciudadano.get_estado() == 'I':
            total_infectados += 1

        if paso < len(self.__historial):
            self.__historial[paso] = estado
        else:
            self.__historial.append(estado)

        if paso < len(self.__total_infectados_por_dia):
            self.__total_infectados_por_dia[paso] = total_infectados
        else:
            self.__total_infectados_por_dia.extend([0] * (paso - len(self.__total_infectados_por_dia) + 1))
            self.__total_infectados_por_dia[paso] = total_infectados

        print(f"Estado guardado para el paso {paso}: {total_infectados} infectados.")  # Mensaje de depuración
        self.guardar_csv(paso, estado)

    def guardar_csv(self, paso, estado):
        df = pd.DataFrame(estado)
        filename = f'estado_paso_{paso}.csv'
        df.to_csv(filename, index=False)
        print(f"CSV guardado: {filename}")  #Mensaje de depuracion

    def obtener_estado_actual(self):  # Método privado para obtener el estado actual
        estado = []
        for ciudadano in self.__comunidad.get_ciudadanos():
            estado.append({
                'nombre': ciudadano.get_nombre(),
                'apellido': ciudadano.get_apellido(),
                'estado': ciudadano.get_estado()
            })
        print(self.__comunidad.get_ciudadanos())
        return estado

    def obtener_estado(self, paso): 
        # print("paso", paso)
        # print(self.__historial)
        if 0 <= paso < len(self.__historial):
            print(f"Obteniendo estado para el paso {paso}.")  #Mensaje de depuracion
            return self.__historial[paso]
        else:
            print(f"Paso {paso} fuera de rango.")  #Mensaje de depuracion
            return []
    