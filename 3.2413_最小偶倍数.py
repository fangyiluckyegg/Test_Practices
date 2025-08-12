#2413. 最小偶倍数
#给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return (n)
        else:
            return (n*2)

if __name__ == "__main__":
    sol = Solution()
    result = sol.smallestEvenMultiple(5)   
    print(result)