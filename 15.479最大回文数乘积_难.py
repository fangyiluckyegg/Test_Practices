#479. 最大回文数乘积
#给定一个整数n ，返回可表示为两个n位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。

#数学公式推导：
#1.palindrome=X∗Y, 其中X和Y都非常接近10^n,
#2.可知X和Y的赋值表达式为：X=10^n−i,Y=10^n−j，其中 i∗j<10^n 且i,j均为正整数，不然X和Y就超过n位整数条件
#3.恒等式 palindrome=(10^n−i)∗(10^n−j)=(10^n−i−j)∗10^n +i∗j=upper∗10^n +lower
#4.将两数的乘积化简为两数相加可知 upper=10^n−(i+j),lower=i∗j , 根据回文串还存在等式 lower=int(str(upper)[::−1])
#5.变量转换有 const=i+j 且 lower=i∗(const−i) 且 upper=10^n −const
#6.等式变换 lower=i∗(const−i)=> i^2 −const∗i+lower=0 => (i−const/2)^2 =0.25∗const^2 −lower=0.25∗(const^2 −lower∗4)=>i=0.5∗sqrt(const^2 −lower∗4)+0.5∗const>=1
#7.lower 和 upper 互为可推导大小值只与 const 有关，求解其中之一即可, 由于 i 必定为正整数所以 sqrt(const^2 −lower∗4) 为整数时， 返回 upper∗10^n +lower

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        a = 2
        hi = 10 ** n - 1
        lo = 10 ** (n - 1)
        while a < 2 * 10 ** n:
            upper = 10 ** n - a
            lower = int(str(upper)[::-1])
            if a ** 2 - 4 * lower >= 0 and (a ** 2 - 4 * lower) ** 0.5 == int((a ** 2 - 4 * lower)**0.5):
                num = int(str(upper)+ str(upper)[::-1])
                return num % 1337
            a += 1

if __name__ == "__main__":
    sol = Solution()
    result = sol.largestPalindrome(2)   
    print(result)


