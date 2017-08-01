import chickens
import unittest

class Tests(unittest.TestCase):
    def test_init(self):
        '''Test initialization of the class'''
        c = chickens.Chickens()
        self.assertEqual(len(c.field), 100)
        self.assertEqual(c.count, 100)
        c = chickens.Chickens(5)
        self.assertEqual(len(c.field), 5)
        self.assertEqual(c.count, 5)
        self.assertEqual(c.field, [0, 0, 0, 0, 0])
        self.assertRaises(chickens.OutOfRangeError, chickens.Chickens, 0)
        self.assertRaises(chickens.OutOfRangeError, chickens.Chickens, 1)
        self.assertRaises(chickens.OutOfRangeError, chickens.Chickens, -1)
        self.assertRaises(chickens.NotIntError, chickens.Chickens, 10.5)
        self.assertRaises(chickens.NotIntError, chickens.Chickens, '')
        self.assertRaises(chickens.NotIntError, chickens.Chickens, 'abc')
        self.assertRaises(chickens.NotIntError, chickens.Chickens, [1, 2])

    def test_peck(self):
        '''Test single pecks'''
        c = chickens.Chickens(5)
        c.peck(3, 0)
        self.assertEqual(c.field, [0, 0, 1, 0, 0])
        c.peck(4, 1)
        self.assertEqual(c.field, [1, 0, 1, 0, 0])
        c.peck(2, 1)
        self.assertEqual(c.field, [1, 0, 1, 1, 0])
        c.peck(1, 1)
        self.assertEqual(c.field, [1, 0, 1, 1, 0])
        c.peck(0, 0)
        self.assertEqual(c.field, [1, 0, 1, 1, 1])

    def test_randomness(self):
        '''Generated fields must be random'''
        c = chickens.Chickens()
        gen = c.gen_rounds()
        first = list(next(gen).field)
        second = list(next(gen).field)
        self.assertEqual(first != second, True)

    def test_result(self):
        '''Test counting of unpecked chikens'''
        c = chickens.Chickens(5)
        c.field = [1, 1, 1, 0, 0]
        self.assertEqual(c.result(), 2)
        c.field = [0, 0, 0, 0, 0]
        self.assertEqual(c.result(), 5)
        c.field = [0, 0, 0, 0, 1]
        self.assertEqual(c.result(), 4)
        c.field = [1, 1, 1, 1, 1]
        self.assertEqual(c.result(), 0)

if __name__ == '__main__':
    unittest.main()
