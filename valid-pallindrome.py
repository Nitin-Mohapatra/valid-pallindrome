class Solution(object):
    def isPalindrome(self, s):
        pl = ""
        for ch in s:
            if ch.isalnum():
                pl += ch.lower()
        return pl == pl[::-1]
