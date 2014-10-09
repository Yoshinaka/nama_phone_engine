# -*- coding:utf-8 -*-
import threading

class Fuel():
    def __init__(self):
        self.fuel = 0;

    def add_fuel(self, addition):
        fuel_lock = threading.Lock()
        with fuel_lock:
            self.fuel += addition

    def give_fuel(self):
        given_fuel = self.fuel
        fuel_lock = threading.Lock()
        with fuel_lock:
            self.fuel = 0
            print "Fuel is given."
        return given_fuel

