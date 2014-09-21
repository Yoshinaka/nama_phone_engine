
class Gpio:
    def __init__(self):
        self.state = 'off'
        print "init GPIO"

    def on(self):
        print "turn on"

    def off(self):
        print "turn off"

if __name__ == '__main__':
    print "HELLO"

