#70. 爬楼梯
#假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:return 1
        # 1. 定义状态.i: 第i个台阶； dp[i]: 跳到第i个台阶的跳法
        dp = [0] * (n + 1)
        # 2. 初始化边界条件：dp[1] = 1，即第一个台阶只有1种跳法；dp[2] = 2，即第二个台阶有2种跳法；
        dp[1] = 1
        dp[2] = 2
        # 3. 确定递推公式： dp[i] = dp[i - 1] + dp[i - 2]
        for i in range(3, n + 1):
            # 到第i个台阶有2种方法：从第 i-1跳上来，或者从第 i-2跳上来
            dp[i] = dp[i-1] + dp[i-2]
        # 4.输出结果
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(12)   
    print(result)