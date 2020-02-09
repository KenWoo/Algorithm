public int LengthOfLongestSubstring(string s)
{
    var res = 0;
    var dict = new Dictionary<char, int>();
    for (int start = 0,end = 0; end < s.Length; end++)
    {
        if (dict.ContainsKey(s[end]))
        {
            start = Math.Max(dict[s[end]], start);
        }
        res = Math.Max(res, end - start + 1);
        dict[s[end]] = end + 1;
    }

    return res;
}