"""Class from leetcode to convert between roman and integer numbers."""


class Solution:
  """Class to be able to test the code on leetcode."""

  def roman_to_int(self, roman_str: str) -> int:
    """Converts a roman number to an integer."""
    conversion_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    int_list_sum = 0
    for i in range(len(roman_str) - 1):
      if conversion_table[roman_str[i + 1]] > conversion_table[roman_str[i]]:
        int_list_sum -= conversion_table[roman_str[i]]
        continue
      int_list_sum += conversion_table[roman_str[i]]
    int_list_sum += conversion_table[roman_str[-1]]

    return int_list_sum

  def do_something_else(self):
    """Second method to avoid the error of only having one method on the class."""
    print("Doing something else.")
