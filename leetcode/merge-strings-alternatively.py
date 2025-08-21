###
# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
###
def mergeAlternately(word1: str, word2: str):
    result = ""

    if len(word1) < len(word2):
        count = len(word1)
    else:
        count = len(word2)

    for i in range(count):
        result += word1[i]
        result += word2[i]

    print(result)

if __name__ == "__main__":

    mergeAlternately("abc", "pqr")
    mergeAlternately("ab", "pqrs")
    mergeAlternately("abcd", "pq")