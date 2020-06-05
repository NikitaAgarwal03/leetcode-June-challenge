class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs=sorted(costs, key=lambda x:x[0]-x[1])
        half=0
        total=0
        
        for costA,costB in costs:
            total=total+costA if half<(len(costs)/2) else total+costB
            half+=1
        return total   
