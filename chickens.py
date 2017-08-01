import random

class Chickens:
    '''
    This class simulates chickens behaviour.
    '''

    def __init__(self, count = 100):
        '''
        count -- total number of chickens
        '''
        if type(count) is not int:
            raise NotIntError('Number of chickens must be integer.')

        if count < 2:
            raise OutOfRangeError('Number of chickens must be greater or '
                + 'equal to 2.')

        self.count = count
        self.field = [0] * count

    def peck(self, who, direction):
        '''
        One peck from one chicken.
        who -- the index of the chicken who is pecking.
        If direction == 0 then he pecks previous chicken, otherwise the next
        '''
        if direction == 1:
            if who == self.count - 1:
                self.field[0] = 1
            else:
                self.field[who + 1] = 1
        elif direction == 0:
            if who == 0:
                self.field[self.count - 1] = 1
            else:
                self.field[who - 1] = 1

    def gen_rounds(self):
        '''
        Make all chickens peck a random neighbour
        '''
        while True:
            self.field = [0] * self.count
            for i in range(self.count):
                self.peck(i, random.getrandbits(1))
            yield self

    def result(self):
        '''
        Count unpecked chickens.
        '''
        return self.field.count(0)

class OutOfRangeError(ValueError):
    pass

class NotIntError(ValueError):
    pass
