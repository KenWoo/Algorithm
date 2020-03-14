from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {v: [0] * len(votes[0]) for v in votes[0]}
        dict = {}
        for v in votes:
            for i, s in enumerate(v):
                count[s][i] -= 1
        return ''.join(sorted(votes[0], key=lambda v: count[v] + [v]))


if __name__ == "__main__":
    s = Solution()
    result = s.rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"])
    print(result)
    result = s.rankTeams(["WXYZ", "XYZW"])
    print(result)
    result = s.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"])
    print(result)
    result = s.rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"])
    print(result)
    result = s.rankTeams(["M", "M", "M", "M"])
    print(result)
    result = s.rankTeams(["FVSHJIEMNGYPTQOURLWCZKAX", "AITFQORCEHPVJMXGKSLNZWUY", "OTERVXFZUMHNIYSCQAWGPKJL", "VMSERIJYLZNWCPQTOKFUHAXG", "VNHOZWKQCEFYPSGLAMXJIUTR", "ANPHQIJMXCWOSKTYGULFVERZ", "RFYUXJEWCKQOMGATHZVILNSP", "SCPYUMQJTVEXKRNLIOWGHAFZ", "VIKTSJCEYQGLOMPZWAHFXURN", "SVJICLXKHQZTFWNPYRGMEUAO", "JRCTHYKIGSXPOZLUQAVNEWFM",
                          "NGMSWJITREHFZVQCUKXYAPOL", "WUXJOQKGNSYLHEZAFIPMRCVT", "PKYQIOLXFCRGHZNAMJVUTWES", "FERSGNMJVZXWAYLIKCPUQHTO", "HPLRIUQMTSGYJVAXWNOCZEKF", "JUVWPTEGCOFYSKXNRMHQALIZ", "MWPIAZCNSLEYRTHFKQXUOVGJ", "EZXLUNFVCMORSIWKTYHJAQPG", "HRQNLTKJFIEGMCSXAZPYOVUW", "LOHXVYGWRIJMCPSQENUAKTZF", "XKUTWPRGHOAQFLVYMJSNEIZC", "WTCRQMVKPHOSLGAXZUEFYNJI"])
    print(result)
