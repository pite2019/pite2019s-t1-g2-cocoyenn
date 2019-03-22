# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository. 
#
#Delete these comments before commit!
#Good luck.

class Event:
    def __init__(self,name= "", time = 0):
        self.name = name
        self.time = time
         
class Car:
    def __init__(self):
        self.speed = 0
        self.wheel_angle = 0
        self.startMode = False;
        self.action = ['start', 'gainSpeed', 'obstacle', 'turn',]

    def act(self, event):
        if event.name in self.action:
            print(event.name)
            if event.name is 'start':
                self.startMode = True
            if event.name is 'gainSpeed':
                self.speed += 10
        else:
            print('Unknown event.')
            
def eventLoop():
    car = Car()
    while True:
        print("If you want to quit a program, press q")
        event = Event()
        event.name = raw_input('Please write a name of event:  ')
        if event.name is "q":
            break
        event.time = int(raw_input('Please give information about how long event would be: '))
        car.act(event)
        print(car.speed)
        
eventLoop()

