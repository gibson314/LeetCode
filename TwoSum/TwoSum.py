class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        addindex = []
        for i in range (len(nums)):
            addindex.append((nums[i], i))
        sortedarray = sorted(addindex, key=lambda x : x[0])
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if (sortedarray[i][0] + sortedarray[j][0] == target):
                    return [sortedarray[i][1], sortedarray[j][1]]
                if sortedarray[j][0] > target:
                    continue




if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([1, 12, 3, 4], 16))


