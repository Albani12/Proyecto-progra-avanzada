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
        self.__ciudadanos = []
        self.__gamma = gamma
        self.__familias = []
        self.__subcomunidades = []
        
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

    def set_ciudadanos(self, ciudadano):
        self.__ciudadanos.append(ciudadano)

    def set_familias(self, familia):
        self.__familias.append(familia)

    def set_subcomunidades(self, subcomunidades):
        self.__subcomunidades = subcomunidades
    
    def get_subcomunidades(self):
        return self.__subcomunidades

    def get_gamma(self):
        return self.__gamma

    def set_gamma(self, gamma):
        self.__gamma = gamma

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
            self.set_ciudadanos(ciudadano)

        return ciudadanos

    def asignar_familias(self): #Divide a los ciudadanos en 50 familias de tamaño aleatorio (entre 2 y 5 personas)
        familias = []
        num_ciudadanos = len(self.__ciudadanos)
        ciudadanos_sin_familia = self.__ciudadanos[:]
        
        for i in range(num_ciudadanos // 5):  #Crear aproximadamente 200 familias
            tamaño_familia = np.random.randint(2, 5)  #Familias de 2 a 5 personas
            if len(ciudadanos_sin_familia) < tamaño_familia:
                tamaño_familia = len(ciudadanos_sin_familia)
                
            familia = np.random.choice(ciudadanos_sin_familia, tamaño_familia)
            for ciudadano in familia:
                ciudadano.set_familia(i)  #Asigna un identificador de familia a cada ciudadano
                #ciudadanos_sin_familia.remove(ciudadano)
            self.set_familias(familia)

        return familias
    
    def asignar_subcomunidades(self, promedio_personas_por_grupo):
        ciudadanos = self.__ciudadanos
        num_ciudadanos = len(ciudadanos)
        num_grupos = num_ciudadanos // promedio_personas_por_grupo
        subcomunidades = [[] for _ in range(num_grupos)]

        random.shuffle(ciudadanos)

        for i, ciudadano in enumerate(ciudadanos):
            grupo_index = i % num_grupos
            subcomunidades[grupo_index].append(ciudadano)

        self.__subcomunidades = subcomunidades

    #numero inicial de ciudadanos infectados en la comunidad
    def inicializar_infectados(self):
        num_infectados = min(self.__num_infectados, len(self.__ciudadanos))
        infectados = random.sample(self.__ciudadanos, num_infectados)
        for ciudadano in infectados:
            ciudadano.infectar(self.get_enfermedad())
        print(f"{num_infectados} ciudadanos infectados inicialmente.")  # Mensaje de depuración


    def interaccion_aleatoria(self): #Simula interacciones aleatorias entre los ciudadanos basadas en la probabilidad de conexión física,
                                    #si un ciudadano infectado interactúa con uno susceptible, este se contagia
        for ciudadano in self.__ciudadanos:
            if np.random.random() < self.__probabilidad_conexion_fisica:
                posibles_interactores = [otro for otro in self.__ciudadanos if otro != ciudadano]
                interactor = np.random.choice(posibles_interactores)
                if ciudadano.get_estado() == 'I' and interactor.get_estado() == 'S':
                    if np.random.random() < self.get_enfermedad().get_infeccion_probable():
                        interactor.infectar(self.get_enfermedad())

    def interaccion_familiar(self):   #interacciones dentro de las familias, donde los miembros 
                                      #pueden infectarse si un miembro infectado está presente
        for familia in self.__familias:
            for i in range(len(familia)):
                for j in range(i + 1, len(familia)):
                    persona1 = familia[i]
                    persona2 = familia[j]
                    if persona1.get_estado() == 'I' and persona2.get_estado() == 'S':
                        if np.random.random() < self.get_enfermedad().get_infeccion_probable():
                            persona2.infectar(self.get_enfermedad())
    
    
    def simulacion_paso(self):
        self.interaccion_aleatoria()
        self.interaccion_familiar()
        for subcomunidad in self.get_subcomunidades():
            for ciudadano in subcomunidad:
                if ciudadano.get_estado() == 'I':
                    for otro_ciudadano in random.sample(self.__ciudadanos, self.__promedio_conexion_fisica):
                        if otro_ciudadano.get_estado() == 'S' and random.random() < self.__enfermedad.get_infeccion_probable():
                            otro_ciudadano.infectar(self.get_enfermedad())
        # Actualizar estados de todos los ciudadanos después de las interacciones
        for ciudadano in self.__ciudadanos:
            ciudadano.actualizar_estado()


    def resultados(self):
        estados = {'S': 0, 'I': 0, 'R': 0, 'M': 0}
        for ciudadano in self.__ciudadanos:
            estados[ciudadano.get_estado()] += 1
        return estados

    def tiempo_recuperacion(self):
        #Utilizando una distribucion gamma para el tiempo de recuperación
        return int(np.random.gamma(self.__enfermedad.get_promedio_pasos(), 1))


#Al inicio, un número inicial de ciudadanos se infectan 
#En cada paso de la simulación, los ciudadanos se conectan aleatoriamente o entre familias y se contagian basados en la probabilidad de infección.
#Los ciudadanos infectados pueden recuperarse o morir 

