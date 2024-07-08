import random
import csv
import numpy as np
#Gestiona la población de ciudadanos, las conexiones entre ellos, y la propagación y recuperación de la enfermedad 
class Comunidad():
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica, ciudadanos, gamma):
        self.__num_ciudadanos = num_ciudadanos
        self.__promedio_conexion_fisica = promedio_conexion_fisica 
        self.__enfermedad = enfermedad 
        self.__num_infectados = num_infectados 
        self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.__ciudadanos = ciudadanos
        

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

    

    def crear_ciudadanos():
        # Lista de nombres y apellidos
        nombres = []
        apellidos = []

        #Generar 1000 nombres y apellidos aleatorios
        nombres_aleatorios = random.choices(nombres, k =1000)
        apellidos_aleatorios = random.choices(apellidos, k =1000)

        #Crear lista de nombres y apellidos combinados
        nombres_apellidos = list(zip(nombres_aleatorios , apellidos_aleatorios))

        #Escribir los nombres y apellidos en un archivo CSV
        with open ("nombres_apellidos.csv","w",newline = "" ) as file :
            writer = csv.writer(file)
            writer.writerow(["nombre","apellido"])
            writer.writerows(nombres_apellidos )

        print("Archivo CSV generado con exito")

    

    def asignar_familias(self): #Divide a los ciudadanos en 50 familias de tamaño aleatorio (entre 2 y 5 personas)
        familias = []
        for i in range(50):  #50 familias
            familia = random.sample(self.get_num_ciudadanos, k=random.randint(2, 5))  #Familias de 2 a 5 personas
            for ciudadano in familia: 
                ciudadano.set_familia = i  #Asignar un identificador de familia a cada ciudadano
            familias.append(familia)

    
    def simular_interaccion_fisica(self):
        for ciudadano in self.__ciudadanos:
            if random.random() < self.__promedio_conexion_fisica * self.__probabilidad_conexion_fisica:
                otra_persona = random.choice(self.__ciudadanos)
                self.interactuar_persona(ciudadano, otra_persona)

    def interactuar_persona(self, persona1, persona2):
        if persona1.get_estado() == 'I' and persona2.get_estado() == 'S':
            if random.random() < persona1.get_enfermedad().get_infeccion_probable():
                persona2.infectar()

    def recuperar_infectados(self):
        for ciudadano in self.__ciudadanos:
            ciudadano.paso()

    
    def tiempo_recuperacion(self):
        return int(np.random.gamma(self.get_promedio_pasos, 1))


    def contagiar(self):
        for ciudadano in self.__ciudadanos:
            if ciudadano.get_estado() == 'I':
                for otro in self.__ciudadanos:
                    if ciudadano != otro and np.random.random() < self.__enfermedad.get_infeccion_probable():
                        otro.infectar()

    def simulacion_paso(self):
        self.contagiar()
        self.recuperar_infectados()




        


