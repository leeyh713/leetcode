class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = re.sub('[^a-z]', ' ', paragraph.lower()).split()
        # words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]

        occur = defaultdict(int)
        for word in words:
            occur[word] += 1

        for ban_word in banned:
            try:
                del occur[ban_word]
            except:
                pass

        # counts = Counter(words)
        # return counts.most_coomon(1)[0][0]

        return max(occur, key=occur.get)