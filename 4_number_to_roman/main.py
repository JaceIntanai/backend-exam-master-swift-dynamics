"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return ""
        if number > 3999:
            return "number exceeds maximum limit"

        list_number_units = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        list_roman_numerals = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_number = ""
        i = 0
        while number > 0:
            counts_numerals = number // list_number_units[i]
            for _ in range(counts_numerals):
                roman_number += list_roman_numerals[i]
                number -= list_number_units[i]
            i += 1
        return roman_number
    
solution = Solution()
print(solution.number_to_roman(1995))
