class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()
        # print(clean)
        for i in range(len(clean)//2):
            if clean[i] != clean[-1*(i+1)]:
                # print(clean[i], clean[-1*(i+1)])
                return False
        return True
        