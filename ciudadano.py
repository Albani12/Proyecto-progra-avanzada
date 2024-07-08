import random
import numpy as np
class Ciudadano():  #Representa a cada individuo en la simulación
    def __init__(self, id, nombre, apellido, comunidad, familia, enfermedad, estado, gamma):
        self.__id = id 
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__comunidad = comunidad 
        self.__familia = familia 
        self.__enfermedad = enfermedad
        self.__estado = estado  #'S': Susceptible, 'I': Infectado, 'R': Recuperado
        self.__gamma = gamma
        self.__contador = 0

    #Set y get para atributo privado de la clase

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_comunidad(self):
        return self.__comunidad

    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad
    
    def get_familia(self):
        return self.__familia

    def set_familia(self, familia):
        self.__familia = familia

    def get_enfermedad(self):
        return self.__enfermedad

    def set_enfermedad(self, enfermedad):
        self.__enfermedad = enfermedad

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_contador(self):
        return self.__contador

    def set_contador(self, contador):
        self.__contador = contador
    
    def infectar(self):
        self.__estado = 'I'
        self.__contador = 0

    def recuperar(self):
        self.__estado = 'R'
        self.__contador = 0

    def get_gamma(self):
        return self.__gamma

    def set_gamma(self, gamma):
        self.__gamma = gamma

    def paso(self, gamma): #Gamma es la tasa de recuperacion
        if self.__estado == 'I':
            self.__contador += 1
            if np.random.random() < self.__gamma:  #probabilidad gamma de que el individuo se recupere
                self.recuperar()
            #sugerencia del profe: usar random de numpy

    def representacion(self):
        return f"{self.get_nombre} {self.get_apellido}: {self.get_estado}"
    
    
