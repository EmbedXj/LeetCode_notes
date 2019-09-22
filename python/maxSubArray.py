class Solution:
    def maxSubArray(self, nums) -> int:
        """
        动态规划--通项公式如下：
        从0至len-1, premaxsum = max(premaxsum + nums[i], nums[i])
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxsum = nums[0]
        premaxsum = nums[0]
        for i in range(1, len(nums)):
            premaxsum = max(premaxsum + nums[i], nums[i])
            maxsum = premaxsum if premaxsum > maxsum else maxsum
        return max(maxsum, nums[-1])