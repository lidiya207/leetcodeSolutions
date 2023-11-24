from typing import List
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = (celsius * 9/5) + 32.00
        return [Kelvin,Fahrenheit]
  