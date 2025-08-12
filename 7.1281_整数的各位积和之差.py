#1281. 整数的各位积和之差
#给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]   
        count = len(list(digits))-1
        he = 0
        ji = 1
        while count >=0:
            #print(count)
            #print(digits[count])      
            ji = ji*digits[count]
            he = he+digits[count]
            count = count -1
        return(ji-he)
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.subtractProductAndSum(234)   
    print(result)