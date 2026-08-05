class Solution(object):
    def longestPalindrome(self, s):

        if len(s) < 2:
            return s

        start = 0
        maxLength = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):

            # Odd length
            left, right = expand(i, i)

            if right - left + 1 > maxLength:
                start = left
                maxLength = right - left + 1

            # Even length
            left, right = expand(i, i + 1)

            if right - left + 1 > maxLength:
                start = left
                maxLength = right - left + 1

        return s[start:start + maxLength]
