public int[] TwoSum(int[] nums, int target)
{
    var dic = new Dictionary<int, int>();
    for (int i = 0; i < nums.Length; i++)
    {
        if (dic.ContainsKey(target - nums[i]))
        {
            return new int[] { dic[target - nums[i]], i };
        }
        dic[nums[i]] = i;
    }

    return null;
}