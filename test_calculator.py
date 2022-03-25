import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.x = 34
        self.y = 36
        print('Setup is Executed')
    def tearDown(self):
        self.x = 0
        self.y = 0
        print("TearDown is Executed")




    def test_add(self):

        result = Calculator.add(self.x,self.y)
        self.assertEqual(result, self.x+self.y)
    def test_sub(self):

        result = Calculator.sub(self.x,self.y)
        self.assertEqual(result, self.x-self.y)
    def test_mult(self):

        result = Calculator.mult(self.x,self.y)
        self.assertEqual(result, self.x*self.y)
    def test_div(self):

        result = Calculator.div(self.x,self.y)
        self.assertEqual(result, self.x/self.y)



if __name__=="__main__":
    unittest.main()