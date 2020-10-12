from unittest import TestCase, skip
from demo.demo import add_numbers, multiply_numbers


@skip
class TestFunctionsFail(TestCase):

    def test_add(self):
        """Test add numbers fails."""
        result = add_numbers(1, 2)
        self.assertEqual(result, 0)

    def test_multiply(self):
        """Test multiply numbers fails."""
        result = multiply_numbers(1, 2)
        self.assertEqual(result, 0)
