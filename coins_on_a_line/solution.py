class Solution:
    dic_ = {}
    def firstWillWin(self,n):

        dic = self.dic_
        if str(n) not in dic:
            if n == 0:
                dic[str(n)] = False
            elif n <= 2:
                dic[str(n)] = True
            else:
                res = not self.firstWillWin(n-1) or not self.firstWillWin(n-2)
                dic[str(n)] = res
        return dic[str(n)]
