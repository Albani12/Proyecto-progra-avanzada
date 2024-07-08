import random
import csv
import numpy as np
from ciudadano import Ciudadano
#Gestiona la población de ciudadanos, las conexiones entre ellos, y la propagación y recuperación de la enfermedad 
class Comunidad():
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica, ciudadanos,gamma):
        self.__num_ciudadanos = num_ciudadanos
        self.__promedio_conexion_fisica = promedio_conexion_fisica 
        self.__enfermedad = enfermedad 
        self.__num_infectados = num_infectados 
        self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.__ciudadanos = ciudadanos 
        self.__gamma = gamma
        self.__familias = {} 
        self.familias = self.asignar_familias()
        
    #Set y get para cada atributo privado de la clase
    def get_num_ciudadanos(self):
        return self.__num_ciudadanos

    def set_num_ciudadanos(self, num_ciudadanos):
        self.__num_ciudadanos = num_ciudadanos

    def get_promedio_conexion_fisica(self):
        return self.__promedio_conexion_fisica

    def set_promedio_conexion_fisica(self, promedio_conexion_fisica):
        self.__promedio_conexion_fisica = promedio_conexion_fisica
    
    def get_enfermedad(self):
        return self.__enfermedad

    def set_enfermedad(self, enfermedad):
        self.__enfermedad = enfermedad

    def get_num_infectados(self):
        return self.__num_infectados

    def set_num_infectados(self, num_infectados):
        self.__num_infectados = num_infectados

    def get_probabilidad_conexion_fisica(self):
        return self.__probabilidad_conexion_fisica

    def set_probabilidad_conexion_fisica(self, probabilidad_conexion_fisica):
        self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica

    def get_ciudadanos(self):
        return self.__ciudadanos

    def set_ciudadanos(self, ciudadanos):
        self.__ciudadanos = ciudadanos

    
    def crear_ciudadanos(self):
        nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Carla"] 
        apellidos = ["Perez", "Gomez", "Rodriguez", "Fernandez", "Martinez"]
        
        nombres_aleatorios = random.choices(nombres, k=1000)
        apellidos_aleatorios = random.choices(apellidos, k=1000)
        nombres_apellidos = list(zip(nombres_aleatorios, apellidos_aleatorios))

        with open("nombres_apellidos.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "apellido"])
            writer.writerows(nombres_apellidos)

        print("Archivo CSV generado con éxito")

        ciudadanos = []
        
        for i in range(1000):
            nombre = nombres_aleatorios[i]
            apellido = apellidos_aleatorios[i]
            ciudadano = Ciudadano(id=i+1, nombre=nombre, apellido=apellido, comunidad=self, familia=None, enfermedad=None, estado='S', gamma=None)
            ciudadanos.append(ciudadano)

        return ciudadanos


    def asignar_familias(self): ##Divide a los ciudadanos en 50 familias de tamaño aleatorio (entre 2 y 5 personas)
        familias = []
        num_ciudadanos = len(self.__ciudadanos)
        ciudadanos_sin_familia = self.__ciudadanos[:]
        
        for i in range(50):
            tamaño_familia = np.random.randint(2, 5)
            if len(ciudadanos_sin_familia) < tamaño_familia:
                tamaño_familia = len(ciudadanos_sin_familia)
                
            familia = np.random.choice(ciudadanos_sin_familia, size=tamaño_familia, replace=False).tolist()
            for ciudadano in familia:
                ciudadano.set_familia(i)   #Asignar un identificador de familia a cada ciudadano
                ciudadanos_sin_familia.remove(ciudadano)
                
            familias.append(familia)

        return familias

    def inicializar_infectados(self):
        infectados = np.random.choice(self.__ciudadanos, size=self.__num_infectados, replace=False)
        for ciudadano in infectados:
            ciudadano.infectar()

    def conexiones_aleatorias(self):
        for ciudadano in self.__ciudadanos:
            if ciudadano.get_estado() != 'D':  # No interactuar si está muerto
                for otro in np.random.choice(self.__ciudadanos, size=self.__num_ciudadanos, replace=True):
                    if ciudadano != otro and np.random.random() < self.__promedio_conexion_fisica:
                        self.interactuar_persona(ciudadano, otro)

    def interactuar_persona(self, persona1, persona2):
        if persona1.get_estado() == 'I' and persona2.get_estado() == 'S':
            if np.random.random() < persona1.get_enfermedad().get_infeccion_probable():
                persona2.infectar()

    def recuperar_infectados(self):
        for ciudadano in self.__ciudadanos:
            if ciudadano.get_estado() == 'I':
                if np.random.random() < ciudadano.get_enfermedad().get_probabilidad_recuperacion():
                    ciudadano.recuperar()
                elif np.random.random() < ciudadano.get_enfermedad().get_probabilidad_muerte():
                    self.eliminar_ciudadano(ciudadano)


    def contagiar(self):
        for ciudadano in self.__ciudadanos:
            if ciudadano.get_estado() == 'I':
                for otro in self.__ciudadanos:
                    if ciudadano != otro and np.random.random() < ciudadano.get_enfermedad().get_infeccion_probable():
                        otro.infectar()

    def simulacion_paso(self):
        self.conexiones_aleatorias()
        self.contagiar()
        self.recuperar_infectados()

    def tiempo_recuperacion(self):
         # Utilizando una distribución gamma para el tiempo de recuperación
         return int(np.random.gamma(self.__enfermedad.get_promedio_pasos(), 1))

    def resultados(self):
        estados = {'S': 0, 'I': 0, 'R': 0, 'D': 0}
        for ciudadano in self.__ciudadanos:
            estados[ciudadano.get_estado()] += 1
        return estados

        

#Al inicio, un número inicial de ciudadanos se infectan 
#En cada paso de la simulación, los ciudadanos se conectan aleatoriamente y se contagian basados en la probabilidad de infección.
#Los ciudadanos infectados pueden recuperarse o morir 