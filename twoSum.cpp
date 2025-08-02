//1. 两数之和
//给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
//你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
//你可以按任意顺序返回答案。

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_map; // 用于存储值和其索引的映射
        std::vector<int> result;              // 存储结果的向量

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i]; // 计算需要找到的另一个数
            if (num_map.find(complement) != num_map.end()) { // 如果找到了互补数
                result.push_back(num_map[complement]);       // 添加互补数的索引
                result.push_back(i);                         // 添加当前数的索引
                return result;                               // 返回结果
            }
            num_map[nums[i]] = i; // 将当前数及其索引存入映射中
        }
        return result; // 如果没有找到符合条件的两个数，返回空向量
    }
};
