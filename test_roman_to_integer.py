"""Integration tests for the solution class."""
from roman_to_integer import Solution


def test_solution():
  """Tests the Solution class."""
  sol_instance = Solution()
  assert sol_instance.roman_to_int("MXI") == 1011
  assert sol_instance.roman_to_int("MIX") == 1009
  assert sol_instance.roman_to_int("I") == 1
  assert sol_instance.roman_to_int("V") == 5
  assert sol_instance.roman_to_int("X") == 10
  assert sol_instance.roman_to_int("L") == 50
  assert sol_instance.roman_to_int("C") == 100
  assert sol_instance.roman_to_int("D") == 500
  assert sol_instance.roman_to_int("M") == 10000
