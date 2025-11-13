#!/usr/bin/env python3

class Person:
    # Class body goes here
    def talk(self):
        print("Hello World!")
    

    #Instance method definition
    def walk(self):
        print("The person is walking.")
    
hillary = Person()
hillary.talk()  # Hello World!
hillary.walk()  # The person is walking.
