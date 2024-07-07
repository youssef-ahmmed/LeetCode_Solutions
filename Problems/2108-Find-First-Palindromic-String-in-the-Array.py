class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindrome(word):
            return word == word[::-1]
        
        for w in words:
            if palindrome(w):
                return w
        
        return ""
