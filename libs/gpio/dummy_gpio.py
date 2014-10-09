# -*- coding:utf-8 -*-

class DummyGpio:
    def __init__(self):
        self.state = 'OFF'
        print "init GPIO"

    def on(self):
        try:
            self.state = 'ON'
            print "turn ON"
        except KeyboardInterrupt:
            print "turn OFF"
            self.state = 'OFF'

    def off(self):
        try:
            self.state = 'OFF'
            print "turned OFF"
        except KeyboardInterrupt:
            print "turn ON"
            self.state = 'ON'


