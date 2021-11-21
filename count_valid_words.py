class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        import re
        import collections
        word_count = collections.Counter(re.findall(r'\w+', sentence.lower()))
        word_count['and'] = word_count['and'] - word_count['not']
        word_count['or'] = word_count['or'] - word_count['not']
        word_count['not'] = 0
        return sum(word_count.values())

        