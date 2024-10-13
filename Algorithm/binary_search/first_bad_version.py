# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n

        while L < R:
            guess_version = (L + R) // 2

            if isBadVersion(guess_version):
                R = guess_version
            else:
                L = guess_version + 1
        
        return R
