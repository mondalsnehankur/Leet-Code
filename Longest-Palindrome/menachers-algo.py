class Solution(object):
    def longestPalindrome(self, s):

        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        p = [0] * n
        center = 0
        right = 0

        for i in range(1, n - 1):

            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        maxLen = max(p)
        centerIndex = p.index(maxLen)

        start = (centerIndex - maxLen) // 2

        return s[start:start + maxLen]
      
