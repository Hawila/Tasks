def is_balanced(s):
    # pairs_dictionary
    pairs = {"}": "{", ")": "(", "]": "["}
    # first half of given string to match it with second sub-string
    j = midpoint = int(len(s)/2)
    fSub = list(s[:midpoint])

    # check for odd string length
    if (len(s) % 2 != 0):
        return False
    else:
        while j < len(s):
            # opening bracket from dictionary related to the current closing bracket s[j] if found
            current = pairs[s[j]]
            # top of the stack(First sub-string)
            top = fSub[-1]
            if current == top:
                fSub.pop()
                j += 1
            else:
                return False
    # True if list is empty which means all brackets are matched
    return len(fSub) == 0


str = input("Enter a string of brackets:")
print(str+" Is Balanced" if is_balanced(str) else str+" is Not Balanced")
