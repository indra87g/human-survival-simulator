import unittest
from lib.classes.humanClass import Human

class TestUnit(unittest.TestCase):
    def test(self):
        name = 'John'
        human1 = Human(name)
              
if __name__ == '__main__':
    unittest.main()