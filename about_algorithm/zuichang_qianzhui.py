class Longest:
    def find_longest(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans =''
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        first_str=strs[0]
        i=0
        while i <len(first_str):
            for j in range(len(strs)):
                if first_str[:i+1] != strs[j][:i+1]:
                    return first_str[:i]
                else:
                    ans = first_str[:i+1]
            i+=1
        return ans


a = ["aaa","flow","flight"]
s = Longest()
print(s.find_longest(a))