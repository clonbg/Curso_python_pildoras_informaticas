#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:35:00 2019

@author: clonbg
"""


class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugar_residencia

    def mostrar(self):
        print("Nombre: ", self.nombre, "Edad: ",
              self.edad, "Nacido en: ", self.lugar)


class Empleado(Persona):
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, lugar_empleado):
        super().__init__(nombre_empleado, edad_empleado, lugar_empleado)
        self.salario = salario
        self.antigüedad = antigüedad
    
    def mostrar(self):
        super().mostrar()
        print("Salario: ",self.salario,"Antigüedad: ",self.antigüedad)

Persona1 = Persona("Manuel", 32, "Valencia")
Persona1.mostrar()

Empleado1 = Empleado(1300, 23, "Lucas", 56, "Vitoria")
Empleado1.mostrar()

print(isinstance(Empleado1,Empleado))
print(isinstance(Persona1, Persona))
print(isinstance(Empleado1,Persona))
print(isinstance(Persona1, Empleado))