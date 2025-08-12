
#如果一个数是2的n次幂，那么，这个数换算成二进制，一定是最左边是1，其他位是0的形式：比如4，它的二进制是100，8的二进制是1000
#n-1的二进制，一定是n的每一位取反，也就是1变成0，0变成1：比如7的二进制是0111，3的二进制是011
#恒有 n & (n - 1) == 0 且一定满足 n > 0



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    sol = Solution()
    result = sol.isPowerOfTwo(3)   
    print(result)

