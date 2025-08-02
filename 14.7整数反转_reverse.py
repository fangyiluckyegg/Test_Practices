
#7. 整数反转
#给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
#假设环境不允许存储 64 位整数（有符号或无符号）。
 
class Solution:
    def reverse(self, x: int) -> int:
        #print(x)
        #第一将整数转换为字符串;第二遍历字符串中的每个字符；第三将每个字符转换为整数。
        if x < 0:
            digits_list = [int(digit) for digit in str(-x)]
            #第一将每个字符反转顺序;第二将单个字符连接成字符串；第三将字符串转换为整数。
            result_num = int(''.join([str(x) for x in digits_list[::-1]])) 
            result_num = -result_num
        else:
            digits_list = [int(digit) for digit in str(x)]
            result_num = int(''.join([str(x) for x in digits_list[::-1]])) 
        #print(digits_list)        
        if result_num < -2**31 or result_num > 2**31 - 1:
            return 0
        else:
            return result_num
        

if __name__ == "__main__":
    sol = Solution()
    result = sol.reverse(-231431234)   
    print(result)