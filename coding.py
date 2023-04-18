class Solution:

  def __init__(self):
    pass

  def romanToInt(self, roman_str: str) -> int:
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


sol_instance = Solution()
print(sol_instance.romanToInt("MXI") == 1011)
print(sol_instance.romanToInt("MIX") == 1009)
