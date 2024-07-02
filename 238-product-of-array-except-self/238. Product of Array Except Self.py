class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
            right[-i-1] = nums[-i] * right[-i]




        for i in range(len(nums)):
            res[i] = left[i] * right[i]

        #print(left, right)
        return res
            
        

        

            
        