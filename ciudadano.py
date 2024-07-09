import numpy as np 
import random
from enfermedad import Enfermedad

class Ciudadano():  #Representa a cada individuo en la simulación
    def __init__(self, id, nombre, apellido, comunidad, familia, enfermedad, estado, gamma=0.5):
        self.__id = id 
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__comunidad = comunidad 
        self.__familia = familia 
        self.__enfermedad = enfermedad
        self.__estado = estado  #'S': Susceptible, 'I': Infectado, 'R': Recuperado, Se agrega M, cuando muere
        self.__gamma = gamma #Tasa de recuperación
        self.__contador_pasos = 0

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

    def get_contador_pasos(self):
        return self.__contador_pasos

    def set_contador_pasos(self, contador_pasos):
        self.__contador_pasos = contador_pasos

    def get_gamma(self):
        return self.__gamma

    def set_gamma(self, gamma):
        self.__gamma = gamma
    
    def infectar(self):
        self.__estado = 'I'
        self.__contador_pasos = 0

    def recuperar(self):
        self.__estado = 'R'
        self.__contador_pasos = 0

    def morir(self):
        if self.__estado == 'I':
            self.__estado = 'M'  # Indicar estado de muerte

    def paso(self):
        if self.__estado == 'I':
            self.__contador_pasos += 1
            if np.random.normal() < self.__enfermedad.get_gamma():   #probabilidad gamma de que el individuo se recupere
                self.recuperar()
            elif np.random.normal() < self.__enfermedad.get_probabilidad_muerte():
                self.morir()

    def actualizar_estado(self):
        if self.__estado == 'I':
            self.__contador_pasos += 1
            if self.__contador_pasos >= self.__enfermedad.tiempo_recuperacion():
                if np.random.normal() < self.__enfermedad.get_probabilidad_recuperacion():
                    self.recuperar()
                elif np.random.normal() < self.__enfermedad.get_probabilidad_muerte():
                    self.morir()
            else:
                for otro in self.__familia:
                    if otro.get_estado() == 'S' and np.random.normal() < self.__enfermedad.get_infeccion_probable():
                        otro.infectar()
    #sugerencia del profe: usar random de numpy

    def representacion(self):
        return f"{self.__nombre} {self.__apellido}: {self.__estado}"
    


    