#2119. 反转两次的数字
#反转 一个整数意味着倒置它的所有位。
#例如，反转 2021 得到 1202 。反转 12300 得到 321 ，不保留前导零 。
#给你一个整数 num ，反转 num 得到 reversed1 ，接着反转 reversed1 得到 reversed2 。如果 reversed2 等于 num ，返回 true ；否则，返回 false 。


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        #print(num)
        digits_list = [int(digit) for digit in str(num)]
        #print(digits_list)
        result_num = int(''.join([str(num) for num in digits_list[::-1]]))
        #print(result_num)
        digits_list_again = [int(digit) for digit in str(result_num)]
        #print(digits_list_again)
        #result_num_again = int(''.join([str(x) for x in digits_list_again]))
        result_num_again = int(''.join([str(result_num) for result_num in digits_list_again[::-1]]))
        #print(result_num_again)        
        if (result_num_again == num):
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    result = sol.isSameAfterReversals(0)   
    print(result)