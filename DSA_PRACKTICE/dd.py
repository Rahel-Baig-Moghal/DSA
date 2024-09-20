class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        a = []
        for n in nums:
            if n in a:
                return True
            a.append(n)
        return False
         
s = Solution()

print(s.hasDuplicate([1,2,3,3]))