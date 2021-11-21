class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        if len(chars) == 0:
            return 0
        
        i, j = 0, 1
        while j < len(chars):
            if chars[i] == chars[j]:
                j += 1
            else:
                if j - i > 1:
                    chars[i+1] = str(j-i)
                    i += 2
                else:
                    i += 1
                j += 1
        
        if j - i > 1:
            chars[i+1] = str(j-i)
        else:
            i += 1
        
        return i
