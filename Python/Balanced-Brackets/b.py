# using stack
def is_balanced(s):
    # pairs_dictionary
    pairs = {"}": "{", ")": "(", "]": "["}
    # Stack
    fSub = []

    # check for odd string length
    if (len(s) % 2 != 0):
        return False
    else:
        j = 0
        while j < len(s):
            # if current bracket is opening bracket we push it
            if s[j] in ["{", "[", "("]:
                fSub.append(s[j])
            elif (len(fSub) == 0):
                return False
            elif (pairs[s[j]] == fSub[-1]):
                fSub.pop()
            j += 1
    # True if list is empty which means all brackets are matched
    return len(fSub) == 0


str = input("Enter a string of brackets:")
print(str+" Is Balanced" if is_balanced(str) else str+" is Not Balanced")


# using regex
""" import re


def is_balanced(s):
    pattern = "\{}|\[]|\(\)"
    while (re.search(pattern, s)):
        s = re.sub(pattern, "", s)
    return len(s) == 0
 """
