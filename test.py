import unittest
from util import Util
from students import Student

class MyTestCase(unittest.TestCase):
    def test_addUser(self):
        exp1 = "diwa"
        act1 = Student.addUser("diwa",80)
        self.assertEqual(exp1,act1)
    def test_getScore(self):
        exp2 = 90
        act2 = Util.getScore("diwakar")
        self.assertEqual(exp2,act2)
    def test_display(self):
        exp3 = None
        act3 = Student.display()
        self.assertEqual(exp3,act3)

if __name__ == '__main__':
    unittest.main()
