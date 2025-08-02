#2520. 统计能整除数字的位数
#给你一个整数 num ，返回 num 中能整除 num 的数位的数目。
#如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。

class Solution:
    def countDigits(self, num: int) -> int:
        digit = [int(digit) for digit in str(num)]
        count = len(list(digit))-1
        i=int (0)
        while count >= 0:
            if (num % digit[count] == 0):
                i=i+1
            count=count-1
        return(i)    

if __name__ == "__main__":
    sol = Solution()
    result = sol.countDigits(1235)   
    print(result)