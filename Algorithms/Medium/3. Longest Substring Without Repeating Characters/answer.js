/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    var res = 0;
    var dict = {};
    for (var start = 0, end = 0; end < s.length; end++) {
        if (s[end] in dict) {
            start = Math.max(dict[s[end]], start);
        }
        res = Math.max(res, end - start + 1);
        dict[s[end]] = end + 1;
    }
    return res;
};