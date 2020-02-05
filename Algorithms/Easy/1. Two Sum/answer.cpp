class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        vector<int> v;

        map<int, int> dic;
        for (auto i = 0; i < nums.size(); i++)
        {
            auto remainer = target - nums[i];
            auto iter = dic.find(remainer);
            if (iter != dic.end())
            {
                v.push_back(iter->second);
                v.push_back(i);
                break;
            }

            dic[nums[i]] = i;
        }

        return v;
    }
};