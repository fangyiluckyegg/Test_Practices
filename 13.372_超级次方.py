#372. 超级次方
#你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
       return pow(a, int("".join(map(str,b))), 1337)  

#pow() 函数的基本语法如下
#1.x：底数（base）;y：指数（exponent）;z（可选）：模数（modulus），用于取模运算;根据是否提供第三个参数 z，pow() 的行为会有所不同。
#2.当只提供两个参数时，pow(x, y) 等价于 x ** y，即计算 x^y
#负指数的处理：当指数 b 是负数时，幂运算 a^b 等于 ，其中 ∣b∣ 是 b 的绝对值。
#负底数的处理：当底数 a 是负数时，幂运算 ab 的结果取决于 b 的奇偶性：
#如果 b 是奇数，结果是负数。
#如果 b 是偶数，结果是正数
#a是浮点数或复数都是可以的
#3.当提供三个参数时，pow(x, y, z) 会计算 (x^y )%z，即先计算幂运算，然后对结果取模。这种用法在密码学和大数运算中非常常见
#如果 a 或 b 是浮点数或复数，pow(a, b, c) 会抛出错误。
#Python 中的 pow() 函数是一个功能强大且灵活的工具，支持多种数据类型和运算方式。它不仅能够高效地计算幂运算，还能结合模运算处理复杂的数学问题。在实际编程中，合理使用 pow() 可以提高代码的效率和可读性。

if __name__ == "__main__":
    sol = Solution()
    result = sol.superPow(2,[1,0])   
    print(result)