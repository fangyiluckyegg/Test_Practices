#2427. 公因子的数目
#给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
#如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        x=1
        num=0
        smaller = int(min(a, b))
        while x<=smaller:
            if (a%x==0 and b%x==0):
                print(x)
                num=num+1
            x=x+1
        return(num)
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.commonFactors(12,6)   
    print(result)