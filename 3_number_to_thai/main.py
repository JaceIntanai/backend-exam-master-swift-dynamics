"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10000000:
            return "number exceeds maximum limit"

        list_thai_numerals = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        list_thai_units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        if number == 0:
            return "ศูนย์"

        result = ""
        num_str = str(number)
        length = len(num_str)

        for i, digit in enumerate(num_str):
            digit_str = int(digit)
            position = length - i - 1
            
            if digit_str == 0:
                continue
            
            if position == 0 and digit_str == 1 and length > 1:
                result += "เอ็ด"
            elif position == 1 and digit_str == 1:
                result += "สิบ"
            elif position == 1 and digit_str == 2:
                result += "ยี่สิบ"
            else:
                result += list_thai_numerals[digit_str] + list_thai_units[position]
        
        return result
    
solution = Solution()
print(solution.number_to_thai(10101))
