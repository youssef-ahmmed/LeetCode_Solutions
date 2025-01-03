class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        n = len(words)

        def is_vowel(word):
            return word[0] in vowels and word[-1] in vowels

        bin_words = []
        for word in words:
            if is_vowel(word):
                bin_words.append(1)
            else:
                bin_words.append(0)
        
        prefix = [0] * n
        prefix[0] = bin_words[0]

        for i in range(1, n):
            prefix[i] = bin_words[i] + prefix[i - 1]

        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] - prefix[l - 1])
            
        return res
