class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == -1:
            return False
        y = []
        for i in range(len(str(x))):
            t = x % 10
            y.append(t)
            x = x//10
        if y == y[::-1]:
            return True
        return False
        