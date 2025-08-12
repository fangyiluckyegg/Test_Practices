#2235. 两整数相加
#给你两个整数 num1 和 num2，返回这两个整数的和。
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return (num1+num2)

if __name__ == "__main__":
    sol = Solution()
    result = sol.sum(36,50)   
    print(result)
        