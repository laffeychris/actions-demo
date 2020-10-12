from unittest import TestCase
from demo.demo import add_numbers, multiply_numbers


class TestFunctionsPass(TestCase):

    def test_add(self):
        """Test add numbers passes."""
        result = add_numbers(1, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        """Test multiply numbers passes."""
        result = multiply_numbers(1, 2)
        self.assertEqual(result, 2)
