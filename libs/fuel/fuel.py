# -*- coding:utf-8 -*-
import threading

class Fuel():
    def __init__(self):
        self.fuel = 0;

    def add_fuel(self, addition):
        fuel_lock = threading.Lock()
        with fuel_lock:
            self.fuel += addition

