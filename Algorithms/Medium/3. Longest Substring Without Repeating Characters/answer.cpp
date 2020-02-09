#include <string>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        map<char, int> dict;
        for (auto start = 0,end = 0; end < s.length(); end++)
        {
            auto iter = dict.find(s[end]);
            if (iter != dict.end())
            {
                start = max(iter->second, start);
                dict.erase(s[end]);
            }
            res = max(res, end - start + 1);
            dict.insert(pair<char, int>(s[end], end + 1));
        }
        return res;
    }
};