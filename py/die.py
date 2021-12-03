from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides
        
    def roll_die(self, number_of_throws):
        self.number_of_throws = number_of_throws
        throws = 0
        numbers = []
        while number_of_throws != throws:
            number = randint(1, self.sides)
            numbers.append(number)
            throws += 1
        return numbers
