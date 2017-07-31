import random

class PeckField:
    '''
    Status of chickens in one round: pecked (1) or not (0).
    '''

    def __init__(self, count = 100):
        '''
        count -- total number of chickens
        '''
        self.count = count
        self.field = [0] * count

    def peck(self, who, direction):
        '''
        who -- the index of the chiken who is pecking.
        If direction == 0 then he pecks previous chiken, otherwise the next
        '''

    def genField(self):
        '''
        Make all chikens peck one of random neighbour
        '''

    def result(self):
        '''
        Count pecked chikens.
        '''

class OutOfRangeError(ValueError):
    pass

class NotIntError(ValueError):
    pass
