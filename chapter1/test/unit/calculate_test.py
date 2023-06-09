import unittest
from app.calculate import Calculate

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()
        
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        
    def test_add_method_raises_type_error_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "hello", "world")
        
    def test_assert_raises(self):
        with self.assertRaises(AttributeError):
            [].get

    def test_assert_dict_contains_subset(self):
        expected = {'a': 'b'}
        actual = {'a': 'b', 'c': 'd', 'e': 'f'}
        self.assertDictContainsSubset(expected, actual)
        

if __name__ == '__main__':
    unittest.main()