"""Integration tests for the solution class."""
from unittest import TestCase
from roman_to_integer import Solution


class TestRomanToInteger(TestCase):
  def setUp(self) -> None:
    self.sol_instance = Solution()
    return super().setUp()

  def test_conversions(self):
    """Test case"""

    self.assertEqual(self.sol_instance.roman_to_int("I"), 1)
    self.assertEqual(self.sol_instance.roman_to_int("V"), 5)
    self.assertEqual(self.sol_instance.roman_to_int("X"), 10)
    self.assertEqual(self.sol_instance.roman_to_int("L"), 50)
    self.assertEqual(self.sol_instance.roman_to_int("C"), 100)
    self.assertEqual(self.sol_instance.roman_to_int("D"), 500)
    self.assertEqual(self.sol_instance.roman_to_int("M"), 1000)

  def test_addition(self):
    """Test case"""
    self.assertEqual(self.sol_instance.roman_to_int("MXI"), 1011)

  def test_subtraction(self):
    """Test case"""
    self.assertEqual(self.sol_instance.roman_to_int("MIX"), 1009)

  def test_extra(self):
    """Test case"""
    self.assertEqual(self.sol_instance.roman_to_int("MX"), 1010)
    self.assertEqual(self.sol_instance.roman_to_int("XM"), 990)
