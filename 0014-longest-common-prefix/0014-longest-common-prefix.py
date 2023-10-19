class Solution(object):
    def longestCommonPrefix(self, strs):
      

        n = len(strs)
        if (n < 2):
            return strs[0]

        commonPrefix = []

        for charIndex, char in enumerate(strs[0]):
            needToTerminate = False
            for i in range(1, n):
                if ((charIndex == len(strs[i])) or (char != strs[i][charIndex])):
                    needToTerminate = True
                    break
            if (needToTerminate):
                break
            commonPrefix.append(char)

        return "".join(commonPrefix)