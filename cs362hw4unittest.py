import unittest
import cs362hw4

class testCaseCalc(unittest.TestCase):
    def test_1(self):
        result = cs362hw4.volume(3)
        self.assertEqual(result,27)
    def test_2(self):
        result = cs362hw4.volume(-3)
        self.assertEqual(result,"Please only enter a positive number")
    def test_3(self):
        result = cs362hw4.volume("three")
        self.assertEqual(result,"Please only enter positive integers") #This results in an error and shows the program must be edited
    def test_4(self):
        result = cs362hw4.volume(10.5) 
        self.assertEqual(result,1157.625) #This results in an error and shows the program must be edited
    def test_5(self):
        result = cs362hw4.avg([5, 9, 10])
        self.assertEqual(result,8) 
    def test_6(self):
       result = cs362hw4.avg([-1, 86])
       self.assertEqual(result,42.5) 
    def test_7(self):
        result = cs362hw4.avg([])
        self.assertEqual(result, "Please enter a list")  #This is an error that shows the program must be edited
    def test_8(self):
        result = cs362hw4.avg(["abc", "def"])
        self.assertEqual(result, "Please enter a list") #This is a fail and shows that this program must be edited
    def test_9(self):
        result = cs362hw4.name("John", "Smith")
        self.assertEqual(result,"John Smith") 
    def test_10(self):
        result = cs362hw4.name("5", "8")
        self.assertEqual(result,"5 8") 
    

if __name__ == '__main__':
    unittest.main();