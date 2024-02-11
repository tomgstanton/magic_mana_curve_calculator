import unittest

from calculator import ManaCurveCalculator

class InputLengthTestCase(unittest.TestCase):

    def test_ForTooFewInputs(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17)

    def test_ForTooManyInputs(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,40,60)

class TypesTestCase(unittest.TestCase):

    def test_ForNoneInput(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,None)
    
    def test_ForStringInput(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,str)

    def test_ForListInput(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,list)
    
    def test_ForSetInput(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,set)

    def test_ForFrozenSetInput(self):    
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,frozenset)

    def test_ForFloatInput(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,float)   
            
    def test_ForComplexInput(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(17,complex)
    
class ValuesTestCase(unittest.TestCase):

    def test_ForFewerLands(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(40,17)

    def test_ForMoreCardsThanInStartingHand(self):
        with self.assertRaises(Exception):
            ManaCurveCalculator(3,6)
            
class OutputsTestCase(unittest.TestCase):

    def test_ForOutputBeingAList(self):
        self.assertIsInstance(ManaCurveCalculator(17,40),list)

    def test_ForOutputToEqualNonLandCards(self):
        number_to_test = round(sum(ManaCurveCalculator(17,40)),5)
        self.assertEqual(number_to_test,23)

    def test_ForLengthOfOutput(self):
        number_to_test = len(ManaCurveCalculator(17,40))
        self.assertEqual(number_to_test,33)

if __name__ == '__main__':
    unittest.main()