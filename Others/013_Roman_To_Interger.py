class Solution:
    def romanToInt(self, s: str) -> int:
        # IV, IX
        # XL, XC
        # CD, CM
        # 이 외에는 한 글자씩 읽음

        def simpleRomanToInt(s: str) -> int:
            if s == 'I':
                return 1
            if s == 'V':
                return 5
            if s == 'X':
                return 10
            if s == 'L':
                return 50
            if s == 'C':
                return 100
            if s == 'D':
                return 500
            if s == 'M':
                return 1000

        sum, i = 0, 0

        while i < len(s) - 1:  # 0~len(s)-2
            if s[i] == 'I' and s[i + 1] == 'V':
                sum += 4
                i += 2
            elif s[i] == 'I' and s[i + 1] == 'X':
                sum += 9
                i += 2
            elif s[i] == 'X' and s[i + 1] == 'L':
                sum += 40
                i += 2
            elif s[i] == 'X' and s[i + 1] == 'C':
                sum += 90
                i += 2
            elif s[i] == 'C' and s[i + 1] == 'D':
                sum += 400
                i += 2
            elif s[i] == 'C' and s[i + 1] == 'M':
                sum += 900
                i += 2
            else:
                sum += simpleRomanToInt(s[i])
                i += 1

        if i == len(s) - 1:  # if i == last index
            sum += simpleRomanToInt(s[i])

        return sum