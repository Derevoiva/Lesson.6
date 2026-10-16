"""Lesson 6: corrected object-oriented exercises."""
from time import sleep

class TrafficLight:
    __colors = (("red",7),("yellow",2),("green",3))
    def running(self, wait=sleep):
        for color,seconds in self.__colors:
            yield color
            wait(seconds)

class Road:
    def __init__(self,length,width):
        if length < 0 or width < 0: raise ValueError("Dimensions must be non-negative")
        self._length,self._width = length,width
    def asphalt_tons(self, thickness_cm=5, kg_per_m2_cm=25):
        if thickness_cm < 0 or kg_per_m2_cm < 0: raise ValueError("Invalid layer")
        return self._length*self._width*thickness_cm*kg_per_m2_cm/1000

class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name,self.surname,self.position=name,surname,position
        self._income={"wage":wage,"bonus":bonus}
class Position(Worker):
    def get_full_name(self): return f"{self.name} {self.surname}"
    def get_total_income(self): return sum(self._income.values())

class Car:
    def __init__(self,speed,color,name,is_police=False):
        if speed < 0: raise ValueError("Negative speed")
        self.speed,self.color,self.name,self.is_police=speed,color,name,is_police
    def go(self): return f"{self.name} is moving"
    def stop(self): return f"{self.name} stopped"
    def turn(self,direction): return f"{self.name} turned {direction}"
    def show_speed(self): return f"{self.speed} km/h"
class TownCar(Car):
    def show_speed(self): return super().show_speed() + (" (speeding)" if self.speed > 60 else "")
class WorkCar(Car):
    def show_speed(self): return super().show_speed() + (" (speeding)" if self.speed > 40 else "")
class SportCar(Car): pass
class PoliceCar(Car): pass

class Stationery:
    def __init__(self,title): self.title=title
    def draw(self): return "Drawing started"
class Pen(Stationery):
    def draw(self): return f"Drawing with pen: {self.title}"
class Pencil(Stationery):
    def draw(self): return f"Drawing with pencil: {self.title}"
class Marker(Stationery):
    def draw(self): return f"Drawing with marker: {self.title}"
