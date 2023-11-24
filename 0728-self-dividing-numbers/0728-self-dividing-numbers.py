class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        
        for x in range(left, right + 1):
            is_self_dividing = True
            digits = str(x)
            
            for digit in digits:
                if digit != '0' and x % int(digit) == 0:
                    pass
                else:
                    is_self_dividing = False
                    break
            
            if is_self_dividing:
                result.append(x)
                
        return result

    