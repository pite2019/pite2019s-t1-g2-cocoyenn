import event

class Car:
    def __init__(self):
        self.speed = 0.0
        self.wheel_angle = '0.0'
        self.engine_on = False;
        self.speed_limit = 120.0

    def act(self, evn):
        if isinstance(evn, event.Event):
            print(evn)
            evn.process(self)
        else:
            print('Unknown event.')

    def __str__(self):
        return "\tCar status: \n\tENGINE ON: {}\n\tSPEED: {}\n\tWHEEL ANGLE: {} ".format(self.engine_on, self.speed, self.wheel_angle)

    def isEngineOn(self):
        return self.engine_on