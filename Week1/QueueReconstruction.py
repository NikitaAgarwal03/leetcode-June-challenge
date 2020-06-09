class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(k, [h, k])
        return res       
