class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        sorted_list = nums1 + nums2
        sorted_list.sort()

        if len(sorted_list) % 2 !=0:
            return float(sorted_list[len(sorted_list)//2])
        else:
            first_half = sorted_list[:len(sorted_list)//2]
            second_half = sorted_list[len(sorted_list)//2:]
            median = (first_half[len(first_half)-1] + second_half[0])/2
            return median



sol = Solution()

print(sol.findMedianSortedArrays([1, 2, 3], [3, 4]))




        