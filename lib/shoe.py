#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
        self.condition = 'Used'

    @property
    def shoe_size(self):
        return self.size
    
    @shoe_size.setter
    def shoe_size(self,size):
        if not isinstance(size, int):
            print('size must be an integer')
        else: 
            self.size = size

    def can_cobble(self):
        print("Your shoe has been repaired!")
        self.condition = 'New'
        return self