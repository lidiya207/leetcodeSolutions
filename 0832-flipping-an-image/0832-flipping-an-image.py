class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            # Reverse the row
            row.reverse()
            
            # Invert each element in the row
            for i in range(len(row)):
                row[i] = 1 - row[i]
        
        return image