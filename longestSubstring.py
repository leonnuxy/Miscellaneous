class Solution(object):
    def lengthOfLongestSubstring(self, s):
      
        # Creating a set to store the last positions of occurrence
        seen = {}
        max_len = 0
    
        # starting the inital point of window to index 0
        start = 0
        
        for end in range(len(s)):
            
            # Checking if we have already seen the element or not
            if s[end] in seen:
                # If we have seen the number, move the start pointer
                # to position after the last occurrence
                start = max(start, seen[s[end]] + 1)
    
            # Updating the last seen value of the character
            seen[s[end]] = end
            max_len = max(max_len, end-start + 1)

        return max_len



input_list = "abcabcbb"
ob1 = Solution()
print(ob1.lengthOfLongestSubstring(input_list))
