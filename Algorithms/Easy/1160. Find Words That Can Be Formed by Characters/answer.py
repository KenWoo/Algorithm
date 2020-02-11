from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        c_dict = {}
        for c in chars:
            c_dict.setdefault(c, 0)
            c_dict[c] += 1
        for w in words:
            if len(w) > len(chars):
                continue

            w_dict = {}
            for k in w:
                w_dict.setdefault(k, 0)
                w_dict[k] += 1
            flag = True
            for k, v in w_dict.items():
                if k not in c_dict:
                    flag = False
                    break
                else:
                    if v > c_dict[k]:
                        flag = False
                        break
            if not flag:
                continue
            else:
                count += len(w)
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.countCharacters(
        ["hello", "world", "leetcode"], "welldonehoneyr")
    print(result)
