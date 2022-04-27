# https://leetcode.com/problems/roman-to-integer

class Solution:
    
    def __init__(self) -> None:
        self._translate = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000,
        )
        self._special_cases = dict(
            IV=4,
            IX=9,
            XL=40,
            XC=90,
            CD=400,
            CM=900,
        )
    
    def romanToInt(self, s: str) -> int:
        numeral_components = list()
        left_modifier = 0
        right_modifier = 0
        for i in range(len(s)):
            left_val = s[i + left_modifier] if i + left_modifier <= len(s) - 1 else ""
            right_val = s[i + 1 + right_modifier] if i + 1 + right_modifier <= len(s) - 1 else ""
            
            val = self._translate.get(left_val)
            special_case = self._special_cases.get(left_val + right_val)
            
            if special_case is not None:
                left_modifier += 1
                right_modifier += 1
                numeral_components.append(special_case)
            elif val is not None:
                numeral_components.append(val)
        
        return sum(numeral_components)
