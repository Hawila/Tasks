# using stack
def isBalanced(s):
    # Write your code here
    # pairs_dictionary
    pairs = {"}": "{", ")": "(", "]": "["}
    # first half of given string to match it with second sub-string
    fSub = []

    # check for odd string length
    if (len(s) % 2 != 0):
        return "NO"
    else:
        j = 0
        while j < len(s):
            # if current bracket is opening bracket we push it
            if s[j] in ["{", "[", "("]:
                fSub.append(s[j])
            elif (len(fSub) == 0):
                return "NO"
            elif (pairs[s[j]] == fSub[-1]):
                fSub.pop()
            j += 1
    # True if list is empty which means all brackets are matched
    return "YES" if len(fSub) == 0 else "NO"


str = input("Enter a string of brackets:")
isBalanced(str)


# using regex
""" import re


def is_balanced(s):
    pattern = "\{}|\[]|\(\)"
    while (re.search(pattern, s)):
        s = re.sub(pattern, "", s)
    return len(s) == 0
 """
