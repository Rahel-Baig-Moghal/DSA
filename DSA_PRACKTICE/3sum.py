import random
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        values = {}
        lenght_of_nums= len(nums)
        triplets = set()

        for i, num in enumerate(nums):
            values[num]=i
        
        for i in range(lenght_of_nums):
            for j in range(i+1, lenght_of_nums):
                desired  = - nums[i] - nums[j]
                if desired in values and values[desired]!=i and values[desired]!=j:
                    triplets.add(tuple(sorted([nums[i], nums[j], desired])))
        return list(triplets)



s = Solution()

print(s.threeSum([-1,0,1,2,-1,-4]))