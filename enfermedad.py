import numpy as np
import random
class Enfermedad(): #Define la enfermedad con la probabilidad de infección y el tiempo promedio de recuperación
    def __init__(self, infeccion_probable, promedio_pasos, gamma=0.5,enfermo=False, contador=0):

        self.__infeccion_probable = infeccion_probable
        self.__promedio_pasos = promedio_pasos
        self.__enfermo = enfermo
        self.__contador = contador
        self.__gamma = gamma   # Valor por defecto para gamma
    #Set y get para cada uno de los atributos privados de la clase

    def get_infeccion_probable(self):
        return self.__infeccion_probable

    def set_infeccion_probable(self, infeccion_probable):
        self.__infeccion_probable = infeccion_probable

    def get_promedio_pasos(self):
        return self.__promedio_pasos
    
    def set_promedio_pasos(self, promedio_pasos):
        self.__promedio_pasos = promedio_pasos

    def get_enfermo(self):
        return self.__enfermo

    def set_enfermo(self, enfermo):
        self.__enfermo = enfermo

    def get_infeccion_probable(self):
        return self.__infeccion_probable

    def set_infeccion_probable(self, infeccion_probable):
        self.__infeccion_probable = infeccion_probable

    def get_contador(self):
        return self.__contador

    def set_contador(self, contador):
        self.__contador = contador

    def get_gamma(self):
        return self.__gamma

    def set_gamma(self, gamma):
        self.__gamma = gamma







    #infectar muestra aleatoria de ciudadanos
    def infectar_familia(self, familia):
        for ciudadano in familia:
            if random.random() <self.enfermedad.get_infeccion_probable():
                ciudadano.infectar(self.get_enfermedad)
            #Compara el número aleatorio generado con la probabilidad de infección.
            #cambiar random.random

    def conexiones_aleatorias(self):
        for ciudadano in self.get_num_ciudadanos:
            for otro in self.get_num_ciudadanos:
                if ciudadano != otro and random.random() < self.get_promedio_conexion_fisica:
                    ciudadano.conectar(otro)

    

