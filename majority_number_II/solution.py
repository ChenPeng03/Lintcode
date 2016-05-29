class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        count1, count2, a, b, = 0, 0, 0, 0
        for i in nums:
            if i == a:
                count1 += 1
            elif i == b:
                count2 += 1
            elif count1 == 0:
                a = i
                count1 += 1
            elif count2 == 0:
                b = i
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        print a, b
        for i in nums:
            if i == a:
                count1 += 1
            if i == b:
                count2 += 1
        if count1 > count2:
            return a
        else:
            return b
