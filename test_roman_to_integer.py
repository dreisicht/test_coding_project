"""Integration tests for the solution class."""
from roman_to_integer import Solution


def test_solution():
  """Tests the Solution class."""
  sol_instance = Solution()
  print(sol_instance.roman_to_int("MXI") == 1011)
  print(sol_instance.roman_to_int("MIX") == 1009)
