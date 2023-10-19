class Solution(object):
    def isValid(self, s):
      show =[]
      look = {")":"(","}":"{","]":"["}
      for a in s:
         if  a in look.values():
              show.append(a)
         elif show and look[a] == show[-1]:
              show.pop()
         else:
                    return False
      return show == []