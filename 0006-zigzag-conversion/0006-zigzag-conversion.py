class Solution:
    def convert(self, s: str, numRows: int) -> str:
      
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Create a list of strings to store each row in the zigzag pattern
        rows = [''] * numRows
        index, step = 0, 1
        
        # Traverse each character in the string
        for char in s:
            rows[index] += char  # Add the character to the current row
            # Change direction when reaching the top or bottom row
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            # Update the index for the next character
            index += step
        
        # Join all the rows together to get the zigzag conversion result
        return ''.join(rows)