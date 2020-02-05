/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    var map = {};
    for (var i = 0; i < nums.length; i++) {
        var remainder = target - nums[i];
        if (remainder in map) {
            return [map[remainder], i];
        }
        map[nums[i]] = i;
    }
    return null;
};