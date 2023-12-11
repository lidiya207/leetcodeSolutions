class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Zip the names and heights together, then sort based on heights in descending order
        s = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names
        s= [person[0] for person in s]

        return s
