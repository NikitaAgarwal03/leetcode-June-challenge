class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            index = t.find(i)
            if index >= 0:
                t=t[index+1:]
            else:
                return False
        return True
