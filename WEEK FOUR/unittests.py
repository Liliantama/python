##Write a program with a function that multiplies two numbers. Create a unit test that checks if the function returns the correct sum for different input values.


def multiply(a, b):
    return a * b

import unittests
from unittests import multiply

class TestMultiply(unittests):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3))

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3))

    def test_multiply_positive_and_negative_numbers(self):
        self.assertEqual(multiply(-2, 3))

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 5))
        self.assertEqual(multiply(5, 0))

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.0))
        self.assertAlmostEqual(multiply(-2.5, 4.0))

if __name__ == '__main__':
    unittests.main()


    ##Write a program with a function that removes all vowels from a string. Create a unit test that verifies the function removes vowels and keeps consonants for different input strings.
    def remove_vowels(input_string):
     vowels = 'aeiouAEIOU'
     return ''.join([char for char in input_string if char not in vowels])
    
    import unittest

class TestRemoveVowels(unittest.TestCase):

    def test_remove_vowels_all_vowels(self):
        self.assertEqual(remove_vowels("aeiouAEIOU"), "")

    def test_remove_vowels_no_vowels(self):
        self.assertEqual(remove_vowels("bcdfg"), "bcdfg")

    def test_remove_vowels_mixed_case(self):
        self.assertEqual(remove_vowels("Hello World"), "Hll Wrld")

    def test_remove_vowels_with_numbers(self):
        self.assertEqual(remove_vowels("Python 3.8"), "Pythn 3.8")

    def test_remove_vowels_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_remove_vowels_special_characters(self):
        self.assertEqual(remove_vowels("Hello, World!"), "Hll, Wrld!")

if __name__ == '__main__':
    unittest.main()