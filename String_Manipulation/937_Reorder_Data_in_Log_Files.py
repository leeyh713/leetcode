class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letlog = []
        diglog = []
        for i in range(len(logs)):
            if logs[i].split()[1].isalpha(): # if letter logs
                letlog.append(logs[i])
            else: # digit logs : maintain their relative ordering
                diglog.append(logs[i])

        # letter logs : sorted lexicographically
        # if contents are the same, sort them lexicographically by their idenfiers
        letlog.sort(key = lambda x: (x.split()[1:], x.split()[0]))

        return letlog + diglog