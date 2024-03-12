class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) / 2

        for i in range(len(nums) - 1, -1 , -1):
            if nums[i] > target:
                return False
            nextdp = dp.copy()
            for t in dp:
                if t + nums[i] == target:
                    return True
                if t + nums[i] < target:
                    nextdp.add(t + nums[i])
            dp = nextdp
        return True if target in dp else False