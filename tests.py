import PeckField
import unittest

class Tests(unittest.TestCase):
    def testInit(self):
        '''Test initialization of the class'''
        f = PeckField.PeckField()
        self.assertEqual(len(f.field), 100)
        self.assertEqual(f.count, 100)
        f = PeckField.PeckField(5)
        self.assertEqual(len(f.field), 5)
        self.assertEqual(f.count, 5)
        self.assertEqual(f.field, [0, 0, 0, 0, 0])
        self.assertRaises(PeckField.OutOfRangeError, PeckField.PeckField, 0)
        self.assertRaises(PeckField.OutOfRangeError, PeckField.PeckField, 1)
        self.assertRaises(PeckField.OutOfRangeError, PeckField.PeckField, -1)
        self.assertRaises(PeckField.NotIntError, PeckField.PeckField, 10.5)
        self.assertRaises(PeckField.NotIntError, PeckField.PeckField, '')
        self.assertRaises(PeckField.NotIntError, PeckField.PeckField, 'abc')
        self.assertRaises(PeckField.NotIntError, PeckField.PeckField, [1, 2])

    def testPeck(self):
        '''Test single pecks'''
        f = PeckField.PeckField(5)
        f.peck(3, 0)
        self.assertEqual(f.field, [0, 0, 1, 0, 0])
        f.peck(4, 1)
        self.assertEqual(f.field, [1, 0, 1, 0, 0])
        f.peck(2, 1)
        self.assertEqual(f.field, [1, 0, 1, 0, 0])
        f.peck(0, 0)
        self.assertEqual(f.field, [1, 0, 1, 0, 1])

    def testGenField(self):
        '''Generated fields must be random'''
        f1 = PeckField.PeckField()
        f2 = PeckField.PeckField()
        f1.genField()
        f2.genField()
        self.assertEqual(f1 == f2, False)
        f2 = f1
        f2.genField()
        self.assertEqual(f1 == f2, False)

    def result(self):
        '''Test result counting'''
        f = PeckField.PeckField(5)
        f.field = [1, 1, 1, 0, 0]
        self.assertEqual(f.result(), 3)
        f.field = [0, 0, 0, 0, 0]
        self.assertEqual(f.result(), 0)
        f.field = [0, 0, 0, 0, 1]
        self.assertEqual(f.result(), 1)
        f.field = [1, 1, 1, 1, 1]
        self.assertEqual(f.result(), 5)

if __name__ == '__main__':
    unittest.main()
