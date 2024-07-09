import numpy as np 
import random
from ciudadano import Ciudadano

class Enfermedad(): #Define la enfermedad con la probabilidad de infección y el tiempo promedio de recuperación
    def __init__(self, infeccion_probable, promedio_pasos, probabilidad_muerte, probabilidad_recuperacion, enfermo=False, contador=0):

        self.__infeccion_probable = infeccion_probable
        self.__promedio_pasos = promedio_pasos
        self.__enfermo = enfermo
        self.__contador = contador
        self.__probabilidad_recuperacion = probabilidad_recuperacion
        self.__probabilidad_muerte = probabilidad_muerte
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

    def get_contador(self):
        return self.__contador

    def set_contador(self, contador):
        self.__contador = contador

    def get_infeccion_probable(self):
        return self.__infeccion_probable
    
    def set_infeccion_probable(self, infeccion_probable):
        self.__infeccion_probable= infeccion_probable

    def get_probabilidad_recuperacion(self):
        return self.__probabilidad_recuperacion
    
    def set_probabilidad_recuperacion(self, probabilidad_recuperacion):
        self.__probabilidad_recuperacion = probabilidad_recuperacion

    def get_probabilidad_muerte(self):
        return self.__probabilidad_muerte
    
    def set_probabilidad_muerte(self, probabilidad_muerte):
        self.__probabilidad_muerte = probabilidad_muerte


    def infectar_familia(self, familia): #Para los contactos estrechos
        #Infecta una familia completa con la probabilidad de infección de la enfermedad
        for ciudadano in familia:
            if np.random.random() < self.__infeccion_probable:
                ciudadano.infectar()

    def contagiar(self, ciudadanos): #Para los contactos aleatorios
        #Método para contagiar a otros ciudadanos en base a la probabilidad de infección
        for ciudadano in ciudadanos:
            if ciudadano.get_estado() == 'I':
                for otro in ciudadanos:
                    if ciudadano != otro and np.random.random() < self.__infeccion_probable:
                        otro.infectar()

    def probabilidad_infeccion(self):
        #Devuelve la probabilidad de infección de la enfermedad
        return self.__infeccion_probable

    def probabilidad_recuperacion(self):
        # Devuelve la probabilidad de recuperación de la enfermedad
        return self.__probabilidad_recuperacion
    
    def tiempo_recuperacion(self):
        # Devuelve el tiempo de recuperación basado en una distribución normal
        return int(np.random.normal(self.__promedio_pasos, 1))

    def probabilidad_muerte(self):
        # Devuelve la probabilidad de muerte de la enfermedad
        return self.__probabilidad_muerte

