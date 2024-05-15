"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""
import math

class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        
        number_factorial = str(math.factorial(number))
        trailing_zeros_counts = len(number_factorial) - len(number_factorial.rstrip('0'))
        return trailing_zeros_counts
    
solution = Solution()
print(solution.find_tailing_zeroes(0))