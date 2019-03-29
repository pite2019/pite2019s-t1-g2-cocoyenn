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

from car import Car
import event as evn

def print_defined_events():
    pass

def program_end_check():
    return input("If you want to quit a program, type 'quit'...\t") == "quit"


def event_creator():
    print('Select next event: ')
    name = input("\tEvent name: ")
    if name == 'Start':
        return evn.Start()
    if name == 'End':
        return evn.End()   
    if name == 'Speed':
        return evn.ChangeSpeed()
    if name == 'Turn':
        return evn.Turn()           
    else:
        return 0

if __name__ == "__main__":
    c = Car()
    print("Initial parametrs:\n", c)
    event = evn.Event
    while True:
        if program_end_check():
            break
        event = event_creator()
        if isinstance(event, evn.Event):
            event.define()
        c.act(event)
        print(c)
        


