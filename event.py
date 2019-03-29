import car as c

class Event:
    def __init__(self, name = "Event"):
        self.name = name
        
    def process(self, car):
        pass
        
    def define(self):
        pass

class Start(Event):
    def __init__(self):
        super().__init__("Start")

    def __str__(self):
        return "Event: {}".format(self.name)
        
    def define(self):
        pass

    def process(self, car):
        if isinstance(car, c.Car):
            if car.isEngineOn(): 
                print('WARNING:\tCar is already turn on.')
            print('ENGINE: Turn on.')
            car.engine_on = True

                
class End(Event):
    def __init__(self):
        super().__init__("End")

    def __str__(self):
        return "Event: {}".format(self.name)
    
    def define(self):
        pass

    def process(self, car):
        if isinstance(car, c.Car):
            if not car.isEngineOn(): 
                print('Car is already turn off.')
                return 
            if (car.speed != 0):
                print('WARNING:\tCar is in move, please slow down first.')
                return
            print('Engine is turning off...')
            car.engine_on = False               

class ChangeSpeed(Event):
    def __init__(self):
        super().__init__("ChangeSpeed")
        self.speed = 0

    def __str__(self):
        return "Event: {}".format(self.name)

    def define(self):
        self.speed = float(input('Gain speed: '))

    def process(self, car):
        if isinstance(car, c.Car):
            if car.isEngineOn(): 
                if car.speed + self.speed > car.speed_limit :
                    print('WARNING:\tCar will be moving to fast!')
                    return
                elif car.speed + self.speed < 0:
                    print('WARNING:\tCar is slowing down to fast!')
                    return
                car.speed += self.speed
            else:
                print('Turn car on first, please.')

class Turn(Event):
    def __init__(self):
        super().__init__("Turn")
        self.angle = 'None'

    def __str__(self):
        return "Event: {}".format(self.name)

    def define(self):
        self.angle = float(input('Angle: '))

    def process(self, car):
        if isinstance(car, c.Car):
            if car.isEngineOn(): 
                car.wheel_angle = self.angle
                