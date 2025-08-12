#728. 自除数
#自除数 是指可以被它包含的每一位数整除的数。
#例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
#自除数 不允许包含 0 。
#给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right]（包括两个端点）内所有的 自除数 。


from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        flag=True  
        for num in range(left, right + 1):    
            digit = [int(digit) for digit in str(num)]
            #print(num)
            #print(digit)
            count = len(list(digit))-1 
            while count >= 0:
                #print(num)
                #print(digit[count])
                if (digit[count] == 0 or num % digit[count] != 0):
                    flag=False 
                count=count-1
            #print(flag)
            if (flag==True):
                result.append(num)  # 添加到列表中
            flag=True  
        return (result)
    
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.selfDividingNumbers(1,22)   
    print(result)