

# Given a string s and a string array dictionary,
# return the longest string in the dictionary that can be formed by deleting some of the given string characters.
# If there is more than one possible result,
# return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.


def findLongestWord(s, dictionary):
    dictionary.sort(key=lambda x: (len(x),x))
    for word in dictionary:
        if isSubSeq(word,s):
            return word
    return ''
def isSubSeq(word,s):
    i = 0
    for char in s:
        if char == word[i]:
            i += 1
        if i == len(word):
            return True
    return False


# s = "abpcplea"
# dictionary = ["a","b","c"]

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
print(findLongestWord(s, dictionary))
