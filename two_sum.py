class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[j]== target- nums[i]:
                    return[i,j]
