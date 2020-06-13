from typing import List
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        row = rand7()
        col = rand7()
        idx = col + (row-1) * 7
        while idx > 40:
            row = rand7()
            col = rand7()
            idx = col + (row-1) * 7
        return 1 + (idx-1) % 10


if __name__ == "__main__":
    pass
