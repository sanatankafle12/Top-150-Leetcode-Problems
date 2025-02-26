class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_len = [len(str) for str in strs]    
        min_ = min(str_len)
        max = 0
        for i in range(1,min_+1):
            x = [str[:i] for str in strs]
            if len(set(x)) == 1 and max <= i:
                max = i
                continue
        return(strs[0][:max])
