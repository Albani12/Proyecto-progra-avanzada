import random
import csv

class Comunidad():
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica, ciudadanos, gamma):
        self.__num_ciudadanos = num_ciudadanos
        self.__promedio_conexion_fisica = promedio_conexion_fisica
        self.__enfermedad = enfermedad
        self.__num_infectados = num_infectados
        self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.__ciudadanos = self.crear_ciudadanos()
        self.__gamma = gamma

    #Set y get para cada atributo privado de la clase...
    def get_num_ciudadanos(self):
        return self.__num_ciudadanos

    def set_num_ciudadanos(self, num_ciudadanos):
        self.__num_ciudadanos = num_ciudadanos

    def get_enfermedad(self):
        return self.__enfermedad

    def set_enfermedad(self, enfermedad):
        self.__enfermedad = enfermedad

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
                ciudadano.familia = i  #Asignar un identificador de familia a cada ciudadano
            familias.append(familia)

    #infectar muestra aleatoria de ciudadanos
    def infectar_familia(self, familia):
        for ciudadano in familia:
            if random.random() <self.enfermedad.get_infeccion_probable():
                ciudadano.infectar(self.get_enfermedad)
            #Compara el número aleatorio generado con la probabilidad de infección.
            #cambiar random.random

    def simular_paso():
        pass
        #avance en el tiempo, por dia
        #Simular la propagación de la enfermedad por la comunidad


