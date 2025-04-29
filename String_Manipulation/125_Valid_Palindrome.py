class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        return s == s[::-1]

# string.lower() : alphabet -> convert all alphabetic characters to lowercase
# re : regular expression module
# re.sub('pattern', 'replacement', string) : replace parts of the string that match the pattern with the replacement