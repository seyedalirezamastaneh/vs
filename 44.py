import turtle
import pygame
import random
import math


class square :

    def __init__(self,color,size,number,power,life,speed,location,angle):
         self.color = "red"
         self.size = 5*5
         self.number = "n" 
         self.Destroyer = triangle
         self.angle = random
         self.power = 4
         self.life = 4
         self.speed =  random
         self.location = random
class triangle:
      def __init__(self,color,size,number, Destroyer,angle,destruction):
         self.color = "blue"
         self.size = 3*3*3
         self.number = "m"
         self.Destroyer = rectangle
         self.angle = random
         self.power = 3
         self.life = 3
         self.speed =  random
         self.location =random
class rectangle:
    def __init__(self,color,size,number, Destroyer,angle,destruction):
         self.color = "yellow"
         self.size = 4*2
         self.number = "p"
         self.Destroyer = circle
         self.angle = random
         self.power = 5
         self.life = 5
         self.speed =  random
         self.location = random
class circle:    
    def __init__(self,color,size,number, Destroyer,angle,destruction):
         self.color = "blue"
         self.size =3
         self.number = "q"
         self.Destroyer = circle
         self.angle = random
         self.power = 6
         self.life = 6
         self.speed = random
         self.location = random
class method :
     def move(self,speed,angle,x,y):
        self.speed = 30
        self.angle = random
        self.location = random
    
        
