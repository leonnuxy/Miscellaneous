class Solution(object):
    def reverseString(self, s):
        
        len_s = len(s)

        # Loop from the the last integer
        for x in reversed(range(len(s))):
            s.append(s[x])

        del s[0:len_s]
        return s


input_list = ["H","a","n","n","a","h"]
ob1 = Solution()
print(ob1.reverseString(input_list))
