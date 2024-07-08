import numpy as np 
import random
from ciudadano import Ciudadano
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


    def infectar_familia(self, familia): 
        for ciudadano in familia: 
            if np.random.random() < self.__infeccion_probable: 
                ciudadano.infectar() 

    def contagiar(self, ciudadanos): 
        for ciudadano in ciudadanos: 
            if ciudadano.get_estado() == 'I': 
                for otro in ciudadanos: 
                    if ciudadano != otro and np.random.random() < self.__infeccion_probable: 
                        otro.infectar_familia() 

    def tiempo_recuperacion(self): 
        return int(np.random.gamma(self.__promedio_pasos, 1)) 

