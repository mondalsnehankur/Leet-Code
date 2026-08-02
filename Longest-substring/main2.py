class Solution(object):
    def lengthOfLongestSubstring(self, s):

        maxLength = 0

        for i in range(len(s)):

            seen = set()

            for j in range(i, len(s)):

                if s[j] in seen:
                    break

                seen.add(s[j])
                maxLength = max(maxLength, j - i + 1)

        return maxLength
