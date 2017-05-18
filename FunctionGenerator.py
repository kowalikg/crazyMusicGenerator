import math
from random import randint

class FunctionGenerator:
    trigonometric_list = [math.sin, math.cos, math.atan] #shared with all FunctionGenerator objects

    def __init__(self, x0_range, x0_max_count):
        self.x0_range = x0_range
        self.x0_max_count = x0_max_count

    def generate_function(self):

        x0_amount = randint(1, self.x0_max_count) #how many x0's

        zero_places = self.generate_zero_places(x0_amount)
        trigonometric_function = self.trigonometric_list[randint(0, len(self.trigonometric_list) - 1)] #which trg function

        def function(x): #function to return
            result = trigonometric_function(math.radians(x))

            for x0 in zero_places:
                result *= (x-x0)
            return result

        return function

    def generate_zero_places(self, x0_amount):
        zero_places = []
        for x0 in range(0, x0_amount):
            x = randint(-self.x0_range, self.x0_range)
            zero_places.append(x)
        return zero_places

