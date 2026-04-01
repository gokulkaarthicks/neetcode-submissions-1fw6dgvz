class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if not self.alpnumo(s[l]):
                l = l+1
            elif not self.alpnumo(s[r]):
                r = r - 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l = l+1
                r= r-1
        return True
    
    def alpnumo(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z')
            or
            ord('a') <= ord(c) <= ord('z')
            or
            ord('0') <= ord(c) <= ord('9')
        )
        