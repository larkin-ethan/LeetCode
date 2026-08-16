class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        finalString = []
        L1 = len(word1)
        L2 = len(word2)
        LT = min(L1,L2)

        for x in range(LT):
            finalString.append(word1[x])
            finalString.append(word2[x])

        x += 1
        if L1 > L2:
            finalString.append(word1[x:])
        elif L2 > L1:
            finalString.append(word2[x:])

        return "".join(finalString)