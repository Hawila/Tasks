
# as string is iteratable so by using array slicing to obtain 2 sub-strings
# first sub-string [:index]  from start to the given index and because the end is exclusive so index not included
# then concatenate the char u want to replace + second sub-string after charater
def str_replace(str, index, char):
    return str[:index] + char + str[index+1:]


print(str_replace("Dev", 1, "a"))  # dav

print(str_replace("asdfg", 4, "H"))  # asdfH

print(str_replace("asdmsadkm", 0, "K"))  # asdmsadkm
